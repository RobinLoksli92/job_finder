from os import name
import requests
import math
from pprint import pprint
from itertools import count
from pprint import pprint
from terminaltables import AsciiTable
from make_it_table import make_it_table

salaries_dict ={}


def predict_rub_salary(vacancy_item):
    salary_info = vacancy_item['salary']
    if salary_info is not None:
        if salary_info['currency'] == 'RUR':
            if salary_info['from'] != None and salary_info['to'] != None:
                salary = (vacancy_item['salary']['to'] + vacancy_item['salary']['from'])/2
            elif salary_info['from'] == None:
                salary = salary_info['to'] * 0.8
            elif salary_info['to'] == None:
                salary = salary_info['from'] * 1.2
            return salary
        else:
            salary = 0
    else:
        salary = 0
    return salary
        

def get_vacancy(developer_type):
    salaries_summ = 0
    vacancies_processed = 0
    hh_url = 'https://api.hh.ru/vacancies'
    for page in count(0):
        try:
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
            vacancies_items = vacancies['items']
           
            vacancies_found = vacancies['found']
            for vacancy_item in vacancies_items:
                salary = predict_rub_salary(vacancy_item)
                if salary != 0:
                    vacancies_processed += 1
                    salaries_summ += salary

            if page >= vacancies['pages']:
                break
        except requests.exceptions.HTTPError:
                break
    average_salary= int(salaries_summ/vacancies_processed)    
    
    salaries_dict.update({
        developer_type: {
            'vacancies_found': vacancies_found,
            'vacancies_processed': vacancies_processed,
            'average_salary': average_salary
        }
    })    
    return salaries_dict


def main():
    get_vacancy('Python')
    get_vacancy('Java')
    get_vacancy('С++')
    table_data = make_it_table(salaries_dict)
    title = 'HeadHunter Moscow'
    table = AsciiTable(table_data, title)
    print(table.table)

if __name__ == '__main__':
    main()
    