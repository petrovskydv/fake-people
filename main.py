import file_operations
from faker import Faker

fake = Faker("ru_RU")

context = {
    'first_name': fake.first_name(),
    'last_name': fake.last_name(),
    'job': fake.job(),
    'town': fake.city(),
    'strength': '',
    'agility': '',
    'endurance': '',
    'intelligence': '',
    'luck': '',
    'skill_1': '',
    'skill_2': '',
    'skill_3': ''
}

file_operations.render_template('charsheet.svg', 'result.svg', context)
