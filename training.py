import requests
import previous_training
from selenium import webdriver
import os
previous_training.getInfo()
level = int(input('Input the level [1-3] : '))
week = int(input('Input the week [1-6] : '))
add = ''
if level == 1:
        level = 'first'
        add = ' active '
if level == 2:
        level = 'second'
        add = ' '
if level == 3:
        level = 'third'
        add = ' '
try:
        resp = requests.get('https://dailyfit.ru/programmy-trenirovok/programma-100-otzhimanij/')
        data = resp.text
        left = data.find('<div class="ui'+add+'tab" data-tab="{}">'.format(level))
        right = data[left:].find('</div>')
        data = data[left:right + left]
        query = '<h2>Неделя {}</h2>'.format(week)
        index_1 = data.find(query)
        index_2 = data[index_1:].find('</table>') + 8 + index_1
        needed = data[index_1:index_2]
        with open('./training.html','w') as webpage:
                webpage.write(needed)
        # Opening my webpage
        driver = webdriver.Chrome('./chromedriver')
        driver.get('file://' + os.getcwd() + '/training.html')
        # # # Saving info about this request
        previous_training.setInfo(level,week)
except Exception as e: print(e)

