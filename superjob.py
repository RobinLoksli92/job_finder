from itertools import count
import os

from dotenv import load_dotenv
import requests

from make_it_table import make_it_table
from predict_salary import predict_salary


def predict_rub_salary_for_superJob(vacancy):
    if vacancy['currency'] == 'rub':
        salary_to = vacancy['payment_to']
        salary_from = vacancy['payment_from']
        return predict_salary(salary_to, salary_from)
    return 0


def get_vacancy_details(developer_type, superjob_key):
    salaries_summ = 0
    vacancies_processed = 0

    url = 'https://api.superjob.ru/2.0/vacancies'
    headers = {
        'X-Api-App-Id': superjob_key
    }
    payload = {
            'keyword':f'Программист {developer_type}',
            'town':'Moscow'
        }

    for page in count(0):
        payload.update({'page': page})
        response = requests.get(url, headers=headers, params=payload)
        response.raise_for_status()
        vacancies = response.json()
        vacancies_found = vacancies['total']

        for vacancy in vacancies['objects']:
            salary = predict_rub_salary_for_superJob(vacancy)
            if salary:
                    vacancies_processed += 1
                    salaries_summ += salary

        if not vacancies['more']:
            break
    if not vacancies_processed:
        average_salary = 0
    else:
        average_salary= salaries_summ//vacancies_processed  
    vacancy_details = {
            'vacancies_found': vacancies_found,
            'vacancies_processed': vacancies_processed,
            'average_salary': average_salary
        }
    
    return vacancy_details


def main():
    load_dotenv()
    salaries = {}
    developer_types = ['Python', 'Java', 'C++']
    superjob_key = os.getenv('SUPERJOB_KEY')
    for developer_type in developer_types:
        salaries.update({developer_type:get_vacancy_details(developer_type, superjob_key)})
    title = 'SuperJob'
    table = make_it_table(salaries, title)
    print(table.table)


if __name__ == '__main__':
    main()


