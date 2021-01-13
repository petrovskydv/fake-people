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

    three_random_skills = random.sample(skills_list, 3)

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
        'skill_1': three_random_skills[0],
        'skill_2': three_random_skills[1],
        'skill_3': three_random_skills[2]
    }

    file_operations.render_template('charsheet.svg', 'result.svg', context)


if __name__ == '__main__':
    main()
