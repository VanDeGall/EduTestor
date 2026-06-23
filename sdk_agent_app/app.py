from __future__ import annotations

import uuid
from datetime import date, datetime
from pathlib import Path

from flask import Flask, jsonify, redirect, render_template, request, send_file, url_for

from .db import connect, fetch_all, fetch_one, init_db
from .exporter import export_daily_log, export_leadership_register, export_monthly_report


def create_app() -> Flask:
    app = Flask(__name__)
    init_db()

    @app.get("/")
    def dashboard():
        today = date.today().isoformat()
        month = today[:7]
        stats = fetch_one(
            """
            SELECT
                COALESCE(SUM(duration_minutes), 0) AS tracked_minutes,
                COALESCE(SUM(CASE WHEN sdk_alignment LIKE 'directly%' THEN duration_minutes ELSE 0 END), 0) AS sdk_minutes,
                COALESCE(SUM(CASE WHEN sdk_alignment LIKE 'non-SDK%' THEN duration_minutes ELSE 0 END), 0) AS non_sdk_minutes
            FROM work_blocks
            WHERE date = ?
            """,
            (today,),
        ) or {"tracked_minutes": 0, "sdk_minutes": 0, "non_sdk_minutes": 0}

        open_leadership = fetch_one(
            "SELECT COUNT(*) AS count FROM leadership_outputs WHERE status IN ('draft', 'ready', 'waiting')"
        )["count"]
        evidence_count = fetch_one("SELECT COUNT(*) AS count FROM evidence_files")["count"]
        upcoming_deadlines = fetch_all("SELECT * FROM upcoming_deadlines_view LIMIT 5")
        recent_activities = fetch_all(
            "SELECT * FROM activities ORDER BY created_at DESC LIMIT 8"
        )
        active_block = fetch_one("SELECT * FROM work_blocks WHERE status = 'active' ORDER BY created_at DESC LIMIT 1")

        return render_template(
            "index.html",
            today=today,
            month=month,
            stats=stats,
            open_leadership=open_leadership,
            evidence_count=evidence_count,
            upcoming_deadlines=upcoming_deadlines,
            recent_activities=recent_activities,
            active_block=active_block,
        )

    @app.get("/api/health")
    def api_health():
        return jsonify({"success": True, "data": {"status": "ok"}, "error": None})

    @app.get("/api/dashboard")
    def api_dashboard():
        today = date.today().isoformat()
        stats = fetch_one(
            """
            SELECT
                COALESCE(SUM(duration_minutes), 0) AS tracked_minutes,
                COALESCE(SUM(CASE WHEN sdk_alignment LIKE 'directly%' THEN duration_minutes ELSE 0 END), 0) AS sdk_minutes,
                COALESCE(SUM(CASE WHEN sdk_alignment LIKE 'non-SDK%' THEN duration_minutes ELSE 0 END), 0) AS non_sdk_minutes
            FROM work_blocks
            WHERE date = ?
            """,
            (today,),
        )
        return jsonify({"success": True, "data": stats, "error": None})

    @app.post("/activities")
    def create_activity():
        form = request.form
        activity_id = f"act_{uuid.uuid4().hex[:12]}"
        with connect() as conn:
            conn.execute(
                """
                INSERT INTO activities (
                    id, date, time, raw_note, clean_activity, category, sdk_alignment,
                    priority, size, output, status, report_include
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    activity_id,
                    form.get("date") or date.today().isoformat(),
                    form.get("time") or None,
                    form.get("raw_note") or "",
                    form.get("clean_activity") or form.get("raw_note") or "",
                    form.get("category") or "documentation and reporting",
                    form.get("sdk_alignment") or "directly aligned with SDK role",
                    form.get("priority") or "medium",
                    form.get("size") or "M",
                    form.get("output") or "",
                    "confirmed",
                    form.get("report_include") or "yes",
                ),
            )
            conn.commit()
        return redirect(url_for("dashboard"))

    @app.post("/work-blocks/start")
    def start_work_block():
        form = request.form
        block_id = f"wb_{uuid.uuid4().hex[:12]}"
        now = datetime.now()
        with connect() as conn:
            conn.execute(
                """
                INSERT INTO work_blocks (
                    id, date, start_time, title, category, sdk_alignment,
                    recognition_confidence, tracking_source, status, leadership_relevance
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, 'active', ?)
                """,
                (
                    block_id,
                    now.date().isoformat(),
                    now.isoformat(timespec="seconds"),
                    form.get("title") or "SDK work block",
                    form.get("category") or "documentation and reporting",
                    form.get("sdk_alignment") or "directly aligned with SDK role",
                    form.get("recognition_confidence") or "high",
                    "manual",
                    form.get("leadership_relevance") or "maybe",
                ),
            )
            conn.commit()
        return redirect(url_for("dashboard"))

    @app.post("/work-blocks/<block_id>/stop")
    def stop_work_block(block_id: str):
        block = fetch_one("SELECT * FROM work_blocks WHERE id = ?", (block_id,))
        if not block:
            return redirect(url_for("dashboard"))

        now = datetime.now()
        started = datetime.fromisoformat(block["start_time"])
        duration = max(0, int((now - started).total_seconds() // 60))
        form = request.form
        with connect() as conn:
            conn.execute(
                """
                UPDATE work_blocks
                SET end_time = ?, duration_minutes = ?, output = ?, status = 'confirmed',
                    leadership_relevance = ?, next_step = ?, updated_at = CURRENT_TIMESTAMP
                WHERE id = ?
                """,
                (
                    now.isoformat(timespec="seconds"),
                    duration,
                    form.get("output") or block.get("output") or "",
                    form.get("leadership_relevance") or block.get("leadership_relevance") or "maybe",
                    form.get("next_step") or "",
                    block_id,
                ),
            )
            conn.commit()
        return redirect(url_for("dashboard"))

    @app.post("/leadership")
    def create_leadership_output():
        form = request.form
        item_id = f"lead_{uuid.uuid4().hex[:12]}"
        with connect() as conn:
            conn.execute(
                """
                INSERT INTO leadership_outputs (
                    id, date_prepared, topic, output_type, summary, related_sdk_area,
                    proposed_decision, status, next_step
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    item_id,
                    form.get("date_prepared") or date.today().isoformat(),
                    form.get("topic") or "Leadership topic",
                    form.get("output_type") or "briefing",
                    form.get("summary") or "",
                    form.get("related_sdk_area") or "digital strategy",
                    form.get("proposed_decision") or "",
                    form.get("status") or "draft",
                    form.get("next_step") or "Consult with principal",
                ),
            )
            conn.commit()
        return redirect(url_for("leadership"))

    @app.get("/leadership")
    def leadership():
        rows = fetch_all("SELECT * FROM leadership_outputs ORDER BY date_prepared DESC")
        return render_template("leadership.html", rows=rows, today=date.today().isoformat())

    @app.post("/deadlines")
    def create_deadline():
        form = request.form
        deadline_id = f"dl_{uuid.uuid4().hex[:12]}"
        with connect() as conn:
            conn.execute(
                """
                INSERT INTO deadlines (
                    id, title, deadline_at, source, target_group, category, alert_level, status
                ) VALUES (?, ?, ?, ?, ?, ?, ?, 'open')
                """,
                (
                    deadline_id,
                    form.get("title") or "Deadline",
                    form.get("deadline_at") or datetime.now().isoformat(timespec="minutes"),
                    form.get("source") or "manual",
                    form.get("target_group") or "user",
                    form.get("category") or "document",
                    form.get("alert_level") or "attention",
                ),
            )
            conn.commit()
        return redirect(url_for("deadlines"))

    @app.get("/deadlines")
    def deadlines():
        rows = fetch_all("SELECT * FROM deadlines ORDER BY deadline_at ASC")
        return render_template("deadlines.html", rows=rows)

    @app.post("/evidence")
    def create_evidence():
        form = request.form
        evidence_id = f"ev_{uuid.uuid4().hex[:12]}"
        with connect() as conn:
            conn.execute(
                """
                INSERT INTO evidence_files (
                    id, date, title, evidence_type, file_name, file_path,
                    evidence_value, sensitive_data, anonymisation_needed, status
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    evidence_id,
                    form.get("date") or date.today().isoformat(),
                    form.get("title") or "Evidence",
                    form.get("evidence_type") or "document",
                    form.get("file_name") or "",
                    form.get("file_path") or "",
                    form.get("evidence_value") or "medium",
                    1 if form.get("sensitive_data") == "on" else 0,
                    1 if form.get("anonymisation_needed") == "on" else 0,
                    form.get("status") or "confirmed",
                ),
            )
            conn.commit()
        return redirect(url_for("evidence"))

    @app.get("/evidence")
    def evidence():
        rows = fetch_all("SELECT * FROM evidence_files ORDER BY date DESC, created_at DESC")
        return render_template("evidence.html", rows=rows, today=date.today().isoformat())

    @app.get("/settings")
    def settings():
        row = fetch_one("SELECT * FROM settings WHERE id = 'settings_default'")
        return render_template("settings.html", settings=row)

    @app.post("/settings")
    def update_settings():
        form = request.form
        with connect() as conn:
            conn.execute(
                """
                UPDATE settings
                SET voice_input_enabled = ?, voice_output_enabled = ?, avatar_enabled = ?,
                    automatic_tracking_enabled = ?, silent_mode = ?, default_export_folder = ?,
                    workday_start = ?, workday_end = ?, updated_at = CURRENT_TIMESTAMP
                WHERE id = 'settings_default'
                """,
                (
                    1 if form.get("voice_input_enabled") == "on" else 0,
                    1 if form.get("voice_output_enabled") == "on" else 0,
                    1 if form.get("avatar_enabled") == "on" else 0,
                    1 if form.get("automatic_tracking_enabled") == "on" else 0,
                    1 if form.get("silent_mode") == "on" else 0,
                    form.get("default_export_folder") or "",
                    form.get("workday_start") or "",
                    form.get("workday_end") or "",
                ),
            )
            conn.commit()
        return redirect(url_for("settings"))

    @app.get("/exports/daily")
    def export_daily():
        date_value = request.args.get("date") or date.today().isoformat()
        path = export_daily_log(date_value)
        return send_file(Path(path).resolve(), as_attachment=True)

    @app.get("/exports/monthly")
    def export_monthly():
        month_value = request.args.get("month") or date.today().isoformat()[:7]
        path = export_monthly_report(month_value)
        return send_file(Path(path).resolve(), as_attachment=True)

    @app.get("/exports/leadership")
    def export_leadership():
        month_value = request.args.get("month")
        path = export_leadership_register(month_value)
        return send_file(Path(path).resolve(), as_attachment=True)

    return app


app = create_app()


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5050, debug=True)
