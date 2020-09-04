import tkinter as tk
import pymongo

### class for skills of persona
class pSkill:
	def __init__(self,name,description="",power="",accuracy="",critical="",cost=""):
		self.name = name
		self.descrip = description
		self.pwr = power
		self.acc = accuracy
		self.crit = critical
		self.cost = cost

	# finds the skill in the mongodb
	def findSkill(self):
		client = pymongo.MongoClient("mongodb+srv://<usernamne>:<password>@cluster0.mrb1o.mongodb.net/Persona_Skills?retryWrites=true&w=majority")
		db = client.Persona
		collection = db.Persona_Skills
		result = collection.find({"Skill":self.name})
		print(result)
		client.close()
		for doc in result:
			self.descrip = str(doc["Effect"])
			if("Power" in doc):
				self.pwr = str(doc["Power"])
			else:
				self.pwr = "N/A"
			if("Acc" in doc):
				self.acc = str(doc["Acc"])
			else:
				self.acc = "N/A"
			if("Crit" in doc):
				self.crit = str(doc["Crit"])
			else:
				self.crit = "N/A"
			if("Cost" in doc):
				self.cost = str(doc["Cost"])
			else:
				self.cost = "N/A"

	#prints the skill data into cmd
	def printSkill(self):
		print("NAME: "+str(self.name))
		print("EFFECT: " + str(self.descrip))
		print("POWER: " + str(self.pwr))
		print("ACCURACY: " + str(self.acc))
		print("CRITICAL CHANCE: " + str(self.crit))
		print("COST: " + str(self.cost))

### basic information of persona 
class Persona:
	def __init__(self,name="",level="",arcana=""):
		self.name = name
		self.level = level
		self.arcana = arcana

	### finds persona with matching skill from mongoDB
	def findPersona(self,skill):
		client = pymongo.MongoClient("mongodb+srv://<username>:<password>@cluster0.mrb1o.mongodb.net/Persona_Data?retryWrites=true&w=majority")
		db = client.Persona
		collection = db.Persona_Data
		result = collection.find({"Skills":{"$elemMatch":{"Skill":skill}}})

		client.close()
		return result

	### print out basic persona information
	def printPersona(self):
		print("NAME: " + str(self.name))
		print("LEVEL: " + str(self.level))
		print("ARCANA: " + str(self.arcana))


### change code below into a class
class gui:
	def __init__(self,master):
		self.master = master
		master.title("Wow very cool")

		self.master.geometry("1000x700")

		self.array = []

		self.greeting = tk.Label(self.master,text = "Enter Skill Name: ")
		self.greeting.grid(row = 0, column = 0)

		self.setLabels()

		self.skillTxtBox = tk.Entry(self.master)
		self.skillTxtBox.grid(row = 0,column=1)

		self.searchBtn = tk.Button(self.master,text="Search",command = self.search)
		self.searchBtn.grid(row = 0,column = 2)

		self.setChangeableLabels()

		self.pLabels = []
		self.leveltxt = []
		self.personatxt = []
		self.arcanatxt = []
		col = 2
		for i in range(4,32):
			self.lvl = tk.StringVar()
			self.lvl.set("")
			self.lol = tk.Label(self.master,textvariable=self.lvl)
			self.lol.grid(row=i,column=col)
			self.leveltxt.append(self.lvl)

			col += 1
			self.p = tk.StringVar()
			self.p.set("")
			self.lpl = tk.Label(self.master,textvariable=self.p)
			
			labelNum = len(self.pLabels)
			self.lpl.bind("<Button-1>",lambda event, labelNum = i-4: self.newWindow(labelNum))
			self.lpl.bind("<Enter>",lambda event, labelNum = i-4: self.red_text(labelNum))
			self.lpl.bind("<Leave>",lambda event, labelNum = i-4: self.black_text(labelNum))

			self.pLabels.append(self.lpl)
			self.lpl.grid(row = i,column = col)
			self.personatxt.append(self.p)

			col += 1
			self.a = tk.StringVar()
			self.a.set("")
			self.lal = tk.Label(self.master,textvariable=self.a)
			self.lal.grid(row = i,column = col)
			self.arcanatxt.append(self.a)

			if(col == 4):
				col = 2

	### creates new window when clicking on a Persona name
	def newWindow(self,labelNum):
		### when you click on it it shows the persona data

		pName = str(self.personatxt[labelNum].get())
		if(pName != ""):
			print(pName)

			window = tk.Toplevel(self.master)
			window.geometry("1000x700")
			
			res = self.getPersonaData(pName)

			for doc in res:

				nameVal = tk.Label(window,text = pName)
				nameVal.grid(row = 0, column = 0)

				arcanaLabel = tk.Label(window,text = "Arcana")
				arcanaLabel.grid(row = 0,column = 1)

				arcanaVal = tk.Label(window,text = str(doc["Arcana"]))
				arcanaVal.grid(row = 1,column = 1)

				lvlLabel = tk.Label(window,text = "Level")
				lvlLabel.grid(row = 0,column=2)

				lvlVal = tk.Label(window,text = str(doc["Level"]))
				lvlVal.grid(row = 1 , column = 2)

				strLbl = tk.Label(window,text = "Strength")
				strLbl.grid(row = 2,column = 0)

				strVal = tk.Label(window,text = str(doc["Strength"]))
				strVal.grid(row = 2, column = 1)

				mgLbl = tk.Label(window,text = "Magic")
				mgLbl.grid(row = 3,column = 0)

				magVal = tk.Label(window,text = str(doc["Magic"]))
				magVal.grid(row = 3,column = 1)

				endLbl = tk.Label(window,text = "Endurance")
				endLbl.grid(row = 4,column = 0)

				endVal = tk.Label(window,text = str(doc["Endurance"]))
				endVal.grid(row = 4,column = 1)

				agLbl = tk.Label(window,text = "Agility")
				agLbl.grid(row = 5, column = 0)

				agVal = tk.Label(window,text = str(doc["Agility"]))
				agVal.grid(row = 5,column = 1)

				lkVal = tk.Label(window,text = "Luck")
				lkVal.grid(row = 6,column = 0)

				lkVal = tk.Label(window,text = str(doc["Luck"]))
				lkVal.grid(row = 6, column = 1)

				inherLbl = tk.Label(window,text = "Inherit")
				inherLbl.grid(row = 7, column = 0)

				inheritVal = tk.Label(window, text = str(doc["Inherit"]))
				inheritVal.grid(row = 8, column = 0)

				refLbl = tk.Label(window, text = "Reflects")
				refLbl.grid(row = 7, column = 1)

				reflectVal = tk.Label(window, text = str(doc["Reflects"]))
				reflectVal.grid(row = 8, column = 1)

				abLbl = tk.Label(window,text = "Absorbs")
				abLbl.grid(row = 7, column = 2)

				absorbVal = tk.Label(window,text = str(doc["Absorbs"]))
				absorbVal.grid(row = 8, column = 2)

				blkLbl = tk.Label(window,text = "Block")
				blkLbl.grid(row = 7, column = 3)

				blkVal = tk.Label(window,text = str(doc["Block"]))
				blkVal.grid(row = 8, column = 3)

				resLbl = tk.Label(window, text = "Resists")
				resLbl.grid(row = 7, column = 4)

				resVal = tk.Label(window, text = str(doc["Resists"]))
				resVal.grid(row = 8, column = 4)

				wkLbl = tk.Label(window, text = "Weak")
				wkLbl.grid(row = 7, column = 5)

				wkVal = tk.Label(window,text = str(doc["Weak"]))
				wkVal.grid(row=8,column =5)

				sLabels = ["Skill","Cost","Effect","Skill_Level"]

				skillLbl = tk.Label(window,text = sLabels[0])
				skillLbl.grid(row = 9, column = 0)

				cstLbl = tk.Label(window,text = sLabels[1])
				cstLbl.grid(row = 9,column = 3)

				effLbl = tk.Label(window,text = sLabels[2])
				effLbl.grid(row = 9, column = 2)

				slvlLbl = tk.Label(window, text = sLabels[3])
				slvlLbl.grid(row = 9,column =4)

				for i in range(len(doc["Skills"])):
					skillVal = tk.Label(window,text = str(doc["Skills"][i]["Skill"]))
					skillVal.grid(row = 10+i,column = 0)

					effVal = tk.Label(window,text = str(doc["Skills"][i]["Effect"]))
					effVal.grid(row = 10+i,column = 2)

					cstVal = tk.Label(window,text = str(doc["Skills"][i]["Cost"]))
					cstVal.grid(row = 10+i,column = 3)

					lvlVal = tk.Label(window,text = str(doc["Skills"][i]["Skill_Level"]))
					lvlVal.grid(row = 10+i,column = 4) 

			window.mainloop()

	### grabs persona data from MongoDB
	def getPersonaData(self,name):
		client = pymongo.MongoClient("mongodb+srv://<username>:<password>@cluster0.mrb1o.mongodb.net/Persona_Data?retryWrites=true&w=majority")
		db = client.Persona
		collection = db.Persona_Data
		res = collection.find({"Name":name})
		client.close()
		return res

	### hover text changes colour to red
	def red_text(self,labelNum):
		self.pLabels[labelNum].config(fg="red")

	### hover away text changes colour to black
	def black_text(self,labelNum):
		self.pLabels[labelNum].config(fg="black")

	### intializes the StringVars that will be changed after searching for a skill
	def setChangeableLabels(self):
		self.sName = tk.StringVar()
		self.sName.set("")
		self.resName = tk.Label(self.master,textvariable=self.sName)
		self.resName.grid(row=2,column=0)

		self.desc = tk.StringVar()
		self.desc.set("")
		self.descLabel = tk.Label(self.master,textvariable=self.desc)
		self.descLabel.grid(row =2, column = 1)

		self.pwrtxt = tk.StringVar()
		self.pwrtxt.set("")
		self.pwrLabel = tk.Label(self.master,textvariable=self.pwrtxt)
		self.pwrLabel.grid(row=2,column=2)

		self.acctxt = tk.StringVar()
		self.acctxt.set("")
		self.accLabel = tk.Label(self.master,textvariable=self.acctxt)
		self.accLabel.grid(row=2,column=3)

		self.crittxt = tk.StringVar()
		self.crittxt.set("")
		self.critLabel = tk.Label(self.master,textvariable=self.crittxt)
		self.critLabel.grid(row=2,column=4)

		self.costtxt = tk.StringVar()
		self.costtxt.set("")
		self.costLabel = tk.Label(self.master,textvariable=self.costtxt)
		self.costLabel.grid(row=2,column=5)


	### sets the initial labels that wont be changed in the gui
	def setLabels(self):
		name = tk.Label(self.master,text="Name")
		name.grid(row=1,column=0)

		descrip = tk.Label(self.master,text="Description")
		descrip.grid(row=1,column=1)

		power = tk.Label(self.master, text = "Power")
		power.grid(row = 1,column = 2)

		acc = tk.Label(self.master, text = "Accuracy")
		acc.grid(row = 1,column = 3)

		crit = tk.Label(self.master, text = "Critical Chance")
		crit.grid(row=1,column =4)

		cost = tk.Label(self.master,text="Cost")
		cost.grid(row=1,column=5)

		lvl = tk.Label(self.master,text = "Level")
		lvl.grid(row = 3,column = 2)

		persona = tk.Label(self.master,text = "Persona")
		persona.grid(row = 3,column = 3)

		arcana = tk.Label(self.master,text = "Arcana")
		arcana.grid(row = 3,column = 4)

	### performs the search for the skill and the search of Persona's that have the skill
	def search(self):
		self.searchSkill()
		self.searchPersona()


	### finds the data of the skill in the database
	def searchSkill(self):

		skill = self.skillTxtBox.get()

		nameSkill = self.parseSkill(skill)

		print(nameSkill)

		lol = pSkill(nameSkill)

		lol.findSkill()


		self.displaySkill(lol)

	### displays the skill data onto the gui
	def displaySkill(self,skill: pSkill):
		self.sName.set(str(skill.name))

		self.desc.set(str(skill.descrip))

		self.pwrtxt.set(str(skill.pwr))

		self.acctxt.set(str(skill.acc))

		self.crittxt.set(str(skill.crit))

		self.costtxt.set(str(skill.cost))

	### find Persona from database
	def searchPersona(self):
		skill = self.skillTxtBox.get()

		nameSkill = self.parseSkill(skill)

		lol = Persona()
		cur = lol.findPersona(nameSkill)

		for doc in cur:
			lol.name = str(doc["Name"])
			lol.level = str(doc["Level"])
			lol.arcana = str(doc["Arcana"])
			lol.printPersona()
			self.array.append(lol)
			lol = Persona()
		
		self.displayPersona()

	### displays Persona data 
	def displayPersona(self):

		for i in range(len(self.array)):
			self.leveltxt[i].set(str(self.array[i].level))
			self.personatxt[i].set(str(self.array[i].name))
			self.arcanatxt[i].set(str(self.array[i].arcana))

		for k in range(len(self.array),len(self.leveltxt)):
			self.leveltxt[k].set("")
			self.personatxt[k].set("")
			self.arcanatxt[k].set("")

		self.array.clear()

	### parses the skill into readable text
	def parseSkill(self,skill):
		### for spaces
		spacePos = skill.find(" ")
		if(spacePos == -1):
			nameSkill = skill[0].upper() + skill[1:].lower()
		else:
			nameSkill = skill[0].upper() + skill[1:spacePos].lower()+" "+skill[spacePos+1].upper()+skill[spacePos+2:].lower()

		spacePos2 = skill.find(" ",spacePos+2,-1)
		print(spacePos2)
		if(spacePos != -1):
			nameSkill = nameSkill[0:spacePos2] + " " + skill[spacePos2+1].upper()+skill[spacePos2+2:].lower()
			### list of words that are not capatilize
			# of, For, Man's, to 
			specialCase = ["Of", "To"]
			if(nameSkill[spacePos+1:spacePos2] in specialCase):
				nameSkill = skill[0].upper() + skill[1:spacePos].lower() + " " + skill[spacePos+1:spacePos2].lower()+ " " + skill[spacePos2+1].upper()+skill[spacePos2+2:].lower()
			print(nameSkill[spacePos+1:spacePos2])

		print("Parse Skill: " + str(nameSkill))

		### for -
		dashPos = skill.find("-")
		if(dashPos != -1):
			nameSkill = skill[0].upper() + skill[1:dashPos].lower() +"-" + skill[dashPos+1].upper() + skill[dashPos+2:].lower()

		return nameSkill


root = tk.Tk()
gui = gui(root)
root.mainloop()
