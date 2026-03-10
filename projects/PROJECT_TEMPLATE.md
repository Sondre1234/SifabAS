# Project: [Project Name]

## Project Metadata

| Field            | Value                                      |
|------------------|--------------------------------------------|
| **SP Number**    | SP-XXXXX                                   |
| **Project Name** | [Full project name]                        |
| **Client**       | [Direct client / contracting party]        |
| **End Client**   | [Operator or end user, if different]       |
| **Scope**        | [Brief scope description]                  |
| **Bid Deadline** | [YYYY-MM-DD or N/A]                        |
| **Team**         | [Sifab team members assigned]              |
| **Standards**    | [Primary standards: Norsok, ANSI, PED...] |
| **Status**       | [Opportunity / Quoted / Awarded / Active / Completed / Archived] |
| **Created**      | [YYYY-MM-DD]                               |

---

## Scope of Supply

Describe the full scope of supply here. Include:

- Equipment to be delivered (meters, provers, skids, instruments, etc.)
- Services included (design, fabrication, testing, installation support, commissioning)
- Documentation deliverables (data books, test reports, certificates)
- Any exclusions or clarifications

---

## OneDrive Project Folder

All project files (drawings, specifications, correspondence, purchase orders, data books, etc.) are stored on the shared OneDrive drive:

```
<USERPROFILE>/OneDrive - Sifab AS/Dokumenter - Felles/SP-XXXXX [Project Name]/
```

### Standard OneDrive Subfolder Structure

| Folder                  | Contents                                                |
|-------------------------|---------------------------------------------------------|
| `01.Bestillinger`       | Purchase orders (from client and to suppliers)          |
| `02 Tilbud`             | Quotations (outgoing to client, incoming from suppliers)|
| `03.Spesifikasjoner`    | Technical specifications, data sheets, standards        |
| `04.Korrespondanse`     | Email correspondence, meeting minutes, letters          |
| `05.Tegninger`          | Drawings (P&IDs, GAs, isometrics, fabrication drawings) |
| `06.Beregninger`        | Engineering calculations                                |
| `07.Kvalitet`           | Quality records, inspection reports, NCRs               |
| `08.Sertifikater`       | Material certificates, test certificates, calibration   |
| `09.Transport`          | Shipping, packing, transport documentation              |
| `10.Sluttdokumentasjon` | Final documentation / data book                         |
| `11.Bilder`             | Project photos                                          |
| `Transmittel`           | Document transmittals (distribution records)            |

> **Note:** Not all folders are required for every project. Create only the folders needed for the project scope.

---

## Git Repository Folder Structure

Within this repository, each project has a lightweight folder under `/projects/<project-slug>/`. This folder contains **only markdown files and structured data** -- not the full project file archive (which lives on OneDrive).

```
/projects/<project-slug>/
  PROJECT.md              -- This file: project overview, metadata, status
  engineering/            -- Engineering notes, decision logs, calculations (markdown)
  handoffs/               -- Inter-agent handoff files (structured markdown)
```

### What goes in Git vs. OneDrive

| Git (this repo)                          | OneDrive (shared drive)                      |
|------------------------------------------|----------------------------------------------|
| Project overview and status (PROJECT.md) | Purchase orders, contracts, quotations       |
| Engineering decision logs (.md)          | Drawings (DWG, PDF)                          |
| Agent handoff files (.md)                | Specifications and data sheets               |
| Meeting notes and action items (.md)     | Correspondence (emails, letters)             |
| Standards compliance checklists (.md)    | Quality records, certificates, test reports  |
|                                          | Final documentation / data books             |

---

## Key Standards

List the primary standards and regulations applicable to this project:

- [ ] Norsok S-001 (Technical Safety)
- [ ] Norsok S-002 (Working Environment)
- [ ] Norsok I-001 (Field Instrumentation)
- [ ] Norsok I-002 (Safety and Automation Systems)
- [ ] Norsok Z-001 (Documentation for Operation)
- [ ] PED 2014/68/EU (Pressure Equipment Directive)
- [ ] ANSI/ASME standards (specify)
- [ ] API standards (specify)
- [ ] Client-specific requirements (specify)

---

## Status / Progress

### Current Status

[Describe current project phase and status]

### Key Milestones

| Milestone                | Target Date | Actual Date | Status  |
|--------------------------|-------------|-------------|---------|
| Quotation submitted      |             |             |         |
| Order received           |             |             |         |
| Engineering start        |             |             |         |
| Material procurement     |             |             |         |
| Fabrication start        |             |             |         |
| FAT (Factory Acceptance) |             |             |         |
| Delivery / Shipping      |             |             |         |
| Commissioning support    |             |             |         |

### Open Actions

| # | Action Item | Owner | Due Date | Status |
|---|-------------|-------|----------|--------|
| 1 |             |       |          |        |

### Risks / Issues

| # | Risk / Issue | Impact | Mitigation | Owner |
|---|-------------|--------|------------|-------|
| 1 |             |        |            |       |

---

## Notes

[Any additional project notes, context, or background information]
