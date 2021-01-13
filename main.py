import file_operations
from faker import Faker
import random

fake = Faker("ru_RU")

context = {
    'first_name': fake.first_name(),
    'last_name': fake.last_name(),
    'job': fake.job(),
    'town': fake.city(),
    'strength': random.randint(8, 14),
    'agility': random.randint(8, 14),
    'endurance': random.randint(8, 14),
    'intelligence': random.randint(8, 14),
    'luck': random.randint(8, 14),
    'skill_1': '',
    'skill_2': '',
    'skill_3': ''
}

file_operations.render_template('charsheet.svg', 'result.svg', context)
