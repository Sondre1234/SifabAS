# D.SI.06.01 — Procedure for Control of Documents

| Field | Value |
|---|---|
| **Document No.** | D.SI.06.01 |
| **Title** | Control of Documents |
| **Type** | ISO 9001 QMS Procedure |
| **Revision** | 02 |
| **Date** | 2026-07-13 |
| **Prepared by** | Sondre Falch |
| **Approved by** | Tom Sverre Falch, General Manager |
| **Supersedes** | D SI 06 01 Control of Documents 21.rtf |

---

## 1. Purpose

This procedure governs how Sifab AS creates, reviews, approves, distributes, revises and archives two categories of controlled documents:

1. **Governing documents** — the QMS itself: policies, procedures, work instructions, forms (Parts A, B, C, D, O, P, S).
2. **Project documents** — engineering documents, drawings, quotations, correspondence, quality records and certificates produced within individual customer projects (SP-xxxxx).

It ensures documentation is controlled, traceable, and compliant with ISO 9001:2015 §7.5 and applicable industry standards.

## 2. Scope

This procedure applies to all governing documents of Sifab's QMS and to all project documentation across all disciplines, including but not limited to: engineering documents, drawings, quotations and purchase orders, correspondence, quality records (inspection reports, NCRs, test reports), certificates, final documentation/data books, and transmittals.

## 3. Governing Document System Structure

Sifab's QMS is composed of 8 parts:

| Part | Content |
|---|---|
| A | HSEQ System (incl. Policy and Ethics) |
| B | Technical Procedures |
| C | Development and Construction |
| D | Administrative Procedures |
| O | Organization |
| P | Processes |
| R | Registrations (Records) |
| S | Forms |

Governing documents are written in standard formats (Word, Excel, Visio or PDF) and are prepared and stored in Sifab's document system (historically Zigma360; the physical copy of record for the 2026 QMS revision is the `ISO 9001-2015 SIFAB AS - Rev 2026` folder on the shared drive, with markdown source maintained in the SifabAS git repository under `documents/iso/`).

### 3.1 Governing Document Numbering

Governing document numbers follow: `[Part].SI.[Sub-part].[Doc No.]` — e.g. `D.SI.06.01`.

| Component | Meaning | Example |
|---|---|---|
| Part | A/B/C/D/O/P/R/S | `D` |
| SI | Company ID (Sifab) | `SI` |
| Sub-part | Numbered sub-area within the part | `06` |
| Doc No. | Sequential document number within the sub-part | `01` |

### 3.2 Project Document Numbering

Project documents follow: `[ProjectID]-[Discipline]-[DocType]-[SeqNo]`

| Component | Description | Example Values |
|---|---|---|
| **ProjectID** | Sifab project number | `P2024`, `SP-01415` |
| **Discipline** | Engineering discipline code | `IA` (Instrumentation & Automation), `PR` (Process), `ST` (Structural), `ME` (Metering), `HS` (HSE), `QA` (Quality), `PM` (Project Management) |
| **DocType** | Document type code | `REP` (Report), `DWG` (Drawing), `SPC` (Specification), `CAL` (Calculation), `MOM` (Minutes of Meeting), `TRN` (Transmittal), `NCR` (Non-Conformance Report), `ITP` (Inspection & Test Plan), `DSH` (Data Sheet) |
| **SeqNo** | Sequential number (three digits) | `001`, `002`, `003` |

Example: `SP-01415-ME-CAL-003` — Metering calculation #3 for project SP-01415.

## 4. Standard Project Folder Structure

All project files are stored on the shared OneDrive drive under `Zigma360/Projects/SP-XXXXX [Project Name]/`:

| Folder | Contents |
|---|---|
| `01.Bestillinger & Ordrebekreftelser` | Orders & confirmations |
| `02 Tilbud` | Quotations — to/from customer and suppliers |
| `03 Underlag fra Kunde` | Customer-provided documents |
| `04 E-mail` | Email correspondence |
| `05 Dokumentasjon` | Documentation (produced deliverables) |
| `06 Møtereferat` | Meeting minutes |
| `07 Clarifications` | Clarifications |
| `08 Underlag fra Leverandører` | Supplier documents |
| `09 VOR` | Variation Order Requests |
| `10 Bilder` | Photos |
| `11 Punch lists` | Punch lists |

Not all subfolders are required for every project; create only what the project scope needs.

## 5. Document Lifecycle

```
Draft --> Internal Review --> Approved --> Issued --> Archived
```

| Stage | Description | Who |
|---|---|---|
| **Draft** | Document is being prepared | Author |
| **Internal Review** | Reviewed for technical accuracy and completeness | Reviewer (peer or lead) |
| **Approved** | Approved for issue by the responsible authority | Approver (Project Manager, discipline lead, or General Manager for handbooks) |
| **Issued** | Formally issued to client/stakeholder via transmittal, or published in the QMS | Project Manager / QMS owner |
| **Archived** | Archived after project completion or supersession | Project Manager / Quality Management |

## 6. Approval Authority

- The **General Manager** is responsible for approving governing handbooks and policies (Parts A and top-level D procedures).
- **Discipline managers** approve governing documents within their discipline.
- At initial registration, each governing document's document card is completed with the required approval information before being forwarded to the approver.

## 7. Revision Control

### 7.1 Project Documents (Draft/Issued convention)

- **Rev A, B, C…** — draft revisions during preparation/internal review.
- **Rev 0, 1, 2…** — numeric revisions once formally issued (Rev 0 = first issue).

### 7.2 Governing Documents (Sequential revision convention)

- Each governing document carries a sequential revision number (e.g. Rev 00, 01, 02…) that increments on every substantive change — it is **never reset** when a document is renumbered, reformatted, or migrated between systems.
- The revision field explains the reason for the revision. The QMS is revised in response to: non-conformances, internal/external audits, improvement suggestions, and changes in laws, regulations or standards.
- The prior revision is retained in the document's revision history, not deleted.
- Obsolete documents are archived to a clearly marked archive folder, not left mixed in with current documents.

Every controlled document includes a revision history table recording revision number, date, description of change, and author/approver.

## 8. Document Distribution

### 8.1 Transmittals (external)

All formal distributions to external parties (clients, suppliers, third parties) are recorded via a transmittal (stored in the `Transmittel` project subfolder), stating: transmittal number, date, recipient(s), documents transmitted (number, title, revision), purpose (For Review / For Approval / For Construction / For Information), and any comments.

### 8.2 Internal Distribution

Internal sharing is via the shared OneDrive drive; no transmittal is required, but the document must be stored in the correct project or QMS subfolder.

## 9. Document Storage and Retention

| Document type | Storage location | Retention period | Responsible |
|---|---|---|---|
| QHSE system overview | Shared drive / git repo | 5 years | Quality lead |
| QHSE / HSEQ Handbook | Shared drive / git repo | 10 years | General Manager |
| Procedures | Shared drive / git repo | 5 years | Quality lead |
| Forms | Shared drive / git repo | 5 years | Quality lead |
| Management review minutes | Shared drive | 5 years | Quality lead |
| Non-conformances | Shared drive (Deviations - NCR Tracker) | 5 years | Quality lead |
| Supplier evaluations | Shared drive | 5 years | Quality lead |
| Customer surveys | Shared drive | 5 years | Quality lead |
| Corrective / preventive actions | Shared drive | 5 years | Quality lead |
| Internal / external audits | Shared drive | 5 years | Quality lead |
| Safety inspections | Shared drive | 5 years | Safety representative (Verneombud) |
| Position descriptions | Shared drive | 5 years | General Manager |
| Emergency response plan | Shared drive | 5 years | General Manager |
| Personnel handbook | Shared drive | 10 years | General Manager |
| Customer contracts | Shared drive | 10 years after termination | General Manager |
| Employee contracts | Shared drive | 10 years after termination | General Manager |
| Supplier agreements | Shared drive | 10 years after termination | General Manager |
| Project documentation | Shared drive (SP-xxxxx folder) | Minimum 10 years after project completion | Project Manager / Quality |

Project documentation includes all issued revisions, transmittal records, quality records/certificates, and correspondence related to engineering decisions. Client contracts or regulatory requirements may stipulate longer retention — always check project-specific requirements.

The SifabAS git repository (`documents/iso/`, `documents/iso/procedures/`) holds the markdown source of record for QMS governing documents; it does **not** store project documents or binary files (PDF/Word/Excel/PPT), which remain exclusively on the shared OneDrive drive.

## 10. Responsibilities

| Role | Responsibility |
|---|---|
| General Manager | Overall accountability for the QMS, including document control; approves governing handbooks |
| Quality lead | Enforces this procedure across all projects and governing documents; conducts periodic audits of document control; maintains this procedure |
| Discipline managers/engineers | Approve/author documents within their discipline; follow numbering and revision conventions |
| Project Manager | Controls project documentation; manages transmittals and distribution |

## 11. References

| Document | Description |
|---|---|
| A.SI.01.01 | HSEQ Handbook |
| A.SI.02.01 | Quality Policy |
| D.SI.05.01 | System Audits |
| NORSOK Z-001 | Documentation for operation (where applicable) |
| ISO 9001:2015 §7.5 | Documented Information |

---

## Revision History

| Rev. | Date | Author | Change |
|---|---|---|---|
| — | 2021 | Sifab AS | D SI 06 01 Control of Documents 21.rtf — governing-document control practice (Zigma360, numbering, retention table) |
| 00 | 2026-03-10 | Quality Management (repo) | Markdown summary covering project document control in detail |
| 01 | 2026-07-09 | Sondre Falch | Merged project-document-control content with the governing-document control procedure into a single document (D.SI.06.01); part of the 2026 QMS revision |
| 02 | 2026-07-13 | Sondre Falch | Finalized for ISO 9001 recertification audit |
