import pandas as pd

# 1. Load the Excel file and select the sales dataset sheet
file_name = "ApexPlanet_DataAnalytics_Dataset.xlsx"
sheet_name = "Sales_Dataset.csv" # Or adjust if the sheet has a different tab name

try:
    # Read the Excel file
    df = pd.read_excel(file_name, sheet_name=0) # sheet_name=0 reads the first sheet
    print("Dataset loaded successfully from Excel!")
    
    print(f"Total rows before cleaning: {len(df)}")
    
    # 2. Handle missing categorical values (City and Gender)
    if 'City' in df.columns:
        df['City'] = df['City'].fillna('Unknown')
    if 'Gender' in df.columns:
        df['Gender'] = df['Gender'].fillna('Unknown')

    # 3. Handle missing numerical values (Age)
    if 'Age' in df.columns:
        df['Age'] = pd.to_numeric(df['Age'], errors='coerce')
        median_age = df['Age'].median()
        df['Age'] = df['Age'].fillna(median_age)

    # 4. Save the cleaned dataset as a CSV for easy use in dashboards/GitHub
    output_file = "Cleaned_Sales_Dataset.csv"
    df.to_csv(output_file, index=False)
    print(f"Cleaned dataset successfully saved as '{output_file}'!")

except Exception as e:
    print(f"An error occurred: {e}")