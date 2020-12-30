from selenium import webdriver
from time import sleep

browser = webdriver.Chrome(r'C:\Users\user\Documents\Python\Ecosia bot\chromedriver.exe')
browser.get('https://www.betclic.it/scommesse/calcio/serie-a_1_31_33')

main = browser.find_element_by_id('panel')
#element found

body = main.find_element_by_xpath('/html/body')

wrapper = body.find_element_by_xpath('/html/body/div[3]')

sleep(3)


content = wrapper.find_element_by_xpath('/html/body/div[3]/div[2]')


#sleep(5)

table = wrapper.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[2]/div/div[3]/div[2]/div[2]/div/table')
#/html/body/div[3]/div[2]/div/div[2]/div/div[3]/div[2]/div[2]/div/table


for row in table.find_elements_by_class_name('simple-row'):
    one = row.find_element_by_tag_name('td')
    two = one.find_element_by_tag_name('span')
    print(two)