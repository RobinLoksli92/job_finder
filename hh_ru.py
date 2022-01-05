from itertools import count

import requests

from make_it_table import make_it_table
from predict_salary import predict_salary


def predict_rub_salary_hh(vacancy):
    salary_details = vacancy['salary']
    if salary_details:
        salary_to = salary_details['to']
        salary_from = salary_details['from']
        if salary_details['currency'] == 'RUR':
            return predict_salary(salary_to, salary_from)
    return 0
        

def get_vacancy_details(developer_type):
    salaries_summ = 0
    vacancies_processed = 0
    hh_url = 'https://api.hh.ru/vacancies'
    for page in count(0):
        payload = {
            'text': f'Программист {developer_type}',
            'area': '1',
            'period': '30',
            'page': page,
            'per_page': '100'
        }
        response = requests.get(hh_url, params=payload)
        response.raise_for_status()
        vacancies = response.json()
        vacancies_details = vacancies['items']
        
        vacancies_found = vacancies['found']
        for vacancy_details in vacancies_details:
            salary = predict_rub_salary_hh(vacancy_details)
            if salary:
                vacancies_processed += 1
                salaries_summ += salary

        if page+1 >= vacancies['pages']:
            break
    if not vacancies_processed:
        average_salary = 0
    else:
        average_salary= salaries_summ//vacancies_processed 
    
    vacancy_details = {developer_type:{
        'vacancies_found': vacancies_found,
        'vacancies_processed': vacancies_processed,
        'average_salary': average_salary
        }
    }
    return vacancy_details


def main():
    salaries = {}
    developer_types = ['Python', 'Java', 'С++' ]
    for developer_type in developer_types:
        salaries.update(get_vacancy_details(developer_type))
    title = 'HeadHunters'
    table = make_it_table(salaries, title)
    print(table.table)

if __name__ == '__main__':
    main()
    