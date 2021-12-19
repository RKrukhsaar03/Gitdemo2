# js DOM can access any elements on web page just like how selenium does
# selenium have a method to execute javascript code in it

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_name("name").send_keys("hello")
print(driver.find_element_by_name("name").text)  # not gonna work because value is give by selenium
print(driver.find_element_by_name("name").get_attribute("value"))  # get_attribute is derived by DOM javascript
print(driver.execute_script('return document.getElementsByName("name")[0].value'))  # it is pure javascript no selenium

shopButton = driver.find_element_by_css_selector("a[href*='shop']")

driver.execute_script("arguments[0].click();", shopButton)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);") # by default selenium does not have scrolling method so we use javascript DOM  execruiter


