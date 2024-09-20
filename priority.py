import pandas as pd
import sys

print("""Currently We only Support two College 
    1. Pulchowk Engineering Campus
    2. Purwanchal Campus
    Note: This Program only support Numbers
""")
college_name = int(input("Enter your College Number from above:"))

if college_name==1:
    print("\nSo your College is Pulchowk")
    print("""
Civil Engineering Regular (1)
Civil Engineering Full Fee (2)
Architecture Regular (3)
Architecture Full Fee (4)
Electrical Engineering Regular (5)
Electrical Engineering Full Fee (6)
Electronics... Engineering Regular (7)
Electronics... Engineering Full Fee (8)
Mechanical Engineering Regular (9)
Mechanical Engineering Full Fee (10)
Computer Engineering Regular (11)
Computer Engineering Full Fee (12)
Aerospace Engineering Regular (27)
Aerospace Engineering Full Fee (28)
Chemical Engineering Regular (29)
Chemical Engineering Full Fee (30) 
    """)
    file_path = "./Colleges/Pulchowk.xlsx"
elif college_name==2:
    print("\nSo your College is Purwanchal Campus / ERC")
    file_path = "./Colleges/Erc.xlsx"
else:
    print("This Program only Supports two colleges")
    sys.exit()



user_input = int(input("Enter your Priority number: "))


df = pd.read_excel(file_path)

columns_to_check = df.columns[df.columns.str.startswith('p')]

rows_with_input = df[df[columns_to_check].isin([user_input]).any(axis=1)]

# Replace NaN with an empty string
rows_with_input = rows_with_input.fillna('')

# Add a serial number column starting from 1
rows_with_input.insert(0, 'No.', range(1, len(rows_with_input) + 1))

# Display the result in the terminal
print(rows_with_input.to_string(index=False))  # Disable index display

