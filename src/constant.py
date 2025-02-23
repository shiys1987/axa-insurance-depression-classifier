# store all constants

data_dtypes = {
    "Name": str, 
    "Age": "Int16", 
    "Marital Status": str, 
    "Education Level": str, 
    "Number of Children": "Int16",
    "Smoking Status": str, 
    "Physical Activity Level": str, 
    "Employment Status": str, 
    "Alcohol Consumption": str, 
    "Dietary Habits": str, 
    "Sleep Patterns": str, 
    "History of Mental Illness": str, 
    "History of Substance Abuse": str, 
    "Family History of Depression": str, 
    "Chronic Medical Conditions": str
    }

data_path = "../data/depression_data.csv"

target_var = "History of Mental Illness"

all_categorical_cols = [
    "Marital Status", 
    "Education Level", 
    "Smoking Status", 
    "Physical Activity Level", 
    "Employment Status", 
    "Alcohol Consumption", 
    "Dietary Habits", 
    "Sleep Patterns", 
    "History of Substance Abuse", 
    "Family History of Depression", 
    "Chronic Medical Conditions"
    ]

all_numerical_cols = [
    "Age",
    "Number of Children",
    "Income",
]

categorical_col_feature_values = [
    ["Married", "Widowed", "Divorced", "Single"],
    ["High School", "Associate Degree", "Bachelor's Degree", "Master's Degree", "PhD"],
    ["Non-smoker", "Former", "Current"],
    ["Sedentary", "Moderate", "Active"],
    ["Unemployed", "Employed"],
    ["Low", "Moderate", "High"],
    [ "Unhealthy", "Moderate", "Healthy"],
    ["Poor", "Fair", "Good"],
    ["No", "Yes"],
    ["No", "Yes"],
    ["No", "Yes"],
]