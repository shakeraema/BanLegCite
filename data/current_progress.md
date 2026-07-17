# Current Progress & Action Plan — BanLegit-Cite

## Git & Repository Status
- Reconciled branch histories and resolved conflicts.
- Completed directory layout alignments and log merges.
- Successfully pushed local updates to the remote repository.
- Live commits up to date at `main` on: `https://github.com/ZahidHasan7/BanLegit-Cite.git`.

---

## Active Phase: Phase 3 (Annotation & Gold-Set Certification)
**Owner:** Researcher A (Ema)

Below is the step-by-step action plan to execute Phase 3 annotation milestones.

### Step 1: Onboard Annotation Pool
- **Task:** Recruit 2 independent annotators (advanced law students) and 1 legal adjudicator.
- **Templates:** Use email templates and guidelines located in:
  - Recruitment Plan: [recruitment_plan.md](file:///Users/shakera/Downloads/Study/Researches/ICCIT/BanLegit-Cite/annotation/recruitment_plan.md)
  - Onboarding Training: [annotator_training.md](file:///Users/shakera/Downloads/Study/Researches/ICCIT/BanLegit-Cite/annotation/annotator_training.md)
  - Annotation Guidelines: [guidelines.md](file:///Users/shakera/Downloads/Study/Researches/ICCIT/BanLegit-Cite/annotation/guidelines.md)

### Step 2: Spin Up Label Studio
- **Task:** Start the Label Studio server on your local machine:
- **Terminal Command:**
  ```bash
  source venv/bin/activate
  label-studio start
  ```
- **Action:** Open `http://localhost:8080` in your web browser.

### Step 3: Project Configuration
- **Task:** Configure the project interface and tasks:
  1. Create a new project in Label Studio.
  2. Select **Settings** -> **Labeling Interface** -> **Custom Template**.
  3. Paste the contents of [config.xml](file:///Users/shakera/Downloads/Study/Researches/ICCIT/BanLegit-Cite/annotation/config.xml).
  4. Select **Import** and upload the generated tasks in [label_studio_import.json](file:///Users/shakera/Downloads/Study/Researches/ICCIT/BanLegit-Cite/annotation/label_studio_import.json).

### Step 4: Perform Double Annotation
- **Task:** Have both Annotator 1 and Annotator 2 verify the 150 citation tasks.

### Step 5: Export & Calculate Agreement (IAA)
- **Task:** When annotation completes, export the project annotations in JSON format from Label Studio and save the file to `annotation/project_export.json`.
- **Task:** Execute the Kappa calculation script to get overall agreement and generate the disagreement review sheet:
- **Terminal Command:**
  ```bash
  venv/bin/python3 scripts/utils/calculate_iaa.py --export annotation/project_export.json
  ```
- **Output:** The script will print the Kappa scores and write all disagreements to a review sheet: `logs/adjudication_sheet.md`.

### Step 6: Adjudication & Freeze
- **Task:** Have the senior legal adjudicator review the disagreements logged in `logs/adjudication_sheet.md`, choose the correct label, and save the finalized gold dataset as `gold_dataset_v1.0.json` (Phase 3 exit gate).