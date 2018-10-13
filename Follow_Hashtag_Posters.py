from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support import expected_conditions as EC
from lxml import html

browser = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')
browser.get("https://www.instagram.com/")

browser.find_element_by_link_text("Log in").click()
wait_for_load = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, """//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[1]/div/div[1]/label""")))

def login(username = 'Your username', password = 'Your password'):  #Enter username and password
	text_area_username = browser.find_element_by_name('username')
	text_area_username.send_keys(username)
	text_area_password = browser.find_element_by_name('password')
	text_area_password.send_keys(password)

def pop_up_block():
	pop_up_1 = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div/div/div[3]/button[2]")))
	pop_up_1.click()									
	pop_up_2 = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/button")))
	pop_up_2.click()

def search_hashtag():
	search_tag = "Your hashtag" #Enter searched hashtag
	search_area = browser.find_element_by_xpath("""//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input""")
	search_area.send_keys(search_tag)
	load_hastag = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, """//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]""")))
	load_hastag.click()

def first_pic():
	click = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, """//*[@id="react-root"]/section/main/article/div[2]/div/div[1]/div[1]""")))
	click.click()

def wait_for_follower_to_load():
	follow = browser.find_element_by_css_selector('button')
	follow.click()

def close_unfollow_page():
	close_unfollow_button = browser.find_element_by_xpath("""/html/body/div[4]/div/div/div/div[3]/button[1]""")
	close_unfollow_button.click()
	click_next = browser.find_element_by_xpath("""/html/body/div[3]/div/div[1]/div/div/a[2]""")
	click_next.click()

def click_next():
	click_next = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, """/html/body/div[3]/div/div[1]/div/div/a[2]""")))
	click_next.click()

def keyword_following():
	keyword =  WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, """/html/body/div[3]/div/div[2]/div/article/header/div[2]/div[1]/div[2]/button""")))
	return keyword.text

def main():
	login()
	browser.find_element_by_xpath("""//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]""").click()
	pop_up_block()
	search_hashtag()
	first_pic()
	while True:
		print (keyword_following())
		if keyword_following() == 'Follow':
			wait_for_follower_to_load()
			time.sleep(2)
			click_next()
		elif keyword_following() == 'Following':
			click_next()
			time.sleep(1)

if __name__ == "__main__":
	main()
