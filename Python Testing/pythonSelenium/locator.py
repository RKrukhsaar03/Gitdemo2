from selenium import webdriver
from selenium.webdriver.support.select import Select

# driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe")

driver.get("https://rahulshettyacademy.com/angularpractice/")

#driver.find_element_by_name("email").send_keys("Rahul")
#driver.find_element_by_id("exampleCheck1").click()

# select class provide the methods to handle the option in dropdown
dropdown = Select(driver.find_element_by_id("exampleFormControlSelect"))
dropdown.select_by_visible_text("Female")
dropdown.select_index(0)

driver.find_element_by_css_selector("input[name='name']").send_keys("Rahul")
driver.find_element_by_name("email").send_keys("Shetty")

driver.find_element_by_xpath("//input[@type='submit']").click()

# print(driver.find_element_by_class_name("alert-success").text)
message = driver.find_element_by_class_name("alert-success").text

assert "success" in message


# //*[contain(@class,'alert-success')] - Xpath
# [class*='alert-success'] - CSS
