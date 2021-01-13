import file_operations
from faker import Faker
import random


def main():
    fake = Faker("ru_RU")

    skills_list = [
        'Стремительный прыжок',
        'Электрический выстрел',
        'Ледяной удар',
        'Стремительный удар',
        'Кислотный взгляд',
        'Тайный побег',
        'Ледяной выстрел',
        'Огненный заряд'
    ]

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
        'skill_1': random.choice(skills_list),
        'skill_2': random.choice(skills_list),
        'skill_3': random.choice(skills_list)
    }

    file_operations.render_template('charsheet.svg', 'result.svg', context)


if __name__ == '__main__':
    main()
