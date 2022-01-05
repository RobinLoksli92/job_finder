def predict_salary(salary_to, salary_from):
    if salary_from and salary_to:
        return (salary_to + salary_from)/2
    elif not salary_from:
        return salary_to * 0.8
    elif not salary_to:
        return salary_from * 1.2