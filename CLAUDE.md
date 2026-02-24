# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## About SifabAS

Sifab AS is a specialized supplier in the Norwegian energy market, located in Sandnes (Stavanger region). The company delivers flow metering solutions (fiscal, custody transfer, process), automatic tank gauging (Honeywell Enraf), volume provers & spheres, wave monitoring (Radac), and Norsok-compliant skid fabrication & special items (SI) for offshore and onshore installations.

Sifab AS is an authorized channel partner for Honeywell, Faure Herman, McCrometer, Maloney, GFSA, and Emerson. The team has extensive experience in design, materials, welding, coating, and machining for offshore product manufacturing.

Sifab AS is **ISO 9001 certified** and compliant with **PED**, **TR 2000**, and **Norsok** standards. All work must comply with the company's quality management system (B.SI.xx.xx procedure series), relevant Norsok standards (S-001, S-002, I-001, I-002, I-104, Z-001, Z-008, Z-015, R-003, etc.), and applicable Norwegian regulations (Petroleumstilsynet / PSA, Arbeidstilsynet, DSB, NPD/OD).

**Website:** [www.sifab.no](https://www.sifab.no)

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
  /quality-management      — ISO 9001 QMS enforcement & B.SI.01.07 document control
  /iso-document-producer   — Authors all internal ISO 9001 documents, procedures, and forms
  /email                   — Email drafting, parsing, and routing
  /customer-followup       — Customer relationship & follow-up
/projects                  — Active and archived project folders
/documents                 — Controlled document store
  /norsok                  — Norsok standard references and summaries
  /contracts               — Customer contracts and framework agreements
  /rfq                     — Requests for quotation (incoming and outgoing)
  /reports                 — Engineering reports and deliverables
  /drawings                — P&IDs, layout drawings, isometrics, etc.
  /iso                     — ISO 9001 QMS documents (manual, procedures, forms, records)
/email                     — Email templates, logs, and drafts
/customers                 — Customer profiles, contact lists, history
```

## Key Conventions

- **Language**: All documents, correspondence, and written output must be in **English**. No Norwegian in written material.
- **Standards referencing**: Always cite the specific Norsok standard clause (e.g., "Norsok S-001 §6.3") when making engineering decisions or recommendations.
- **Document handling**: All project document management follows SifabAS procedure **B.SI.01.07** (Procedure for Document Handling). This is the standard procedure used by human project managers when running projects.
- **Document numbering**: Follow the convention `[ProjectID]-[Discipline]-[DocType]-[SeqNo]` (e.g., `P2024-IA-REP-001`).
- **Agent collaboration**: Agents communicate through structured handoff files in each project folder. When an agent produces output that another agent needs, it writes to a shared `/projects/<project-id>/handoffs/` directory.
- **Traceability**: Every engineering decision must be traceable to a requirement, standard, or customer specification. Agents must log the rationale in their outputs.

## Agent Interaction Model

Agents operate in a hub-and-spoke model:

1. **Project Manager** is the hub — coordinates scope, schedule, and cross-discipline interfaces.
2. **Quality Management Agent** enforces ISO 9001 QMS and B.SI.01.07 document handling across all deliverables.
3. **ISO Document Producer Agent** authors and maintains all internal QMS documents, procedures, forms, and templates.
4. **Discipline agents** (Instrumentation, Process, Structural, Metering, HSE) produce and review engineering deliverables.
5. **Email Agent** handles all external communication drafting and parsing.
6. **Customer Follow-up Agent** tracks commitments, deadlines, and satisfaction.

When working on a task, always check the relevant `AGENT.md` for the agent's scope, required standards, and expected output formats.
