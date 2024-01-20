from files.models import *


def get_navigation_data():
    return CustomNavigation.objects.all()


def get_main_page_data():
    return CustomMainPage.objects.all()


def get_demand_page_data():
    return CustomDemand.objects.all()


def get_geography_page_data():
    return CustomGeography.objects.all()


def get_skills_page_data():
    return CustomSkills.objects.all()


def get_last_vacancy_page_data():
    return CustomLastVacancyModel.objects.all()
