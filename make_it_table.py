from terminaltables import AsciiTable


def make_it_table(salaries, title):
    table_rows = [
        ['Язык программирования',
         'Вакансий найдено',
         'Вакансий обработано',
         'Средняя зарплата']
    ]
    for developer_type, salary_details in salaries.items():
        table_rows.append(
            [developer_type,
             salary_details['vacancies_found'],
             salary_details['vacancies_processed'],
             salary_details['average_salary']]
        )
    table = AsciiTable(table_rows, title)
    return table


