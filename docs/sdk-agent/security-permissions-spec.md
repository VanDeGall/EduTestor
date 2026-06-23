# Security and permissions specification

## Purpose

This document defines the security, privacy and permission rules for the SDK Strategic AI Assistant.

The system is intended to support the user's own professional work as a school digital coordinator. It must not become hidden surveillance software.

## Core security principle

The user remains in control.

The assistant may prepare, classify, recommend, remind, summarise and export drafts. It must not perform external actions without explicit user approval.

## Permission groups

The application should separate permissions into clear groups.

### 1. Voice permissions

- voice input,
- voice output,
- transcript generation,
- saving voice notes.

User must be able to disable each separately.

### 2. Work tracking permissions

- manual timer,
- automatic work context recognition,
- active work block tracking,
- document-title recognition,
- approved workspace recognition.

Automatic work tracking must be off by default.

### 3. File permissions

- read approved folder,
- register file path,
- suggest file name,
- export to folder,
- link evidence file.

The app must not scan the whole computer by default.

### 4. Calendar and deadline permissions

- read approved calendar items,
- create local reminders,
- suggest calendar event,
- create calendar event only after approval.

### 5. Cloud and external tool permissions

- Microsoft 365 integration,
- Google integration,
- GitHub integration,
- AI API integration,
- web monitoring.

Each integration must be optional.

## Actions always requiring explicit approval

The assistant must never automatically:

- send email,
- send chat message,
- create calendar event,
- invite users,
- register anyone for training,
- upload files,
- publish documents,
- delete files,
- move files,
- change permissions,
- share documents,
- submit reports,
- mark an item as approved by leadership,
- process sensitive data in an external AI tool.

## Hidden monitoring prohibition

The assistant must not secretly:

- record screen,
- take screenshots,
- capture keystrokes,
- read private messages,
- inspect personal files,
- track browser history,
- monitor pupils,
- monitor other employees,
- record meetings without consent,
- collect unnecessary personal data.

## Allowed tracking

Allowed tracking applies only to the user's own work and only when enabled.

Allowed signals:

- manual activity entry,
- user voice note,
- manual timer,
- approved document title,
- approved file path,
- approved workspace,
- approved task list,
- approved calendar item.

## Tracking indicator

When tracking is active, the interface must clearly show:

- tracking on/off status,
- active work category,
- timer,
- pause button,
- stop button,
- current evidence status.

## Sensitive data categories

The assistant must flag sensitive data when it detects or is told about:

- pupil names,
- health data,
- disability data,
- disciplinary information,
- parent data,
- staff personal data,
- passwords,
- account credentials,
- private recordings,
- internal conflict documents,
- personnel matters.

## Sensitive data handling

When sensitive data is present, the assistant should recommend:

- anonymisation,
- minimisation,
- local processing,
- not uploading to external AI tools,
- separate evidence storage,
- restricted access,
- shorter summary instead of full transcript.

## Export safety check

Before exporting, the app should check:

1. Does the export include sensitive data?
2. Is anonymisation needed?
3. Is the export for personal record or leadership?
4. Is the target folder approved?
5. Did the user confirm export?

## Voice safety

Voice mode must follow these rules:

- show transcript before saving,
- ask before storing voice-derived notes,
- avoid saving unnecessary personal details,
- allow user to delete transcript,
- do not keep raw audio unless explicitly approved.

## Leadership output safety

Leadership outputs must not be marked as:

- submitted,
- discussed,
- approved,
- rejected,

unless the user explicitly sets or confirms that status.

## Audit log requirements

The system should log:

- created records,
- corrected records,
- status changes,
- exports,
- deleted draft records,
- permission changes,
- sensitive data warnings.

## User control requirements

The user must always be able to:

- pause tracking,
- stop tracking,
- disable automatic recognition,
- disable voice output,
- disable avatar,
- delete draft notes,
- correct categories,
- mark an item as non-SDK,
- export manually,
- refuse a suggested action.

## Default safe settings

Recommended defaults:

- automatic tracking: off,
- voice input: off,
- voice output: off,
- avatar: on,
- file scanning: off,
- external integrations: off,
- export requires confirmation: on,
- sensitive data warning: on.

## Final principle

The assistant exists to protect and prove the user's professional work. It must never become a tool for hidden monitoring of people, private messages or uncontrolled data processing.
