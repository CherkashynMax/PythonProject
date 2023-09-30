from Ex1_custom_faker import CustomFaker
import csv
import random

def generate_employee_data(num_records=2000):
    fake = CustomFaker()

    employee_data = []
    for _ in range(num_records):
        is_male = random.random() < 0.6
        data = fake.custom_employee_info(is_male)
        employee_data.append(data)

    return employee_data

def write_to_csv(output_path, data):
    with open(output_path, 'w', newline='', encoding='utf-8-sig') as file:
        csv_writer = csv.writer(file, delimiter=';')
        csv_writer.writerow(["Прізвище Ім*я", "По батькові", "Стать", "Дата народження", "Посада", "Місто проживання", "Адреса проживання", "Телефон", "Email"])
        csv_writer.writerows(data)

def main():
    num_records = 2000
    output_path = "employees.csv"

    employee_data = generate_employee_data(num_records)
    write_to_csv(output_path, employee_data)

    print(f"Generated {num_records} records in {output_path}")


if __name__ == "__main__":
    main()