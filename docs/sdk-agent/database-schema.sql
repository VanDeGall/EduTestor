-- Database schema for SDK Strategic AI Assistant
-- Target: SQLite-compatible first prototype
-- Purpose: activity tracking, evidence, leadership outputs, deadlines, training, policy monitoring and document register

PRAGMA foreign_keys = ON;

-- =====================================================
-- USERS AND SETTINGS
-- =====================================================

CREATE TABLE IF NOT EXISTS users (
    id TEXT PRIMARY KEY,
    display_name TEXT NOT NULL,
    role TEXT NOT NULL,
    school_name TEXT,
    email TEXT,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS settings (
    id TEXT PRIMARY KEY,
    user_id TEXT NOT NULL,
    voice_input_enabled INTEGER NOT NULL DEFAULT 0,
    voice_output_enabled INTEGER NOT NULL DEFAULT 0,
    avatar_enabled INTEGER NOT NULL DEFAULT 1,
    automatic_tracking_enabled INTEGER NOT NULL DEFAULT 0,
    silent_mode INTEGER NOT NULL DEFAULT 0,
    default_export_folder TEXT,
    workday_start TEXT,
    workday_end TEXT,
    updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- =====================================================
-- ACTIVITIES AND WORK BLOCKS
-- =====================================================

CREATE TABLE IF NOT EXISTS activities (
    id TEXT PRIMARY KEY,
    date TEXT NOT NULL,
    time TEXT,
    raw_note TEXT NOT NULL,
    clean_activity TEXT NOT NULL,
    category TEXT NOT NULL,
    sdk_alignment TEXT NOT NULL,
    priority TEXT NOT NULL DEFAULT 'medium',
    size TEXT,
    output TEXT,
    evidence_id TEXT,
    status TEXT NOT NULL DEFAULT 'draft',
    report_include TEXT NOT NULL DEFAULT 'maybe',
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (evidence_id) REFERENCES evidence_files(id)
);

CREATE TABLE IF NOT EXISTS work_blocks (
    id TEXT PRIMARY KEY,
    date TEXT NOT NULL,
    start_time TEXT NOT NULL,
    end_time TEXT,
    duration_minutes INTEGER,
    activity_id TEXT,
    title TEXT NOT NULL,
    category TEXT NOT NULL,
    sdk_alignment TEXT NOT NULL,
    recognition_confidence TEXT,
    tracking_source TEXT NOT NULL DEFAULT 'manual',
    output TEXT,
    evidence_id TEXT,
    status TEXT NOT NULL DEFAULT 'draft',
    leadership_relevance TEXT NOT NULL DEFAULT 'maybe',
    next_step TEXT,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (activity_id) REFERENCES activities(id),
    FOREIGN KEY (evidence_id) REFERENCES evidence_files(id)
);

-- =====================================================
-- LEADERSHIP OUTPUTS
-- =====================================================

CREATE TABLE IF NOT EXISTS leadership_outputs (
    id TEXT PRIMARY KEY,
    date_prepared TEXT NOT NULL,
    topic TEXT NOT NULL,
    output_type TEXT NOT NULL,
    summary TEXT NOT NULL,
    related_sdk_area TEXT,
    proposed_decision TEXT,
    status TEXT NOT NULL DEFAULT 'draft',
    evidence_id TEXT,
    related_work_block_id TEXT,
    next_step TEXT,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (evidence_id) REFERENCES evidence_files(id),
    FOREIGN KEY (related_work_block_id) REFERENCES work_blocks(id)
);

-- =====================================================
-- DEADLINES AND ALERTS
-- =====================================================

CREATE TABLE IF NOT EXISTS deadlines (
    id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    deadline_at TEXT NOT NULL,
    source TEXT,
    target_group TEXT NOT NULL,
    category TEXT NOT NULL,
    alert_level TEXT NOT NULL DEFAULT 'attention',
    status TEXT NOT NULL DEFAULT 'open',
    related_entity_type TEXT,
    related_entity_id TEXT,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS alerts (
    id TEXT PRIMARY KEY,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    alert_at TEXT,
    title TEXT NOT NULL,
    message TEXT NOT NULL,
    alert_level TEXT NOT NULL DEFAULT 'info',
    channel TEXT NOT NULL DEFAULT 'text',
    status TEXT NOT NULL DEFAULT 'open',
    related_entity_type TEXT,
    related_entity_id TEXT
);

-- =====================================================
-- TRAINING AND PROFESSIONAL DEVELOPMENT
-- =====================================================

CREATE TABLE IF NOT EXISTS training_opportunities (
    id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    provider TEXT NOT NULL,
    source_url TEXT,
    target_group TEXT NOT NULL,
    area TEXT NOT NULL,
    cost TEXT,
    certificate TEXT,
    workload TEXT,
    deadline_id TEXT,
    recommendation_level TEXT NOT NULL DEFAULT 'recommended',
    verification_status TEXT NOT NULL DEFAULT 'unverified',
    notes TEXT,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (deadline_id) REFERENCES deadlines(id)
);

CREATE TABLE IF NOT EXISTS professional_development_items (
    id TEXT PRIMARY KEY,
    target_group TEXT NOT NULL,
    development_need TEXT NOT NULL,
    training_proposal TEXT NOT NULL,
    provider TEXT,
    term TEXT,
    expected_output TEXT NOT NULL,
    evidence TEXT,
    school_strategy_link TEXT,
    digital_strategy_link TEXT,
    priority TEXT NOT NULL DEFAULT 'medium',
    smart_goal TEXT,
    status TEXT NOT NULL DEFAULT 'draft',
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- =====================================================
-- POLICY AND STRATEGY MONITORING
-- =====================================================

CREATE TABLE IF NOT EXISTS policy_findings (
    id TEXT PRIMARY KEY,
    date_checked TEXT NOT NULL,
    source TEXT NOT NULL,
    title TEXT NOT NULL,
    source_url TEXT,
    category TEXT NOT NULL,
    key_finding TEXT NOT NULL,
    relevance_for_school TEXT NOT NULL,
    recommended_action TEXT,
    leadership_relevance TEXT NOT NULL DEFAULT 'maybe',
    document_update_needed TEXT NOT NULL DEFAULT 'maybe',
    status TEXT NOT NULL DEFAULT 'new',
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- =====================================================
-- DOCUMENTS AND EVIDENCE
-- =====================================================

CREATE TABLE IF NOT EXISTS evidence_files (
    id TEXT PRIMARY KEY,
    date TEXT NOT NULL,
    title TEXT NOT NULL,
    evidence_type TEXT NOT NULL,
    file_name TEXT,
    file_path TEXT,
    related_entity_type TEXT,
    related_entity_id TEXT,
    evidence_value TEXT NOT NULL DEFAULT 'medium',
    sensitive_data INTEGER NOT NULL DEFAULT 0,
    anonymisation_needed INTEGER NOT NULL DEFAULT 0,
    status TEXT NOT NULL DEFAULT 'draft',
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS documents (
    id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    file_name TEXT,
    file_path TEXT,
    document_type TEXT NOT NULL,
    category TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'draft',
    related_activity_id TEXT,
    related_work_block_id TEXT,
    related_leadership_output_id TEXT,
    suggested_folder TEXT,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (related_activity_id) REFERENCES activities(id),
    FOREIGN KEY (related_work_block_id) REFERENCES work_blocks(id),
    FOREIGN KEY (related_leadership_output_id) REFERENCES leadership_outputs(id)
);

-- =====================================================
-- TAGS AND AUDIT LOG
-- =====================================================

CREATE TABLE IF NOT EXISTS tags (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    category TEXT,
    color TEXT
);

CREATE TABLE IF NOT EXISTS entity_tags (
    id TEXT PRIMARY KEY,
    entity_type TEXT NOT NULL,
    entity_id TEXT NOT NULL,
    tag_id TEXT NOT NULL,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (tag_id) REFERENCES tags(id)
);

CREATE TABLE IF NOT EXISTS audit_log (
    id TEXT PRIMARY KEY,
    timestamp TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    entity_type TEXT NOT NULL,
    entity_id TEXT NOT NULL,
    action TEXT NOT NULL,
    old_value TEXT,
    new_value TEXT,
    note TEXT
);

-- =====================================================
-- INDEXES
-- =====================================================

CREATE INDEX IF NOT EXISTS idx_activities_date ON activities(date);
CREATE INDEX IF NOT EXISTS idx_activities_category ON activities(category);
CREATE INDEX IF NOT EXISTS idx_activities_sdk_alignment ON activities(sdk_alignment);
CREATE INDEX IF NOT EXISTS idx_work_blocks_date ON work_blocks(date);
CREATE INDEX IF NOT EXISTS idx_work_blocks_category ON work_blocks(category);
CREATE INDEX IF NOT EXISTS idx_work_blocks_status ON work_blocks(status);
CREATE INDEX IF NOT EXISTS idx_leadership_outputs_date ON leadership_outputs(date_prepared);
CREATE INDEX IF NOT EXISTS idx_leadership_outputs_status ON leadership_outputs(status);
CREATE INDEX IF NOT EXISTS idx_deadlines_deadline_at ON deadlines(deadline_at);
CREATE INDEX IF NOT EXISTS idx_deadlines_status ON deadlines(status);
CREATE INDEX IF NOT EXISTS idx_training_target_group ON training_opportunities(target_group);
CREATE INDEX IF NOT EXISTS idx_policy_source ON policy_findings(source);
CREATE INDEX IF NOT EXISTS idx_policy_category ON policy_findings(category);
CREATE INDEX IF NOT EXISTS idx_documents_type ON documents(document_type);
CREATE INDEX IF NOT EXISTS idx_evidence_date ON evidence_files(date);

-- =====================================================
-- EXPORT VIEWS
-- =====================================================

CREATE VIEW IF NOT EXISTS monthly_sdk_report_view AS
SELECT
    wb.date AS date,
    wb.title AS activity,
    wb.category AS category,
    wb.sdk_alignment AS sdk_alignment,
    wb.duration_minutes AS duration_minutes,
    wb.output AS output,
    ef.file_name AS evidence_file,
    wb.status AS status,
    wb.leadership_relevance AS leadership_relevance
FROM work_blocks wb
LEFT JOIN evidence_files ef ON wb.evidence_id = ef.id;

CREATE VIEW IF NOT EXISTS leadership_evidence_view AS
SELECT
    lo.date_prepared AS date_prepared,
    lo.topic AS topic,
    lo.output_type AS output_type,
    lo.summary AS summary,
    lo.proposed_decision AS proposed_decision,
    lo.status AS status,
    ef.file_name AS evidence_file,
    lo.next_step AS next_step
FROM leadership_outputs lo
LEFT JOIN evidence_files ef ON lo.evidence_id = ef.id;

CREATE VIEW IF NOT EXISTS upcoming_deadlines_view AS
SELECT
    id,
    title,
    deadline_at,
    target_group,
    category,
    alert_level,
    status
FROM deadlines
WHERE status = 'open'
ORDER BY deadline_at ASC;

CREATE VIEW IF NOT EXISTS professional_development_export_view AS
SELECT
    target_group,
    development_need,
    training_proposal,
    provider,
    term,
    expected_output,
    evidence,
    school_strategy_link,
    digital_strategy_link,
    priority,
    smart_goal,
    status
FROM professional_development_items;

-- =====================================================
-- STARTER TAGS
-- =====================================================

INSERT OR IGNORE INTO tags (id, name, category, color) VALUES
('tag_sdk', 'SDK', 'work-type', 'green'),
('tag_leadership', 'Leadership', 'output', 'blue'),
('tag_ai', 'AI', 'topic', 'purple'),
('tag_m365', 'Microsoft 365', 'topic', 'blue'),
('tag_training', 'Training', 'topic', 'orange'),
('tag_policy', 'Policy', 'topic', 'gray'),
('tag_evidence', 'Evidence', 'output', 'green');
