# Windows IT Support & Account Management Lab

**Target roles:** Desktop Support Technician, IT Support Specialist, Help Desk Technician.

## Scenario
A fictional campus help desk needs a consistent way to handle tickets, prioritize impact, and document account-support tasks. The `tickets.csv` file is synthetic sample data.

## What this includes
- `tickets.csv`: Six simulated support requests.
- `ticket_triage.py`: Standard-library Python tool that prioritizes and summarizes tickets.
- `windows_lab.ps1`: **Optional** read-only Windows environment checks, with an example local-user command printed but not executed.
- `runbook.md`: Step-by-step help desk troubleshooting runbook and escalation rules.

## Run it
```bash
python ticket_triage.py
```
On a Windows test machine, optionally run approved read-only PowerShell checks from `windows_lab.ps1`. Do not run scripts on your employer's systems without authorization.

## Record your own work
Add screenshots of the report and your diagnostic output, describe what you verified, and explain how you would close a ticket professionally.

## Skills illustrated
Ticket triage, desktop troubleshooting, documentation, customer communication, Windows diagnostics.
