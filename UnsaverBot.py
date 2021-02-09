import sys
from time import sleep
from tqdm import tqdm
from selenium import webdriver

class instaBot():
	def __init__(self, username, password):
		self.username = username
		self.password = password

		self.driver = webdriver.Firefox(executable_path=r'geckodriver.exe')
		#self.driver = webdriver.Chrome('chromedriver.exe')
		self.driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
		sleep(2)

		#login to the user account
		print('logging-in')
		self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
		.send_keys(username)
		self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
		.send_keys(password)
		self.driver.find_element_by_xpath("//button[@type=\"submit\"]")\
		.click()
		sleep(8)
		self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
		.click()

	def UnsaveImages(self):
		#goto profile
		print('going to user profile')
		self.driver.find_element_by_xpath("//a[contains(@href, '/{}')]".format(self.username))\
		.click()
		sleep(6)
		#goto Saved
		print('opening Saved tab')
		self.driver.find_element_by_xpath("//span[contains(text(), 'Saved')]")\
		.click()
		sleep(4)
		
		#open first image
		print('opening images')
		self.driver.find_element_by_xpath("//div[@class=\"v1Nh3 kIKUG  _bz0w\"]")\
		.click()
		sleep(4)
		print('starting unsaver')

		for x in tqdm(range(1,100)):
			#remove image
			self.driver.find_element_by_xpath("//span[@class=\"wmtNn\"]")\
			.click()
			sleep(1)

			#goto next image
			self.driver.find_element_by_xpath("//a[@class=\" _65Bje  coreSpriteRightPaginationArrow\"]")\
			.click()
			sleep(4)

if __name__ == "__main__":
	if len(sys.argv) == 3:
		username = sys.argv[1]
		password = sys.argv[2]
		my_bot = instaBot(username, password)
		my_bot.UnsaveImages()
	else:
		print("Invalid number of arguments")
		print(f"Syntax: python {sys.argv[0]} username password")
		exit()