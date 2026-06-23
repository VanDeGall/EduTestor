# Data model for SDK Strategic AI Assistant

## Purpose

This document defines the core data model for the SDK Strategic AI Assistant.

The goal is to make the system programmable and exportable. Each table should support evidence of work, activity tracking, leadership outputs, deadlines, professional development planning, policy monitoring and document organisation.

## Design principles

The data model must support:

- dated evidence,
- measurable work,
- SDK alignment,
- leadership reporting,
- export to spreadsheet,
- correction history,
- user approval,
- privacy and safe data handling.

## Core entities

```text
users
settings
activities
work_blocks
leadership_outputs
deadlines
training_opportunities
professional_development_items
policy_findings
documents
evidence_files
alerts
tags
audit_log
```

## 1. users

Stores basic local user profile information.

| Field | Type | Required | Description |
|---|---|---|---|
| id | string | yes | unique user ID |
| display_name | string | yes | user display name |
| role | string | yes | e.g. school digital coordinator |
| school_name | string | no | school name |
| email | string | no | optional user email |
| created_at | datetime | yes | profile creation time |
| updated_at | datetime | yes | last update |

## 2. settings

Stores user-controlled app settings.

| Field | Type | Required | Description |
|---|---|---|---|
| id | string | yes | settings record ID |
| user_id | string | yes | related user |
| voice_input_enabled | boolean | yes | voice input enabled |
| voice_output_enabled | boolean | yes | voice output enabled |
| avatar_enabled | boolean | yes | avatar visible |
| automatic_tracking_enabled | boolean | yes | automatic work tracking enabled |
| silent_mode | boolean | yes | no voice alerts |
| default_export_folder | string | no | local export path |
| workday_start | time | no | expected start time |
| workday_end | time | no | expected end time |
| updated_at | datetime | yes | last update |

## 3. activities

Stores activity notes, manual entries and extracted tasks.

| Field | Type | Required | Description |
|---|---|---|---|
| id | string | yes | activity ID |
| date | date | yes | activity date |
| time | time | no | activity time |
| raw_note | text | yes | original note or voice transcript |
| clean_activity | text | yes | cleaned activity description |
| category | string | yes | activity category |
| sdk_alignment | string | yes | alignment with SDK role |
| priority | string | yes | critical, high, medium, low, archive |
| size | string | no | S, M, L, XL, ongoing |
| output | text | no | expected or produced output |
| evidence_id | string | no | linked evidence file |
| status | string | yes | draft, confirmed, revised, archived |
| report_include | string | yes | yes, no, maybe, background |
| created_at | datetime | yes | creation time |
| updated_at | datetime | yes | last update |

## 4. work_blocks

Stores tracked work time blocks.

| Field | Type | Required | Description |
|---|---|---|---|
| id | string | yes | work block ID |
| date | date | yes | date |
| start_time | datetime | yes | work start |
| end_time | datetime | no | work end |
| duration_minutes | integer | no | calculated duration |
| activity_id | string | no | linked activity |
| title | string | yes | short work block title |
| category | string | yes | work category |
| sdk_alignment | string | yes | relation to SDK work |
| recognition_confidence | string | no | high, medium, low, non-work |
| tracking_source | string | yes | manual, voice, automatic, calendar, document |
| output | text | no | produced output |
| evidence_id | string | no | linked evidence |
| status | string | yes | active, paused, draft, confirmed, revised, archived |
| leadership_relevance | string | yes | yes, no, maybe |
| next_step | text | no | follow-up recommendation |
| created_at | datetime | yes | creation time |
| updated_at | datetime | yes | last update |

## 5. leadership_outputs

Stores materials prepared for principal or school leadership.

| Field | Type | Required | Description |
|---|---|---|---|
| id | string | yes | leadership output ID |
| date_prepared | date | yes | date prepared |
| topic | string | yes | topic |
| output_type | string | yes | briefing, approval request, risk note, report, action item |
| summary | text | yes | short summary |
| related_sdk_area | string | no | related SDK area |
| proposed_decision | text | no | decision requested from leadership |
| status | string | yes | draft, ready, submitted, discussed, approved, rejected, waiting, revised, archived |
| evidence_id | string | no | linked evidence file |
| related_work_block_id | string | no | linked work block |
| next_step | text | no | next step |
| created_at | datetime | yes | creation time |
| updated_at | datetime | yes | last update |

## 6. deadlines

Stores deadlines, reminders and follow-up dates.

| Field | Type | Required | Description |
|---|---|---|---|
| id | string | yes | deadline ID |
| title | string | yes | deadline title |
| deadline_at | datetime | yes | deadline date/time |
| source | string | no | source of deadline |
| target_group | string | yes | user, teachers, leadership, school |
| category | string | yes | training, report, policy, Erasmus, leadership, document |
| alert_level | string | yes | info, attention, important, critical |
| status | string | yes | open, done, postponed, archived |
| related_entity_type | string | no | activity, leadership_output, training, policy, document |
| related_entity_id | string | no | linked record ID |
| created_at | datetime | yes | creation time |
| updated_at | datetime | yes | last update |

## 7. training_opportunities

Stores external or internal training opportunities.

| Field | Type | Required | Description |
|---|---|---|---|
| id | string | yes | training opportunity ID |
| title | string | yes | training title |
| provider | string | yes | provider |
| source_url | string | no | link to official source |
| target_group | string | yes | user, teachers, leadership, school team |
| area | string | yes | AI, M365, cybersecurity, FCL, Erasmus, leadership, etc. |
| cost | string | no | free, paid, unknown |
| certificate | string | no | certificate or proof type |
| workload | string | no | expected workload |
| deadline_id | string | no | linked deadline |
| recommendation_level | string | yes | must include, recommended, useful later, optional, not suitable now |
| verification_status | string | yes | unverified, verified, outdated |
| notes | text | no | recommendation notes |
| created_at | datetime | yes | creation time |
| updated_at | datetime | yes | last update |

## 8. professional_development_items

Stores items proposed for the professional development plan.

| Field | Type | Required | Description |
|---|---|---|---|
| id | string | yes | item ID |
| target_group | string | yes | user, teachers, leadership, subject team |
| development_need | text | yes | need addressed |
| training_proposal | text | yes | proposed training or activity |
| provider | string | no | provider |
| term | string | no | proposed term |
| expected_output | text | yes | expected practical output |
| evidence | text | no | expected evidence |
| school_strategy_link | text | no | link to school strategy |
| digital_strategy_link | text | no | link to digital strategy |
| priority | string | yes | critical, high, medium, low |
| smart_goal | text | no | connected SMART goal |
| status | string | yes | draft, proposed, approved, completed, archived |
| created_at | datetime | yes | creation time |
| updated_at | datetime | yes | last update |

## 9. policy_findings

Stores monitored policy, strategy and programme findings.

| Field | Type | Required | Description |
|---|---|---|---|
| id | string | yes | finding ID |
| date_checked | date | yes | date checked |
| source | string | yes | OECD, ministry, FCL, European Schoolnet, Erasmus, etc. |
| title | string | yes | finding title |
| source_url | string | no | official source link |
| category | string | yes | policy category |
| key_finding | text | yes | main finding |
| relevance_for_school | text | yes | relevance for school |
| recommended_action | text | no | recommended action |
| leadership_relevance | string | yes | yes, no, maybe |
| document_update_needed | string | yes | yes, no, maybe |
| status | string | yes | new, reviewed, used, archived |
| created_at | datetime | yes | creation time |
| updated_at | datetime | yes | last update |

## 10. documents

Stores registered documents and suggested classification.

| Field | Type | Required | Description |
|---|---|---|---|
| id | string | yes | document ID |
| title | string | yes | document title |
| file_name | string | no | file name |
| file_path | string | no | local path if approved |
| document_type | string | yes | strategy, report, briefing, training, evidence, archive, etc. |
| category | string | yes | document category |
| status | string | yes | draft, reviewed, approved, archived |
| related_activity_id | string | no | linked activity |
| related_work_block_id | string | no | linked work block |
| related_leadership_output_id | string | no | linked leadership output |
| suggested_folder | string | no | recommended folder |
| created_at | datetime | yes | creation time |
| updated_at | datetime | yes | last update |

## 11. evidence_files

Stores evidence references.

| Field | Type | Required | Description |
|---|---|---|---|
| id | string | yes | evidence ID |
| date | date | yes | evidence date |
| title | string | yes | evidence title |
| evidence_type | string | yes | document, report, note, table, training, screenshot, transcript |
| file_name | string | no | file name |
| file_path | string | no | file path if approved |
| related_entity_type | string | no | activity, work_block, leadership_output, training, policy |
| related_entity_id | string | no | linked record ID |
| evidence_value | string | yes | low, medium, high, very high |
| sensitive_data | boolean | yes | contains sensitive data |
| anonymisation_needed | boolean | yes | anonymisation needed |
| status | string | yes | draft, confirmed, revised, archived |
| created_at | datetime | yes | creation time |
| updated_at | datetime | yes | last update |

## 12. alerts

Stores reminders and system notices.

| Field | Type | Required | Description |
|---|---|---|---|
| id | string | yes | alert ID |
| created_at | datetime | yes | alert creation time |
| alert_at | datetime | no | scheduled alert time |
| title | string | yes | alert title |
| message | text | yes | alert message |
| alert_level | string | yes | info, attention, important, critical |
| channel | string | yes | text, voice, avatar, silent |
| status | string | yes | open, shown, dismissed, completed, archived |
| related_entity_type | string | no | linked type |
| related_entity_id | string | no | linked ID |

## 13. tags

Stores reusable tags.

| Field | Type | Required | Description |
|---|---|---|---|
| id | string | yes | tag ID |
| name | string | yes | tag name |
| category | string | no | tag category |
| color | string | no | display colour |

## 14. audit_log

Stores corrections and important changes.

| Field | Type | Required | Description |
|---|---|---|---|
| id | string | yes | audit entry ID |
| timestamp | datetime | yes | change time |
| entity_type | string | yes | changed table/entity |
| entity_id | string | yes | changed record |
| action | string | yes | created, updated, corrected, deleted, exported |
| old_value | text | no | previous value |
| new_value | text | no | new value |
| note | text | no | explanation |

## Export views

The application should provide export views for:

1. daily work log,
2. weekly summary,
3. monthly SDK report,
4. leadership briefing register,
5. evidence register,
6. training opportunities,
7. professional development plan,
8. policy monitoring,
9. document register,
10. deadline overview.

## Required spreadsheet columns for monthly SDK report

| Date | Activity | Category | SDK alignment | Duration | Output | Evidence | Priority | Status | Leadership relevance |
|---|---|---|---|---|---|---|---|---|---|

## Required dashboard indicators

The dashboard should show:

- total work time,
- SDK work time,
- non-SDK work time,
- work without evidence,
- open leadership items,
- upcoming deadlines,
- trainings to consider,
- policy findings to review,
- documents needing approval,
- completed outputs this month.

## Privacy rule

The data model must avoid unnecessary personal data. Sensitive data must be marked and anonymisation should be recommended where needed.

## Final principle

The data model is designed to prove work, organise evidence and support leadership communication. It must remain transparent, user-controlled and exportable.
