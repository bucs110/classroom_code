import time

class Animal:
	cid = 0
	def __init__(self, pname, ptype="dog"):
		self.name = pname
		self.type = ptype
		self.arrival_date = time.strftime("%m/%d/%Y")
		self.did = id(self)
		Animal.cid += 1
		self.adopted = "N/A"

	def adopt(self):
		self.adopted = time.strftime("%m/%d/%Y")
		return self.did

	def __str__(self):
		mystr = "Name: " + self.name
		mystr += "\nType: " + self.type
		mystr += "\nArrived: " + self.arrival_date
		mystr += "\nAdopted: " + self.adopted
		mystr += "\nID: " + str(self.did)
		return mystr
