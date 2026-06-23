# SDK Agent module index

## Purpose

This index provides a quick overview of all modules that belong to the SDK Strategic AI Assistant.

It helps the user, developer or school leadership understand what each module does and when it should be used.

## Main architecture

```text
SDK Strategic AI Assistant
├── master control and task routing
├── communication, voice and avatar interface
├── activity collection and work monitoring
├── evidence, reporting and leadership outputs
├── digital strategy and action planning
├── platforms and AI tools
├── teacher methodology and training
├── policy, strategy and professional development monitoring
├── database, API, exports and implementation specs
└── legal, GDPR and safety support
```

## Core files

| File | Module | Main purpose |
|---|---|---|
| `master-agent-blueprint.md` | Master blueprint | Main architecture of the whole SDK assistant system |
| `README.md` | Introductory overview | Basic introduction to the SDK Agent package |
| `agent-instructions.md` | Agent behaviour | Core behavioural rules and response style |
| `core-modules.md` | Core module structure | Main functional areas of the SDK Agent |
| `knowledge-map.md` | Knowledge map | What the agent must know and connect |

## Implementation and build files

| File | Module | Main purpose |
|---|---|---|
| `local-app-implementation-spec.md` | Local app specification | Desktop app requirements, avatar, voice, tracking and local workflows |
| `prototype-roadmap.md` | Prototype roadmap | Development phases from MVP to full assistant |
| `data-model.md` | Data model | Tables and entities for work, evidence, deadlines and reports |
| `database-schema.sql` | SQLite schema | Concrete database schema for the first local prototype |
| `api-spec.md` | API specification | Endpoints for activities, work blocks, leadership outputs, exports and settings |
| `ui-ux-spec.md` | UI/UX specification | Screens, controls, dashboard, avatar and workflow design |
| `export-spec.md` | Export specification | XLSX, DOCX, PDF and report export requirements |
| `security-permissions-spec.md` | Security and permissions | Permissions, safety boundaries, hidden monitoring prohibition and user approval rules |
| `mvp-build-backlog.md` | MVP backlog | Buildable tasks and acceptance criteria for the first usable version |

## Communication and interface

| File | Module | Main purpose |
|---|---|---|
| `communication-mode.md` | Communication and voice | Human-like dialogue, voice input, voice output and colleague-style alerts |
| `avatar-interface.md` | Avatar interface | Visible avatar, text bubbles, voice mode, silent mode and notification states |

## Work tracking and evidence

| File | Module | Main purpose |
|---|---|---|
| `activity-inbox-and-priority-table.md` | Activity inbox | Collects notes, classifies activities, prepares priority tables |
| `automatic-work-monitor.md` | Automatic work monitor | Recognises work context, tracks time and measurable outputs when enabled |
| `activity-alignment-and-reporting.md` | Activity alignment | Checks whether activities match SDK work and prepares reports |
| `templates/vystupy-a-reporting-sdk.md` | Reporting template | Monthly reports, evidence and outputs for SDK work |
| `leadership-briefing-and-evidence.md` | Leadership evidence | Prepares dated outputs for principal consultation and approval |

## Strategy, leadership and planning

| File | Module | Main purpose |
|---|---|---|
| `templates/digitalna-strategia-skoly.md` | Digital strategy | School digital strategy template |
| `templates/plan-cinnosti-sdk.md` | SDK activity plan | Daily, weekly and monthly planning template |
| `policy-strategy-monitor.md` | Policy and Strategy Monitor | OECD, ministry, FCL, European Schoolnet and Erasmus+ monitoring |
| `professional-development-planner.md` | Professional Development Planner | Training deadlines, professional development plan and school training proposals |

## Platforms and AI ecosystem

| File | Module | Main purpose |
|---|---|---|
| `universal-ai-school-ecosystem.md` | AI and school ecosystem | Microsoft, Google, Gemini, NotebookLM, Claude, ChatGPT and other AI tools |
| `m365-teams-onenote-notebooklm.md` | M365 and NotebookLM | Teams, OneNote, Class Notebook, SharePoint and source-based workflows |
| `teacher-methodology-and-training.md` | Teacher methodology | Teaching ideas, digital lessons, practical teacher training outputs |

## Legal, safety and governance

| File | Module | Main purpose |
|---|---|---|
| `legal-support.md` | Legal and competence support | Orientation support for SDK role, work scope and legal-administrative arguments |
| `security-permissions-spec.md` | Security and permissions | Concrete permission model and safety controls for the application |

## Recommended use by task type

| User need | Recommended module |
|---|---|
| I need to record what I did today | `activity-inbox-and-priority-table.md` |
| I need proof of my work | `activity-alignment-and-reporting.md` and `templates/vystupy-a-reporting-sdk.md` |
| I need to prepare something for the principal | `leadership-briefing-and-evidence.md` |
| I need a digital strategy or action plan | `templates/digitalna-strategia-skoly.md` and `templates/plan-cinnosti-sdk.md` |
| I am working and want automatic recognition | `automatic-work-monitor.md` |
| I want the agent to talk like a colleague | `communication-mode.md` |
| I want avatar, voice and alerts | `avatar-interface.md` |
| I need training recommendations | `professional-development-planner.md` |
| I need OECD, FCL, Erasmus or ministry alignment | `policy-strategy-monitor.md` |
| I need help with Teams, OneNote or SharePoint | `m365-teams-onenote-notebooklm.md` |
| I need AI tool comparison | `universal-ai-school-ecosystem.md` |
| I need a teacher training or lesson idea | `teacher-methodology-and-training.md` |
| I need careful role or legal argumentation | `legal-support.md` |
| I need API endpoints for development | `api-spec.md` |
| I need database tables | `data-model.md` and `database-schema.sql` |
| I need Excel/Word/PDF exports | `export-spec.md` |
| I need screens and user flows | `ui-ux-spec.md` |
| I need build tasks for MVP | `mvp-build-backlog.md` |

## Output principle

Every module should help produce one or more of these outputs:

- dated activity record,
- measurable work evidence,
- leadership briefing,
- approval proposal,
- monthly SDK report,
- digital strategy input,
- action plan item,
- SMART goal,
- training proposal,
- teacher support material,
- risk note,
- professional development plan item,
- archived document with clear file name.

## Safety principle

No module may perform external actions without the user's approval.

The assistant may prepare, classify, recommend, summarise and warn. The user decides what is saved, sent, approved, presented, published or implemented.

## Current implementation package

The repository now contains a complete planning package for the first prototype:

1. architecture,
2. module index,
3. local app specification,
4. data model,
5. SQLite schema,
6. API specification,
7. UI/UX specification,
8. export specification,
9. security and permissions,
10. MVP build backlog.

## Next recommended development step

Implement the MVP in this order:

1. SQLite database initialization,
2. Activity Inbox,
3. Work Tracker,
4. Evidence Register,
5. Leadership Outputs,
6. Deadline Register,
7. XLSX exports,
8. Dashboard,
9. Settings,
10. later voice, avatar and automatic recognition.
