from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as BS
import time
PATH = r'C:\Users\acer laptop\miniconda3\chromedriver.exe'


class Scraper:
    def __init__(self, driver= webdriver.Chrome()):
        self.driver = driver
        self.URL = "https://www.myprotein.com/?affil=awin&utm_content=https%3A%2F%2Fdeals.traffifly.com%2F&utm_term=Editorial+Content&utm_source=AWin-1052475&utm_medium=affiliate&utm_campaign=AffiliateWin&sv_campaign_id=1052475&sv_tax1=affiliate&sv_tax2=&sv_tax3=JVT+DIGITAL+PTE.+LTD.&sv_tax4=0&awc=3196_1669634006_dc32e84ca958e4648a6bc63962b1a42a"
        self.all_links = []

    def page(self):
        self.page = self.driver.get(self.URL)

    def close_pop_up(self):
        time.sleep(3)
        close_pop_up = self.driver.find_element(By.CLASS_NAME,'close-button')
        close_pop_up.click()

    def accept_cookies(self):
        accept_cookies = self.driver.find_element(By.CLASS_NAME, "cookie_modal_button")
        accept_cookies.click()
       
    def shop_protein(self):
        time.sleep(6)
        protein = self.driver.find_element(By.CLASS_NAME, "brandLogos_image")
        protein.click()
    
    def get_data(self):
        time.sleep(3)
        soup = BS(self.driver.page_source , 'lxml')
        container = soup.find_all('div', class_= "athenaProductBlock")
        for link in container:
            href = link.find('a').get('href')
            self.all_links.append(href)
                        
        print(self.all_links)
   

       
if __name__ == "__main__":
    shop = Scraper()
    shop.page()
    shop.close_pop_up()
    shop.accept_cookies()
    shop.shop_protein()
    shop.get_data()

time.sleep(8)



