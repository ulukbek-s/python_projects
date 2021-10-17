from selenium import webdriver
# this code worked with most of the websites but some of them(including hackthebox)
# did not allow me to do automation with python
driver = webdriver.Chrome()
driver.get('https://app.hackthebox.eu/invite')

username = input('Enter username: ')
email = input('Enter email: ')
password = input('Enter the password: ')
password2 = input('Repeat the password')

username_box = driver.find_element_by_xpath('//*[@id="input-22"]')
username_box.send_keys(username)

email_box = driver.find_element_by_xpath('//*[@id="input-25"]')
email_box.send_keys(email)

password_box = driver.find_element_by_xpath('//*[@id="input-28"]')
password_box.send_keys(password)

password2_box = driver.find_element_by_xpath('//*[@id="input-32"]')
password2_box.send_keys(password2)

reg = driver.find_element_by_xpath('//*[@id="registerform"]/button')
reg.click()

