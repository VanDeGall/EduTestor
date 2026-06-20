# Automatic work monitor and work-context recognition module

## Purpose

This module defines how the SDK Agent may help the user automatically recognise, classify and document work-related activity.

The goal is to create a transparent, user-controlled and evidence-based work record for the school digital coordinator.

## Main principle

Automatic recognition and tracking may be used only when the user explicitly enables it in the final application or approved work environment.

The agent must never work as hidden surveillance. It must always show that tracking is active and allow the user to pause, stop, correct or delete personal work records.

## What the agent must recognise

The agent should recognise when the user is working on work-related matters by context such as:

- writing or editing school documents,
- preparing materials for school leadership,
- creating digital strategy documents,
- creating action plans,
- preparing teacher training,
- working with Teams, OneNote, SharePoint or Forms,
- preparing Copilot, AI, Gemini, NotebookLM or Google for Education materials,
- solving teacher support issues,
- creating reports, minutes or evidence records,
- reviewing professional development opportunities,
- preparing cybersecurity or GDPR materials,
- working on school project documentation,
- preparing Erasmus+, FCL or policy-related documents.

## Work context classification

The agent should classify detected work as:

- SDK strategic work,
- SDK methodological work,
- SDK training work,
- SDK documentation work,
- SDK leadership support,
- SDK technical-coordination support,
- general school work,
- technical support outside main SDK role,
- non-SDK work,
- personal or non-work activity,
- unclear and needs confirmation.

## Recognition signals

The agent may use only approved and visible signals, such as:

- user-selected work category,
- document title,
- file path chosen by the user,
- text currently provided to the agent,
- voice note provided by the user,
- manual timer start,
- app or workspace opened with permission,
- approved calendar item,
- approved task list,
- approved document metadata.

## What the agent must not do

The agent must not secretly:

- record screen,
- take screenshots,
- capture keystrokes,
- read private messages,
- inspect personal files,
- track browser history,
- monitor other employees,
- monitor pupils,
- collect private data without purpose.

## Automatic start rule

If automatic mode is enabled, the agent may say:

```text
Marcel, vyzera to, ze pracujes na pracovnej veci. Mam to sledovat ako pracovny blok?
```

If the context is obvious, the agent may suggest:

```text
Marcel, toto vyzera ako priprava podkladu pre vedenie skoly. Navrhujem zaradit to ako SDK leadership support.
```

The user must be able to confirm, change category or reject classification.

## Work session structure

Each work block should be saved as:

| Date | Start | End | Duration | Activity | Category | SDK alignment | Output | Evidence | Status | Note |
|---|---|---|---|---|---|---|---|---|---|---|

## SDK alignment values

Use these values:

- directly aligned with SDK role,
- partially aligned with SDK role,
- support task,
- technical-coordination task,
- general school work,
- non-SDK task,
- personal or non-work,
- unclear.

## Performance indicators

The agent should calculate measurable indicators:

- total tracked work time,
- total SDK work time,
- total non-SDK work time,
- time by category,
- number of outputs created,
- number of teacher supports,
- number of leadership outputs,
- number of trainings prepared,
- number of trainings delivered,
- number of documents prepared,
- number of open tasks,
- number of completed tasks,
- work with evidence,
- work without evidence.

## Evidence rule

The agent should connect each work block to evidence when possible:

- document created,
- report prepared,
- consultation note,
- training material,
- email draft,
- meeting note,
- table row,
- task record,
- screenshot only if explicitly provided by the user,
- file path only if provided or approved by the user.

## Deadline and follow-up tracking

The agent should track and remind the user about:

- leadership consultation items,
- principal approval items,
- school deadlines,
- reporting deadlines,
- training deadlines,
- professional development deadlines,
- Erasmus+ deadlines,
- policy review deadlines,
- unfinished evidence items.

## Alerts

The agent should alert the user about:

- upcoming deadlines,
- unfinished outputs,
- work without evidence,
- tasks waiting for principal consultation,
- overdue review items,
- too much work classified as non-SDK,
- missing monthly report,
- missing leadership briefing,
- activity that should be documented but is not yet recorded.

## Daily summary

At the end of the day, the agent should prepare:

- total tracked time,
- SDK work time,
- non-SDK work time,
- outputs created,
- open tasks,
- items for leadership,
- evidence files,
- recommended next step.

## Weekly and monthly summary

The agent should prepare:

- performance overview,
- measurable outputs,
- category summary,
- leadership evidence summary,
- professional development summary,
- work alignment analysis,
- risks and recommendations.

## Correction rule

The user must be able to correct activity records. The agent should mark corrected items as revised rather than hiding changes.

## Final principle

The automatic work monitor should help the user prove real work, protect time, organise outputs and prepare evidence. It must remain transparent, user-controlled and focused on the user's own SDK and school-related work.
