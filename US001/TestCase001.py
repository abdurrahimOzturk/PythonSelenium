from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
from faker import Faker
from selenium.webdriver.support.ui import Select


serv_obj = Service("C:\\browserdrivers\\chromedriver.exe")

driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10) #when driver has problem. it will be here to take a break



#1- User goes to "www.belgiantrain.be"
driver.get("https://www.belgiantrain.be/en/")
driver.maximize_window()
driver.find_element(By.XPATH, "//button[@id='CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll']").click()
driver.implicitly_wait(2)

#2- User writes departure
driver.find_element(By.XPATH,"//input[@id='Origin_Reference-input']").send_keys("Gent Sint Pieters")
driver.find_element(By.XPATH,"//li[@id='location-search-Origin_Reference-input-0']").click()

#3- User writes destination city
driver.find_element(By.XPATH,"//input[@id='Destination_Reference-input']").send_keys("Hasselt, Kiewit")
driver.implicitly_wait(2)
driver.find_element(By.XPATH,"//li[@id='location-search-Destination_Reference-input-0']").click()

#4- User clicks on "Plan my journey" button
driver.find_element(By.XPATH,"//button[@id='routePlannerFormSubmit']").click()

#5- User clicks on "Buy a train ticket" button
driver.implicitly_wait(2)
driver.find_element(By.XPATH,"(//a[@class='show-popup-if-season-ticket-in-basket btn--primary btn float-right'])[1]").click()


#6- User chooce tickets clicks on "Complete order" button
driver.implicitly_wait(1)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
driver.implicitly_wait(2)
driver.find_element(By.XPATH,"//button[@id='goto-next-page']").click()
driver.implicitly_wait(2)
driver.find_element(By.XPATH,"//button[normalize-space()='Buy']").click()
driver.implicitly_wait(2)
driver.find_element(By.XPATH,"//a[@id='checkout-btn']").click()


#7- User gives Personal informations
driver.implicitly_wait(2)
fake = Faker('it_IT')
full_name = (fake.name())
first,last = full_name.split()
driver.find_element(By.XPATH,"//input[@id='Basket_Customer_FirstName']").send_keys(first)
driver.find_element(By.XPATH,"//input[@id='Basket_Customer_LastName']").send_keys(last)
driver.find_element(By.XPATH,"//input[@id='Basket_Customer_Email']").send_keys(first+last+"@gmail.com")



#8- User choose payment method
driver.implicitly_wait(2)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
driver.find_element(By.XPATH,"(//div[@class='select__trigger__icon'])[2]").click()
driver.implicitly_wait(2)
driver.find_element(By.XPATH,"(//span[@class='select__option__txt'])[2]").click()
driver.implicitly_wait(2)




#9- User clicks on "go to payment" and verify
btn = driver.find_element(By.XPATH,"//label[@for='AcceptTermsConditions']")
driver.execute_script("arguments[0].click();", btn);
driver.find_element(By.XPATH,"//button[@type='submit']").click()
driver.implicitly_wait(2)
actual_result = driver.find_element(By.XPATH,"(//div[@class='appDescription'])[2]").text
print(actual_result)
expected_result = "Scan the QR code and follow the instructions"
if actual_result == expected_result:
    print("Test_case_001 Passed")
else:
    print("Test_case_001 failed")

