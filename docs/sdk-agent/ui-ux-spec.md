# UI and UX specification for SDK Strategic AI Assistant

## Purpose

This document defines the user interface and user experience requirements for the SDK Strategic AI Assistant local application.

The interface must be practical, fast and focused on evidence of work, work tracking, leadership outputs and daily support.

## UX principles

The application should be:

- simple,
- visible but not intrusive,
- fast to use during work,
- controlled by the user,
- suitable for text and voice,
- focused on outputs and evidence,
- safe for school context.

## Main screens

The application should contain these screens:

1. Dashboard,
2. Activity Inbox,
3. Work Tracker,
4. Leadership Outputs,
5. Evidence Register,
6. Deadlines and Alerts,
7. Professional Development,
8. Policy Monitor,
9. Documents,
10. Exports,
11. Settings.

## 1. Dashboard

### Purpose

The dashboard gives the user an immediate overview of work, deadlines and pending outputs.

### Required widgets

- active work timer,
- today tracked time,
- SDK work time,
- non-SDK work time,
- open leadership items,
- upcoming deadlines,
- activities without evidence,
- documents needing approval,
- monthly progress,
- recommended next action.

### Main dashboard message

The assistant should show a short daily message:

```text
Marcel, dnes mas rozpracovane 3 pracovne bloky, 1 podklad pre vedenie a 2 terminy na sledovanie.
```

## 2. Activity Inbox

### Purpose

The Activity Inbox collects raw notes, voice notes, detected work blocks and unclassified items.

### Required columns

| Date | Raw note | Clean activity | Category | SDK alignment | Priority | Size | Output | Status |
|---|---|---|---|---|---|---|---|---|

### Required actions

- Add manual note,
- Add voice note,
- Split note into activities,
- Classify activity,
- Change category,
- Mark as SDK,
- Mark as non-SDK,
- Link evidence,
- Include in report,
- Archive.

## 3. Work Tracker

### Purpose

Tracks work blocks transparently.

### Required elements

- Start button,
- Pause button,
- Stop button,
- Current category,
- SDK alignment,
- Recognition confidence,
- Output field,
- Evidence field,
- Leadership relevance switch.

### Required states

- inactive,
- active,
- paused,
- waiting for confirmation,
- saved.

### Work tracker prompt

```text
Marcel, mam tento blok ulozit ako cinnost SDK?
```

## 4. Leadership Outputs

### Purpose

Stores and prepares materials for the principal and school leadership.

### Required output types

- Briefing note,
- Approval request,
- Consultation proposal,
- Risk note,
- Action plan item,
- Monthly report section.

### Required columns

| Date | Topic | Output type | Decision needed | Status | Evidence | Next step |
|---|---|---|---|---|---|---|

### Required actions

- Create briefing,
- Create approval request,
- Mark as ready,
- Mark as submitted,
- Mark as discussed,
- Mark as approved,
- Mark as rejected,
- Link work block,
- Export document.

## 5. Evidence Register

### Purpose

Keeps proof of work.

### Required columns

| Date | Evidence title | Type | Related activity | Evidence value | Sensitive data | Status |
|---|---|---|---|---|---|---|

### Evidence value levels

- low,
- medium,
- high,
- very high.

### Required actions

- Add evidence,
- Link to activity,
- Link to leadership output,
- Mark sensitive,
- Mark anonymisation needed,
- Archive.

## 6. Deadlines and Alerts

### Purpose

Shows deadlines, reminders and important alerts.

### Required columns

| Deadline | Title | Category | Target group | Alert level | Status |
|---|---|---|---|---|---|

### Alert levels

- info,
- attention,
- important,
- critical.

### Required actions

- Add deadline,
- Snooze,
- Mark done,
- Link to training,
- Link to leadership item,
- Create reminder.

## 7. Professional Development

### Purpose

Plans trainings and development items for the user, teachers and leadership.

### Required columns

| Target group | Development need | Training proposal | Provider | Term | Output | Priority | Status |
|---|---|---|---|---|---|---|---|

### Required actions

- Add training proposal,
- Add to professional development plan,
- Mark recommended,
- Mark must include,
- Export plan,
- Link SMART goal.

## 8. Policy Monitor

### Purpose

Tracks OECD, ministry, FCL, European Schoolnet, Erasmus+ and similar policy or strategy findings.

### Required columns

| Date checked | Source | Topic | Category | Relevance for school | Recommended action | Leadership relevance |
|---|---|---|---|---|---|---|

### Required actions

- Add finding,
- Mark reviewed,
- Mark used,
- Convert to leadership briefing,
- Convert to SMART goal,
- Export monthly policy brief.

## 9. Documents

### Purpose

Organises school and SDK documents.

### Required columns

| Title | File name | Type | Category | Status | Suggested folder | Evidence link |
|---|---|---|---|---|---|---|

### Required actions

- Register document,
- Suggest file name,
- Suggest folder,
- Link evidence,
- Mark draft,
- Mark approved,
- Archive.

## 10. Exports

### Purpose

Allows the user to export work outputs.

### Required exports

- Daily work log XLSX,
- Weekly summary XLSX,
- Monthly SDK report XLSX/DOCX,
- Leadership evidence XLSX/DOCX,
- Professional development plan XLSX/DOCX,
- Deadline overview XLSX,
- Policy monitoring brief DOCX/PDF,
- Document register XLSX.

## 11. Settings

### Required settings

- voice input on/off,
- voice output on/off,
- avatar on/off,
- automatic tracking on/off,
- silent mode,
- default export folder,
- working hours,
- alert preferences,
- data privacy settings.

## Floating avatar requirements

The avatar should support:

- minimal mode,
- expanded mode,
- listening state,
- thinking state,
- work tracking state,
- alert state,
- silent state.

The avatar should not interrupt unless alert level is important or critical.

## Voice UX

Voice input workflow:

1. user presses microphone,
2. app records user speech,
3. transcript is shown,
4. agent proposes structured activity,
5. user confirms or edits,
6. record is saved.

Voice output workflow:

1. agent prepares short message,
2. checks silent mode,
3. speaks only if voice output is enabled,
4. also shows text version.

## Colour system

Recommended colour semantics:

- red: critical,
- orange: high,
- yellow: medium,
- green: completed or low risk,
- blue: leadership,
- purple: waiting or attention,
- gray: archive or non-active,
- dark gray: non-SDK work.

## Accessibility requirements

The app should support:

- readable font sizes,
- high contrast option,
- keyboard navigation,
- silent mode,
- no forced voice interaction,
- exportable text outputs.

## Final principle

The UI must not feel like surveillance software. It must feel like a professional work dashboard that helps the user prove, organise and defend real SDK work.
