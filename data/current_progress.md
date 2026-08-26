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

### Step 2: Generate Google Form
- **Task:** Since Label Studio is cumbersome for external annotators, generate a Google Form using Google Apps Script.
- **Action:** Open `https://script.google.com/`, create a new project, paste the contents of `scripts/utils/generate_google_form.js`, and click "Run".
- **Action:** Verify the generated Form in your Google Drive and copy the "Send" link.

### Step 3: Project Configuration
- **Task:** Configure the project interface and tasks:
  1. Go to the Settings of the generated Google Form.
  2. Ensure "Collect email addresses" is turned on.
  3. Ensure "Limit to 1 response" is turned OFF so multiple students can participate if needed (or keep it strictly assigned).

### Step 4: Perform Double Annotation
- **Task:** Send the Google Form link to Annotator 1 and Annotator 2. Have them both complete the 90 citation tasks.

### Step 5: Export & Calculate Agreement (IAA)
- **Task:** When annotation completes, go to the Google Form "Responses" tab, click "Link to Sheets", and download the responses as a CSV or JSON file to `annotation/project_export.json` (you may need a simple script to map the CSV headers to the original JSON format).
- **Task:** Execute the Kappa calculation script to get overall agreement and generate the disagreement review sheet:
- **Terminal Command:**
  ```bash
  venv/bin/python3 scripts/utils/calculate_iaa.py --export annotation/project_export.json
  ```
- **Output:** The script will print the Kappa scores and write all disagreements to a review sheet: `logs/adjudication_sheet.md`.

### Step 6: Adjudication & Freeze
- **Task:** Have the senior legal adjudicator review the disagreements logged in `logs/adjudication_sheet.md`, choose the correct label, and save the finalized gold dataset as `gold_dataset_v1.0.json` (Phase 3 exit gate).