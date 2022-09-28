import argparse
import json
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as Chrome_Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'

# EC.element_to_be_clickable()

# log in:  python Upload.py -k "sudden divide wealth what motor question script fat gain indoor morning medal" -p "Luckytrail208!"

Chrome_Options = webdriver.ChromeOptions()
Chrome_Options.add_extension(r"D:\10.18.4_0.crx")
driver = webdriver.Chrome(r"D:\chromedriver.exe", options=Chrome_Options)
driver.get("https://opensea.io/asset/create")


def load_Data():
    jpg_files = []
    json_files = []
    full_dict = {}
    for root, dir, files in os.walk(r"Data_Upload"):
        for file in files:
            if file.endswith(".json"):
                json_files.append(os.path.join(root, file))
            if file.endswith(".jpg"):
                jpg_files.append(os.path.join(root, file))

    for i in range(len(json_files)):
        full_dict[jpg_files[i]] = json_files[i]

    return full_dict, jpg_files

def get_args():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument("-s", "--source_dir", help="enter source directory")
    parser.add_argument("-k", "--key_words", help="enter 12 key words")
    parser.add_argument("-p", "--password", help="enter password")
    parser.add_argument("-d", "--dir", help="enter name")
    args = parser.parse_args()
    return args


def set_up_metamask(key_words, password):
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[0])
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/button'))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/div/div[5]/div[1]/footer/button[2]'))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/div[2]/div/div[2]/div[1]/button'))).click()

    for i in range(0, 12):  # 12 keywords Entering
        time.sleep(0.2)
        input_keywords = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f'//*[@id="import-srp__srp-word-{i}"]')))
        input_keywords.click()
        input_keywords.send_keys(key_words[i])

    password_box = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="password"]')))
    password_box.click()
    password_box.send_keys(password)  # password

    password_box_again = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="confirm-password"]')))
    password_box_again.click()
    password_box_again.send_keys(password)  # password again

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="create-new-vault__terms-checkbox"]'))).click()  # Agree to terms and conditions

    time.sleep(1)

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/div[2]/form/button'))).click()  # CLick Agree and Continue

    time.sleep(10)

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/button'))).click()  # Click Continue

    driver.close()


def connect_metamask():
    time.sleep(2)

    driver.switch_to.window(driver.window_handles[1])  # switch to metamask tab

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div[3]/div[2]/button[2]'))).click()  # Click Connect
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                                '//*[@id="app-content"]/div/div[2]/div/div[2]/div[2]/div[2]/footer/button[2]'))).click()  # Click Connect

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div[3]/button[2]'))).click()  # Click Next


def open_sea(password):
    driver.switch_to.window(driver.window_handles[0])  # switch to open sea tab

    driver.find_element(By.XPATH, '//*[@id="main"]/div/div/div/div[2]/ul/li[1]/button').click()

    connect_metamask()


def main_upload(image_files, json_files):
    driver.switch_to.window(driver.window_handles[0])  # switch to open sea tab

    print(json_files)
    input('wait')


def main():
    full_key_value, jpg_path = load_Data()
    args = get_args()

    keywords = args.key_words
    keywords = keywords.split(" ")
    password = args.password

    set_up_metamask(keywords, args.password)
    time.sleep(2)
    open_sea(password)
    main_upload(full_key_value, jpg_path)


if __name__ == '__main__':
    main()
