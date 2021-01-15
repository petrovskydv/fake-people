import random
import os

from faker import Faker

import file_operations


def generate_questionnaire(skills_list, alphabet, example_file, result_file):
    fake = Faker("ru_RU")

    three_random_skills = random.sample(skills_list, 3)
    runic_skills = []
    for skill in three_random_skills:
        for symbol in skill:
            skill = skill.replace(symbol, alphabet[symbol])
        runic_skills.append(skill)

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
        'skill_1': runic_skills[0],
        'skill_2': runic_skills[1],
        'skill_3': runic_skills[2]
    }

    file_operations.render_template(example_file, result_file, context)


def main():
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

    alphabet = {
        'а': 'а͠', 'б': 'б̋', 'в': 'в͒͠',
        'г': 'г͒͠', 'д': 'д̋', 'е': 'е͠',
        'ё': 'ё͒͠', 'ж': 'ж͒', 'з': 'з̋̋͠',
        'и': 'и', 'й': 'й͒͠', 'к': 'к̋̋',
        'л': 'л̋͠', 'м': 'м͒͠', 'н': 'н͒',
        'о': 'о̋', 'п': 'п̋͠', 'р': 'р̋͠',
        'с': 'с͒', 'т': 'т͒', 'у': 'у͒͠',
        'ф': 'ф̋̋͠', 'х': 'х͒͠', 'ц': 'ц̋',
        'ч': 'ч̋͠', 'ш': 'ш͒͠', 'щ': 'щ̋',
        'ъ': 'ъ̋͠', 'ы': 'ы̋͠', 'ь': 'ь̋',
        'э': 'э͒͠͠', 'ю': 'ю̋͠', 'я': 'я̋',
        'А': 'А͠', 'Б': 'Б̋', 'В': 'В͒͠',
        'Г': 'Г͒͠', 'Д': 'Д̋', 'Е': 'Е',
        'Ё': 'Ё͒͠', 'Ж': 'Ж͒', 'З': 'З̋̋͠',
        'И': 'И', 'Й': 'Й͒͠', 'К': 'К̋̋',
        'Л': 'Л̋͠', 'М': 'М͒͠', 'Н': 'Н͒',
        'О': 'О̋', 'П': 'П̋͠', 'Р': 'Р̋͠',
        'С': 'С͒', 'Т': 'Т͒', 'У': 'У͒͠',
        'Ф': 'Ф̋̋͠', 'Х': 'Х͒͠', 'Ц': 'Ц̋',
        'Ч': 'Ч̋͠', 'Ш': 'Ш͒͠', 'Щ': 'Щ̋',
        'Ъ': 'Ъ̋͠', 'Ы': 'Ы̋͠', 'Ь': 'Ь̋',
        'Э': 'Э͒͠͠', 'Ю': 'Ю̋͠', 'Я': 'Я̋',
        ' ': ' '
    }

    example_file = 'src/charsheet.svg'
    destination_path = 'output'
    if not os.path.exists(destination_path):
        os.mkdir(destination_path)

    for number_questionnaire in range(10):
        name_result_file = 'result{}.svg'.format(number_questionnaire)
        result_file = os.path.join(destination_path, name_result_file)
        generate_questionnaire(skills_list, alphabet, example_file, result_file)


if __name__ == '__main__':
    main()
