from terminaltables import AsciiTable


def make_it_table(salaries_dict, title):
    table_data = [
        ['Язык программирования',
         'Вакансий найдено',
         'Вакансий обработано',
         'Средняя зарплата']
    ]
    for developer_type, salary_info in salaries_dict.items():
        table_data.append(
            [developer_type,
             salary_info['vacancies_found'],
             salary_info['vacancies_processed'],
             salary_info['average_salary']]
        )
    table = AsciiTable(table_data, title)
    return table


