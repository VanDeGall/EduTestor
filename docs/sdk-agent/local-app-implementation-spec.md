# Local app implementation specification

## Purpose

This document defines the implementation requirements for a future local desktop application of the SDK Strategic AI Assistant.

The goal is to move the assistant from a document-based blueprint into a real working application that can support the school digital coordinator during daily work.

## Target application

The application should run as a local or hybrid desktop assistant.

It should provide:

- visible avatar,
- text chat,
- voice input,
- voice output,
- work tracking,
- activity inbox,
- task classification,
- evidence register,
- leadership briefing generator,
- spreadsheet export,
- reminder and deadline centre,
- document organisation support,
- safe integration with school tools.

## Main interface components

### 1. Floating avatar

The avatar should be visible as a small floating assistant panel.

It should support these states:

- Ready,
- Listening,
- Thinking,
- Tracking work,
- Alert,
- Draft ready,
- Waiting for approval,
- Silent mode.

The avatar must not obstruct normal work. It should be movable and minimisable.

### 2. Chat panel

The chat panel should show:

- user instructions,
- agent responses,
- activity suggestions,
- classification proposals,
- leadership outputs,
- reminders,
- warnings,
- generated drafts.

### 3. Voice controls

The application should include:

- microphone button,
- push-to-talk option,
- voice output toggle,
- silent mode,
- transcript preview,
- confirmation before saving voice-derived notes.

### 4. Work tracking panel

The work tracking panel should show:

- current timer,
- current category,
- SDK alignment,
- active document or task title if approved,
- pause button,
- stop button,
- save block button,
- change category button,
- evidence field.

### 5. Activity inbox

The activity inbox should collect:

- manual notes,
- voice notes,
- automatic work blocks,
- imported tasks,
- leadership items,
- training items,
- reminders,
- unclassified activities.

Each activity should be reviewed before being locked into the evidence register.

## Core workflows

### Start of work workflow

1. User opens the app or starts tracking.
2. App shows visible tracking status.
3. Agent detects or asks for work context.
4. User confirms or changes category.
5. Timer starts.
6. Activity is saved as a draft work block.

Example prompt:

```text
Marcel, vyzera to, ze pracujes na pracovnej veci. Mam to sledovat ako pracovny blok?
```

### Automatic work recognition workflow

The app may recognise work context from approved signals:

- selected work category,
- approved document title,
- approved workspace,
- approved task list,
- manual note,
- voice note,
- calendar item,
- visible file path chosen by user.

The app must not secretly capture screen, keystrokes, private messages or browser history.

### End of work block workflow

1. User stops or pauses tracking.
2. Agent summarises the work block.
3. Agent proposes category, output and evidence.
4. User confirms or edits.
5. Record is saved to the work log.

### Daily summary workflow

At the end of the day, the assistant prepares:

- total tracked time,
- SDK time,
- non-SDK time,
- outputs created,
- open tasks,
- leadership items,
- evidence files,
- next recommended step.

### Leadership output workflow

When a work item is relevant for school leadership, the assistant should ask:

```text
Marcel, toto je vhodne pripravit ako podklad pre riaditela. Mam z toho vytvorit briefing alebo navrh na schvalenie?
```

Possible outputs:

- briefing note,
- approval request,
- consultation proposal,
- risk note,
- action plan item,
- monthly report section.

## Data model

### Work block

| Field | Description |
|---|---|
| id | unique work block ID |
| date | date of work |
| start_time | start time |
| end_time | end time |
| duration | calculated time |
| raw_note | original note or detected context |
| clean_activity | refined activity description |
| category | work category |
| sdk_alignment | relation to SDK role |
| confidence | recognition confidence |
| output | produced output |
| evidence | evidence link or file name |
| status | draft, confirmed, revised, archived |
| leadership_relevance | yes, no, maybe |
| next_step | recommended follow-up |

### Leadership item

| Field | Description |
|---|---|
| id | unique leadership item ID |
| date_prepared | date prepared |
| topic | topic |
| output_type | briefing, approval request, risk note, report |
| decision_needed | what decision is needed |
| status | draft, ready, submitted, discussed, approved, rejected |
| related_work_block | link to work record |
| evidence_file | file name or path |

### Deadline item

| Field | Description |
|---|---|
| id | unique deadline ID |
| deadline | date and time |
| title | deadline title |
| source | source of deadline |
| target_group | user, teachers, leadership, school |
| category | training, report, policy, Erasmus, leadership |
| alert_level | info, attention, important, critical |
| status | open, done, postponed, archived |

## Export requirements

The app should export:

- daily work log,
- weekly summary,
- monthly SDK report,
- leadership evidence table,
- professional development plan table,
- training deadline overview,
- policy monitoring summary.

Preferred formats:

- XLSX,
- CSV,
- DOCX,
- PDF,
- Markdown.

## Spreadsheet export

The spreadsheet should include colour coding:

- critical: red,
- high: orange,
- medium: yellow,
- low: green,
- archive: gray,
- non-SDK work: dark gray,
- personal/non-work: blue-gray,
- waiting: purple,
- completed: green marker.

## Local folders

Recommended folder structure:

```text
SDK-dokumentacia/
├── 01-denne-zaznamy/
├── 02-tyzdenne-suhrny/
├── 03-mesacne-reporty/
├── 04-vykaz-cinnosti/
├── 05-podklady-pre-vedenie/
├── 06-schvalene-vystupy/
├── 07-skolenia/
├── 08-profesijny-rozvoj/
├── 09-policy-monitoring/
├── 10-ai-a-nastroje/
├── 11-m365/
├── 12-fcl-erasmus-oecd/
└── 99-archiv/
```

## File naming rule

Use this pattern:

```text
YYYY-MM-DD_area_output-type_short-title_v01
```

Examples:

```text
2026-09-15_vedenie_navrh-schvalenie_Copilot-skolenie_v01.docx
2026-09-20_sdk-vykaz_denny-zaznam_pondelok_v01.xlsx
2026-10-01_profesijny-rozvoj_navrh-skoleni_AI-ucitelia_v01.docx
```

## Permission model

The application should have separate permissions for:

- voice input,
- voice output,
- local file access,
- calendar access,
- document folder access,
- work tracking,
- notifications,
- cloud integrations,
- export location.

Each permission must be visible and reversible.

## Privacy and safety rules

The app must not:

- secretly record screen,
- capture keystrokes,
- read private messages,
- monitor other employees,
- monitor pupils,
- upload files without approval,
- send documents without approval,
- create events without approval,
- register anyone for trainings without approval.

## Required user controls

The user must always be able to:

- pause tracking,
- stop tracking,
- change category,
- delete draft record,
- correct activity classification,
- mark activity as non-SDK,
- switch to silent mode,
- disable voice output,
- disable automatic recognition,
- export or not export data.

## Technical implementation options

Possible implementation paths:

1. Local desktop app with Python and a web UI.
2. Electron or Tauri desktop app.
3. Progressive web app with local storage and optional desktop wrapper.
4. Microsoft Power Platform prototype.
5. Hybrid app connected to ChatGPT or another LLM API.

## Recommended first prototype

The first prototype should include:

- local activity inbox,
- manual timer,
- category selection,
- voice note field,
- avatar placeholder,
- daily summary,
- XLSX export,
- leadership briefing generator,
- no hidden tracking.

## Final principle

The local app is not meant to monitor the user against his will. It is a personal professional evidence system that helps the school digital coordinator prove work, organise tasks, prepare leadership outputs and keep strategic school development under control.
