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

## Next recommended development step

Create implementation-level specifications for:

1. local desktop work monitor,
2. avatar and voice interface,
3. activity spreadsheet export,
4. leadership evidence folder structure,
5. scheduled policy and training monitoring.
