import pandas as pd

# Sample clinical trial data
data = [
    {
        "NCT Number": "NCT000001",
        "Study Title": "A Study of Chemotherapy in Stage II Breast Cancer",
        "Conditions": "Breast Cancer",
        "Brief Summary": "Evaluates the efficacy of standard chemotherapy in patients with stage II breast cancer.",
        "Eligibility Criteria": "Female, age 18-70, no prior chemotherapy.",
        "Interventions": "Drug: Doxorubicin and Cyclophosphamide",
        "Sex": "Female",
        "Age": "18-70",
        "Study Status": "Recruiting",
        "Study Type": "Interventional",
        "Phases": "Phase 2"
    },
    {
        "NCT Number": "NCT000002",
        "Study Title": "Immunotherapy for Advanced Melanoma",
        "Conditions": "Melanoma",
        "Brief Summary": "Testing checkpoint inhibitors in late-stage melanoma patients.",
        "Eligibility Criteria": "Age 18+, metastatic melanoma, ECOG ≤ 2.",
        "Interventions": "Drug: Nivolumab",
        "Sex": "All",
        "Age": "18+",
        "Study Status": "Active, not recruiting",
        "Study Type": "Interventional",
        "Phases": "Phase 3"
    },
    {
        "NCT Number": "NCT000003",
        "Study Title": "Lifestyle Changes in Type 2 Diabetes Prevention",
        "Conditions": "Type 2 Diabetes",
        "Brief Summary": "Assessing effects of diet and exercise in preventing Type 2 diabetes.",
        "Eligibility Criteria": "Age 30-65, BMI > 25, no current diabetes diagnosis.",
        "Interventions": "Behavioral: Lifestyle Program",
        "Sex": "All",
        "Age": "30-65",
        "Study Status": "Recruiting",
        "Study Type": "Interventional",
        "Phases": "N/A"
    },
    {
        "NCT Number": "NCT000004",
        "Study Title": "Aspirin Use in Colorectal Cancer Prevention",
        "Conditions": "Colorectal Cancer",
        "Brief Summary": "Testing low-dose aspirin's role in preventing colorectal adenomas.",
        "Eligibility Criteria": "Age 40+, personal history of adenomas.",
        "Interventions": "Drug: Aspirin",
        "Sex": "All",
        "Age": "40+",
        "Study Status": "Completed",
        "Study Type": "Interventional",
        "Phases": "Phase 3"
    },
    {
        "NCT Number": "NCT000005",
        "Study Title": "Cognitive Training in Alzheimer’s Disease",
        "Conditions": "Alzheimer's Disease",
        "Brief Summary": "Evaluates memory training in early Alzheimer's patients.",
        "Eligibility Criteria": "Age 60-80, MMSE > 20, mild cognitive impairment.",
        "Interventions": "Behavioral: Cognitive Training",
        "Sex": "All",
        "Age": "60-80",
        "Study Status": "Recruiting",
        "Study Type": "Interventional",
        "Phases": "Phase 1"
    },
    {
        "NCT Number": "NCT000006",
        "Study Title": "Smoking Cessation for COPD Patients",
        "Conditions": "COPD",
        "Brief Summary": "Tests nicotine patches and counseling in smokers with COPD.",
        "Eligibility Criteria": "Smokers age 40+, COPD diagnosis.",
        "Interventions": "Drug: Nicotine patch + Counseling",
        "Sex": "All",
        "Age": "40+",
        "Study Status": "Recruiting",
        "Study Type": "Interventional",
        "Phases": "Phase 2"
    },
    {
        "NCT Number": "NCT000007",
        "Study Title": "COVID-19 Vaccine Effectiveness in Immunocompromised Adults",
        "Conditions": "COVID-19",
        "Brief Summary": "Monitoring breakthrough infection rates in vaccinated immunocompromised individuals.",
        "Eligibility Criteria": "Age 18+, post-organ transplant or chemotherapy within 6 months.",
        "Interventions": "Biological: mRNA COVID Vaccine",
        "Sex": "All",
        "Age": "18+",
        "Study Status": "Recruiting",
        "Study Type": "Observational",
        "Phases": "N/A"
    },
    {
        "NCT Number": "NCT000008",
        "Study Title": "Pain Management After Knee Replacement Surgery",
        "Conditions": "Postoperative Pain",
        "Brief Summary": "Tests use of nerve blocks for pain after knee surgery.",
        "Eligibility Criteria": "Age 50-80, scheduled knee replacement.",
        "Interventions": "Drug: Local anesthetic nerve block",
        "Sex": "All",
        "Age": "50-80",
        "Study Status": "Recruiting",
        "Study Type": "Interventional",
        "Phases": "Phase 2"
    }
]

# Convert to DataFrame and save
df = pd.DataFrame(data)
df.to_csv("clinical_trials.csv", index=False)

print("✅ Generated sample clinical_trials.csv")
