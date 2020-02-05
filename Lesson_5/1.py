'''
 Урок 5
 Задание 1
Пользователь вводит данные о количестве предприятий,
их наименования и прибыль за 4 квартала (т.е. 4
отдельных числа) для каждого предприятия.. Программа
должна определить среднюю прибыль (за год для всех
предприятий) и вывести наименования предприятий, чья
прибыль выше среднего и отдельно вывести наименования
предприятий, чья прибыль ниже среднего.
'''

from collections import namedtuple


def task1():
    COMPANY = namedtuple('Company', 'name income')
    companies = []
    n_companies = int(input("Введите кол-во предприятий: "))
    for i in range(n_companies):
        company_name = input(f"Введите имя предприятия №{i+1}: ")
        income = input(f"Введите прибыль этого предприятия за 4 квартала через пробел: ")
        companies.append(COMPANY(name=company_name, income=[int(n) for n in income.split()]))

    average_yearly_income = 0
    for company in companies:
        average_yearly_income += sum(company.income)

    average_yearly_income = average_yearly_income / n_companies

    print(f"\nСредняя годовая прибыль по всем: {average_yearly_income}")

    print("Предприятия, заработавшие больше средней прибыли:")
    for company in companies:
        if sum(company.income) >= average_yearly_income:
            print(company.name)

    print("Предприятия, заработавшие меньше средней прибыли:")
    for company in companies:
        if sum(company.income) < average_yearly_income:
            print(company.name)


if __name__ == "__main__":
    task1()
