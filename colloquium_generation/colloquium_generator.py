import pandas as pd
import json

# Load JSON files
with open("colloquium_problems.json", "r", encoding="utf-8") as f:
    problems = json.load(f)

with open("colloquium_students.json", "r", encoding="utf-8") as f:
    students = json.load(f)

# Convert to DataFrames
df_problems = pd.DataFrame(problems)
df_students = pd.DataFrame(students)

# Define Excel file path
file_path = "/home/khagani/2454i_colloquium1.xlsx"

# Save both DataFrames into separate sheets of the same Excel file
with pd.ExcelWriter(file_path, engine="openpyxl") as writer:
    df_problems.to_excel(writer, sheet_name="Problems", index=False)
    df_students.to_excel(writer, sheet_name="Students", index=False)

print(f"✅ Excel file saved as {file_path}")