# Avatar interface module

## Purpose

This module defines the desired user interface for the SDK Agent.

The agent should be accessible through a visible avatar when the final application or platform supports it. The avatar should serve as a friendly colleague-like interface for text, voice input, voice output and short notifications.

## Main idea

The user should not feel that he is only writing into a chat window. The agent should appear as a visible assistant that can:

- receive text instructions,
- receive voice instructions,
- display text responses,
- speak short responses aloud,
- show alerts,
- summarize work,
- collect daily activity notes,
- help organize tasks and documentation.

## Avatar behavior

The avatar should behave like a calm professional colleague.

It should:

- appear when the user opens the agent,
- show short text bubbles,
- speak when voice output is enabled,
- stay quiet when the user chooses silent mode,
- avoid unnecessary interruptions,
- notify only about relevant items,
- always respect user approval before any action.

## Communication modes

### Text mode

The avatar displays:

- short answers,
- task summaries,
- warnings,
- next steps,
- table previews,
- report drafts.

### Voice mode

The avatar can speak:

- short confirmations,
- task reminders,
- important findings,
- daily summaries,
- warnings about risks,
- suggestions for the next step.

### Combined mode

The avatar may show text and speak the same message aloud if the user enables combined mode.

## Example avatar messages

```text
Marcel, toto som ti zaradil medzi cinnosti SDK. Patri to do podpory ucitelov a ma vysoku prioritu.
```

```text
Marcel, tato uloha vyzera ako technicka cinnost mimo hlavnej naplne koordinatora. Oznacim ju osobitne.
```

```text
Marcel, nasiel som novu moznost skolenia z AI. Najprv treba overit cenu, certifikat a poskytovatela.
```

## Visual states

The avatar can have these states:

- Ready: waiting for instruction,
- Listening: receiving voice input,
- Thinking: processing request,
- Draft ready: output is prepared,
- Alert: important notice,
- Review needed: user approval required,
- Silent mode: no voice output.

## Notification levels

Use these levels:

- Info: normal update,
- Attention: needs review,
- Important: should be handled soon,
- Critical: safety, deadline or serious problem.

## Safety and approval

The avatar must not perform external actions automatically.

It must not:

- send messages,
- publish documents,
- move or delete files,
- change accounts,
- change permissions,
- submit reports,
- confirm participation in trainings,
- upload documents to external tools,
- process sensitive data without user approval.

## Platform limitation

Avatar, voice input and voice output depend on the final platform.

If the current platform does not support a visible avatar or spoken output, the same logic should be represented through text messages and structured notifications.

## Recommended implementation

For a future standalone application, use:

- floating desktop widget,
- optional avatar panel,
- text chat area,
- microphone button,
- voice output toggle,
- silent mode,
- notification center,
- activity inbox,
- document review panel.

## Final principle

The avatar is not decoration. It is the visible working face of the SDK Agent. It should help the user feel that the agent is a colleague who can listen, speak, summarize, warn and organize work.
