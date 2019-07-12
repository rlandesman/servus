#Begin testing with beautifulsoup and requests
#TODO: Loop through attached text file and read each link individually

import requests
from bs4 import BeautifulSoup

print("Starting Script")
print("-------------------------------\n")


url = ("https://www.scope-online.de/firma/ab-anlagenplanung-gmbh.htm")
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

generalTable = soup.find(class_='companyPortAddressShell')
web_link = generalTable.a['href']

print("The link being followed (step 1): " + str(web_link))
