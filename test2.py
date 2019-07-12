from bs4 import BeautifulSoup as BS
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import requests

url1 = 'https://www.scope-online.de/firma/ab-anlagenplanung-gmbh.htm'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'}

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url1) #At the SCOPE level now

soup = BS(driver.page_source, 'html.parser')
generalTable = soup.find(class_='companyPortAddressShell')
url2 = generalTable.a['href']

response = requests.get(url2 + '?showEmail=true', headers=headers)
alpha_soup = BS(response.text, 'html.parser')



"""
companylist = ['Blue Yonder']

error = []
for company in companylist:
    inputElement = driver.find_element_by_id("searchPhrase0")
    inputElement.clear()
    inputElement.send_keys(company)
    inputElement.submit()

    soup = BS(driver.page_source, 'html.parser')

    link = soup.find('span',{'class':'company--name'})
    a_link = link.find('a')['href']

    response = requests.get('https://www.firmenwissen.de' + a_link + '?showEmail=true', headers=headers)
    alpha_soup = BS(response.text, 'html.parser')


    try:
        phone = alpha_soup.find('span', {'class':'yp_phoneNumber'}).text.strip()
    except:
        phone = ''

    try:
        email = alpha_soup.find('span', {'class':'yp_email'}).text.strip()
    except:
        email = ''

    try:
        website = alpha_soup.find('span', {'class':'yp_website'}).text.strip()
    except:
        webiste = ''

    try:
        contact = soup.find('div', {'class':'company--info'})
        address = contact.find_all('p')[-1].text.strip()
    except:
        print ('Could not locate %s company info' %(company))
        error.append(company)

    print('%s\n%s\n%s\n%s\n' %(address, phone, email, website))
"""
