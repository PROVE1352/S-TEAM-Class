from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options) # Your Chrome Driver path

driver.get('https://ecampus.kookmin.ac.kr/course/view.php?id=55365')

pre_elem = driver.find_element(by=By.XPATH,value="/html/body/div[1]/div[3]/div/div[2]/div[2]/div/div/div[3]/ul/li/div[3]/ul/li[2]/div/div/span/span/span")
#code_elem = pre_elem.find_element(by=By.)
#print(driver.find_element(by=By.XPATH,value="/html/body/div[1]/div[3]/div/div[2]/div[2]/div/div/div[3]/ul/li/div[3]/ul/li[2]/div/div/span/span/span").text)
print(pre_elem.txt)