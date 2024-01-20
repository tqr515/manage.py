from datetime import datetime
from django.shortcuts import render
from files.db.db_executor import (
    get_navigation_data, get_main_page_data, get_demand_page_data,
    get_geography_page_data, get_skills_page_data, get_last_vacancy_page_data
)
from files.api.hh.v1 import HeadHunterVacancies


def get_context_data(page_function):
    def wrapper(request):
        context = {'context': page_function()}
        context['navigation'] = get_navigation_data()
        return render(request, f'{page_function.__name__.replace("_page", "")}_page.html', context)

    return wrapper


@get_context_data
def home_page_data():
    return get_main_page_data()


@get_context_data
def demand_page_data():
    return get_demand_page_data()


@get_context_data
def geography_page_data():
    return get_geography_page_data()


@get_context_data
def skills_page_data():
    return get_skills_page_data()


def last_vacancy_page(request):
    last_vacancies_data = get_last_vacancy_page_data()

    if last_vacancies_data:
        name_vacancy_to_parse = last_vacancies_data[0].vacancy_to_parse
        hh_api = HeadHunterVacancies(name_vacancy_to_parse)
        vacancies = hh_api.get_data_vacancies('2023-12-20', 10)
    else:
        vacancies = []

    context = {'vacs': vacancies, 'last_vacancies': last_vacancies_data}
    context['navigation'] = get_navigation_data()
    return render(request, 'last_vacancy_page.html', context)
