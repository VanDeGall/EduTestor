# API specification for SDK Strategic AI Assistant

## Purpose

This document defines the application API for the SDK Strategic AI Assistant prototype.

The API should allow the local app, avatar interface, work monitor, activity inbox, evidence register and export tools to communicate with the local database.

## API principles

The first prototype should use a local API. It may later be exposed as a REST API or internal service.

The API must support:

- activity creation,
- work block tracking,
- leadership outputs,
- deadlines,
- alerts,
- training opportunities,
- professional development plan items,
- policy findings,
- evidence files,
- documents,
- exports,
- user settings.

## Response format

All API responses should use this structure:

```json
{
  "success": true,
  "data": {},
  "error": null
}
```

Error response:

```json
{
  "success": false,
  "data": null,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Missing required field: category"
  }
}
```

## Core endpoints

## 1. Activities

### Create activity

`POST /api/activities`

Creates a manual, voice-derived or imported activity record.

Request:

```json
{
  "date": "2026-09-15",
  "time": "09:30",
  "raw_note": "Priprava podkladu pre vedenie k Copilotu",
  "clean_activity": "Preparation of leadership briefing for Copilot training",
  "category": "AI and Copilot",
  "sdk_alignment": "directly aligned with SDK role",
  "priority": "high",
  "size": "M",
  "output": "Draft briefing note",
  "report_include": "yes"
}
```

### List activities

`GET /api/activities?date_from=2026-09-01&date_to=2026-09-30&category=AI`

### Update activity

`PATCH /api/activities/{id}`

### Confirm activity

`POST /api/activities/{id}/confirm`

### Archive activity

`POST /api/activities/{id}/archive`

## 2. Work blocks

### Start work block

`POST /api/work-blocks/start`

Starts a transparent tracked work block.

Request:

```json
{
  "title": "Priprava skoleni pre ucitelov",
  "category": "training creation",
  "sdk_alignment": "directly aligned with SDK role",
  "tracking_source": "manual",
  "recognition_confidence": "high"
}
```

### Pause work block

`POST /api/work-blocks/{id}/pause`

### Resume work block

`POST /api/work-blocks/{id}/resume`

### Stop work block

`POST /api/work-blocks/{id}/stop`

Request:

```json
{
  "output": "Training outline prepared",
  "evidence_id": "ev_001",
  "leadership_relevance": "maybe",
  "next_step": "Prepare invitation for teachers"
}
```

### List work blocks

`GET /api/work-blocks?date_from=2026-09-01&date_to=2026-09-30`

### Correct work block

`PATCH /api/work-blocks/{id}`

Used when the user changes category, SDK alignment or evidence.

## 3. Work recognition

### Suggest work context

`POST /api/work-recognition/suggest`

Request:

```json
{
  "signal_type": "document_title",
  "signal_value": "Digitalna strategia skoly 2026",
  "current_tool": "Word",
  "user_note": "pracujem na navrhu pre vedenie"
}
```

Response:

```json
{
  "success": true,
  "data": {
    "is_work_related": true,
    "suggested_category": "digital strategy",
    "sdk_alignment": "directly aligned with SDK role",
    "recognition_confidence": "high",
    "suggested_message": "Marcel, toto vyzera ako strategicka cinnost SDK. Navrhujem sledovat pracovny blok."
  },
  "error": null
}
```

## 4. Leadership outputs

### Create leadership briefing

`POST /api/leadership-outputs`

Request:

```json
{
  "date_prepared": "2026-09-15",
  "topic": "Copilot training for teachers",
  "output_type": "briefing",
  "summary": "Proposal for internal teacher training focused on safe and practical Copilot use.",
  "related_sdk_area": "AI and Copilot",
  "proposed_decision": "Approve internal training plan",
  "related_work_block_id": "wb_001",
  "next_step": "Consult with principal"
}
```

### Change leadership output status

`PATCH /api/leadership-outputs/{id}/status`

Request:

```json
{
  "status": "submitted"
}
```

### List leadership outputs

`GET /api/leadership-outputs?status=ready`

## 5. Deadlines and alerts

### Create deadline

`POST /api/deadlines`

### List upcoming deadlines

`GET /api/deadlines/upcoming`

### Create alert

`POST /api/alerts`

### Dismiss alert

`POST /api/alerts/{id}/dismiss`

### Complete alert

`POST /api/alerts/{id}/complete`

## 6. Training opportunities

### Create training opportunity

`POST /api/training-opportunities`

### List training opportunities

`GET /api/training-opportunities?target_group=teachers&recommendation_level=recommended`

### Verify training opportunity

`POST /api/training-opportunities/{id}/verify`

### Convert to professional development item

`POST /api/training-opportunities/{id}/convert-to-pdp`

## 7. Professional development plan

### Create professional development item

`POST /api/professional-development-items`

### List professional development items

`GET /api/professional-development-items?target_group=leadership`

### Approve professional development item

`POST /api/professional-development-items/{id}/approve`

### Export professional development plan

`GET /api/professional-development-items/export.xlsx`

## 8. Policy findings

### Create policy finding

`POST /api/policy-findings`

### List policy findings

`GET /api/policy-findings?source=OECD&category=digital-transformation`

### Mark finding as used

`POST /api/policy-findings/{id}/mark-used`

### Generate monthly policy brief

`GET /api/policy-findings/monthly-brief?month=2026-09`

## 9. Documents and evidence

### Register document

`POST /api/documents`

### Register evidence file

`POST /api/evidence-files`

### Link evidence to work block

`POST /api/work-blocks/{id}/link-evidence`

### Link evidence to leadership output

`POST /api/leadership-outputs/{id}/link-evidence`

## 10. Exports

### Export daily log

`GET /api/exports/daily-log.xlsx?date=2026-09-15`

### Export monthly SDK report

`GET /api/exports/monthly-sdk-report.xlsx?month=2026-09`

### Export leadership evidence register

`GET /api/exports/leadership-evidence.xlsx?month=2026-09`

### Export deadlines

`GET /api/exports/deadlines.xlsx`

### Export all evidence

`GET /api/exports/evidence-register.xlsx`

## 11. Settings

### Get settings

`GET /api/settings`

### Update settings

`PATCH /api/settings`

Request:

```json
{
  "voice_input_enabled": true,
  "voice_output_enabled": true,
  "avatar_enabled": true,
  "automatic_tracking_enabled": false,
  "silent_mode": false
}
```

## Safety requirements

The API must reject actions that imply external execution without approval.

Examples of actions requiring explicit confirmation:

- sending email,
- creating calendar event,
- registering for training,
- uploading files,
- deleting files,
- changing permissions,
- exporting sensitive data.

## Audit requirements

Every correction or status change should write to `audit_log`.

Audit event types:

- created,
- updated,
- corrected,
- confirmed,
- archived,
- exported,
- status_changed.

## Final principle

The API must support measurable work, evidence and leadership reporting while keeping the user in control of every external or sensitive action.
