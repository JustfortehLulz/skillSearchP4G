import pymongo







######################################## Persona Data ########################################

## Persona
#connection
client = pymongo.MongoClient("mongodb+srv://<username>:<password>@cluster0.mrb1o.mongodb.net/Persona_Data?retryWrites=true&w=majority")
# database
db = client.Persona
# collection inside the database
collection = db.Persona_Data

Keys = ["Name\n","Arcana\n","Level\n","Strength\n","Magic\n","Endurance\n","Agility\n","Luck\n","Inherit\n","Reflects\n","Absorbs\n","Block\n","Resists\n","Weak\n"]
Skill = ["Skill\n","Cost\n","Effect\n","Level\n"]


pData = {}
count = 0
### creates text file
with open("PersonaData.txt") as f:
	for line in f:
		### skips over newline characters
		if(line != "\n"):
			if(line in Keys):
				### everytime Name shows up, pData is reset along with count, skill_count, skill_index
				if(line == "Name\n"):
					if(count != 0):
						pData.pop('_id',None)
						pData["Skills"].pop()
						print("FINAL: " + str(pData))
						#print(collection.insert_one(pData))
					count = 0
					skill_count = 0
					skill_index = 0
					### get ride of id after one insert

					pData.clear()
				### condition for Level to differentiate between Keys Level and Skill Level
				if(count < 14):
					pData[line[:-1]] = ""
			### sets empty list of dictionary 
			elif(line == "List of Skills\n"):
				pData["Skills"] = [{}]
			else:
				# sets data values in dictionary
				#print(count)
				#print("LINE: " + str(line))
				if(count == 0):
					pData["Name"] = line[:-1]
				elif(count == 1):
					pData["Strength"] = line[:-1]
				elif(count == 2):
					pData["Magic"] = line[:-1]
				elif(count == 3):
					pData["Endurance"] = line[:-1]
				elif(count == 4):
					pData["Agility"] = line[:-1]
				elif(count == 5):
					pData["Luck"] = line[:-1]
				elif(count == 6):
					pData["Arcana"] = line[:-1]
				elif(count == 7):
					pData["Level"] = line[:-1]
				elif(count == 8):
					pData["Inherit"] = line[:-1]
				elif(count == 9):
					pData["Reflects"] = line[:-1]
				elif(count == 10):
					pData["Absorbs"] = line[:-1]
				elif(count == 11):
					pData["Block"] = line[:-1]
				elif(count == 12):
					pData["Resists"] = line[:-1]
				elif(count == 13):
					pData["Weak"] = line[:-1]
				elif(count >= 14):
					### sets skill data in list of dictionaries
					if(line in Skill):
						if(line != "Level"):
							pData["Skills"][skill_index][line[:-1]] = ""
						else:
							pData["Skills"][skill_index]["Skill_"+line[:-1]] = ""
						skill_count = 0
					else:
						#### list of dictionaries
						if(skill_count == 0):
							pData["Skills"][skill_index]["Skill"] = line[:-1]
						elif(skill_count == 1):
							pData["Skills"][skill_index]["Cost"] = line[:-1]
						elif(skill_count == 2):
							pData["Skills"][skill_index]["Effect"] = line[:-1]
						elif(skill_count == 3):
							pData["Skills"][skill_index]["Skill_Level"] = line[:-1]
						skill_count += 1
						if(skill_count == 4):
							skill_count = 0
							skill_index += 1
							pData["Skills"].append({})
				count += 1
				#print(pData)

#for izanagi-no-okami
pData.pop('_id',None)
pData["Skills"].pop()
print("FINAL: " + str(pData))
print(collection.insert_one(pData))

client.close()

#####################################################################
############################# skills ################################


# connection
client = pymongo.MongoClient("mongodb+srv://JY:mdbx1critheal@cluster0.mrb1o.mongodb.net/Persona_Skills?retryWrites=true&w=majority")
#database
db = client.Persona
#collection inside the databse
collection = db.Persona_Skills



skills = {}
count = 0
with open("PersonaSkills.txt") as f:
	for line in f:
		print(line)
		if(line == "Skill\n" or line == "Effect\n" or line == "Power\n" or line == "Acc.\n" or line == "Crit.\n" or line == "Cost\n"):
			#print(line)
			if(line == "Skill\n"):
				skills.clear()
			if(line == "Acc.\n" or line == "Crit.\n"):
				skills[line[:-2]] = ""
			else:
				skills[line[:-1]] = ""
		else:
			if(line != "\n"):
				#print(skills)
				skills.pop('_id',None)
				lenD = len(skills)
				# print(len(skills))
				# print(skills)

				if(lenD == 6):
					#print(line)
					if(count == 0):
						skills["Skill"] = line[:-1]
					elif(count == 1):
						skills["Effect"] = line[:-1]
					elif(count == 2):
						skills["Power"] = line[:-1]
					elif(count == 3):
						skills["Acc"] = line[:-1]
					elif(count == 4):
						skills["Crit"] = line[:-1]
					elif(count == 5):
						skills["Cost"] = line[:-1]
					#..... for each count until its equal to lenD
					#print(skills)

					count += 1
					#print(count)
					if(count == lenD):
						print(skills)
						print(collection.insert_one(skills))
						count = 0
				elif(lenD == 5):
					if(count == 0):
						skills["Skill"] = line[:-1]
					elif(count == 1):
						skills["Effect"] = line[:-1]
					elif(count == 2):
						skills["Power"] = line[:-1]
					elif(count == 3):
						skills["Acc"] = line[:-1]
					elif(count == 4):
						skills["Cost"] = line[:-1]
					count += 1

					if(count == lenD):
						print(skills)
						print(collection.insert_one(skills))
						count = 0
				elif(lenD == 4):
					if(count == 0):
						skills["Skill"] = line[:-1]
					elif(count == 1):
						skills["Effect"] = line[:-1]
					elif(count == 2):
						skills["Power"] = line[:-1]
					elif(count == 3):
						skills["Cost"] = line[:-1]
					count += 1

					if(count == lenD):
						print(skills)
						print(collection.insert_one(skills))
						count = 0
				elif(lenD == 3):
					if(count == 0):
						skills["Skill"] = line[:-1]
					elif(count == 1):
						skills["Effect"] = line[:-1]
					elif(count == 2):
						skills["Cost"] = line[:-1]
					count += 1

					if(count == lenD):
						print(skills)
						print(collection.insert_one(skills))
						count = 0
				elif(lenD == 2):
					if(count == 0):
						skills["Skill"] = line[:-1]
					elif(count == 1):
						skills["Effect"] = line[:-1]
					count += 1
					if(count == lenD):
						print(skills)
						print(collection.insert_one(skills))
						count = 0


client.close()

#####################################################################
