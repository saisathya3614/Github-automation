from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement


driver = webdriver.Chrome(executable_path="D:/Selenium_cucumber_jar/chromedriver86.exe")
driver.implicitly_wait(5)
globals()
verify = "Can't find that email, sorry."
join= "Join GitHub"
createacc= "Create your personal account"
driver.get("https://github.com/")
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element_by_xpath("/html/body/div[1]/header/div/div[2]/div[2]/a[1]").click()

#login
driver.implicitly_wait(5)
pagename =driver.title
Signin="Sign in to GitHub · GitHub"
if pagename == Signin:
    print("User is redirected to login page")
else: print("User is not redirected to login page")

#Username and password verification
driver.find_element_by_xpath("//*[@id='login']/form/div[4]/input[12]").click()
driver.implicitly_wait(5)
id=driver.find_element_by_id("js-flash-container")
if id.is_displayed() == True:
    print("Verified that username and password fields are mandatory in login page")
else:  print("Verified that username and password fields are not mandatory in login page")

#verifying m.ie into email field
driver.implicitly_wait(5)
driver.find_element_by_xpath("//*[@id='login']/form/div[4]/label[2]/a").click()


driver.find_element_by_xpath("//*[@id='email_field']").send_keys("m.ie")
driver.find_element_by_xpath("//*[@id='forgot_password_form']/div[3]/input[2]").click()
driver.implicitly_wait(5)
MIE =driver.find_element_by_xpath("//*[@id='js-flash-container']/div/div")
if MIE==verify:
    print("Verified that after inserting m.ie into email field in reset_password page displays message as "+verify);
else:
    print("Verified that after inserting 'm.ie' into email field in reset_password page displays message as "+"'"+MIE.text+" '"+" instead of"+" "+verify)

#Verify that inserting empty value into email field in reset_password page
driver.find_element_by_xpath("//*[@id='email_field']").send_keys(" ")
driver.find_element_by_xpath("//*[@id='forgot_password_form']/div[3]/input[2]").click()
driver.implicitly_wait(5)
MIE =driver.find_element_by_xpath("//*[@id='js-flash-container']/div/div")
if MIE==verify:
    print("Verified that after inserting ' ' into email field in reset_password page displays message as "+verify);
else:
    print("Verified that after inserting ' ' into email field in reset_password page displays message as "+"'"+MIE.text)

#Verify that the first word in error message in reset_password page is "Can't"
Line=MIE.text
Word=Line.partition(' ')[0]

if Word=="Can't":
    print("Verify that the first word in error message in reset_password page is 'Can't'")
else:   print("Verify that the first word in error message in reset_password page is not 'Can't' it is "+"'"+Word+"'")

#Verify that clicking on "Sign up" button will redirect user into "join github" page
driver.back()
driver.back()
driver.back()
driver.implicitly_wait(9)
driver.find_element_by_xpath("//*[@id='login']/p/a").click()
signup=driver.find_element_by_xpath("/html/body/div[4]/main/div/div[1]/div").text
if signup==join:
    print("Verified that clicking on 'Sign up' button will redirect user into 'join github' page")
else:
    print("Verified that clicking on 'Sign up' button it is not redirecting to 'join github' page")
# Verify that "join github" page contains text "Create your personal account"
create=driver.find_element_by_xpath("/html/body/div[4]/main/div/div[1]/h1").text
if create==join:
    print("Verified that 'join github' page contains text 'Create your personal account'")
else:
    print("Verified that 'join github' page contains text "+create)
# Verify that "Create an account" button is greyed when an existing email address is inserted in"join github" page.
driver.find_element_by_xpath("//*[@id='user_email']").send_keys("sathyasai3614@gmail.com")
enable=driver.find_element_by_xpath("//*[@id='signup-form']/div[2]").is_enabled()

if enable==True:
    print("Verified that 'Create an account' button is greyed when an existing email address is inserted in'join github' page.")
else:
    print("Verified that 'Create an account' button is not greyed although an existing email address is inserted in'join github' page.")
driver.quit()