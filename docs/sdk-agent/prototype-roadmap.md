# Prototype roadmap for SDK Strategic AI Assistant

## Purpose

This roadmap defines the recommended development phases for the SDK Strategic AI Assistant.

The goal is to build the assistant in realistic stages, starting with a safe and useful prototype and gradually moving toward a full local application with avatar, voice, work tracking, evidence management and strategic monitoring.

## Development principle

Build the system in layers.

Do not start with full automation. Start with a controlled, transparent, user-approved workflow that produces immediate value.

## Phase 1: Manual evidence prototype

### Goal

Create a simple prototype that allows the user to record activities, classify them and export a daily or monthly evidence table.

### Core features

- activity inbox,
- manual activity entry,
- category selection,
- SDK alignment selection,
- priority selection,
- work size selection,
- output/evidence field,
- daily summary,
- monthly summary,
- XLSX export.

### Required output

- daily work log,
- monthly SDK report draft,
- evidence table,
- leadership item list.

### Success criteria

The user can record one week of work and export a structured table showing:

- what was done,
- when it was done,
- whether it belongs to SDK work,
- what output was created,
- what should be shown to leadership.

## Phase 2: Leadership evidence prototype

### Goal

Add support for outputs that should be discussed with the principal or leadership team.

### Core features

- leadership briefing generator,
- approval request generator,
- consultation proposal generator,
- leadership evidence register,
- decision status tracking,
- suggested file naming.

### Required output

- dated briefing note,
- approval request,
- leadership evidence table,
- monthly list of items for leadership.

### Success criteria

The user can generate and store dated materials for school leadership as proof of professional SDK work.

## Phase 3: Timer and work block tracking

### Goal

Add transparent work time tracking controlled by the user.

### Core features

- start work timer,
- pause timer,
- stop timer,
- classify work block,
- correct category,
- save work block,
- mark non-SDK work,
- daily tracked time summary.

### Required output

- work session table,
- time by category,
- SDK vs non-SDK time,
- work without evidence warning.

### Success criteria

The user can prove work time by category without hidden monitoring.

## Phase 4: Voice note support

### Goal

Allow the user to record or dictate work notes and convert them into structured activity records.

### Core features

- voice input,
- transcript preview,
- activity extraction,
- category proposal,
- priority proposal,
- evidence proposal,
- confirmation before saving.

### Required output

- structured activity records from voice notes,
- daily summary from spoken notes,
- suggested leadership items.

### Success criteria

The user can speak several work notes during the day and turn them into a clean evidence table.

## Phase 5: Avatar and notification interface

### Goal

Add visible assistant interface for text, voice and alerts.

### Core features

- floating avatar,
- text bubble alerts,
- voice output toggle,
- silent mode,
- notification states,
- short colleague-style reminders,
- review-needed status.

### Required output

- avatar state model,
- notification centre,
- user-controlled alert settings.

### Success criteria

The assistant can notify the user about important work items without becoming intrusive.

## Phase 6: Automatic work-context recognition

### Goal

Recognise likely school or SDK work from approved visible signals.

### Core features

- approved workspace recognition,
- approved document title recognition,
- approved task context,
- confidence level,
- suggested classification,
- user correction.

### Required output

- work-context suggestion,
- recognition confidence,
- corrected classification log.

### Success criteria

The assistant can suggest that the user is working on a school or SDK matter and ask whether to track it.

## Phase 7: Professional development and training planner

### Goal

Track training opportunities and recommend realistic items for the professional development plan.

### Core features

- training register,
- deadline list,
- target group classification,
- recommendation level,
- professional development plan export,
- SMART connection.

### Required output

- training overview,
- professional development plan table,
- recommended training by target group,
- reminders for deadlines.

### Success criteria

The user can prepare a realistic professional development proposal for himself, teachers and leadership.

## Phase 8: Policy and strategy monitoring

### Goal

Connect school planning with OECD, ministry, FCL, European Schoolnet and Erasmus+ sources.

### Core features

- source register,
- policy finding table,
- category classification,
- SMART goal recommendations,
- strategic alignment notes,
- monthly policy brief.

### Required output

- policy monitoring table,
- strategic recommendations,
- school document update suggestions,
- leadership briefing items.

### Success criteria

The user can show that school digital strategy is informed by recognised policy and innovation sources.

## Phase 9: Document organisation assistant

### Goal

Help organise documents and evidence into a clean folder structure.

### Core features

- suggested file names,
- folder recommendations,
- duplicate warning,
- draft vs approved distinction,
- archive support,
- document evidence links.

### Required output

- document register,
- file naming suggestions,
- folder structure plan,
- archive table.

### Success criteria

The user no longer keeps SDK work notes and outputs scattered across folders.

## Phase 10: Integrated local app

### Goal

Combine all modules into a complete local desktop application.

### Core features

- avatar,
- voice,
- activity inbox,
- work tracking,
- evidence register,
- leadership outputs,
- training planner,
- policy monitor,
- document archive,
- spreadsheet export,
- user permissions.

### Required output

- full SDK assistant prototype,
- local database,
- export tools,
- user settings,
- safety controls.

### Success criteria

The user can manage daily SDK work, outputs, leadership communication, policy monitoring and professional development from one assistant.

## Minimum viable product

The first usable MVP should include:

1. activity inbox,
2. manual timer,
3. category classification,
4. SDK alignment field,
5. evidence field,
6. daily summary,
7. monthly report draft,
8. XLSX export,
9. leadership briefing generator,
10. visible approval rules.

## Development priority

Build in this order:

1. evidence table,
2. category model,
3. daily and monthly summaries,
4. leadership outputs,
5. timer,
6. voice notes,
7. avatar,
8. automatic recognition,
9. policy and training monitoring,
10. full integrations.

## Final principle

The prototype must first make the user's work visible and measurable. Advanced automation should come only after the evidence workflow is reliable.
