
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import csv
import pickle

driver = webdriver.Chrome()
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=options)
driver.get('https://sp4n.lapor.go.id/')
driver.implicitly_wait(7)
driver.find_element(By.XPATH,'//a[text()="Masuk"]').click()
driver.implicitly_wait(15)
user=driver.find_element(By.ID,'userSigninLogin')
password=driver.find_element(By.ID,'userSigninPassword')
user.send_keys('dharma1305')
password.send_keys('@S0kes0kk1pre1')
driver.find_element(By.XPATH, "//button[@class='btn btn-primary btn-block' and text()='Masuk']").click()
time.sleep(10)
desired_url="https://sp4n.lapor.go.id/instansi/badan-pengembangan-pemberdayaan-sumber-daya-manusia-kesehatan"
driver.get(desired_url)
time.sleep(10)
elements = driver.find_elements(By.CLASS_NAME, 'text-user')
title=driver.find_elements(By.CLASS_NAME,'complaint-title')
detail_keluhan=driver.find_elements(By.CLASS_NAME,'readmore')
instasi_list=["https://sp4n.lapor.go.id/instansi/badan-pengembangan-pemberdayaan-sumber-daya-manusia-kesehatan",
              "https://sp4n.lapor.go.id/instansi/direktorat-jenderal-perhubungan-darat" ,"https://sp4n.lapor.go.id/instansi/divisi-pemasaran-dan-pelayanan-pelanggan"]
instansi_alfabet=["Direktorat Jenderal Tenaga Kesehatan","Direktorat Jenderal Perhubungan Darat","Divisi Pemasaran dan Pelayanan Pelanggan"]
filename='dataset/final_dataset_final.csv'
#
switch=True
instansi_count=0
much=310
stop=True
text_content_list=[]
while instansi_count < len(instansi_alfabet) :
    driver.find_element(By.CSS_SELECTOR, 'body').send_keys(Keys.CONTROL + Keys.END)
    time.sleep(7)
    div_element = driver.find_element(By.CLASS_NAME, "ias-trigger-next")
    div_element.find_element(By.TAG_NAME, "a").click()
    time.sleep(30)
    elements = driver.find_elements(By.CLASS_NAME, 'text-user')
    print(len(elements))
    if instansi_count>=1 :
        much=600
    if len(elements) > much :
        elements = driver.find_elements(By.CLASS_NAME, 'text-user')
        title = driver.find_elements(By.CLASS_NAME, 'complaint-title')
        detail_keluhan = driver.find_elements(By.CLASS_NAME, 'readmore')
        tanggal_masuk_laporan=driver.find_elements(By.CLASS_NAME,'text-channel')
        for i in range(len(elements)):
            data = {}
            data['pelapor'] = elements[i].text
            data['tanggal_masuk_laporan'] =tanggal_masuk_laporan[i].text
            data['judul_laporan'] = title[i].text
            data['detail_keluhan'] = detail_keluhan[i].text
            data['instansi'] = instansi_alfabet[instansi_count]
            text_content_list.append(data)
        filename=f"dataset/final_dataset{instansi_count}.csv"
        if instansi_count <= len(instansi_alfabet) :
            try :
                with open(filename, 'w', newline='', encoding='utf-8') as f:
                    fieldnames = ['pelapor', 'tanggal_masuk_laporan', 'judul_laporan', 'detail_keluhan', 'instansi']
                    writer = csv.DictWriter(f, fieldnames=fieldnames)
                    writer.writeheader()
                    for dat in text_content_list:
                        writer.writerow(dat)
            except Exception as e:
                        print("An error occurred:", e)
                        # Continue with code execution
                        pass
        break
        instansi_count += 1
        if instansi_count < len(instansi_alfabet) :
            driver.get(instasi_list[instansi_count])
            time.sleep(40)


with open('saved_data.pkl', 'wb') as file:
    # A new file will be created
    pickle.dump(text_content_list, file)
with open(filename, 'w', newline='', encoding='utf-8') as f:
    fieldnames = ['pelapor', 'tanggal_masuk_laporan','judul_laporan' , 'detail_keluhan','instansi']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for dat in text_content_list:
        writer.writerow(dat)

# Iterate over the 