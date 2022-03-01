import time
import json
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# instagram post list (for example, news on Russia's invasion of Ukraine)
urls = ['https://www.instagram.com/p/CaQpRE8oeHr/', 'https://www.instagram.com/p/CaVfhypIXgL/']

# location of driver
driver= webdriver.Chrome('/home/username/projects/myproject/chromedriver')

driver.get("https://www.instagram.com/")

# login to instagram 
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='username']"))).send_keys("your-username")
driver.find_element_by_xpath("//input[@name='password']").send_keys("your-password")
time.sleep(3)  # necessary for the login to work
driver.find_element_by_xpath("//button/div[text()='Log In']").click()
# open the window that pops up and accept cookies

# for each instagram post
counter = 0
for url in urls:
    # get post
    time.sleep(3)
    driver.get(url)
    time.sleep(3)

    # write page source to file to analyze later
    with open(f'{counter}_url.txt', "w") as f:
        json.dump(driver.page_source, f)

    # load all replies iteratively without the nested replies
    hasLoadMore = True
    while hasLoadMore:
        time.sleep(5)
        try:
            if driver.find_element_by_css_selector('#react-root > section > main > div > div > article > div.eo2As > div.EtaWk > ul > li > div > button > span'):
                driver.find_element_by_css_selector('#react-root > section > main > div > div > article > div.eo2As > div.EtaWk > ul > li > div > button > span').click()
        except:
            hasLoadMore = False

    # scrape user text pairs
    user_text = {}
    all_users = [user for user in driver.find_elements_by_class_name('_6lAjh')]
    replies = [reply for reply in driver.find_elements_by_css_selector('#react-root > section > main > div > div > article > div > div > div > div.eo2As > div.EtaWk > ul > ul > div > li > div > div > div.C4VMK > div.MOdxS > span')]
    original_post = driver.find_element_by_css_selector('#react-root > section > main > div > div > article > div > div > div > div.eo2As > div.EtaWk  > ul > div > li > div > div > div.C4VMK > div.MOdxS > span')
    print(f'{len(all_users)} users (including the original post and the replies), and {len(replies)} replies under the original post')

    # save user text pairs
    i = 0
    user_text[all_users[i].text] = original_post.text
    for text in replies:
        user_text[all_users[i+1].text] = replies[i].text
        i += 1

    # write user text pairs in json file
    with open(f'{counter}_content.json', "w") as f:
        json.dump(user_text, f)

    counter += 1
    print(user_text)
    
