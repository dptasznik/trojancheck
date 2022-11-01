from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from DuoMatch import DuoMatch

driver = webdriver.Chrome()
driver.get("https://trojancheck.usc.edu/login")

try:
    login_btn = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[@aria-label='Log in with your USC NetID']"))
    )
    login_btn.click()
except:
    driver.quit()

try:
    username = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "username"))
    )
    #input username
    username.send_keys("<USERNAME>")
    #input password
    password = driver.find_element(By.ID, "password")
    password.send_keys("<PASSWORD>")
    #click button
    sign_in_btn = driver.find_element(By.NAME, "_eventId_proceed")
    sign_in_btn.click()
except:
    driver.quit()

try:
    duo_iframe = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "duo_iframe"))
    )
    driver.switch_to.frame("duo_iframe")

except:
    driver.quit()

# driver.switch_to.frame("duo_iframe")

try:
    passcode_btn = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "passcode"))
    )
    passcode_btn.click()

    # select_phone = driver.find_element(By.NAME, "device")
    # select_phone.click()
    # option = driver.find_element(By.XPATH, "//option[@value='phone2']")
    # option.click()

    passcode_input = driver.find_element(By.NAME, "passcode")

    passcode_msg = driver.find_element(By.CLASS_NAME, 'next-passcode-msg').text
    code = DuoMatch.duo_match("duo_codes.txt", passcode_msg)
    passcode_input.send_keys(code)
    passcode_btn.click()

except:
    driver.quit()

driver.switch_to.default_content()

try:
    trocheck_btn = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "submit-button"))
    )
    trocheck_btn.click()

# IF NEED XPATH: "//button[@class='mat-focus-indicator submit-button btn-next mat-button mat-button-base mat-accent']"

except:
    driver.quit()

#take screenshot
try:
    qrcode = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "day-pass"))
    )
    qrcode.screenshot("qrcode.png")

except:
    driver.quit()
