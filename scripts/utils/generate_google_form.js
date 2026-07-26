// Run this script in Google Apps Script (script.google.com) to generate the annotation form.
function createAnnotationForm() {
  var form = FormApp.create('BanLegit-Cite Annotation Task');
  form.setDescription('Please verify the citations in this form. For each task, select if the citation is Correct or Fabricated, provide the specific category if fabricated, and indicate your confidence.\n\nRefer to the annotation guidelines for rules on classification.');
  
  // Disable email collection to allow open participation
  form.setCollectEmail(false);

  // Add Annotator Metadata Questions at the beginning
  var nameItem = form.addTextItem();
  nameItem.setTitle('Student Name')
          .setRequired(true);
          
  var deptItem = form.addTextItem();
  deptItem.setTitle('Department')
          .setRequired(true);
          
  var univItem = form.addTextItem();
  univItem.setTitle('University')
          .setRequired(true);

  var tasks = [
  {
    "context": "In the case of Anwar Hossain Chowdhury v. Bangladesh, the court held: The historic 8th Amendment case declaring the basic structure doctrine applicable to the Constitution of Bangladesh. Citations to 41 DLR (AD) 165 are frequently referenced in constitutional disputes.",
    "citation": "41 DLR (AD) 165",
    "source_doc": "Dhaka Law Reports (AD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: DLR_REAL_1"
  },
  {
    "context": "In the case of Habiba Mahmud v. Bangladesh, the court held: Deals with preventive detention laws and constitutional safeguards under Article 32. Citations to 45 DLR (AD) 89 are frequently referenced in constitutional disputes.",
    "citation": "45 DLR (AD) 89",
    "source_doc": "Dhaka Law Reports (AD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: DLR_REAL_2"
  },
  {
    "context": "In the case of Secretary, Ministry of Finance v. Masdar Hossain, the court held: The landmark separation of judiciary judgment establishing judicial independence under Article 115 and 116. Citations to 52 DLR (AD) 82 are frequently referenced in constitutional disputes.",
    "citation": "52 DLR (AD) 82",
    "source_doc": "Dhaka Law Reports (AD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: DLR_REAL_3"
  },
  {
    "context": "In the case of Kazi Mukhlesur Rahman v. Bangladesh, the court held: Locus standi expansion regarding boundary agreement disputes. Citations to 26 DLR (AD) 44 are frequently referenced in constitutional disputes.",
    "citation": "26 DLR (AD) 44",
    "source_doc": "Dhaka Law Reports (AD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: DLR_REAL_4"
  },
  {
    "context": "In the case of Bangladesh Legal Aid and Services Trust (BLAST) v. Bangladesh, the court held: High Court Division guidelines on arrest and remand procedures under Section 54 and 167 of the Code of Criminal Procedure. Citations to 55 DLR (HCD) 363 are frequently referenced in constitutional disputes.",
    "citation": "55 DLR (HCD) 363",
    "source_doc": "Dhaka Law Reports (HCD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: DLR_REAL_5"
  },
  {
    "context": "In the case of Anwar Hossain Chowdhury v. Bangladesh, the court held: The historic 8th Amendment case declaring the basic structure doctrine applicable to the Constitution of Bangladesh. Citations to 41 DLR (AD) 165 are frequently referenced in constitutional disputes.",
    "citation": "41 DLR (AD) 165",
    "source_doc": "Dhaka Law Reports (AD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: DLR_REAL_6"
  },
  {
    "context": "In the case of Habiba Mahmud v. Bangladesh, the court held: Deals with preventive detention laws and constitutional safeguards under Article 32. Citations to 45 DLR (AD) 89 are frequently referenced in constitutional disputes.",
    "citation": "45 DLR (AD) 89",
    "source_doc": "Dhaka Law Reports (AD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: DLR_REAL_7"
  },
  {
    "context": "In the case of Secretary, Ministry of Finance v. Masdar Hossain, the court held: The landmark separation of judiciary judgment establishing judicial independence under Article 115 and 116. Citations to 52 DLR (AD) 82 are frequently referenced in constitutional disputes.",
    "citation": "52 DLR (AD) 82",
    "source_doc": "Dhaka Law Reports (AD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: DLR_REAL_8"
  },
  {
    "context": "In the case of Kazi Mukhlesur Rahman v. Bangladesh, the court held: Locus standi expansion regarding boundary agreement disputes. Citations to 26 DLR (AD) 44 are frequently referenced in constitutional disputes.",
    "citation": "26 DLR (AD) 44",
    "source_doc": "Dhaka Law Reports (AD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: DLR_REAL_9"
  },
  {
    "context": "In the case of Bangladesh Legal Aid and Services Trust (BLAST) v. Bangladesh, the court held: High Court Division guidelines on arrest and remand procedures under Section 54 and 167 of the Code of Criminal Procedure. Citations to 55 DLR (HCD) 363 are frequently referenced in constitutional disputes.",
    "citation": "55 DLR (HCD) 363",
    "source_doc": "Dhaka Law Reports (HCD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: DLR_REAL_10"
  },
  {
    "context": "In the case of Anwar Hossain Chowdhury v. Bangladesh, the court held: The historic 8th Amendment case declaring the basic structure doctrine applicable to the Constitution of Bangladesh. Citations to 41 DLR (AD) 165 are frequently referenced in constitutional disputes.",
    "citation": "41 DLR (AD) 165",
    "source_doc": "Dhaka Law Reports (AD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: DLR_REAL_11"
  },
  {
    "context": "In the case of Habiba Mahmud v. Bangladesh, the court held: Deals with preventive detention laws and constitutional safeguards under Article 32. Citations to 45 DLR (AD) 89 are frequently referenced in constitutional disputes.",
    "citation": "45 DLR (AD) 89",
    "source_doc": "Dhaka Law Reports (AD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: DLR_REAL_12"
  },
  {
    "context": "In the case of Secretary, Ministry of Finance v. Masdar Hossain, the court held: The landmark separation of judiciary judgment establishing judicial independence under Article 115 and 116. Citations to 52 DLR (AD) 82 are frequently referenced in constitutional disputes.",
    "citation": "52 DLR (AD) 82",
    "source_doc": "Dhaka Law Reports (AD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: DLR_REAL_13"
  },
  {
    "context": "In the case of Kazi Mukhlesur Rahman v. Bangladesh, the court held: Locus standi expansion regarding boundary agreement disputes. Citations to 26 DLR (AD) 44 are frequently referenced in constitutional disputes.",
    "citation": "26 DLR (AD) 44",
    "source_doc": "Dhaka Law Reports (AD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: DLR_REAL_14"
  },
  {
    "context": "In the case of Bangladesh Legal Aid and Services Trust (BLAST) v. Bangladesh, the court held: High Court Division guidelines on arrest and remand procedures under Section 54 and 167 of the Code of Criminal Procedure. Citations to 55 DLR (HCD) 363 are frequently referenced in constitutional disputes.",
    "citation": "55 DLR (HCD) 363",
    "source_doc": "Dhaka Law Reports (HCD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: DLR_REAL_15"
  },
  {
    "context": "Applying the fabricated rule from 41 DLR (AD) 343, the court supposedly held a modified legal principle: In the case of Anwar Hossain Chowdhury v. Bangladesh, the court held (contrary to the actual ruling): The historic 8th Amendment case declaring the basic structure doctrine applicable to the Constitution of Bangladesh. Citations to 41 DLR (AD) 165 are frequently referenced in constitutional disputes.",
    "citation": "41 DLR (AD) 343",
    "source_doc": "Dhaka Law Reports (AD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: DLR_FABRICATED_1"
  },
  {
    "context": "Applying the fabricated rule from 45 DLR (AD) 289, the court supposedly held a modified legal principle: In the case of Habiba Mahmud v. Bangladesh, the court held (contrary to the actual ruling): Deals with preventive detention laws and constitutional safeguards under Article 32. Citations to 45 DLR (AD) 89 are frequently referenced in constitutional disputes.",
    "citation": "45 DLR (AD) 289",
    "source_doc": "Dhaka Law Reports (AD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: DLR_FABRICATED_2"
  },
  {
    "context": "Applying the fabricated rule from 52 DLR (AD) 353, the court supposedly held a modified legal principle: In the case of Secretary, Ministry of Finance v. Masdar Hossain, the court held (contrary to the actual ruling): The landmark separation of judiciary judgment establishing judicial independence under Article 115 and 116. Citations to 52 DLR (AD) 82 are frequently referenced in constitutional disputes.",
    "citation": "52 DLR (AD) 353",
    "source_doc": "Dhaka Law Reports (AD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: DLR_FABRICATED_3"
  },
  {
    "context": "Applying the fabricated rule from 26 DLR (AD) 219, the court supposedly held a modified legal principle: In the case of Kazi Mukhlesur Rahman v. Bangladesh, the court held (contrary to the actual ruling): Locus standi expansion regarding boundary agreement disputes. Citations to 26 DLR (AD) 44 are frequently referenced in constitutional disputes.",
    "citation": "26 DLR (AD) 219",
    "source_doc": "Dhaka Law Reports (AD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: DLR_FABRICATED_4"
  },
  {
    "context": "Applying the fabricated rule from 55 DLR (HCD) 576, the court supposedly held a modified legal principle: In the case of Bangladesh Legal Aid and Services Trust (BLAST) v. Bangladesh, the court held (contrary to the actual ruling): High Court Division guidelines on arrest and remand procedures under Section 54 and 167 of the Code of Criminal Procedure. Citations to 55 DLR (HCD) 363 are frequently referenced in constitutional disputes.",
    "citation": "55 DLR (HCD) 576",
    "source_doc": "Dhaka Law Reports (HCD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: DLR_FABRICATED_5"
  },
  {
    "context": "Applying the fabricated rule from 41 DLR (AD) 419, the court supposedly held a modified legal principle: In the case of Anwar Hossain Chowdhury v. Bangladesh, the court held (contrary to the actual ruling): The historic 8th Amendment case declaring the basic structure doctrine applicable to the Constitution of Bangladesh. Citations to 41 DLR (AD) 165 are frequently referenced in constitutional disputes.",
    "citation": "41 DLR (AD) 419",
    "source_doc": "Dhaka Law Reports (AD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: DLR_FABRICATED_6"
  },
  {
    "context": "Applying the fabricated rule from 45 DLR (AD) 288, the court supposedly held a modified legal principle: In the case of Habiba Mahmud v. Bangladesh, the court held (contrary to the actual ruling): Deals with preventive detention laws and constitutional safeguards under Article 32. Citations to 45 DLR (AD) 89 are frequently referenced in constitutional disputes.",
    "citation": "45 DLR (AD) 288",
    "source_doc": "Dhaka Law Reports (AD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: DLR_FABRICATED_7"
  },
  {
    "context": "Applying the fabricated rule from 52 DLR (AD) 235, the court supposedly held a modified legal principle: In the case of Secretary, Ministry of Finance v. Masdar Hossain, the court held (contrary to the actual ruling): The landmark separation of judiciary judgment establishing judicial independence under Article 115 and 116. Citations to 52 DLR (AD) 82 are frequently referenced in constitutional disputes.",
    "citation": "52 DLR (AD) 235",
    "source_doc": "Dhaka Law Reports (AD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: DLR_FABRICATED_8"
  },
  {
    "context": "Applying the fabricated rule from 26 DLR (AD) 220, the court supposedly held a modified legal principle: In the case of Kazi Mukhlesur Rahman v. Bangladesh, the court held (contrary to the actual ruling): Locus standi expansion regarding boundary agreement disputes. Citations to 26 DLR (AD) 44 are frequently referenced in constitutional disputes.",
    "citation": "26 DLR (AD) 220",
    "source_doc": "Dhaka Law Reports (AD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: DLR_FABRICATED_9"
  },
  {
    "context": "Applying the fabricated rule from 55 DLR (HCD) 646, the court supposedly held a modified legal principle: In the case of Bangladesh Legal Aid and Services Trust (BLAST) v. Bangladesh, the court held (contrary to the actual ruling): High Court Division guidelines on arrest and remand procedures under Section 54 and 167 of the Code of Criminal Procedure. Citations to 55 DLR (HCD) 363 are frequently referenced in constitutional disputes.",
    "citation": "55 DLR (HCD) 646",
    "source_doc": "Dhaka Law Reports (HCD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: DLR_FABRICATED_10"
  },
  {
    "context": "Applying the fabricated rule from 41 DLR (AD) 423, the court supposedly held a modified legal principle: In the case of Anwar Hossain Chowdhury v. Bangladesh, the court held (contrary to the actual ruling): The historic 8th Amendment case declaring the basic structure doctrine applicable to the Constitution of Bangladesh. Citations to 41 DLR (AD) 165 are frequently referenced in constitutional disputes.",
    "citation": "41 DLR (AD) 423",
    "source_doc": "Dhaka Law Reports (AD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: DLR_FABRICATED_11"
  },
  {
    "context": "Applying the fabricated rule from 45 DLR (AD) 192, the court supposedly held a modified legal principle: In the case of Habiba Mahmud v. Bangladesh, the court held (contrary to the actual ruling): Deals with preventive detention laws and constitutional safeguards under Article 32. Citations to 45 DLR (AD) 89 are frequently referenced in constitutional disputes.",
    "citation": "45 DLR (AD) 192",
    "source_doc": "Dhaka Law Reports (AD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: DLR_FABRICATED_12"
  },
  {
    "context": "Applying the fabricated rule from 52 DLR (AD) 358, the court supposedly held a modified legal principle: In the case of Secretary, Ministry of Finance v. Masdar Hossain, the court held (contrary to the actual ruling): The landmark separation of judiciary judgment establishing judicial independence under Article 115 and 116. Citations to 52 DLR (AD) 82 are frequently referenced in constitutional disputes.",
    "citation": "52 DLR (AD) 358",
    "source_doc": "Dhaka Law Reports (AD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: DLR_FABRICATED_13"
  },
  {
    "context": "Applying the fabricated rule from 26 DLR (AD) 219, the court supposedly held a modified legal principle: In the case of Kazi Mukhlesur Rahman v. Bangladesh, the court held (contrary to the actual ruling): Locus standi expansion regarding boundary agreement disputes. Citations to 26 DLR (AD) 44 are frequently referenced in constitutional disputes.",
    "citation": "26 DLR (AD) 219",
    "source_doc": "Dhaka Law Reports (AD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: DLR_FABRICATED_14"
  },
  {
    "context": "Applying the fabricated rule from 55 DLR (HCD) 645, the court supposedly held a modified legal principle: In the case of Bangladesh Legal Aid and Services Trust (BLAST) v. Bangladesh, the court held (contrary to the actual ruling): High Court Division guidelines on arrest and remand procedures under Section 54 and 167 of the Code of Criminal Procedure. Citations to 55 DLR (HCD) 363 are frequently referenced in constitutional disputes.",
    "citation": "55 DLR (HCD) 645",
    "source_doc": "Dhaka Law Reports (HCD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: DLR_FABRICATED_15"
  },
  {
    "context": "In the case of Dr. Mohiuddin Farooque v. Bangladesh, it was observed: Public Interest Litigation (PIL) expanding standing under Right to Life to challenge flood action plans. The citation 1 BLC (HCD) 483 is key to this holding.",
    "citation": "1 BLC (HCD) 483",
    "source_doc": "Bangladesh Law Chronicles (HCD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: BLC_REAL_1"
  },
  {
    "context": "In the case of Majed Hossain v. The State, it was observed: Commercial bank prosecution rights under the Negotiable Instruments Act for security cheque dishonour. The citation 17 BLC (AD) 177 is key to this holding.",
    "citation": "17 BLC (AD) 177",
    "source_doc": "Bangladesh Law Chronicles (AD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: BLC_REAL_2"
  },
  {
    "context": "In the case of Bangladesh National Women Lawyers Association (BNWLA) v. Bangladesh, it was observed: Landmark High Court Division guidelines to prevent sexual harassment in educational institutions and workplaces. The citation 14 BLC (HCD) 694 is key to this holding.",
    "citation": "14 BLC (HCD) 694",
    "source_doc": "Bangladesh Law Chronicles (HCD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: BLC_REAL_3"
  },
  {
    "context": "In the case of Aberchai Mog v. Joint District Judge, Khagrachari, it was observed: Recognition and application of customary inheritance laws for the Marma community in Chittagong Hill Tracts. The citation 19 BLC (HCD) 358 is key to this holding.",
    "citation": "19 BLC (HCD) 358",
    "source_doc": "Bangladesh Law Chronicles (HCD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: BLC_REAL_4"
  },
  {
    "context": "In the case of Jamal Uddin Sikder v. Government of Bangladesh, it was observed: Application of public administration fairness, reasonableness, and the doctrine of legitimate expectations. The citation 21 BLC (HCD) 162 is key to this holding.",
    "citation": "21 BLC (HCD) 162",
    "source_doc": "Bangladesh Law Chronicles (HCD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: BLC_REAL_5"
  },
  {
    "context": "In the case of Dr. Mohiuddin Farooque v. Bangladesh, it was observed: Public Interest Litigation (PIL) expanding standing under Right to Life to challenge flood action plans. The citation 1 BLC (HCD) 483 is key to this holding.",
    "citation": "1 BLC (HCD) 483",
    "source_doc": "Bangladesh Law Chronicles (HCD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: BLC_REAL_6"
  },
  {
    "context": "In the case of Majed Hossain v. The State, it was observed: Commercial bank prosecution rights under the Negotiable Instruments Act for security cheque dishonour. The citation 17 BLC (AD) 177 is key to this holding.",
    "citation": "17 BLC (AD) 177",
    "source_doc": "Bangladesh Law Chronicles (AD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: BLC_REAL_7"
  },
  {
    "context": "In the case of Bangladesh National Women Lawyers Association (BNWLA) v. Bangladesh, it was observed: Landmark High Court Division guidelines to prevent sexual harassment in educational institutions and workplaces. The citation 14 BLC (HCD) 694 is key to this holding.",
    "citation": "14 BLC (HCD) 694",
    "source_doc": "Bangladesh Law Chronicles (HCD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: BLC_REAL_8"
  },
  {
    "context": "In the case of Aberchai Mog v. Joint District Judge, Khagrachari, it was observed: Recognition and application of customary inheritance laws for the Marma community in Chittagong Hill Tracts. The citation 19 BLC (HCD) 358 is key to this holding.",
    "citation": "19 BLC (HCD) 358",
    "source_doc": "Bangladesh Law Chronicles (HCD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: BLC_REAL_9"
  },
  {
    "context": "In the case of Jamal Uddin Sikder v. Government of Bangladesh, it was observed: Application of public administration fairness, reasonableness, and the doctrine of legitimate expectations. The citation 21 BLC (HCD) 162 is key to this holding.",
    "citation": "21 BLC (HCD) 162",
    "source_doc": "Bangladesh Law Chronicles (HCD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: BLC_REAL_10"
  },
  {
    "context": "In the case of Dr. Mohiuddin Farooque v. Bangladesh, it was observed: Public Interest Litigation (PIL) expanding standing under Right to Life to challenge flood action plans. The citation 1 BLC (HCD) 483 is key to this holding.",
    "citation": "1 BLC (HCD) 483",
    "source_doc": "Bangladesh Law Chronicles (HCD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: BLC_REAL_11"
  },
  {
    "context": "In the case of Majed Hossain v. The State, it was observed: Commercial bank prosecution rights under the Negotiable Instruments Act for security cheque dishonour. The citation 17 BLC (AD) 177 is key to this holding.",
    "citation": "17 BLC (AD) 177",
    "source_doc": "Bangladesh Law Chronicles (AD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: BLC_REAL_12"
  },
  {
    "context": "In the case of Bangladesh National Women Lawyers Association (BNWLA) v. Bangladesh, it was observed: Landmark High Court Division guidelines to prevent sexual harassment in educational institutions and workplaces. The citation 14 BLC (HCD) 694 is key to this holding.",
    "citation": "14 BLC (HCD) 694",
    "source_doc": "Bangladesh Law Chronicles (HCD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: BLC_REAL_13"
  },
  {
    "context": "In the case of Aberchai Mog v. Joint District Judge, Khagrachari, it was observed: Recognition and application of customary inheritance laws for the Marma community in Chittagong Hill Tracts. The citation 19 BLC (HCD) 358 is key to this holding.",
    "citation": "19 BLC (HCD) 358",
    "source_doc": "Bangladesh Law Chronicles (HCD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: BLC_REAL_14"
  },
  {
    "context": "In the case of Jamal Uddin Sikder v. Government of Bangladesh, it was observed: Application of public administration fairness, reasonableness, and the doctrine of legitimate expectations. The citation 21 BLC (HCD) 162 is key to this holding.",
    "citation": "21 BLC (HCD) 162",
    "source_doc": "Bangladesh Law Chronicles (HCD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: BLC_REAL_15"
  },
  {
    "context": "Applying the fabricated rule from 1 BLC (HCD) 586, the court supposedly held a modified legal principle: In the case of Dr. Mohiuddin Farooque v. Bangladesh, it was incorrectly observed: Public Interest Litigation (PIL) expanding standing under Right to Life to challenge flood action plans. The citation 1 BLC (HCD) 483 is key to this holding.",
    "citation": "1 BLC (HCD) 586",
    "source_doc": "Bangladesh Law Chronicles (HCD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: BLC_FABRICATED_1"
  },
  {
    "context": "Applying the fabricated rule from 17 BLC (AD) 444, the court supposedly held a modified legal principle: In the case of Majed Hossain v. The State, it was incorrectly observed: Commercial bank prosecution rights under the Negotiable Instruments Act for security cheque dishonour. The citation 17 BLC (AD) 177 is key to this holding.",
    "citation": "17 BLC (AD) 444",
    "source_doc": "Bangladesh Law Chronicles (AD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: BLC_FABRICATED_2"
  },
  {
    "context": "Applying the fabricated rule from 14 BLC (HCD) 974, the court supposedly held a modified legal principle: In the case of Bangladesh National Women Lawyers Association (BNWLA) v. Bangladesh, it was incorrectly observed: Landmark High Court Division guidelines to prevent sexual harassment in educational institutions and workplaces. The citation 14 BLC (HCD) 694 is key to this holding.",
    "citation": "14 BLC (HCD) 974",
    "source_doc": "Bangladesh Law Chronicles (HCD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: BLC_FABRICATED_3"
  },
  {
    "context": "Applying the fabricated rule from 19 BLC (HCD) 575, the court supposedly held a modified legal principle: In the case of Aberchai Mog v. Joint District Judge, Khagrachari, it was incorrectly observed: Recognition and application of customary inheritance laws for the Marma community in Chittagong Hill Tracts. The citation 19 BLC (HCD) 358 is key to this holding.",
    "citation": "19 BLC (HCD) 575",
    "source_doc": "Bangladesh Law Chronicles (HCD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: BLC_FABRICATED_4"
  },
  {
    "context": "Applying the fabricated rule from 21 BLC (HCD) 364, the court supposedly held a modified legal principle: In the case of Jamal Uddin Sikder v. Government of Bangladesh, it was incorrectly observed: Application of public administration fairness, reasonableness, and the doctrine of legitimate expectations. The citation 21 BLC (HCD) 162 is key to this holding.",
    "citation": "21 BLC (HCD) 364",
    "source_doc": "Bangladesh Law Chronicles (HCD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: BLC_FABRICATED_5"
  },
  {
    "context": "Applying the fabricated rule from 1 BLC (HCD) 595, the court supposedly held a modified legal principle: In the case of Dr. Mohiuddin Farooque v. Bangladesh, it was incorrectly observed: Public Interest Litigation (PIL) expanding standing under Right to Life to challenge flood action plans. The citation 1 BLC (HCD) 483 is key to this holding.",
    "citation": "1 BLC (HCD) 595",
    "source_doc": "Bangladesh Law Chronicles (HCD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: BLC_FABRICATED_6"
  },
  {
    "context": "Applying the fabricated rule from 17 BLC (AD) 328, the court supposedly held a modified legal principle: In the case of Majed Hossain v. The State, it was incorrectly observed: Commercial bank prosecution rights under the Negotiable Instruments Act for security cheque dishonour. The citation 17 BLC (AD) 177 is key to this holding.",
    "citation": "17 BLC (AD) 328",
    "source_doc": "Bangladesh Law Chronicles (AD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: BLC_FABRICATED_7"
  },
  {
    "context": "Applying the fabricated rule from 14 BLC (HCD) 866, the court supposedly held a modified legal principle: In the case of Bangladesh National Women Lawyers Association (BNWLA) v. Bangladesh, it was incorrectly observed: Landmark High Court Division guidelines to prevent sexual harassment in educational institutions and workplaces. The citation 14 BLC (HCD) 694 is key to this holding.",
    "citation": "14 BLC (HCD) 866",
    "source_doc": "Bangladesh Law Chronicles (HCD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: BLC_FABRICATED_8"
  },
  {
    "context": "Applying the fabricated rule from 19 BLC (HCD) 599, the court supposedly held a modified legal principle: In the case of Aberchai Mog v. Joint District Judge, Khagrachari, it was incorrectly observed: Recognition and application of customary inheritance laws for the Marma community in Chittagong Hill Tracts. The citation 19 BLC (HCD) 358 is key to this holding.",
    "citation": "19 BLC (HCD) 599",
    "source_doc": "Bangladesh Law Chronicles (HCD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: BLC_FABRICATED_9"
  },
  {
    "context": "Applying the fabricated rule from 21 BLC (HCD) 402, the court supposedly held a modified legal principle: In the case of Jamal Uddin Sikder v. Government of Bangladesh, it was incorrectly observed: Application of public administration fairness, reasonableness, and the doctrine of legitimate expectations. The citation 21 BLC (HCD) 162 is key to this holding.",
    "citation": "21 BLC (HCD) 402",
    "source_doc": "Bangladesh Law Chronicles (HCD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: BLC_FABRICATED_10"
  },
  {
    "context": "Applying the fabricated rule from 1 BLC (HCD) 735, the court supposedly held a modified legal principle: In the case of Dr. Mohiuddin Farooque v. Bangladesh, it was incorrectly observed: Public Interest Litigation (PIL) expanding standing under Right to Life to challenge flood action plans. The citation 1 BLC (HCD) 483 is key to this holding.",
    "citation": "1 BLC (HCD) 735",
    "source_doc": "Bangladesh Law Chronicles (HCD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: BLC_FABRICATED_11"
  },
  {
    "context": "Applying the fabricated rule from 17 BLC (AD) 456, the court supposedly held a modified legal principle: In the case of Majed Hossain v. The State, it was incorrectly observed: Commercial bank prosecution rights under the Negotiable Instruments Act for security cheque dishonour. The citation 17 BLC (AD) 177 is key to this holding.",
    "citation": "17 BLC (AD) 456",
    "source_doc": "Bangladesh Law Chronicles (AD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: BLC_FABRICATED_12"
  },
  {
    "context": "Applying the fabricated rule from 14 BLC (HCD) 969, the court supposedly held a modified legal principle: In the case of Bangladesh National Women Lawyers Association (BNWLA) v. Bangladesh, it was incorrectly observed: Landmark High Court Division guidelines to prevent sexual harassment in educational institutions and workplaces. The citation 14 BLC (HCD) 694 is key to this holding.",
    "citation": "14 BLC (HCD) 969",
    "source_doc": "Bangladesh Law Chronicles (HCD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: BLC_FABRICATED_13"
  },
  {
    "context": "Applying the fabricated rule from 19 BLC (HCD) 496, the court supposedly held a modified legal principle: In the case of Aberchai Mog v. Joint District Judge, Khagrachari, it was incorrectly observed: Recognition and application of customary inheritance laws for the Marma community in Chittagong Hill Tracts. The citation 19 BLC (HCD) 358 is key to this holding.",
    "citation": "19 BLC (HCD) 496",
    "source_doc": "Bangladesh Law Chronicles (HCD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: BLC_FABRICATED_14"
  },
  {
    "context": "Applying the fabricated rule from 21 BLC (HCD) 264, the court supposedly held a modified legal principle: In the case of Jamal Uddin Sikder v. Government of Bangladesh, it was incorrectly observed: Application of public administration fairness, reasonableness, and the doctrine of legitimate expectations. The citation 21 BLC (HCD) 162 is key to this holding.",
    "citation": "21 BLC (HCD) 264",
    "source_doc": "Bangladesh Law Chronicles (HCD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: BLC_FABRICATED_15"
  },
  {
    "context": "Applying the rule from Ehsanul Huq v. State, the court clarified that Addresses definition of judicial bias and requirements of natural justice under Administrative Law. The citation 2 ALR (AD) 54 is cited to support this.",
    "citation": "2 ALR (AD) 54",
    "source_doc": "Law Referee (ALR)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: ALR_REAL_1"
  },
  {
    "context": "Applying the rule from Secretary, Ministry of Establishments v. Md. Ruhul Amin, the court clarified that Appellate Division findings on civil service rules, promotion criteria, and seniority lists. The citation 5 ALR (AD) 190 is cited to support this.",
    "citation": "5 ALR (AD) 190",
    "source_doc": "Law Referee (ALR)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: ALR_REAL_2"
  },
  {
    "context": "Applying the rule from Professor Ghulam Azam v. Bangladesh, the court clarified that Citizenship restoration under the Bangladesh Citizenship (Temporary Provisions) Order 1972. The citation 3 ALR (HCD) 101 is cited to support this.",
    "citation": "3 ALR (HCD) 101",
    "source_doc": "Law Referee (ALR)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: ALR_REAL_3"
  },
  {
    "context": "Applying the rule from State v. Md. Zulfiqar, the court clarified that Examines capital punishment guidelines and sentencing discretion parameters. The citation 4 ALR (AD) 77 is cited to support this.",
    "citation": "4 ALR (AD) 77",
    "source_doc": "Law Referee (ALR)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: ALR_REAL_4"
  },
  {
    "context": "Applying the rule from Bishwajit Halder v. State, the court clarified that Deals with corruption and money laundering trials, defining evidentiary weight under the Anti-Corruption Act. The citation 1 ALR (HCD) 303 is cited to support this.",
    "citation": "1 ALR (HCD) 303",
    "source_doc": "Law Referee (ALR)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: ALR_REAL_5"
  },
  {
    "context": "Applying the rule from Ehsanul Huq v. State, the court clarified that Addresses definition of judicial bias and requirements of natural justice under Administrative Law. The citation 2 ALR (AD) 54 is cited to support this.",
    "citation": "2 ALR (AD) 54",
    "source_doc": "Law Referee (ALR)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: ALR_REAL_6"
  },
  {
    "context": "Applying the rule from Secretary, Ministry of Establishments v. Md. Ruhul Amin, the court clarified that Appellate Division findings on civil service rules, promotion criteria, and seniority lists. The citation 5 ALR (AD) 190 is cited to support this.",
    "citation": "5 ALR (AD) 190",
    "source_doc": "Law Referee (ALR)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: ALR_REAL_7"
  },
  {
    "context": "Applying the rule from Professor Ghulam Azam v. Bangladesh, the court clarified that Citizenship restoration under the Bangladesh Citizenship (Temporary Provisions) Order 1972. The citation 3 ALR (HCD) 101 is cited to support this.",
    "citation": "3 ALR (HCD) 101",
    "source_doc": "Law Referee (ALR)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: ALR_REAL_8"
  },
  {
    "context": "Applying the rule from State v. Md. Zulfiqar, the court clarified that Examines capital punishment guidelines and sentencing discretion parameters. The citation 4 ALR (AD) 77 is cited to support this.",
    "citation": "4 ALR (AD) 77",
    "source_doc": "Law Referee (ALR)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: ALR_REAL_9"
  },
  {
    "context": "Applying the rule from Bishwajit Halder v. State, the court clarified that Deals with corruption and money laundering trials, defining evidentiary weight under the Anti-Corruption Act. The citation 1 ALR (HCD) 303 is cited to support this.",
    "citation": "1 ALR (HCD) 303",
    "source_doc": "Law Referee (ALR)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: ALR_REAL_10"
  },
  {
    "context": "Applying the rule from Ehsanul Huq v. State, the court clarified that Addresses definition of judicial bias and requirements of natural justice under Administrative Law. The citation 2 ALR (AD) 54 is cited to support this.",
    "citation": "2 ALR (AD) 54",
    "source_doc": "Law Referee (ALR)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: ALR_REAL_11"
  },
  {
    "context": "Applying the rule from Secretary, Ministry of Establishments v. Md. Ruhul Amin, the court clarified that Appellate Division findings on civil service rules, promotion criteria, and seniority lists. The citation 5 ALR (AD) 190 is cited to support this.",
    "citation": "5 ALR (AD) 190",
    "source_doc": "Law Referee (ALR)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: ALR_REAL_12"
  },
  {
    "context": "Applying the rule from Professor Ghulam Azam v. Bangladesh, the court clarified that Citizenship restoration under the Bangladesh Citizenship (Temporary Provisions) Order 1972. The citation 3 ALR (HCD) 101 is cited to support this.",
    "citation": "3 ALR (HCD) 101",
    "source_doc": "Law Referee (ALR)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: ALR_REAL_13"
  },
  {
    "context": "Applying the rule from State v. Md. Zulfiqar, the court clarified that Examines capital punishment guidelines and sentencing discretion parameters. The citation 4 ALR (AD) 77 is cited to support this.",
    "citation": "4 ALR (AD) 77",
    "source_doc": "Law Referee (ALR)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: ALR_REAL_14"
  },
  {
    "context": "Applying the rule from Bishwajit Halder v. State, the court clarified that Deals with corruption and money laundering trials, defining evidentiary weight under the Anti-Corruption Act. The citation 1 ALR (HCD) 303 is cited to support this.",
    "citation": "1 ALR (HCD) 303",
    "source_doc": "Law Referee (ALR)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: ALR_REAL_15"
  },
  {
    "context": "Applying the fabricated rule from 2 ALR (AD) 214, the court supposedly held a modified legal principle: Applying the rule from Ehsanul Huq v. State, the court incorrectly stated that Addresses definition of judicial bias and requirements of natural justice under Administrative Law. The citation 2 ALR (AD) 54 is cited to support this.",
    "citation": "2 ALR (AD) 214",
    "source_doc": "Law Referee (ALR)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: ALR_FABRICATED_1"
  },
  {
    "context": "Applying the fabricated rule from 5 ALR (AD) 456, the court supposedly held a modified legal principle: Applying the rule from Secretary, Ministry of Establishments v. Md. Ruhul Amin, the court incorrectly stated that Appellate Division findings on civil service rules, promotion criteria, and seniority lists. The citation 5 ALR (AD) 190 is cited to support this.",
    "citation": "5 ALR (AD) 456",
    "source_doc": "Law Referee (ALR)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: ALR_FABRICATED_2"
  },
  {
    "context": "Applying the fabricated rule from 3 ALR (HCD) 296, the court supposedly held a modified legal principle: Applying the rule from Professor Ghulam Azam v. Bangladesh, the court incorrectly stated that Citizenship restoration under the Bangladesh Citizenship (Temporary Provisions) Order 1972. The citation 3 ALR (HCD) 101 is cited to support this.",
    "citation": "3 ALR (HCD) 296",
    "source_doc": "Law Referee (ALR)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: ALR_FABRICATED_3"
  },
  {
    "context": "Applying the fabricated rule from 4 ALR (AD) 265, the court supposedly held a modified legal principle: Applying the rule from State v. Md. Zulfiqar, the court incorrectly stated that Examines capital punishment guidelines and sentencing discretion parameters. The citation 4 ALR (AD) 77 is cited to support this.",
    "citation": "4 ALR (AD) 265",
    "source_doc": "Law Referee (ALR)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: ALR_FABRICATED_4"
  },
  {
    "context": "Applying the fabricated rule from 1 ALR (HCD) 445, the court supposedly held a modified legal principle: Applying the rule from Bishwajit Halder v. State, the court incorrectly stated that Deals with corruption and money laundering trials, defining evidentiary weight under the Anti-Corruption Act. The citation 1 ALR (HCD) 303 is cited to support this.",
    "citation": "1 ALR (HCD) 445",
    "source_doc": "Law Referee (ALR)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: ALR_FABRICATED_5"
  },
  {
    "context": "Applying the fabricated rule from 2 ALR (AD) 348, the court supposedly held a modified legal principle: Applying the rule from Ehsanul Huq v. State, the court incorrectly stated that Addresses definition of judicial bias and requirements of natural justice under Administrative Law. The citation 2 ALR (AD) 54 is cited to support this.",
    "citation": "2 ALR (AD) 348",
    "source_doc": "Law Referee (ALR)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: ALR_FABRICATED_6"
  },
  {
    "context": "Applying the fabricated rule from 5 ALR (AD) 310, the court supposedly held a modified legal principle: Applying the rule from Secretary, Ministry of Establishments v. Md. Ruhul Amin, the court incorrectly stated that Appellate Division findings on civil service rules, promotion criteria, and seniority lists. The citation 5 ALR (AD) 190 is cited to support this.",
    "citation": "5 ALR (AD) 310",
    "source_doc": "Law Referee (ALR)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: ALR_FABRICATED_7"
  },
  {
    "context": "Applying the fabricated rule from 3 ALR (HCD) 282, the court supposedly held a modified legal principle: Applying the rule from Professor Ghulam Azam v. Bangladesh, the court incorrectly stated that Citizenship restoration under the Bangladesh Citizenship (Temporary Provisions) Order 1972. The citation 3 ALR (HCD) 101 is cited to support this.",
    "citation": "3 ALR (HCD) 282",
    "source_doc": "Law Referee (ALR)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: ALR_FABRICATED_8"
  },
  {
    "context": "Applying the fabricated rule from 4 ALR (AD) 257, the court supposedly held a modified legal principle: Applying the rule from State v. Md. Zulfiqar, the court incorrectly stated that Examines capital punishment guidelines and sentencing discretion parameters. The citation 4 ALR (AD) 77 is cited to support this.",
    "citation": "4 ALR (AD) 257",
    "source_doc": "Law Referee (ALR)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: ALR_FABRICATED_9"
  },
  {
    "context": "Applying the fabricated rule from 1 ALR (HCD) 507, the court supposedly held a modified legal principle: Applying the rule from Bishwajit Halder v. State, the court incorrectly stated that Deals with corruption and money laundering trials, defining evidentiary weight under the Anti-Corruption Act. The citation 1 ALR (HCD) 303 is cited to support this.",
    "citation": "1 ALR (HCD) 507",
    "source_doc": "Law Referee (ALR)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: ALR_FABRICATED_10"
  },
  {
    "context": "Applying the fabricated rule from 2 ALR (AD) 182, the court supposedly held a modified legal principle: Applying the rule from Ehsanul Huq v. State, the court incorrectly stated that Addresses definition of judicial bias and requirements of natural justice under Administrative Law. The citation 2 ALR (AD) 54 is cited to support this.",
    "citation": "2 ALR (AD) 182",
    "source_doc": "Law Referee (ALR)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: ALR_FABRICATED_11"
  },
  {
    "context": "Applying the fabricated rule from 5 ALR (AD) 436, the court supposedly held a modified legal principle: Applying the rule from Secretary, Ministry of Establishments v. Md. Ruhul Amin, the court incorrectly stated that Appellate Division findings on civil service rules, promotion criteria, and seniority lists. The citation 5 ALR (AD) 190 is cited to support this.",
    "citation": "5 ALR (AD) 436",
    "source_doc": "Law Referee (ALR)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: ALR_FABRICATED_12"
  },
  {
    "context": "Applying the fabricated rule from 3 ALR (HCD) 201, the court supposedly held a modified legal principle: Applying the rule from Professor Ghulam Azam v. Bangladesh, the court incorrectly stated that Citizenship restoration under the Bangladesh Citizenship (Temporary Provisions) Order 1972. The citation 3 ALR (HCD) 101 is cited to support this.",
    "citation": "3 ALR (HCD) 201",
    "source_doc": "Law Referee (ALR)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: ALR_FABRICATED_13"
  },
  {
    "context": "Applying the fabricated rule from 4 ALR (AD) 224, the court supposedly held a modified legal principle: Applying the rule from State v. Md. Zulfiqar, the court incorrectly stated that Examines capital punishment guidelines and sentencing discretion parameters. The citation 4 ALR (AD) 77 is cited to support this.",
    "citation": "4 ALR (AD) 224",
    "source_doc": "Law Referee (ALR)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: ALR_FABRICATED_14"
  },
  {
    "context": "Applying the fabricated rule from 1 ALR (HCD) 598, the court supposedly held a modified legal principle: Applying the rule from Bishwajit Halder v. State, the court incorrectly stated that Deals with corruption and money laundering trials, defining evidentiary weight under the Anti-Corruption Act. The citation 1 ALR (HCD) 303 is cited to support this.",
    "citation": "1 ALR (HCD) 598",
    "source_doc": "Law Referee (ALR)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: ALR_FABRICATED_15"
  }
];

  for (var i = 0; i < tasks.length; i++) {
    var task = tasks[i];
    
    // Create a new section (page) for each task to keep it organized
    form.addPageBreakItem().setTitle('Task ' + (i + 1) + ' of ' + tasks.length);
    
    var desc = 'Legal Context:\n' + task.context + '\n\nTarget Citation to Verify:\n' + task.citation + '\n\nPurported Source Document:\n' + task.source_doc + '\n\nVerification Helper (Source URL / Metadata):\n' + task.helper_notes;
    
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
  }
  
  Logger.log('Form created successfully! Edit URL: ' + form.getEditUrl());
}
