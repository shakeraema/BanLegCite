Based on the completion of the pilot adjudication and the finalized reproducibility passes, here are the next steps to transition this project from the simulation/pilot phase to the real-world benchmark run:

### Step 1: Launch the Google Form & Onboard Student Annotators
1. Open [Google Apps Script](https://script.google.com/) in your browser.
2. Copy the entire contents of your local [generate_google_form.js](file:///Users/shakera/Downloads/Study/Researches/ICCIT/BanLegit-Cite/scripts/utils/generate_google_form.js) and paste them into the Apps Script editor.
3. Run the `createAnnotationForm()` function. This will automatically compile and generate the live Google Form with the corrected 90 tasks (containing the swapped DLR AD precedents, the Name/Department/University fields, and email-login disabled).
4. Distribute the form to your recruited student annotators along with the training manual.

---

### Step 2: Resolve Disputed Precedents in the Ground Truth (The Adjudication List)
Per the senior review in [senior_review.md](file:///Users/shakera/Downloads/Study/Researches/ICCIT/BanLegit-Cite/senior_review.md), **15 specific tasks** carry structural digitisation or reporting uncertainties (such as the unreleased AD judgment text for *State v. Sukur Ali* or the CHT land-dispute BLC volume for *Aberchai Mog*). 
* **Action:** Route these 9 Medium and 6 Low confidence task groups to a third-party audit with physical print library or direct *Chancery Law Chronicles* register access before locking their ground-truth labels.

---

### Step 3: Run the Real Double-Annotation & Agreement Pipelines
Once the student responses are collected in the Google Sheet:
1. Export the spreadsheet as a CSV and save it over `annotation/project_responses.csv`.
2. Run the Label Studio converter to parse and group their responses:
   ```bash
   venv/bin/python3 scripts/utils/convert_google_sheet_to_label_studio.py --csv annotation/project_responses.csv
   ```
3. Run the Kappa agreement script to verify if the actual inter-annotator agreement meets the $\kappa \ge 0.6$ quality threshold:
   ```bash
   venv/bin/python3 scripts/utils/calculate_iaa.py --export annotation/project_export.json
   ```
4. Adjudicate any actual student disagreements logged in the newly generated `logs/adjudication_sheet.md`.

---

### Step 4: Re-Evaluate and Draft the Final Paper (Phase 5)
1. Re-run model evaluations over the final adjudicated human gold standard:
   ```bash
   venv/bin/python3 -m scripts.evaluation.run_phase4 --limit 30
   ```
2. Synthesize the final stats (annotator agreement rates, baseline standard LLM accuracy vs. agentic-setting performance) into the final academic writeup.