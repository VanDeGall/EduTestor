# MVP build backlog for SDK Strategic AI Assistant

## Purpose

This backlog defines the first buildable version of the SDK Strategic AI Assistant.

The MVP must focus on measurable work, evidence, leadership outputs and export. Advanced automation, avatar and voice can be added after the core evidence workflow is reliable.

## MVP goal

The first version should allow the user to:

1. record work activities,
2. track work blocks,
3. classify work as SDK or non-SDK,
4. link outputs and evidence,
5. prepare leadership briefings,
6. track deadlines,
7. export daily and monthly reports.

## MVP scope

### Included

- local database,
- activity inbox,
- manual timer,
- work block table,
- category classification,
- SDK alignment field,
- leadership output register,
- deadline register,
- evidence register,
- XLSX export,
- basic dashboard,
- settings screen.

### Excluded from MVP

- hidden tracking,
- automatic screen monitoring,
- full avatar animation,
- full voice assistant,
- external calendar write actions,
- automatic training registration,
- automatic document submission,
- cloud sync.

## Epic 1: Local database

### Tasks

- Create SQLite database from `database-schema.sql`.
- Create database initialization script.
- Add seed user record.
- Add settings record.
- Add starter tags.
- Add migration mechanism for future updates.

### Acceptance criteria

- Database is created locally.
- All required tables exist.
- App can read and write basic records.

## Epic 2: Activity Inbox

### Tasks

- Create activity list UI.
- Add manual activity form.
- Add fields: raw note, clean activity, category, SDK alignment, priority, size, output, status.
- Add save as draft.
- Add confirm activity.
- Add archive activity.
- Add filter by date, category and status.

### Acceptance criteria

- User can add an activity.
- User can classify an activity.
- User can mark activity as reportable.
- Activity appears in daily and monthly views.

## Epic 3: Work Tracker

### Tasks

- Create timer panel.
- Add start button.
- Add pause button.
- Add stop button.
- Add work category selection.
- Add SDK alignment selection.
- Add output field.
- Add leadership relevance field.
- Save stopped timer as work block.

### Acceptance criteria

- User can start and stop a work block.
- Duration is calculated.
- Work block is saved.
- User can edit category before confirmation.

## Epic 4: Leadership Outputs

### Tasks

- Create leadership outputs list.
- Create briefing note form.
- Create approval request form.
- Add status values: draft, ready, submitted, discussed, approved, rejected, waiting, revised, archived.
- Link leadership output to work block.
- Add next step field.

### Acceptance criteria

- User can create a leadership briefing.
- User can mark it ready for consultation.
- User can link it to evidence.
- User can export leadership register.

## Epic 5: Evidence Register

### Tasks

- Create evidence list.
- Add evidence form.
- Add evidence type field.
- Add evidence value field.
- Add sensitive data flag.
- Add anonymisation needed flag.
- Link evidence to activity, work block or leadership output.

### Acceptance criteria

- User can register evidence.
- User can link evidence to work.
- Sensitive evidence is clearly marked.

## Epic 6: Deadlines and Alerts

### Tasks

- Create deadline list.
- Add deadline form.
- Add target group field.
- Add category field.
- Add alert level field.
- Show upcoming deadlines.
- Mark deadline done.

### Acceptance criteria

- User can create deadlines.
- Upcoming deadlines are visible.
- Critical deadlines are highlighted.

## Epic 7: Dashboard

### Tasks

- Show today's tracked time.
- Show SDK vs non-SDK time.
- Show open leadership outputs.
- Show upcoming deadlines.
- Show activities without evidence.
- Show next recommended step.

### Acceptance criteria

- User can see the current status of work at a glance.
- Dashboard updates after activity or work block creation.

## Epic 8: Exports

### Tasks

- Export daily work log to XLSX.
- Export monthly SDK report to XLSX.
- Export leadership evidence register to XLSX.
- Export deadline overview to XLSX.
- Export professional development plan to XLSX if data exists.
- Add colour coding.
- Add safe file naming.

### Acceptance criteria

- Export files open correctly.
- Columns match export specification.
- Priority and status colours are visible.

## Epic 9: Settings

### Tasks

- Create settings screen.
- Add toggles for avatar, voice input, voice output, automatic tracking and silent mode.
- Add default export folder setting.
- Add working hours setting.
- Add privacy warning settings.

### Acceptance criteria

- User can change settings.
- Automatic tracking is off by default.
- Export location can be selected.

## Epic 10: Basic assistant prompts

### Tasks

- Add suggested classification messages.
- Add leadership relevance prompts.
- Add work without evidence warnings.
- Add end-of-day summary prompt.
- Add deadline prompt.

### Acceptance criteria

- Assistant suggests useful next steps.
- Assistant does not perform external actions.
- User can reject suggestions.

## MVP user stories

### Story 1: Record work activity

As a school digital coordinator, I want to record a work activity quickly so that I can later prove what I did.

### Story 2: Track time

As a school digital coordinator, I want to start and stop a timer so that I can measure real work time.

### Story 3: Prepare leadership output

As a school digital coordinator, I want to create a leadership briefing from my work so that I can discuss it with the principal.

### Story 4: Export monthly report

As a school digital coordinator, I want to export a monthly report so that I can document my work.

### Story 5: Mark non-SDK work

As a school digital coordinator, I want to mark a task as non-SDK so that my report clearly distinguishes my main professional role from other tasks.

## MVP acceptance test

The MVP is usable when the user can complete this workflow:

1. Add three activities.
2. Start and stop one work block.
3. Mark one item as leadership relevant.
4. Create one leadership briefing.
5. Add one deadline.
6. Register one evidence file.
7. Export daily work log.
8. Export monthly SDK report.

## Post-MVP backlog

After MVP, add:

1. voice notes,
2. transcript processing,
3. avatar interface,
4. automatic work-context recognition,
5. policy monitoring,
6. training opportunity monitoring,
7. DOCX/PDF exports,
8. local document organisation,
9. optional calendar integration,
10. optional AI API integration.

## Final principle

The MVP must first prove the user's work. Every other feature is secondary until the evidence workflow is stable.
