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
    "context": "Applying the fabricated rule from 41 DLR (AD) 297, the court supposedly held a modified legal principle: In the case of Anwar Hossain Chowdhury v. Bangladesh, the court held (contrary to the actual ruling): The historic 8th Amendment case declaring the basic structure doctrine applicable to the Constitution of Bangladesh. Citations to 41 DLR (AD) 165 are frequently referenced in constitutional disputes.",
    "citation": "41 DLR (AD) 297",
    "source_doc": "Dhaka Law Reports (AD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: DLR_FABRICATED_1"
  },
  {
    "context": "Applying the fabricated rule from 45 DLR (AD) 243, the court supposedly held a modified legal principle: In the case of Habiba Mahmud v. Bangladesh, the court held (contrary to the actual ruling): Deals with preventive detention laws and constitutional safeguards under Article 32. Citations to 45 DLR (AD) 89 are frequently referenced in constitutional disputes.",
    "citation": "45 DLR (AD) 243",
    "source_doc": "Dhaka Law Reports (AD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: DLR_FABRICATED_2"
  },
  {
    "context": "Applying the fabricated rule from 52 DLR (AD) 262, the court supposedly held a modified legal principle: In the case of Secretary, Ministry of Finance v. Masdar Hossain, the court held (contrary to the actual ruling): The landmark separation of judiciary judgment establishing judicial independence under Article 115 and 116. Citations to 52 DLR (AD) 82 are frequently referenced in constitutional disputes.",
    "citation": "52 DLR (AD) 262",
    "source_doc": "Dhaka Law Reports (AD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: DLR_FABRICATED_3"
  },
  {
    "context": "Applying the fabricated rule from 26 DLR (AD) 196, the court supposedly held a modified legal principle: In the case of Kazi Mukhlesur Rahman v. Bangladesh, the court held (contrary to the actual ruling): Locus standi expansion regarding boundary agreement disputes. Citations to 26 DLR (AD) 44 are frequently referenced in constitutional disputes.",
    "citation": "26 DLR (AD) 196",
    "source_doc": "Dhaka Law Reports (AD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: DLR_FABRICATED_4"
  },
  {
    "context": "Applying the fabricated rule from 55 DLR (HCD) 580, the court supposedly held a modified legal principle: In the case of Bangladesh Legal Aid and Services Trust (BLAST) v. Bangladesh, the court held (contrary to the actual ruling): High Court Division guidelines on arrest and remand procedures under Section 54 and 167 of the Code of Criminal Procedure. Citations to 55 DLR (HCD) 363 are frequently referenced in constitutional disputes.",
    "citation": "55 DLR (HCD) 580",
    "source_doc": "Dhaka Law Reports (HCD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: DLR_FABRICATED_5"
  },
  {
    "context": "Applying the fabricated rule from 41 DLR (AD) 275, the court supposedly held a modified legal principle: In the case of Anwar Hossain Chowdhury v. Bangladesh, the court held (contrary to the actual ruling): The historic 8th Amendment case declaring the basic structure doctrine applicable to the Constitution of Bangladesh. Citations to 41 DLR (AD) 165 are frequently referenced in constitutional disputes.",
    "citation": "41 DLR (AD) 275",
    "source_doc": "Dhaka Law Reports (AD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: DLR_FABRICATED_6"
  },
  {
    "context": "Applying the fabricated rule from 45 DLR (AD) 273, the court supposedly held a modified legal principle: In the case of Habiba Mahmud v. Bangladesh, the court held (contrary to the actual ruling): Deals with preventive detention laws and constitutional safeguards under Article 32. Citations to 45 DLR (AD) 89 are frequently referenced in constitutional disputes.",
    "citation": "45 DLR (AD) 273",
    "source_doc": "Dhaka Law Reports (AD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: DLR_FABRICATED_7"
  },
  {
    "context": "Applying the fabricated rule from 52 DLR (AD) 192, the court supposedly held a modified legal principle: In the case of Secretary, Ministry of Finance v. Masdar Hossain, the court held (contrary to the actual ruling): The landmark separation of judiciary judgment establishing judicial independence under Article 115 and 116. Citations to 52 DLR (AD) 82 are frequently referenced in constitutional disputes.",
    "citation": "52 DLR (AD) 192",
    "source_doc": "Dhaka Law Reports (AD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: DLR_FABRICATED_8"
  },
  {
    "context": "Applying the fabricated rule from 26 DLR (AD) 224, the court supposedly held a modified legal principle: In the case of Kazi Mukhlesur Rahman v. Bangladesh, the court held (contrary to the actual ruling): Locus standi expansion regarding boundary agreement disputes. Citations to 26 DLR (AD) 44 are frequently referenced in constitutional disputes.",
    "citation": "26 DLR (AD) 224",
    "source_doc": "Dhaka Law Reports (AD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: DLR_FABRICATED_9"
  },
  {
    "context": "Applying the fabricated rule from 55 DLR (HCD) 546, the court supposedly held a modified legal principle: In the case of Bangladesh Legal Aid and Services Trust (BLAST) v. Bangladesh, the court held (contrary to the actual ruling): High Court Division guidelines on arrest and remand procedures under Section 54 and 167 of the Code of Criminal Procedure. Citations to 55 DLR (HCD) 363 are frequently referenced in constitutional disputes.",
    "citation": "55 DLR (HCD) 546",
    "source_doc": "Dhaka Law Reports (HCD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: DLR_FABRICATED_10"
  },
  {
    "context": "Applying the fabricated rule from 41 DLR (AD) 275, the court supposedly held a modified legal principle: In the case of Anwar Hossain Chowdhury v. Bangladesh, the court held (contrary to the actual ruling): The historic 8th Amendment case declaring the basic structure doctrine applicable to the Constitution of Bangladesh. Citations to 41 DLR (AD) 165 are frequently referenced in constitutional disputes.",
    "citation": "41 DLR (AD) 275",
    "source_doc": "Dhaka Law Reports (AD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: DLR_FABRICATED_11"
  },
  {
    "context": "Applying the fabricated rule from 45 DLR (AD) 347, the court supposedly held a modified legal principle: In the case of Habiba Mahmud v. Bangladesh, the court held (contrary to the actual ruling): Deals with preventive detention laws and constitutional safeguards under Article 32. Citations to 45 DLR (AD) 89 are frequently referenced in constitutional disputes.",
    "citation": "45 DLR (AD) 347",
    "source_doc": "Dhaka Law Reports (AD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: DLR_FABRICATED_12"
  },
  {
    "context": "Applying the fabricated rule from 52 DLR (AD) 190, the court supposedly held a modified legal principle: In the case of Secretary, Ministry of Finance v. Masdar Hossain, the court held (contrary to the actual ruling): The landmark separation of judiciary judgment establishing judicial independence under Article 115 and 116. Citations to 52 DLR (AD) 82 are frequently referenced in constitutional disputes.",
    "citation": "52 DLR (AD) 190",
    "source_doc": "Dhaka Law Reports (AD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: DLR_FABRICATED_13"
  },
  {
    "context": "Applying the fabricated rule from 26 DLR (AD) 192, the court supposedly held a modified legal principle: In the case of Kazi Mukhlesur Rahman v. Bangladesh, the court held (contrary to the actual ruling): Locus standi expansion regarding boundary agreement disputes. Citations to 26 DLR (AD) 44 are frequently referenced in constitutional disputes.",
    "citation": "26 DLR (AD) 192",
    "source_doc": "Dhaka Law Reports (AD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: DLR_FABRICATED_14"
  },
  {
    "context": "Applying the fabricated rule from 55 DLR (HCD) 632, the court supposedly held a modified legal principle: In the case of Bangladesh Legal Aid and Services Trust (BLAST) v. Bangladesh, the court held (contrary to the actual ruling): High Court Division guidelines on arrest and remand procedures under Section 54 and 167 of the Code of Criminal Procedure. Citations to 55 DLR (HCD) 363 are frequently referenced in constitutional disputes.",
    "citation": "55 DLR (HCD) 632",
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
    "context": "In the case of Aberchai Mog v. Joint District Judge, Khagrachari, it was observed: Chittagong Hill Tracts land-dispute forum jurisdiction under the Chittagong Hill Tracts Regulation 1900 and Adivasi rights statutes. The citation 19 BLC (HCD) 358 is key to this holding.",
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
    "context": "In the case of Aberchai Mog v. Joint District Judge, Khagrachari, it was observed: Chittagong Hill Tracts land-dispute forum jurisdiction under the Chittagong Hill Tracts Regulation 1900 and Adivasi rights statutes. The citation 19 BLC (HCD) 358 is key to this holding.",
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
    "context": "In the case of Aberchai Mog v. Joint District Judge, Khagrachari, it was observed: Chittagong Hill Tracts land-dispute forum jurisdiction under the Chittagong Hill Tracts Regulation 1900 and Adivasi rights statutes. The citation 19 BLC (HCD) 358 is key to this holding.",
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
    "context": "Applying the fabricated rule from 1 BLC (HCD) 664, the court supposedly held a modified legal principle: In the case of Dr. Mohiuddin Farooque v. Bangladesh, it was incorrectly observed: Public Interest Litigation (PIL) expanding standing under Right to Life to challenge flood action plans. The citation 1 BLC (HCD) 483 is key to this holding.",
    "citation": "1 BLC (HCD) 664",
    "source_doc": "Bangladesh Law Chronicles (HCD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: BLC_FABRICATED_1"
  },
  {
    "context": "Applying the fabricated rule from 17 BLC (AD) 435, the court supposedly held a modified legal principle: In the case of Majed Hossain v. The State, it was incorrectly observed: Commercial bank prosecution rights under the Negotiable Instruments Act for security cheque dishonour. The citation 17 BLC (AD) 177 is key to this holding.",
    "citation": "17 BLC (AD) 435",
    "source_doc": "Bangladesh Law Chronicles (AD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: BLC_FABRICATED_2"
  },
  {
    "context": "Applying the fabricated rule from 14 BLC (HCD) 901, the court supposedly held a modified legal principle: In the case of Bangladesh National Women Lawyers Association (BNWLA) v. Bangladesh, it was incorrectly observed: Landmark High Court Division guidelines to prevent sexual harassment in educational institutions and workplaces. The citation 14 BLC (HCD) 694 is key to this holding.",
    "citation": "14 BLC (HCD) 901",
    "source_doc": "Bangladesh Law Chronicles (HCD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: BLC_FABRICATED_3"
  },
  {
    "context": "Applying the fabricated rule from 19 BLC (HCD) 531, the court supposedly held a modified legal principle: In the case of Aberchai Mog v. Joint District Judge, Khagrachari, it was incorrectly observed: Chittagong Hill Tracts land-dispute forum jurisdiction under the Chittagong Hill Tracts Regulation 1900 and Adivasi rights statutes. The citation 19 BLC (HCD) 358 is key to this holding.",
    "citation": "19 BLC (HCD) 531",
    "source_doc": "Bangladesh Law Chronicles (HCD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: BLC_FABRICATED_4"
  },
  {
    "context": "Applying the fabricated rule from 21 BLC (HCD) 391, the court supposedly held a modified legal principle: In the case of Jamal Uddin Sikder v. Government of Bangladesh, it was incorrectly observed: Application of public administration fairness, reasonableness, and the doctrine of legitimate expectations. The citation 21 BLC (HCD) 162 is key to this holding.",
    "citation": "21 BLC (HCD) 391",
    "source_doc": "Bangladesh Law Chronicles (HCD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: BLC_FABRICATED_5"
  },
  {
    "context": "Applying the fabricated rule from 1 BLC (HCD) 645, the court supposedly held a modified legal principle: In the case of Dr. Mohiuddin Farooque v. Bangladesh, it was incorrectly observed: Public Interest Litigation (PIL) expanding standing under Right to Life to challenge flood action plans. The citation 1 BLC (HCD) 483 is key to this holding.",
    "citation": "1 BLC (HCD) 645",
    "source_doc": "Bangladesh Law Chronicles (HCD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: BLC_FABRICATED_6"
  },
  {
    "context": "Applying the fabricated rule from 17 BLC (AD) 444, the court supposedly held a modified legal principle: In the case of Majed Hossain v. The State, it was incorrectly observed: Commercial bank prosecution rights under the Negotiable Instruments Act for security cheque dishonour. The citation 17 BLC (AD) 177 is key to this holding.",
    "citation": "17 BLC (AD) 444",
    "source_doc": "Bangladesh Law Chronicles (AD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: BLC_FABRICATED_7"
  },
  {
    "context": "Applying the fabricated rule from 14 BLC (HCD) 976, the court supposedly held a modified legal principle: In the case of Bangladesh National Women Lawyers Association (BNWLA) v. Bangladesh, it was incorrectly observed: Landmark High Court Division guidelines to prevent sexual harassment in educational institutions and workplaces. The citation 14 BLC (HCD) 694 is key to this holding.",
    "citation": "14 BLC (HCD) 976",
    "source_doc": "Bangladesh Law Chronicles (HCD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: BLC_FABRICATED_8"
  },
  {
    "context": "Applying the fabricated rule from 19 BLC (HCD) 575, the court supposedly held a modified legal principle: In the case of Aberchai Mog v. Joint District Judge, Khagrachari, it was incorrectly observed: Chittagong Hill Tracts land-dispute forum jurisdiction under the Chittagong Hill Tracts Regulation 1900 and Adivasi rights statutes. The citation 19 BLC (HCD) 358 is key to this holding.",
    "citation": "19 BLC (HCD) 575",
    "source_doc": "Bangladesh Law Chronicles (HCD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: BLC_FABRICATED_9"
  },
  {
    "context": "Applying the fabricated rule from 21 BLC (HCD) 410, the court supposedly held a modified legal principle: In the case of Jamal Uddin Sikder v. Government of Bangladesh, it was incorrectly observed: Application of public administration fairness, reasonableness, and the doctrine of legitimate expectations. The citation 21 BLC (HCD) 162 is key to this holding.",
    "citation": "21 BLC (HCD) 410",
    "source_doc": "Bangladesh Law Chronicles (HCD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: BLC_FABRICATED_10"
  },
  {
    "context": "Applying the fabricated rule from 1 BLC (HCD) 772, the court supposedly held a modified legal principle: In the case of Dr. Mohiuddin Farooque v. Bangladesh, it was incorrectly observed: Public Interest Litigation (PIL) expanding standing under Right to Life to challenge flood action plans. The citation 1 BLC (HCD) 483 is key to this holding.",
    "citation": "1 BLC (HCD) 772",
    "source_doc": "Bangladesh Law Chronicles (HCD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: BLC_FABRICATED_11"
  },
  {
    "context": "Applying the fabricated rule from 17 BLC (AD) 421, the court supposedly held a modified legal principle: In the case of Majed Hossain v. The State, it was incorrectly observed: Commercial bank prosecution rights under the Negotiable Instruments Act for security cheque dishonour. The citation 17 BLC (AD) 177 is key to this holding.",
    "citation": "17 BLC (AD) 421",
    "source_doc": "Bangladesh Law Chronicles (AD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: BLC_FABRICATED_12"
  },
  {
    "context": "Applying the fabricated rule from 14 BLC (HCD) 946, the court supposedly held a modified legal principle: In the case of Bangladesh National Women Lawyers Association (BNWLA) v. Bangladesh, it was incorrectly observed: Landmark High Court Division guidelines to prevent sexual harassment in educational institutions and workplaces. The citation 14 BLC (HCD) 694 is key to this holding.",
    "citation": "14 BLC (HCD) 946",
    "source_doc": "Bangladesh Law Chronicles (HCD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: BLC_FABRICATED_13"
  },
  {
    "context": "Applying the fabricated rule from 19 BLC (HCD) 510, the court supposedly held a modified legal principle: In the case of Aberchai Mog v. Joint District Judge, Khagrachari, it was incorrectly observed: Chittagong Hill Tracts land-dispute forum jurisdiction under the Chittagong Hill Tracts Regulation 1900 and Adivasi rights statutes. The citation 19 BLC (HCD) 358 is key to this holding.",
    "citation": "19 BLC (HCD) 510",
    "source_doc": "Bangladesh Law Chronicles (HCD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: BLC_FABRICATED_14"
  },
  {
    "context": "Applying the fabricated rule from 21 BLC (HCD) 360, the court supposedly held a modified legal principle: In the case of Jamal Uddin Sikder v. Government of Bangladesh, it was incorrectly observed: Application of public administration fairness, reasonableness, and the doctrine of legitimate expectations. The citation 21 BLC (HCD) 162 is key to this holding.",
    "citation": "21 BLC (HCD) 360",
    "source_doc": "Bangladesh Law Chronicles (HCD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: BLC_FABRICATED_15"
  },
  {
    "context": "In the case of Abdul Latif Mirza v. Government of Bangladesh, the court held: Preventive detention under the Special Powers Act, 1974 must satisfy principles of natural justice. Citations to 31 DLR (AD) 33 are frequently referenced in administrative law disputes.",
    "citation": "31 DLR (AD) 33",
    "source_doc": "Dhaka Law Reports (AD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: ALR_REAL_1"
  },
  {
    "context": "In the case of Mujibur Rahman (Md) v. Government of Bangladesh and others, the court held: Appellate Division findings on civil service seniority disputes between promotees and direct recruits. Citations to 44 DLR (AD) 111 are frequently referenced in administrative law disputes.",
    "citation": "44 DLR (AD) 111",
    "source_doc": "Dhaka Law Reports (AD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: ALR_REAL_2"
  },
  {
    "context": "In the case of Professor Ghulam Azam v. Bangladesh, the court held: Citizenship restoration under the Bangladesh Citizenship (Temporary Provisions) Order 1972. Citations to 46 DLR (AD) 192 are frequently referenced in constitutional disputes.",
    "citation": "46 DLR (AD) 192",
    "source_doc": "Dhaka Law Reports (AD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: ALR_REAL_3"
  },
  {
    "context": "In the case of State v. Sukur Ali, the court held: Mandatory death penalty provisions under the Nari O Shishu Nirjatan Daman Ain declared unconstitutional; sentencing discretion restored to courts. Citations to 67 DLR (AD) 185 are frequently referenced in criminal law disputes.",
    "citation": "67 DLR (AD) 185",
    "source_doc": "Dhaka Law Reports (AD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: ALR_REAL_4"
  },
  {
    "context": "In the case of Anti-Corruption Commission v. Iqbal Hasan Mahmood, the court held: Evidentiary weight of property valuation assessments under Section 27 of the Anti-Corruption Commission Act. Citations to 70 DLR (AD) 109 are frequently referenced in anti-corruption disputes.",
    "citation": "70 DLR (AD) 109",
    "source_doc": "Dhaka Law Reports (AD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: ALR_REAL_5"
  },
  {
    "context": "In the case of Abdul Latif Mirza v. Government of Bangladesh, the court held: Preventive detention under the Special Powers Act, 1974 must satisfy principles of natural justice. Citations to 31 DLR (AD) 33 are frequently referenced in administrative law disputes.",
    "citation": "31 DLR (AD) 33",
    "source_doc": "Dhaka Law Reports (AD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: ALR_REAL_6"
  },
  {
    "context": "In the case of Mujibur Rahman (Md) v. Government of Bangladesh and others, the court held: Appellate Division findings on civil service seniority disputes between promotees and direct recruits. Citations to 44 DLR (AD) 111 are frequently referenced in administrative law disputes.",
    "citation": "44 DLR (AD) 111",
    "source_doc": "Dhaka Law Reports (AD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: ALR_REAL_7"
  },
  {
    "context": "In the case of Professor Ghulam Azam v. Bangladesh, the court held: Citizenship restoration under the Bangladesh Citizenship (Temporary Provisions) Order 1972. Citations to 46 DLR (AD) 192 are frequently referenced in constitutional disputes.",
    "citation": "46 DLR (AD) 192",
    "source_doc": "Dhaka Law Reports (AD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: ALR_REAL_8"
  },
  {
    "context": "In the case of State v. Sukur Ali, the court held: Mandatory death penalty provisions under the Nari O Shishu Nirjatan Daman Ain declared unconstitutional; sentencing discretion restored to courts. Citations to 67 DLR (AD) 185 are frequently referenced in criminal law disputes.",
    "citation": "67 DLR (AD) 185",
    "source_doc": "Dhaka Law Reports (AD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: ALR_REAL_9"
  },
  {
    "context": "In the case of Anti-Corruption Commission v. Iqbal Hasan Mahmood, the court held: Evidentiary weight of property valuation assessments under Section 27 of the Anti-Corruption Commission Act. Citations to 70 DLR (AD) 109 are frequently referenced in anti-corruption disputes.",
    "citation": "70 DLR (AD) 109",
    "source_doc": "Dhaka Law Reports (AD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: ALR_REAL_10"
  },
  {
    "context": "In the case of Abdul Latif Mirza v. Government of Bangladesh, the court held: Preventive detention under the Special Powers Act, 1974 must satisfy principles of natural justice. Citations to 31 DLR (AD) 33 are frequently referenced in administrative law disputes.",
    "citation": "31 DLR (AD) 33",
    "source_doc": "Dhaka Law Reports (AD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: ALR_REAL_11"
  },
  {
    "context": "In the case of Mujibur Rahman (Md) v. Government of Bangladesh and others, the court held: Appellate Division findings on civil service seniority disputes between promotees and direct recruits. Citations to 44 DLR (AD) 111 are frequently referenced in administrative law disputes.",
    "citation": "44 DLR (AD) 111",
    "source_doc": "Dhaka Law Reports (AD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: ALR_REAL_12"
  },
  {
    "context": "In the case of Professor Ghulam Azam v. Bangladesh, the court held: Citizenship restoration under the Bangladesh Citizenship (Temporary Provisions) Order 1972. Citations to 46 DLR (AD) 192 are frequently referenced in constitutional disputes.",
    "citation": "46 DLR (AD) 192",
    "source_doc": "Dhaka Law Reports (AD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: ALR_REAL_13"
  },
  {
    "context": "In the case of State v. Sukur Ali, the court held: Mandatory death penalty provisions under the Nari O Shishu Nirjatan Daman Ain declared unconstitutional; sentencing discretion restored to courts. Citations to 67 DLR (AD) 185 are frequently referenced in criminal law disputes.",
    "citation": "67 DLR (AD) 185",
    "source_doc": "Dhaka Law Reports (AD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: ALR_REAL_14"
  },
  {
    "context": "In the case of Anti-Corruption Commission v. Iqbal Hasan Mahmood, the court held: Evidentiary weight of property valuation assessments under Section 27 of the Anti-Corruption Commission Act. Citations to 70 DLR (AD) 109 are frequently referenced in anti-corruption disputes.",
    "citation": "70 DLR (AD) 109",
    "source_doc": "Dhaka Law Reports (AD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: ALR_REAL_15"
  },
  {
    "context": "Applying the fabricated rule from 31 DLR (AD) 245, the court supposedly held a modified legal principle: In the case of Abdul Latif Mirza v. Government of Bangladesh, the court held (contrary to the actual ruling): Preventive detention under the Special Powers Act, 1974 must satisfy principles of natural justice. Citations to 31 DLR (AD) 33 are frequently referenced in administrative law disputes.",
    "citation": "31 DLR (AD) 245",
    "source_doc": "Dhaka Law Reports (AD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: ALR_FABRICATED_1"
  },
  {
    "context": "Applying the fabricated rule from 44 DLR (AD) 241, the court supposedly held a modified legal principle: In the case of Mujibur Rahman (Md) v. Government of Bangladesh and others, the court held (contrary to the actual ruling): Appellate Division findings on civil service seniority disputes between promotees and direct recruits. Citations to 44 DLR (AD) 111 are frequently referenced in administrative law disputes.",
    "citation": "44 DLR (AD) 241",
    "source_doc": "Dhaka Law Reports (AD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: ALR_FABRICATED_2"
  },
  {
    "context": "Applying the fabricated rule from 46 DLR (AD) 416, the court supposedly held a modified legal principle: In the case of Professor Ghulam Azam v. Bangladesh, the court held (contrary to the actual ruling): Citizenship restoration under the Bangladesh Citizenship (Temporary Provisions) Order 1972. Citations to 46 DLR (AD) 192 are frequently referenced in constitutional disputes.",
    "citation": "46 DLR (AD) 416",
    "source_doc": "Dhaka Law Reports (AD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: ALR_FABRICATED_3"
  },
  {
    "context": "Applying the fabricated rule from 67 DLR (AD) 485, the court supposedly held a modified legal principle: In the case of State v. Sukur Ali, the court held (contrary to the actual ruling): Mandatory death penalty provisions under the Nari O Shishu Nirjatan Daman Ain declared unconstitutional; sentencing discretion restored to courts. Citations to 67 DLR (AD) 185 are frequently referenced in criminal law disputes.",
    "citation": "67 DLR (AD) 485",
    "source_doc": "Dhaka Law Reports (AD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: ALR_FABRICATED_4"
  },
  {
    "context": "Applying the fabricated rule from 70 DLR (AD) 397, the court supposedly held a modified legal principle: In the case of Anti-Corruption Commission v. Iqbal Hasan Mahmood, the court held (contrary to the actual ruling): Evidentiary weight of property valuation assessments under Section 27 of the Anti-Corruption Commission Act. Citations to 70 DLR (AD) 109 are frequently referenced in anti-corruption disputes.",
    "citation": "70 DLR (AD) 397",
    "source_doc": "Dhaka Law Reports (AD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: ALR_FABRICATED_5"
  },
  {
    "context": "Applying the fabricated rule from 31 DLR (AD) 255, the court supposedly held a modified legal principle: In the case of Abdul Latif Mirza v. Government of Bangladesh, the court held (contrary to the actual ruling): Preventive detention under the Special Powers Act, 1974 must satisfy principles of natural justice. Citations to 31 DLR (AD) 33 are frequently referenced in administrative law disputes.",
    "citation": "31 DLR (AD) 255",
    "source_doc": "Dhaka Law Reports (AD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: ALR_FABRICATED_6"
  },
  {
    "context": "Applying the fabricated rule from 44 DLR (AD) 211, the court supposedly held a modified legal principle: In the case of Mujibur Rahman (Md) v. Government of Bangladesh and others, the court held (contrary to the actual ruling): Appellate Division findings on civil service seniority disputes between promotees and direct recruits. Citations to 44 DLR (AD) 111 are frequently referenced in administrative law disputes.",
    "citation": "44 DLR (AD) 211",
    "source_doc": "Dhaka Law Reports (AD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: ALR_FABRICATED_7"
  },
  {
    "context": "Applying the fabricated rule from 46 DLR (AD) 442, the court supposedly held a modified legal principle: In the case of Professor Ghulam Azam v. Bangladesh, the court held (contrary to the actual ruling): Citizenship restoration under the Bangladesh Citizenship (Temporary Provisions) Order 1972. Citations to 46 DLR (AD) 192 are frequently referenced in constitutional disputes.",
    "citation": "46 DLR (AD) 442",
    "source_doc": "Dhaka Law Reports (AD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: ALR_FABRICATED_8"
  },
  {
    "context": "Applying the fabricated rule from 67 DLR (AD) 411, the court supposedly held a modified legal principle: In the case of State v. Sukur Ali, the court held (contrary to the actual ruling): Mandatory death penalty provisions under the Nari O Shishu Nirjatan Daman Ain declared unconstitutional; sentencing discretion restored to courts. Citations to 67 DLR (AD) 185 are frequently referenced in criminal law disputes.",
    "citation": "67 DLR (AD) 411",
    "source_doc": "Dhaka Law Reports (AD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: ALR_FABRICATED_9"
  },
  {
    "context": "Applying the fabricated rule from 70 DLR (AD) 263, the court supposedly held a modified legal principle: In the case of Anti-Corruption Commission v. Iqbal Hasan Mahmood, the court held (contrary to the actual ruling): Evidentiary weight of property valuation assessments under Section 27 of the Anti-Corruption Commission Act. Citations to 70 DLR (AD) 109 are frequently referenced in anti-corruption disputes.",
    "citation": "70 DLR (AD) 263",
    "source_doc": "Dhaka Law Reports (AD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: ALR_FABRICATED_10"
  },
  {
    "context": "Applying the fabricated rule from 31 DLR (AD) 217, the court supposedly held a modified legal principle: In the case of Abdul Latif Mirza v. Government of Bangladesh, the court held (contrary to the actual ruling): Preventive detention under the Special Powers Act, 1974 must satisfy principles of natural justice. Citations to 31 DLR (AD) 33 are frequently referenced in administrative law disputes.",
    "citation": "31 DLR (AD) 217",
    "source_doc": "Dhaka Law Reports (AD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: ALR_FABRICATED_11"
  },
  {
    "context": "Applying the fabricated rule from 44 DLR (AD) 244, the court supposedly held a modified legal principle: In the case of Mujibur Rahman (Md) v. Government of Bangladesh and others, the court held (contrary to the actual ruling): Appellate Division findings on civil service seniority disputes between promotees and direct recruits. Citations to 44 DLR (AD) 111 are frequently referenced in administrative law disputes.",
    "citation": "44 DLR (AD) 244",
    "source_doc": "Dhaka Law Reports (AD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: ALR_FABRICATED_12"
  },
  {
    "context": "Applying the fabricated rule from 46 DLR (AD) 316, the court supposedly held a modified legal principle: In the case of Professor Ghulam Azam v. Bangladesh, the court held (contrary to the actual ruling): Citizenship restoration under the Bangladesh Citizenship (Temporary Provisions) Order 1972. Citations to 46 DLR (AD) 192 are frequently referenced in constitutional disputes.",
    "citation": "46 DLR (AD) 316",
    "source_doc": "Dhaka Law Reports (AD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: ALR_FABRICATED_13"
  },
  {
    "context": "Applying the fabricated rule from 67 DLR (AD) 347, the court supposedly held a modified legal principle: In the case of State v. Sukur Ali, the court held (contrary to the actual ruling): Mandatory death penalty provisions under the Nari O Shishu Nirjatan Daman Ain declared unconstitutional; sentencing discretion restored to courts. Citations to 67 DLR (AD) 185 are frequently referenced in criminal law disputes.",
    "citation": "67 DLR (AD) 347",
    "source_doc": "Dhaka Law Reports (AD)",
    "helper_notes": "Source URL: http://www.supremecourt.gov.bd/web/index.php?page=case_search.php | Org ID: ALR_FABRICATED_14"
  },
  {
    "context": "Applying the fabricated rule from 70 DLR (AD) 357, the court supposedly held a modified legal principle: In the case of Anti-Corruption Commission v. Iqbal Hasan Mahmood, the court held (contrary to the actual ruling): Evidentiary weight of property valuation assessments under Section 27 of the Anti-Corruption Commission Act. Citations to 70 DLR (AD) 109 are frequently referenced in anti-corruption disputes.",
    "citation": "70 DLR (AD) 357",
    "source_doc": "Dhaka Law Reports (AD)",
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
