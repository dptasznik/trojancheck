from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from DuoMatch import DuoMatch
from PIL import Image

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

try:
    begin_btn = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "[aria-label='Begin wellness assessment']"))
    )
    begin_btn.click()

except:
    driver.quit()

try:
    start_screen_btn = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "btn-assessment-start"))
    )

    # take screenshot

    # location = start_screen_btn.location;
    # print(location)
    # size = start_screen_btn.size;
    driver.save_screenshot("pageImage.png");
    start_screen_btn.screenshot("testShot.png")
    #
    # # crop image
    # x = location['x'];
    # y = location['y'];
    # width = location['x'] + size['width'];
    # height = location['y'] + size['height'];
    # print(x, y, width, height)
    # im = Image.open('pageImage.png')
    # im = im.crop((int(x), int(y), int(width), int(height)))
    # im.save('element.png')

    start_screen_btn.click()

except:
    driver.quit()

try:
    no1 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "mat-button-toggle-2-button"))
    )
    no1.click()
    next1 = driver.find_element(By.CLASS_NAME, "btn-next")
    next1.click()

except:
    driver.quit()

try:
    no2 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "mat-button-toggle-11-button"))
    )
    print("success")
    no2.click()

    for i in range(13, 24, 2):
        no_x = driver.find_element(By.ID, f"mat-button-toggle-{i}-button")
        no_x.click()

    next2 = driver.find_element(By.CLASS_NAME, "btn-next")
    next2.click()

except:
    driver.quit()

try:
    attest_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "mat-checkbox-1"))
    )
    attest_box.click()
    submit = driver.find_element(By.CLASS_NAME, "btn-submit")
    submit.click()

except:
    driver.quit()

# take screenshot
try:
    qrcode = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "day-pass"))
    )
    qrcode.screenshot("qrcode.png")

except:
    driver.quit()



    # take screenshot
    # test_item = driver.find_element(By.CLASS_NAME, "home-button")

    # location = next2.location;
    # print(location)
    # size = next2.size;
    # driver.save_screenshot("pageImage.png");
    #
    # # crop image
    # x = location['x'];
    # y = location['y'];
    # width = location['x'] + size['width'];
    # height = location['y'] + size['height'];
    # print(x, y, width, height)
    # im = Image.open('pageImage.png')
    # im = im.crop((int(x), int(y), int(width), int(height)))
    # im.save('element.png')
