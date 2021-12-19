from selenium import webdriver


driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://login.salesforce.com/?locale=in")
driver.find_element_by_css_selector("#username").send_keys('rahul')
driver.find_element_by_css_selector(".password").send_keys('shetty')
driver.find_element_by_css_selector(".password").clear()

#driver.find_element_by_partial_link_text("Forgot Your Password?").click()

# //tagname[text()='xxx']
# generating xpath based on text
# driver.find_element_by_xpath("//a[text()='Cancel']").click()  # code have been change


print(driver.find_element_by_xpath("//form[@name='login']/div[1]/label").text)

print(driver.find_element_by_css_selector("form[name='login'] label:nth-child(4)").text)

