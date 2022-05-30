# Code written by Ioanni Tsaka
# Github : https://github.com/Kygo0

import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

titleVideo = input("Enter the title of the video: ")

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)
# Installing adblock to minimize errors/Ads getting in the way of the code.
chrome_options.add_extension(r'extension_3_13_0_0.crx')
# Add experimental options to remove "Google Chrome is controlled by automated software" notification
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

driver.get('https://www.youtube.com/')
driver.maximize_window()
# Closing "installation tab" of adblock extension.

pyautogui.keyDown('ctrl')
pyautogui.press('w')
time.sleep(1)
pyautogui.keyUp('ctrl')

# Clicking the "Accept All" button when you first launch YouTube.
# Chromedriver/Selenium opens tab without any cookies/profiles saved from original Google Chrome.
driver.find_element(By.XPATH, '/html/body/ytd-app/ytd-consent-bump-v2-lightbox/tp-yt-paper-dialog/div['
                              '4]/div/div[6]/div[1]/ytd-button-renderer['
                              '2]/a/tp-yt-paper-button/yt-formatted-string').click()

# After going on YouTube we find the search bar and type in the user's input.
time.sleep(1.5)
driver.find_element(By.XPATH, value='/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div['
                                    '2]/ytd-searchbox/form/div[1]/div[1]/input').send_keys(titleVideo)

# Clicking search on YouTube.
time.sleep(1)
driver.find_element(By.XPATH,
                    value='/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/button/yt-icon').click()

# Clicking the first recommended YouTube video.
time.sleep(1)
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('enter')
time.sleep(0.6)

# Could delete this "copying link of the video" part if you feel it is useless.
# Start of copy link part.
# Clicking the share button.
time.sleep(2)
driver.find_element(By.XPATH, value='//*[@id="top-level-buttons-computed"]/ytd-button-renderer[1]/a').click()

# Clicking the copy button.
time.sleep(1)
driver.find_element(By.XPATH, value="/html/body/ytd-app/ytd-popup-container/tp-yt-paper-dialog["
                                    "1]/ytd-unified-share-panel-renderer/div["
                                    "2]/yt-third-party-network-section-renderer/div["
                                    "2]/yt-copy-link-renderer/div/yt-button-renderer/a/tp-yt-paper"
                                    "-button/yt-formatted-string").click()
# Clicking X to get out of the share popup window.
driver.find_element(By.XPATH,
                    value="/html/body/ytd-app/ytd-popup-container/tp-yt-paper-dialog/ytd-unified-share-panel-renderer/yt-icon-button/button").click()
# End of copy link part.

# Going into settings.
time.sleep(0.5)
driver.find_element(By.XPATH, value="//button[@aria-label='Settings'][@aria-controls='ytp-id-17']").click()

# Clicking quality settings.
time.sleep(2)
driver.find_element(By.XPATH, value='(//div[@class="ytp-menuitem-label"][text()="Quality"])').click()
time.sleep(1)
driver.find_element(By.XPATH, value='(//div[@class="ytp-menuitem"])[1]').click()


# Going full-screen
pyautogui.press('f')
