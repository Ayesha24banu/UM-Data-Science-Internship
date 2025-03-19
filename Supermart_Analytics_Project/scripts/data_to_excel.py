import pandas as pd

# Load cleaned data
data = pd.read_csv('data/cleaned_supermart_data.csv')

# Export to Excel
data.to_excel('reports/data_analysis.xlsx', index=False)
print("✅ Excel report generated and saved in 'reports/data_analysis.xlsx'!")
