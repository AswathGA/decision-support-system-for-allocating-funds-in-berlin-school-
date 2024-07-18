import pandas as pd
# Provided data
data = {
 'School ID': ['Mitte', 'Pankow', 'Reinickendorf', 'Spandau', 
'Charlottenburg-Wilmersdorf', 'Steglitz-Zehlendorf', 'Tempelhof￾Schöneberg', 'Neukölln', 'Treptow-Köpenick', 'Marzahn-Hellersdorf', 
'Lichtenberg', 'Friedrichshain-Kreuzberg', 'Tempelhof-Schöneberg'],
 'Student-Teacher Ratio': [10, 15, 11, 14, 11, 12, 11, 14, 13, 10, 10, 
11, 12],
 'Academic Performance': [95, 65, 90, 70, 85, 80, 95, 90, 60, 90, 95, 
85, 90],
 'Attendance Rate': [92, 60, 95, 80, 85, 85, 90, 70, 75, 90, 90, 75, 
85],
 'Facilities': [25, 5, 20, 10, 25, 25, 25, 10, 10, 20, 25, 15, 10]
}
df = pd.DataFrame(data)
# Weights of the criteria
weights = {
 'Student-Teacher Ratio': 0.4,
 'Academic Performance': 0.2,
 'Attendance Rate': 0.2,
 'Facilities': 0.2
}
# Calculate scores for each criterion using if and else
C1 = []
for ratio in df['Student-Teacher Ratio']:
 if ratio == 10:
  C1.append(0)
 elif ratio == 11:
  C1.append(1)
 elif ratio == 12:
  C1.append(2)
 elif ratio == 13:
  C1.append(3)
 elif ratio == 14:
  C1.append(4)
 elif ratio == 15:
  C1.append(5)
C2 = []
for performance in df['Academic Performance']:
 if performance == 100:
  C2.append(0)
 elif 91 <= performance <= 99:
  C2.append(1)
 elif 81 <= performance <= 90:
  C2.append(2)
 elif 71 <= performance <= 80:
  C2.append(3)
 elif 61 <= performance <= 70:
  C2.append(4)
 elif 51 <= performance <= 60:
  C2.append(5)
C3 = []
for attendance in df['Attendance Rate']:
 if attendance == 100:
  C3.append(0)
 elif 91 <= attendance <= 99:
  C3.append(1)
 elif 81 <= attendance <= 90:
  C3.append(2)
 elif 71 <= attendance <= 80:
  C3.append(3)
 elif 61 <= attendance <= 70:
  C3.append(4)
 elif 51 <= attendance <= 60:
  C3.append(5)
C4 = []
for facilities in df['Facilities']:
 if facilities == 25:
  C4.append(0)
 elif 21 <= facilities <= 24:
  C4.append(1)
 elif 16 <= facilities <= 20:
  C4.append(2)
 elif 11 <= facilities <= 15:
  C4.append(3)
 elif 6 <= facilities <= 10:
  C4.append(4)
 elif 0 <= facilities <= 5:
  C4.append(5)
df['C1'] = C1
df['C2'] = C2
df['C3'] = C3
df['C4'] = C4
# Calculate the final score for each school
df['Final Score (Si)'] = (df['C1'] * weights['Student-Teacher Ratio'] +
 df['C2'] * weights['Academic Performance'] +
 df['C3'] * weights['Attendance Rate'] +
 df['C4'] * weights['Facilities'])
# Total of scores
total_score = df['Final Score (Si)'].sum()
# Total amount of resources
total_funds = 10_000_000
# Calculate the amount to be distributed to each school
df['Funds'] = (df['Final Score (Si)'] / total_score) * total_funds
# Format the funds in euros without scientific notation
df['Funds'] = df['Funds'].apply(lambda x: f"€{x:,.2f}")
# Display the resulting DataFrame
print(df[['School ID', 'C1', 'C2', 'C3', 'C4', 'Final Score (Si)', 
'Funds']])
# Calculate and print the sum of all allocated funds
total_allocated_funds = df['Funds'].apply(lambda x: float(x.replace('€', 
'').replace(',', ''))).sum()
print(f"Total Allocated Funds: €{total_allocated_funds:,.2f}")