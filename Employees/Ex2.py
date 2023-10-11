import pandas as pd
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows
from datetime import datetime


def calculate_age(birth):
    today = datetime.today()
    age = today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))
    return age

try:
    data = pd.read_csv('employees.csv', sep=';', encoding='utf-8-sig')

    workbook = Workbook()
    all_sheet = workbook.active
    all_sheet.title = "all"
    all_sheet.append(data.columns.tolist())
    for row in dataframe_to_rows(data, index=False, header=False):
        all_sheet.append(row)

    categorize_age = {
        "younger_18": (0, 18),
        "18-45": (18, 45),
        "45-70": (45, 70),
        "older_70": (70, 120)
    }

    for sheet_name, (min_age, max_age) in categorize_age.items():
        table = workbook.create_sheet(title=sheet_name)
        table.append(["№", "Прізвище Ім*я", "По батькові", "Дата народження", "Вік"])
        for index, row in data.iterrows():
            birth = datetime.strptime(row['Дата народження'], '%d-%m-%Y')
            age = calculate_age(birth)
            if min_age <= age < max_age:
                table.append([index+2, row['Прізвище Ім*я'], row['По батькові'], row['Дата народження'], age])

    workbook.save('employees.xlsx')
    print("Ok, програма завершила свою роботу успішно.")
except FileNotFoundError:
    print("Помилка: файл CSV не знайдено або відсутній.")
except Exception as e:
    print(f"Помилка: {str(e)}")
