import pandas as pd

final_data = pd.read_csv('MergedData.csv')
final_data['Mass'].astype(float)
final_data['Radius'].astype(float)

final_data['Mass'] * 0.000954588
final_data['Radius'] * 0.102763