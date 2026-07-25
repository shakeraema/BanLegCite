import json

def build_js_file(fixed_json_path="annotation/label_studio_import_fixed.json", js_output_path="scripts/utils/generate_google_form.js"):
    with open(fixed_json_path, "r", encoding="utf-8") as f:
        tasks = json.load(f)
        
    tasks_js = json.dumps(tasks, indent=2, ensure_ascii=False)
    
    js_template = f"""// Run this script in Google Apps Script (script.google.com) to generate the annotation form.
function createAnnotationForm() {{
  var form = FormApp.create('BanLegit-Cite Annotation Task');
  form.setDescription('Please verify the citations in this form. For each task, select if the citation is Correct or Fabricated, provide the specific category if fabricated, and indicate your confidence.\\n\\nRefer to the annotation guidelines for rules on classification.');
  
  // Collect email addresses to track annotators
  form.setCollectEmail(true);

  var tasks = {tasks_js};

  for (var i = 0; i < tasks.length; i++) {{
    var task = tasks[i];
    
    // Create a new section (page) for each task to keep it organized
    form.addPageBreakItem().setTitle('Task ' + (i + 1) + ' of ' + tasks.length);
    
    var desc = 'Legal Context:\\n' + task.context + '\\n\\nTarget Citation to Verify:\\n' + task.citation + '\\n\\nPurported Source Document:\\n' + task.source_doc + '\\n\\nVerification Helper (Source URL / Metadata):\\n' + task.helper_notes;
    
    // Add Context Item
    form.addSectionHeaderItem().setTitle('Task ' + (i + 1) + ' Context').setHelpText(desc);
    
    // Verification Status
    var statusItem = form.addMultipleChoiceItem();
    statusItem.setTitle('Task ' + (i + 1) + ' - Step 1: Verification Status')
              .setChoiceValues(['Correct', 'Fabricated'])
              .setRequired(true);
              
    // Fabrication Category
    var catItem = form.addMultipleChoiceItem();
    catItem.setTitle('Task ' + (i + 1) + ' - Step 2: Citation Fabrication Category')
           .setChoiceValues([
             'Not Applicable (Citation is Correct)',
             'S1: Non-Existent Section',
             'S2: Wrong Act Attribution',
             'S3: Misstated Content',
             'S4: Cross-Jurisdictional Statute Bleed',
             'S5: Repealed/Superseded',
             'P1: Non-Existent Case',
             'P2: Wrong Citation Locator',
             'P3: Misattributed Holding',
             'P4: Wrong Court Level',
             'P5: Cross-Jurisdictional Precedent Bleed'
           ])
           .setRequired(true);
           
    // Confidence Level
    var confItem = form.addMultipleChoiceItem();
    confItem.setTitle('Task ' + (i + 1) + ' - Step 3: Confidence Level')
            .setChoiceValues(['Low', 'Medium', 'High'])
            .setRequired(true);
            
    // Notes
    var notesItem = form.addParagraphTextItem();
    notesItem.setTitle('Task ' + (i + 1) + ' - Step 4: Annotation Notes');
  }}
  
  Logger.log('Form created successfully! Edit URL: ' + form.getEditUrl());
}}
"""

    with open(js_output_path, "w", encoding="utf-8") as f:
        f.write(js_template)
        
    print(f"Successfully generated Google Form Apps Script: {js_output_path}")

if __name__ == "__main__":
    build_js_file()
