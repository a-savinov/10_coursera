import requests
from bs4 import BeautifulSoup
import random


def get_courses_list(courses_amount):
    xml_feed = requests.get('https://www.coursera.org/sitemap~www~courses.xml').content
    soup = BeautifulSoup(xml_feed, 'lxml')
    urls = soup.find_all('loc')
    random_urls_list = [random.choice(urls).text for i in range(courses_amount)]
    return random_urls_list



def get_course_info(course_url):
    '''
    Зайти на страницу курса и вытащить оттуда название, язык, ближайшую дату начала, количество недель и среднюю оценку.
    '''
    course_info = requests.get(course_url).text
    soup = BeautifulSoup(course_info)
    course_name = soup.find('h1', {'class': 'title display-3-text'}).text
    course_lang = soup.find('div', {'class': 'rc-Language'}).text
    course_rating = soup.find('div', {'class': 'ratings-text bt3-hidden-xs'}).text
    course_duration = soup.find('td', {'class': 'td-data'}).text
    return course_info


def output_courses_info_to_xlsx(filepath):
    pass


if __name__ == '__main__':
    courses_list = get_courses_list(10)
    print(courses_list)
    for course in courses_list:
        course_info = get_course_info(course)


