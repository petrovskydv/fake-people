import file_operations

context = {
    'first_name': 'Презентация',
    'last_name': 'на тему',
    'job': 'Картинки',
    'town': '',
    'strength': '',
    'agility': 'Презентация',
    'endurance': 'на тему',
    'intelligence': 'Картинки',
    'luck': '',
    'skill_1': '',
    'skill_2': '',
    'skill_3': ''
}

file_operations.render_template('charsheet.svg', 'result.svg', context)
