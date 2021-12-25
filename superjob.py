import requests
import os
from dotenv import load_dotenv
from itertools import count
from terminaltables import AsciiTable
from make_it_table import make_it_table


salaries_dict = {}


def predict_rub_salary_for_superJob(vacancy):
    if vacancy['payment_from'] != 0 and vacancy['payment_to'] != 0:
        salary = (vacancy['payment_from'] + vacancy['payment_to'])/2
    elif vacancy['payment_from'] == 0:
        salary = vacancy['payment_to'] * 0.8
    elif vacancy['payment_to'] == 0:
        salary = vacancy['payment_from'] * 1.2
    elif vacancy['payment_from'] == 0 and vacancy['payment_to'] == 0:
        salary = None
    return salary


def get_vacancies(developer_type):
    salaries_summ = 0
    vacancies_processed = 0

    url = 'https://api.superjob.ru/2.0/vacancies'
    headers = {
        'X-Api-App-Id':os.getenv('SECRET_KEY')
    }

    for page in count(0):
        payload = {
            'keyword':f'Программист {developer_type}',
            'town':'Moscow',
            'page': page,
            # 'no_agreement': 1
        }

        response = requests.get(url, headers=headers, params=payload)
        response.raise_for_status()
        vacancies = response.json()
        vacancies_found = vacancies['total']

        for vacancy in vacancies['objects']:
            salary = predict_rub_salary_for_superJob(vacancy)
            if salary != 0 and salary is not None:
                    vacancies_processed += 1
                    salaries_summ += salary

        if vacancies['more']:
            continue
        elif not vacancies['more']:
            break
    average_salary= int(salaries_summ/vacancies_processed) 
    vacancy_info = {developer_type: {
            'vacancies_found': vacancies_found,
            'vacancies_processed': vacancies_processed,
            'average_salary': average_salary
        }
    }
    return vacancy_info


def main():
    load_dotenv()

    salaries_dict.update(get_vacancies('python'))
    salaries_dict.update(get_vacancies('Java'))
    table_data = make_it_table(salaries_dict)
    title = 'SuperJob Moscow '
    table = AsciiTable(table_data,title)
    print(table.table)


if __name__ == '__main__':
    main()


