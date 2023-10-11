import pandas as pd
import matplotlib.pyplot as plt

try:
    data = pd.read_csv('employees.csv', sep=';', encoding='utf-8-sig')
except FileNotFoundError:
    print("Повідомлення про відсутність або проблеми при відкритті файлу CSV")
    exit()
print("Ok")

# кількість співробітників чоловічої і жіночої статі
gender = data['Стать'].value_counts()
print("Кількість співробітників за статтю:")
print(gender)

# побудова діаграми по статі
plt.figure(figsize=(6, 6))
gender.plot(kind='pie', autopct='%1.1f%%', startangle=140, colors=['#20B2AA','#FF1493'])
plt.title("Розподіл співробітників за статтю")
plt.show()

def calculate_age(birthdate):
    today = pd.Timestamp.now()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

def categorize_age(age):
    if age < 18:
        return "younger_18"
    elif 18 <= age < 45:
        return "18-45"
    elif 45 <= age < 70:
        return "45-70"
    else:
        return "older_70"

data['Вік'] = data['Дата народження'].apply(lambda x: calculate_age(pd.to_datetime(x)))
age_category_counts = data['Вік'].apply(lambda x: categorize_age(x)).value_counts()
print("\nКількість співробітників за віковою категорією:")
print(age_category_counts)

#кількість працівників за статтю
gender_age_counts = data.groupby(['Стать', data['Вік'].apply(categorize_age)]).size().unstack(fill_value=0)
print("\nКількість співробітників за статтю та віковою категорією:")
print(gender_age_counts)

#діаграма за віком
plt.figure(figsize=(10, 6))
age_category_counts.plot(kind='bar')
plt.xlabel("Вікова категорія")
plt.ylabel("Кількість співробітників")
plt.title("Розподіл співробітників за віковою категорією")
plt.show()

# Діаграм для статі та вікових категорій
gender_age_counts.plot(kind='bar', stacked=True)
plt.xlabel("Вікова категорія")
plt.ylabel("Кількість співробітників")
plt.title("Розподіл співробітників за статтю та віковою категорією")
plt.show()