import pandas as pd

dict1 = {"shivam": 45, "amit":2390}

KeysList = list(dict1.keys())
ValuesList = list(dict1.values())
df = pd.DataFrame({'List of Words': KeysList, 'words Count': ValuesList,})
df.to_csv('file.csv', index=False)

df.to_excel('../output_files/dict1.xlsx', index=False)
