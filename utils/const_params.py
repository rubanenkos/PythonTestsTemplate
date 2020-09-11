from enum import Enum

ENVIRONMENTS = ['DEV', 'QA', 'STAGE', 'PROD']
CITIES = ['Харьков', 'Днепр', 'Запорожье', 'Киев']
SITE_SECTIONS = {
                'О нас': "https://chisw.com.ua",
                'Вакансии': "https://chisw.com.ua/vacancies/",
                'Интернатура': "https://chisw.com.ua/internship/",
                'Новости': "https://chisw.com.ua/articles/"
                 }


class ProjectPaths(Enum):
    CHROME_DRIVER = 'drivers/chromedriver'
    FILES_USERS = 'settings/'
    FLOW_SCENARIO = 'test_data/scenarios/'
    LOG_IMAGES = 'logs/'
