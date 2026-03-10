# B.SI.01.07 -- Procedure for Document Handling

**Document Number:** B.SI.01.07
**Title:** Procedure for Document Handling
**Type:** ISO 9001 QMS Procedure
**Owner:** Quality Management
**Status:** Active

---

## 1. Purpose

This procedure governs how all project documents at Sifab AS are created, reviewed, approved, distributed, and archived. It ensures that documentation is controlled, traceable, and compliant with ISO 9001 requirements and applicable industry standards.

B.SI.01.07 is the standard procedure used by project managers and all disciplines when managing project documentation throughout the project lifecycle.

---

## 2. Scope

This procedure applies to **all project documentation across all disciplines** at Sifab AS, including but not limited to:

- Engineering documents (specifications, calculations, data sheets)
- Drawings (P&IDs, GAs, isometrics, fabrication drawings)
- Quotations and purchase orders
- Correspondence (emails, letters, meeting minutes)
- Quality records (inspection reports, NCRs, test reports)
- Certificates (material certificates, calibration certificates, test certificates)
- Final documentation and data books
- Transmittals

---

## 3. Document Numbering Convention

All project documents shall follow the standard numbering convention:

```
[ProjectID]-[Discipline]-[DocType]-[SeqNo]
```

### Components

| Component      | Description                              | Example Values                          |
|----------------|------------------------------------------|-----------------------------------------|
| **ProjectID**  | Sifab project number                     | `P2024`, `SP-01415`                     |
| **Discipline** | Engineering discipline code              | `IA` (Instrumentation & Automation), `PR` (Process), `ST` (Structural), `ME` (Metering), `HS` (HSE), `QA` (Quality), `PM` (Project Management) |
| **DocType**    | Document type code                       | `REP` (Report), `DWG` (Drawing), `SPC` (Specification), `CAL` (Calculation), `MOM` (Minutes of Meeting), `TRN` (Transmittal), `NCR` (Non-Conformance Report), `ITP` (Inspection & Test Plan), `DSH` (Data Sheet) |
| **SeqNo**      | Sequential number (three digits)         | `001`, `002`, `003`                     |

### Example

```
P2024-IA-REP-001    -- Instrumentation report #1 for project P2024
SP-01415-ME-CAL-003 -- Metering calculation #3 for project SP-01415
```

---

## 4. Standard Project Folder Structure (Shared Drive)

All project files are stored on the shared OneDrive drive under the project's SP number. The standard subfolder structure is:

```
<USERPROFILE>/OneDrive - Sifab AS/Dokumenter - Felles/SP-XXXXX [Project Name]/
```

| Folder                  | Contents                                                    |
|-------------------------|-------------------------------------------------------------|
| `01.Bestillinger`       | Purchase orders -- both received from client and issued to suppliers |
| `02 Tilbud`             | Quotations -- outgoing to client and incoming from suppliers |
| `03.Spesifikasjoner`    | Technical specifications, data sheets, applicable standards  |
| `04.Korrespondanse`     | Email correspondence, meeting minutes, formal letters        |
| `05.Tegninger`          | Drawings -- P&IDs, general arrangements, isometrics, fabrication drawings |
| `06.Beregninger`        | Engineering calculations                                     |
| `07.Kvalitet`           | Quality records -- inspection reports, NCRs, audit records   |
| `08.Sertifikater`       | Material certificates, test certificates, calibration certificates |
| `09.Transport`          | Shipping documents, packing lists, transport arrangements    |
| `10.Sluttdokumentasjon` | Final documentation / data book for client delivery          |
| `11.Bilder`             | Project photographs                                          |
| `Transmittel`           | Document transmittals (distribution records)                 |

> **Note:** Not all subfolders are required for every project. Create only the folders relevant to the project scope. The folder names use Norwegian conventions for consistency with legacy projects and the shared drive structure.

---

## 5. Document Lifecycle

All controlled documents follow a defined lifecycle:

```
Draft --> Internal Review --> Approved --> Issued --> Archived
```

### Lifecycle Stages

| Stage             | Description                                                        | Who                          |
|-------------------|--------------------------------------------------------------------|------------------------------|
| **Draft**         | Document is being prepared by the responsible discipline engineer   | Author (discipline engineer) |
| **Internal Review** | Document is reviewed internally for technical accuracy and completeness | Reviewer (peer or lead engineer) |
| **Approved**      | Document is approved for issue by the responsible authority         | Approver (Project Manager or discipline lead) |
| **Issued**        | Document is formally issued to the client or stakeholder via transmittal | Project Manager              |
| **Archived**      | Document is archived after project completion or supersession       | Project Manager / QM         |

---

## 6. Revision Control

### Draft Revisions

During the drafting and internal review phase, documents use **letter revisions**:

- Rev A -- First draft
- Rev B -- Second draft (after first review comments)
- Rev C -- Third draft (if further revisions needed)

### Issued Revisions

Once a document is formally issued, it uses **numeric revisions**:

- Rev 0 -- First issue (Issued for Review / Issued for Approval / Issued for Construction)
- Rev 1 -- First revision after issue
- Rev 2 -- Second revision after issue
- Rev 3 -- And so on

### Revision Table

Every controlled document shall include a revision table recording:

| Rev | Date       | Description of Change       | Prepared | Checked | Approved |
|-----|------------|-----------------------------|----------|---------|----------|
| A   | YYYY-MM-DD | First draft                 | [Init]   | --      | --       |
| 0   | YYYY-MM-DD | Issued for [purpose]        | [Init]   | [Init]  | [Init]   |
| 1   | YYYY-MM-DD | [Description of changes]    | [Init]   | [Init]  | [Init]   |

---

## 7. Document Distribution

### Transmittals

All formal document distributions to external parties (clients, suppliers, third parties) shall be recorded via a **transmittal** (stored in the `Transmittel` folder).

A transmittal shall include:

- Transmittal number (project-specific sequential numbering)
- Date of issue
- Recipient(s)
- List of documents transmitted (document number, title, revision)
- Purpose of issue (e.g., For Review, For Approval, For Construction, For Information)
- Any comments or instructions

### Internal Distribution

Internal document sharing between Sifab team members is done via the shared OneDrive drive. No transmittal is required for internal distribution, but the document must be stored in the correct project subfolder.

---

## 8. Document Storage

### Primary Storage

All project documents are stored on the shared OneDrive drive:

```
<USERPROFILE>/OneDrive - Sifab AS/Dokumenter - Felles/SP-XXXXX [Project Name]/
```

This is the single source of truth for all project files.

### Git Repository

The SifabAS Git repository (`/projects/<project-slug>/`) contains **only markdown summaries, engineering decision logs, and agent handoff files**. It does not store the controlled project documents themselves.

### Backup

OneDrive provides automatic version history and cloud backup. No additional backup procedure is required for documents stored on the shared drive.

---

## 9. Responsibilities

| Role                      | Responsibility                                                      |
|---------------------------|---------------------------------------------------------------------|
| **Project Manager**       | Controls project documentation; ensures compliance with this procedure; manages transmittals and distribution; approves documents for issue |
| **Quality Management (QM Agent)** | Enforces compliance with B.SI.01.07 across all projects; conducts periodic audits of document control; maintains the QMS procedure itself |
| **Discipline Engineers**  | Author documents within their discipline; follow numbering and revision conventions; submit documents for review and approval |
| **General Manager**       | Overall accountability for the QMS including document control        |

---

## 10. Document Retention

All project documentation shall be retained for a **minimum of 10 years after project completion**. This includes:

- All issued revisions of controlled documents
- Transmittal records
- Quality records and certificates
- Correspondence related to engineering decisions

After the retention period, documents may be reviewed for archival or disposal in accordance with applicable regulations and client contract requirements.

> **Note:** Some client contracts or regulatory requirements may stipulate longer retention periods. Always check the project-specific requirements.

---

## 11. References

- **ISO 9001:2015** -- Quality Management Systems, Clause 7.5 (Documented Information)
- **B.SI.01.01** -- Quality Manual
- **B.SI.01.02** -- Quality Policy
- **Norsok Z-001** -- Documentation for Operation (where applicable)

---

## Document History

| Rev | Date       | Description            | Author           |
|-----|------------|------------------------|------------------|
| --  | 2026-03-10 | Markdown summary created for SifabAS repository | Quality Management |

> **Note:** This markdown file is a summary representation of the B.SI.01.07 procedure for use within the SifabAS repository and by AI agents. The authoritative version of this procedure is maintained in the Sifab AS QMS document system.
