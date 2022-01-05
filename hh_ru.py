import requests
from itertools import count
from make_it_table import make_it_table
from predict_salary import predict_salary


salaries_dict ={}


def predict_rub_salary_hh(vacancy):
    salary_details = vacancy['salary']
    if salary_details:
        salary_to = salary_details['to']
        salary_from = salary_details['from']
        if salary_details['currency'] == 'RUR':
            return predict_salary(salary_to, salary_from)
    return 0
        

def get_vacancy(developer_type):
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
        vacancies_items = vacancies['items']
        
        vacancies_found = vacancies['found']
        for vacancy_item in vacancies_items:
            salary = predict_rub_salary_hh(vacancy_item)
            if salary:
                vacancies_processed += 1
                salaries_summ += salary

        if page+1 >= vacancies['pages']:
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
    developer_types = ['Python', 'Java', 'С++' ]
    for developer_type in developer_types:
      get_vacancy(developer_type)
    title = 'HeadHunters'
    table = make_it_table(salaries_dict, title)
    print(table.table)

if __name__ == '__main__':
    main()
    