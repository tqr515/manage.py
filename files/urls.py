from django.urls import path
from .views import *

urlpatterns = [
    path('', home_page_data, name='home'),
    path('demend/', demand_page_data, name='demend'),
    path('geography/', geography_page_data, name='geography'),
    path('skills/', skills_page_data, name='skills'),
    path('lastVacancy/', last_vacancy_page, name='lastVacancy'),
]
