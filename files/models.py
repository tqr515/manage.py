from django.db import models

class CustomNavigation(models.Model):
    job_title = models.TextField(blank=False, verbose_name='Должность', max_length=25)
    company_logo = models.ImageField(upload_to='images_db/%Y/%m/%d', blank=False, verbose_name='Логотип компании')
    first_menu_item = models.TextField(blank=False, verbose_name='Первый пункт меню', max_length=25)
    second_menu_item = models.TextField(blank=False, verbose_name='Второй пункт меню', max_length=25)
    third_menu_item = models.TextField(blank=False, verbose_name='Третий пункт меню', max_length=25)
    fourth_menu_item = models.TextField(blank=False, verbose_name='Четвертый пункт меню', max_length=25)
    fifth_menu_item = models.TextField(blank=False, verbose_name='Пятый пункт меню', max_length=25)
    creator = models.TextField(blank=False, verbose_name='Автор', max_length=50)

    def __str__(self):
        return f"CustomNavigation - {self.job_title}"

    class Meta:
        db_table = 'custom_navigation_table'

class CustomMainPage(models.Model):
    job_description = models.TextField(blank=True, verbose_name='Описание профессии')
    job_photo = models.ImageField(upload_to='images_db/%Y/%m/%d', blank=False, verbose_name='Фотография профессии')

    def __str__(self):
        return f"CustomMainPage - {self.job_description[:10]}..."

    class Meta:
        db_table = 'custom_mainpage_table'

class CustomDemand(models.Model):
    salary_level_chart = models.ImageField(upload_to='images_db/%Y/%m/%d', blank=False, verbose_name='График уровня зарплаты по годам')
    vacancy_number_chart = models.ImageField(upload_to='images_db/%Y/%m/%d', blank=False, verbose_name='График количества вакансий по годам')
    data_table = models.TextField(blank=False, verbose_name='Таблица данных')

    def __str__(self):
        return f"CustomDemand - {self.id}"

    class Meta:
        db_table = 'custom_demand_table'

class CustomGeography(models.Model):
    city_salary_chart = models.ImageField(upload_to='images_db/%Y/%m/%d', blank=False, verbose_name='График уровня зарплаты по городам')
    city_vacancy_fraction_chart = models.ImageField(upload_to='images_db/%Y/%m/%d', blank=False, verbose_name='График доли вакансий по городам')
    data_table = models.TextField(blank=False, verbose_name='Таблица данных')

    def __str__(self):
        return f"CustomGeography - {self.id}"

    class Meta:
        db_table = 'custom_geography_table'

class CustomSkills(models.Model):
    table_name = models.TextField(blank=False, verbose_name='Название таблицы', max_length=30)
    data_table = models.TextField(blank=False, verbose_name='Таблица данных')
    skills_chart = models.ImageField(upload_to='images_db/%Y/%m/%d', blank=False, verbose_name='График навыков')

    def __str__(self):
        return f"CustomSkills - {self.table_name[:10]}..."

    class Meta:
        db_table = 'custom_skills_table'

class CustomLastVacancyModel(models.Model):
    job_title = models.CharField(max_length=100, verbose_name='Должность')
    vacancy_to_parse = models.TextField(blank=False, verbose_name='Вакансия для парсинга', max_length=15)

    def __str__(self):
        return f"CustomLastVacancyModel - {self.job_title[:10]}..."

    class Meta:
        db_table = 'custom_lastvacancymodel_table'
