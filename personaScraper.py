import pprint
import pymongo
from bs4 import BeautifulSoup
import requests


def PersonaData(link):
	personaLink = "https://megamitensei.fandom.com" + link
	print(personaLink)
	pData = requests.get(personaLink, headers = headers)
	soup = BeautifulSoup(pData.content, 'html.parser')
	#print(soup.prettify())
	f = open("PeronsaData.txt","a")
	title = soup.find("h1", {"class": "page-header__title"})

	print(title.get_text())

	f.write("Name\n")

	f.write(str(title.get_text()) + "\n")


	tabExist = soup.find("div", {"title" : "Golden"})

	
	### find out if that tab exists
	if(tabExist != None):
		### Golden tab does not repeat twice
		for elem in tabExist.find_all("table", {"class":"customtable"}):
			rows = elem.findChildren("tr")
			for r in rows:
				line = str(r.get_text().strip())
				print(line)
				f.write(line+"\n")
	else:
		data = soup.find("table" , attrs={"style":"margin: 0 auto; min-width:650px;text-align:center; background: #222; border:2px solid #FFE600; border-radius:10px; font-size:75%; font-family:verdana;"})
		rows = data.findChild(["tr"])
		for r in rows.find_all("td"):
			line = str(r.get_text().strip())
			print(line)
			f.write(line+"\n")
			break
	f.close()
			
	




######################################## MONGODB STUFF ########################################
# client = pymongo.MongoClient("mongodb+srv://JY:mdbx1critheal@cluster0.mrb1o.mongodb.net/Persona_Data?retryWrites=true&w=majority")
# db = client.admin


# client.close()

######################################## MONGODB STUFF ########################################

################# scraper ###################

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'}

p4skills = "https://megamitensei.fandom.com/wiki/List_of_Persona_4_Skills"

skillPage = requests.get(p4skills,headers = headers)
soup = BeautifulSoup(skillPage.content, 'html.parser')

f = open("PersonaSkills.txt","a")
printing = True

for elem in soup.find_all("table", {"class": "table p4"}):
	rows = elem.findChildren("tr")
	for r in rows:
		if(printing):
			print(r.get_text())
			f.write(r.get_text())
		if("Spirit Leech" in r.get_text()):
			break
		if("Analysis" in r.get_text()):
			printing = False
		if("Complete Analysis" in r.get_text()):
			printing = True
	print()

f.close()


################################################################## skills ok

personaList = "https://megamitensei.fandom.com/wiki/List_of_Persona_4_Personas"
personaPage = requests.get(personaList, headers = headers)

# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get(personaList)

print("*"*32 +"PERSONA LIST" + "*"*32)

soup = BeautifulSoup(personaPage.content, 'html.parser')

#print(soup)

for elem in soup.find_all("table", {"class" : "table p4"}):
	rows = elem.findChildren(['th','tr'])
	for r in rows:
		cells = r.findChildren('td')
		for c in cells:
			findLink = c.find("a")
			link = findLink['href']
			PersonaData(link)
		print()

