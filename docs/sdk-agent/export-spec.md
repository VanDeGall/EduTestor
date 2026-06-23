# Export specification for SDK Strategic AI Assistant

## Purpose

This document defines the required exports for the SDK Strategic AI Assistant.

The system must generate evidence-based outputs that the user can use for personal records, leadership consultation, professional development planning and school documentation.

## Export principles

Every export should be:

- dated,
- clear,
- structured,
- suitable for school leadership,
- usable as evidence of work,
- exportable to common formats,
- safe for sensitive school data.

## Supported formats

Required formats:

- XLSX,
- CSV,
- DOCX,
- PDF,
- Markdown.

First prototype priority:

1. XLSX,
2. DOCX,
3. PDF,
4. CSV,
5. Markdown.

## Export naming rule

Use this format:

```text
YYYY-MM-DD_area_export-type_short-title_v01
```

Examples:

```text
2026-09-15_sdk_denny-zaznam_praca-sdk_v01.xlsx
2026-09-30_sdk_mesacny-report_september_v01.docx
2026-09-30_vedenie_podklady-riadenie_september_v01.docx
2026-10-01_profesijny-rozvoj_navrh-skoleni_v01.xlsx
```

## 1. Daily work log

### Format

XLSX and CSV.

### Purpose

Records all work activities for one day.

### Required columns

| Date | Time | Activity | Category | SDK alignment | Priority | Size | Duration | Output | Evidence | Status | Note |
|---|---|---|---|---|---|---|---|---|---|---|---|

### Filters

- category,
- SDK alignment,
- priority,
- status,
- report include.

## 2. Weekly summary

### Format

XLSX and DOCX.

### Purpose

Summarises one work week.

### Required sections

1. Total tracked time,
2. SDK work time,
3. Non-SDK work time,
4. Main outputs,
5. Teacher support,
6. Leadership items,
7. Training work,
8. Open tasks,
9. Risks,
10. Next week priorities.

## 3. Monthly SDK report

### Format

XLSX, DOCX and PDF.

### Purpose

Creates a defensible monthly report of SDK work.

### Required sections

1. Reporting period,
2. Main priorities,
3. Activities completed,
4. Outputs created,
5. Teacher support,
6. Leadership support,
7. Training and professional development,
8. Digital strategy progress,
9. AI and tools work,
10. Risks and blockers,
11. Recommendations for leadership,
12. Priorities for next month.

### Required table

| Date | Activity | Category | SDK alignment | Duration | Output | Evidence | Priority | Status | Leadership relevance |
|---|---|---|---|---|---|---|---|---|---|

## 4. Leadership evidence register

### Format

XLSX and DOCX.

### Purpose

Shows what was prepared for the principal or school leadership.

### Required columns

| Date | Topic | Output type | Summary | Decision needed | Status | Evidence | Next step |
|---|---|---|---|---|---|---|---|

### Status values

- draft,
- ready,
- submitted,
- discussed,
- approved,
- rejected,
- waiting,
- revised,
- archived.

## 5. Approval request document

### Format

DOCX and PDF.

### Purpose

A formal short document for principal approval.

### Required sections

1. Title,
2. Date,
3. Prepared by,
4. Topic,
5. Why this is needed,
6. Proposed solution,
7. Expected benefit,
8. Required decision,
9. Resources needed,
10. Risks if not approved,
11. Proposed deadline,
12. Evidence or attachment.

## 6. Briefing note document

### Format

DOCX and PDF.

### Purpose

A concise briefing for leadership consultation.

### Required sections

1. Topic,
2. Short summary,
3. Why it matters,
4. Current state,
5. Recommendation,
6. Decision or discussion needed,
7. Next step,
8. Date prepared.

## 7. Professional development plan export

### Format

XLSX, DOCX and PDF.

### Purpose

Shows recommended professional development items for the user, teachers and leadership.

### Required columns

| Target group | Development need | Training proposal | Provider | Term | Expected output | Evidence | Strategy link | Priority | Status |
|---|---|---|---|---|---|---|---|---|---|

## 8. Training opportunities overview

### Format

XLSX.

### Purpose

Lists available and relevant trainings.

### Required columns

| Deadline | Training | Provider | Target group | Area | Cost | Certificate | Workload | Recommendation | Verification | Link |
|---|---|---|---|---|---|---|---|---|---|---|

## 9. Policy monitoring brief

### Format

DOCX, PDF and Markdown.

### Purpose

Summarises OECD, ministry, FCL, European Schoolnet and Erasmus+ findings.

### Required sections

1. What changed,
2. Why it matters for the school,
3. Relevant source,
4. Category,
5. Recommended action,
6. SMART goal implication,
7. Leadership relevance,
8. Document update needed.

### Required table

| Date checked | Source | Topic | Category | Key finding | Relevance for school | Recommended action | Leadership relevance |
|---|---|---|---|---|---|---|---|

## 10. Evidence register

### Format

XLSX.

### Purpose

Registers all evidence files and documents.

### Required columns

| Date | Evidence title | Evidence type | Related item | Evidence value | Sensitive data | Anonymisation needed | Status | File name |
|---|---|---|---|---|---|---|---|---|

## 11. Document register

### Format

XLSX.

### Purpose

Organises all SDK and school-related documents.

### Required columns

| Title | File name | Document type | Category | Status | Suggested folder | Related activity | Evidence link |
|---|---|---|---|---|---|---|---|

## 12. Deadline overview

### Format

XLSX and PDF.

### Required columns

| Deadline | Title | Source | Target group | Category | Alert level | Status | Related item |
|---|---|---|---|---|---|---|---|

## Colour coding for spreadsheets

| Meaning | Colour |
|---|---|
| Critical | red |
| High | orange |
| Medium | yellow |
| Low | green |
| Completed | green marker |
| Waiting | purple |
| Non-SDK work | dark gray |
| Personal / non-work | blue-gray |
| Archived | light gray |

## Export safety rules

Before export, the app should check:

- whether sensitive data is included,
- whether anonymisation is needed,
- whether the export is for personal use or leadership,
- whether the file path is approved,
- whether the user confirmed the export.

## Export approval rule

The application may generate a draft export automatically, but the user decides:

- where to save it,
- whether to export it,
- whether to send it,
- whether to show it to leadership.

## Final principle

Exports are not decorative outputs. They are evidence, leadership material and professional documentation for the school digital coordinator.
