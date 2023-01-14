from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


usrname=input("Enter your Usename:")
password=input("Enter your Password:")
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.instagram.com/') #go to instagram 
print ("Opened instagram") 
driver.maximize_window()
sleep(3) #delay the script for 1 second

username_box = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input') # find element with the id 'email' on facebook to get the usernameBox
username_box.send_keys(usrname) # write my username in to the box
print ("Your user name has been entered")
sleep(2)

password_box = driver.find_element(By.NAME, "password") # find the passwordBox
password_box.send_keys(password) # write my password in to the box
print ("you password has been entered")
sleep(2)

login_box = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]') #find login button
login_box.click() #click the login button
sleep(6)

print ("Done")
input('You can type quit to exist')
driver.quit()
print("Finished")
