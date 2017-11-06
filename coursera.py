import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook
import random
import progressbar
import argparse


def get_random_courses_list(courses_amount):
    xml_feed = requests.get(
        'https://www.coursera.org/sitemap~www~courses.xml').content
    soup = BeautifulSoup(xml_feed, 'lxml')
    urls = soup.find_all('loc')
    random_urls = [random.choice(urls).text for i in range(courses_amount)]
    return random_urls


def parse_course_info(course_data):
    soup = BeautifulSoup(course_data, 'lxml')
    course_name = soup.find('h1', {'class': 'title display-3-text'}).text
    course_lang = soup.find('div', {'class': 'rc-Language'}).text
    course_start_date = soup.find(
        'div', {'class': 'startdate rc-StartDateString caption-text'}).text
    if soup.find('div', {'class': 'ratings-text bt3-visible-xs'}):
        course_rating = soup.find(
            'div', {'class': 'ratings-text bt3-visible-xs'}).text
    else:
        course_rating = None
    course_duration = len(soup.findAll('div', {'class': 'week'}))
    return {'Course name': course_name,
            'Language': course_lang,
            'Start date': course_start_date,
            'Duration (week)': course_duration,
            'Rating': course_rating}


def output_courses_info_to_xlsx(courses_info, filepath):
    wb = Workbook()
    ws = wb.active
    table_title = ['Course name', 'Language', 'Start date', 'Duration (week)',
                   'Rating']
    ws.append(table_title)
    for course in courses_info:
        course_row = [
            course['Course name'],
            course['Language'],
            course['Start date'],
            course['Duration (week)'],
            course['Rating'],
        ]
        ws.append(course_row)
    wb.save(filepath)


def get_input_argument_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--amount', required=False, default=20, type=int,
                        help='Amount of Coursera courses to view')
    parser.add_argument('-f', '--file', required=True,
                        help='Path to output Excel .xlsx file')
    return parser


if __name__ == '__main__':
    parser = get_input_argument_parser()
    args = parser.parse_args()
    courses_amount = args.amount
    filepath = args.file
    courses_list = get_random_courses_list(courses_amount)
    courses_info_list = []
    bar = progressbar.ProgressBar(max_value=courses_amount, initial_value=1)
    bar_start_position = 1
    for index, course_url in enumerate(courses_list, bar_start_position):
        course_info = requests.get(course_url).content.decode('utf-8')
        courses_info_list.append(parse_course_info(course_info))
        bar.update(index)
    output_courses_info_to_xlsx(courses_info_list, filepath)
