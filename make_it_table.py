def make_it_table(salaries_dict):
    table_data = [['Язык программирования', 'Вакансий найдено', 'Вакансий обработано', 'Средняя зарплата']]
    for developer_type, salary_info in salaries_dict.items():
        table_data.append([developer_type, salary_info['vacancies_found'], salary_info['vacancies_processed'], salary_info['average_salary']])   
    return table_data


def main():
    pass


if __name__ == '__main__':
    main()