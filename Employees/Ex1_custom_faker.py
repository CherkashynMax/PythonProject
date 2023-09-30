from faker import Faker
from EX1_list_fname import fname_male, fname_female
import random

class CustomFaker(Faker):
    def __init__(self, locale='uk_UA'):
        super().__init__(locale)

    def custom_name(self, is_male=True):
        first_name = self.first_name_male() if is_male else self.first_name_female()
        last_name = self.last_name_male() if is_male else self.last_name_female()
        return f"{last_name} {first_name}"

    def custom_employee_info(self, is_male=True):

        name = self.custom_name(is_male)
        gender = 'чоловік' if is_male else 'жінка'
        fname = random.choice(fname_male)  if is_male else random.choice(fname_female)
        birth = self.date_of_birth(tzinfo=None, minimum_age=15, maximum_age=85).strftime('%d-%m-%Y')
        work = self.job()
        city = self.city()
        address = self.address().replace('\n', ', ')
        phone = self.phone_number()
        email = self.email()
        return [name, fname, gender, birth, work, city, address, phone, email]