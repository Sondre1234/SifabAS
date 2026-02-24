# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## About SifabAS

SifabAS is a Norwegian engineering services company specializing in oil & gas, energy, and industrial projects governed by **Norsok standards**. The company delivers multidisciplinary engineering — instrumentation & automation, process, structural, HSE/HMS, and metering — with integrated project management and customer follow-up.

SifabAS is **ISO 9001 certified**. All work must comply with the company's quality management system, relevant Norsok standards (S-001, S-002, I-001, I-002, Z-001, Z-008, Z-015, R-003, etc.), and applicable Norwegian regulations (Petroleumstilsynet / PSA, Arbeidstilsynet, DSB).

## Repository Purpose

This repository is the operational backbone for SifabAS, structured around **AI agents** that assist human engineers. Each agent has a defined role, Norsok compliance scope, and collaboration interfaces with other agents. The `/agents` directory contains one subfolder per agent with an `AGENT.md` describing responsibilities, standards, inputs/outputs, and inter-agent workflows.

## Project Structure

```
/agents                    — AI agent definitions (one subfolder per agent)
  /project-manager         — Norsok project management & coordination
  /instrumentation         — Instrumentation & automation engineering
  /hse                     — HSE/HMS engineering & compliance
  /process                 — Process engineering
  /structural              — Structural engineering
  /metering                — Metering specialist/engineering
  /email                   — Email drafting, parsing, and routing
  /customer-followup       — Customer relationship & follow-up
/projects                  — Active and archived project folders
/documents                 — Controlled document store
  /norsok                  — Norsok standard references and summaries
  /contracts               — Customer contracts and framework agreements
  /rfq                     — Requests for quotation (incoming and outgoing)
  /reports                 — Engineering reports and deliverables
  /drawings                — P&IDs, layout drawings, isometrics, etc.
/email                     — Email templates, logs, and drafts
/customers                 — Customer profiles, contact lists, history
```

## Key Conventions

- **Language**: Project documents and customer-facing material are in **Norwegian (Bokmål)** unless the customer requests English. Internal agent instructions and this repository's markdown files are in English.
- **Standards referencing**: Always cite the specific Norsok standard clause (e.g., "Norsok S-001 §6.3") when making engineering decisions or recommendations.
- **Document handling**: All project document management follows SifabAS procedure **B.SI.01.07** (Procedure for Document Handling). This is the standard procedure used by human project managers when running projects.
- **Document numbering**: Follow the convention `[ProjectID]-[Discipline]-[DocType]-[SeqNo]` (e.g., `P2024-IA-REP-001`).
- **Agent collaboration**: Agents communicate through structured handoff files in each project folder. When an agent produces output that another agent needs, it writes to a shared `/projects/<project-id>/handoffs/` directory.
- **Traceability**: Every engineering decision must be traceable to a requirement, standard, or customer specification. Agents must log the rationale in their outputs.

## Agent Interaction Model

Agents operate in a hub-and-spoke model:

1. **Project Manager** is the hub — coordinates scope, schedule, and cross-discipline interfaces.
2. **Discipline agents** (Instrumentation, Process, Structural, Metering, HSE) produce and review engineering deliverables.
3. **Email Agent** handles all external communication drafting and parsing.
4. **Customer Follow-up Agent** tracks commitments, deadlines, and satisfaction.

When working on a task, always check the relevant `AGENT.md` for the agent's scope, required standards, and expected output formats.
