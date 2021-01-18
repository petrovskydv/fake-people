import random
import os

from faker import Faker

import file_operations


def generate_questionnaire(skills_list, lower_limit_level, upper_limit_level, skills_names, example_filepath,
                           result_filepath):
    fake = Faker("ru_RU")

    first_name, last_name = random.choice([
        [fake.first_name_male(), fake.last_name_male()],
        [fake.first_name_female(), fake.last_name_female()],
    ])

    context = {
        'first_name': first_name,
        'last_name': last_name,
        'job': fake.job(),
        'town': fake.city()
    }

    for skill in skills_names:
        context[skill] = random.randint(lower_limit_level, upper_limit_level)

    for skill_number, skill in enumerate(skills_list):
        context['skill_{}'.format(skill_number + 1)] = skill

    file_operations.render_template(example_filepath, result_filepath, context)


def main():
    skills_names = ['strength', 'agility', 'endurance', 'intelligence', 'luck']
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

    runic_skills = []
    for skill in skills_list:
        for symbol in skill:
            skill = skill.replace(symbol, alphabet[symbol])
        runic_skills.append(skill)

    three_random_skills = random.sample(runic_skills, 3)

    questionnaires_count = 10
    lower_limit_level = 8
    upper_limit_level = 14

    example_filepath = 'src/charsheet.svg'
    destination_path = 'output'
    os.makedirs(destination_path, exist_ok=True)

    for number_questionnaire in range(questionnaires_count):
        result_filename = 'result{}.svg'.format(number_questionnaire)
        result_filepath = os.path.join(destination_path, result_filename)
        generate_questionnaire(three_random_skills, lower_limit_level, upper_limit_level, skills_names,
                               example_filepath, result_filepath)


if __name__ == '__main__':
    main()
