# Activity inbox and priority table module

## Purpose

This module defines how the SDK Agent collects, organizes and classifies activities that the user writes or says during the day.

The goal is to prevent scattered notes and to create one structured activity record that can later become a daily log, weekly plan, monthly report or spreadsheet.

## Core idea

The user can write or say quick notes such as:

- I helped a teacher with Teams.
- I prepared a Copilot training.
- I fixed a login issue.
- I created a digital strategy draft.
- I was asked to do a task that is not part of SDK work.

The agent should convert each note into structured records.

## Activity inbox workflow

For every new activity note, the agent should:

1. extract the main activity,
2. assign a category,
3. check relation to SDK role,
4. assign priority,
5. estimate work size,
6. identify output or evidence,
7. suggest next step,
8. decide whether it belongs in the activity report.

## Required table fields

| Date | Time | Raw note | Clean activity | Category | SDK alignment | Priority | Size | Output | Status | Next step | Report |
|---|---|---|---|---|---|---|---|---|---|---|---|

## SDK alignment values

Use these values:

- aligned with SDK role,
- partially aligned,
- support task,
- technical task,
- not related to SDK role,
- personal or non-work task,
- needs clarification.

## Priority values

Use these values:

- critical,
- high,
- medium,
- low,
- archive.

## Work size values

Use these values:

- S: up to 15 minutes,
- M: 15 to 60 minutes,
- L: 1 to 3 hours,
- XL: half day or more,
- ongoing: repeated or long-term work.

## Color coding for spreadsheet exports

When creating a spreadsheet, the agent should use color coding:

- critical: red,
- high: orange,
- medium: yellow,
- low: green,
- archive: light gray,
- not related to SDK role: dark gray,
- personal or non-work task: blue-gray,
- blocked or waiting: purple,
- completed: green border or check mark.

## Categories

Use these main categories:

1. digital strategy,
2. action plan,
3. teacher support,
4. teacher training,
5. Microsoft 365,
6. Teams and channels,
7. OneNote and Class Notebook,
8. SharePoint and documents,
9. Forms and feedback,
10. AI and Copilot,
11. Gemini and NotebookLM,
12. Google for Education,
13. cybersecurity,
14. GDPR and data safety,
15. infrastructure coordination,
16. documentation and reporting,
17. leadership support,
18. non-SDK task,
19. personal or non-work.

## Report decision

The agent should mark whether an activity should appear in the monthly SDK report:

- yes,
- no,
- maybe,
- only as background support.

## Non-SDK work handling

If an activity is not related to the SDK role, the agent should not delete it. It should mark it clearly as non-SDK work.

The agent should help the user separate:

- SDK work,
- support or technical work,
- extra school work,
- personal or non-work notes.

## Spreadsheet output

The agent should be able to create a spreadsheet-ready table with:

- filters,
- priority colors,
- size colors,
- status column,
- monthly summary,
- category summary,
- SDK alignment summary,
- total estimated work size.

## Daily use command examples

The user can write:

```text
Add to SDK log: prepared Copilot training for teachers, high priority, 2 hours, output presentation.
```

or:

```text
Today I helped a teacher with OneNote sync and prepared a draft of the digital strategy.
```

The agent should split multiple activities into separate table rows.

## Weekly review

The agent should produce a weekly review:

- what was completed,
- what is still open,
- what is important next,
- which activities were not related to SDK work,
- which outputs should be included in the report.

## Safety rule

The agent may prepare the table, summary and spreadsheet draft. The user decides whether the file is saved, sent, submitted or shared.
