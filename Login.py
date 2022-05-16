import time



from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException,ElementClickInterceptedException


EMAIL="Your email"
PASSWORD="Your Password"
class Login:
    def __init__(self):
        self.link="https://www.instagram.com/therock/"
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver=driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


    def Login(self):

        self.driver.get(self.link)

        time.sleep(2)
        try:
            Click=self.driver.find_element(By.XPATH,'//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/span/a[1]/button')
            Click.click()
            time.sleep(4)

            Email_id = self.driver.find_element(By.NAME, 'username')
            Email_id.send_keys(EMAIL)

            Password =self.driver.find_element(By.NAME, 'password')
            Password.send_keys(PASSWORD)

        except NoSuchElementException:
            time.sleep(2)

            Email_id = self.driver.find_element(By.NAME, 'username')
            Email_id.send_keys(EMAIL)

            Password = self.driver.find_element(By.NAME, 'password')
            Password.send_keys(PASSWORD)

        LogIn = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
        LogIn.click()
        time.sleep(7)
        Button=self.driver.find_element(By.XPATH,'//*[@id="react-root"]/section/main/div/div/div/div/button')

        Button.click()
        time.sleep(5)
        followers=self.driver.find_element(By.XPATH,'//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()

    def followers(self):
        time.sleep(2)
        following=self.driver.find_elements(By.CSS_SELECTOR,'li button')

        for n in range(100):
            following = self.driver.find_elements(By.CSS_SELECTOR, 'li button')
            for i in following:

                try:
                    i.click()
                    time.sleep(1)
                except ElementClickInterceptedException:
                    cancel_button = self.driver.find_element(By.XPATH,'/html/body/div[7]/div/div/div/div[3]/button[2]')
                    cancel_button.click()








