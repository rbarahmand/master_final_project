## import libraries
from selenium import webdriver
import pandas as pd
import os
import time
from tqdm import tqdm


## initialization
if not os.path.exists("dataset"):
    os.mkdir("dataset")
    
print(time.ctime(time.time()))
driver = webdriver.Chrome()
data = pd.DataFrame({"name": [],
                    "general_name": [],
                    "drug_type": [],
                    "consumption": [],
                    "license": [],
                    "brand": [],
                    "producer": [],
                    "license_exp": [],
                    "price_per_pack": [],
                    "unit_price": [],
                    "GTIN": [],
                    "IRC": [],
                    "number_per_pack": [],
                    "ingredients": [],
                    "ATC": []})


## change numbers base on your system and website
start = 101
max_allowed_i = 200    # 45433
per_partition = 30    # 5000
num_features_to_crawl = 15


## crawler and organizer 
for i in tqdm(range(start, max_allowed_i+1)):
    driver.get(f"https://irc.fda.gov.ir/nfi/Detail/{i}")
    # time.sleep(1.5)
    temp_data = [None] * num_features_to_crawl
    
    temp_data[0] = driver.find_element(by='xpath', value="""/html/body/div[1]/div[5]/div[1]/div[1]/div/div/div[3]/div[1]/div[1]/span""").text
    temp_data[1] = driver.find_element(by='xpath', value="""/html/body/div[1]/div[5]/div[1]/div[1]/div/div/div[3]/div[1]/div[2]/bdo""").text
    temp_data[2] = driver.find_element(by='xpath', value="""/html/body/div[1]/div[5]/div[1]/div[1]/div/div/div[3]/div[2]/div[1]/span""").text
    temp_data[3] = driver.find_element(by='xpath', value="""/html/body/div[1]/div[5]/div[1]/div[1]/div/div/div[3]/div[2]/div[2]/bdo""").text
    temp_data[4] = driver.find_element(by='xpath', value="""/html/body/div[1]/div[5]/div[1]/div[1]/div/div/div[3]/div[3]/div[1]/span""").text
    temp_data[5] = driver.find_element(by='xpath', value="""/html/body/div[1]/div[5]/div[1]/div[1]/div/div/div[3]/div[3]/div[2]/span""").text
    temp_data[6] = driver.find_element(by='xpath', value="""/html/body/div[1]/div[5]/div[1]/div[1]/div/div/div[3]/div[4]/div[1]/span""").text
    temp_data[7] = driver.find_element(by='xpath', value="""/html/body/div[1]/div[5]/div[1]/div[1]/div/div/div[3]/div[4]/div[2]/span""").text
    temp_data[8] = driver.find_element(by='xpath', value="""/html/body/div[1]/div[5]/div[1]/div[1]/div/div/div[3]/div[5]/div[1]/span[1]""").text
    temp_data[9] = driver.find_element(by='xpath', value="""/html/body/div[1]/div[5]/div[1]/div[1]/div/div/div[3]/div[5]/div[2]/span[1]""").text
    temp_data[10] = driver.find_element(by='xpath', value="""/html/body/div[1]/div[5]/div[1]/div[1]/div/div/div[3]/div[6]/div[1]/span""").text
    temp_data[11] = driver.find_element(by='xpath', value="""/html/body/div[1]/div[5]/div[1]/div[1]/div/div/div[3]/div[6]/div[2]/span""").text
    temp_data[12] = driver.find_element(by='xpath', value="""/html/body/div[1]/div[5]/div[1]/div[1]/div/div/div[3]/div[7]/div[1]/bdo""").text
    temp_data[13] = driver.find_element(by='xpath', value="""/html/body/div[1]/div[5]/div[1]/div[1]/div/div/div[3]/div[9]/div/div/div[1]/div[3]/div[1]/span""").text
    temp_data[14] = driver.find_element(by='xpath', value="""/html/body/div[1]/div[5]/div[1]/div[1]/div/div/div[3]/div[9]/div/div/div[2]/div[3]/label""").text

    data.loc[i] = temp_data

    
    ## data saver
    if i == max_allowed_i:
        data.to_csv(f"dataset/data{i}.csv")
        # print(f"{i}/{max_allowed_i}")
        break
    elif i % per_partition == 0:
        data.to_csv(f"dataset/data{i}.csv")
        data = pd.DataFrame({"name": [],
                    "general_name": [],
                    "drug_type": [],
                    "consumption": [],
                    "license": [],
                    "brand": [],
                    "producer": [],
                    "license_exp": [],
                    "price_per_pack": [],
                    "unit_price": [],
                    "GTIN": [],
                    "IRC": [],
                    "number_per_pack": [],
                    "ingredients": [],
                    "ATC": []})
        # print(f"{i}/{max_allowed_i}")



print(time.ctime(time.time()))

driver.quit()