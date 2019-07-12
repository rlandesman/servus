#Begin testing with BS and requests
#TODO: Loop through attached text file and read each link individually
#TODO: Put failsafes on everything with try/catch

import requests
import time
from bs4 import BeautifulSoup as BS

contact_page_names = ["Impressum","impressum", "contact", "contact-us"]


print("Starting Script")
print("------------------------------")

url = ("https://www.scope-online.de/firma/alba-tooling---engineering-gmbh.htm")
page = requests.get(url)
time.sleep(0.5)
soup = BS(page.content, 'html.parser')
generalTable = soup.find(class_='companyPortAddressShell')
web_link = generalTable.a['href']

print("The link being followed (step 1): " + str(web_link))
str_web_link = str(web_link)
page = requests.get(str_web_link) #Now at the website level
time.sleep(0.25)
siteSoup = BS(page.content, 'html.parser')
impressumLink = (siteSoup.find_all('a', string=contact_page_names, href=True))
str_url = str(impressumLink[0].get('href'))

print("the link being followed(step 2): " + str_web_link + '/' + str_url)
impressumPage = requests.get(str_web_link + '/' + str_url) #Now at contact page
time.sleep(0.25)
impressumSoup = BS(page.content, 'html.parser')
