"""
Same features: Name, Surname, Rabies Vaccine
Only for Dogs: DHLPP, Bordatella, Coronavirus, Lyme
Only for Cats: DRC, Chlamydia, FelineLeukemia)

too much to explain. i add output at the same file.
"""


class Animals:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        self.rabies = False
        
    def printClient(self):
        print("\nClient:", self.name, self.surname, "\nAge:", self.age)
    
class Dogs(Animals):
    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)
        self.dhlpp = False
        self.bordatella = False
        self.coronavirus = False
        self.lyme = False
        
    def vaccineHistory(self):
        print("\nVaccine History", "\nDHLPP:", self.dhlpp, "\nRabies:", self.rabies, "\nBordatella", self.bordatella, "\nCoronavirus:", self.coronavirus, "\nLyme:", self.lyme)

    def updateVaccine(self, DHLPP, Rabies, Bordatella, Coronavirus, Lyme):
        self.dhlpp = DHLPP
        self.rabies = Rabies
        self.bordatella = Bordatella
        self.coronavirus = Coronavirus
        self.lyme = Lyme
        super().printClient()
        print("\nUpdated Vaccine History", "\nDHLPP:", self.dhlpp, "\nRabies:", self.rabies, "\nBordatella", self.bordatella, "\nCoronavirus:", self.coronavirus, "\nLyme:", self.lyme)
        
        
        
class Cats(Animals):
    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)
        self.drc = False
        self.chlamydia = False
        self.felineLeukemia = False
        
    def vaccineHistory(self):
        print("\nVaccine History", "\nDRC:", self.drc, "\nRabies:", self.rabies, "\nChlamydia", self.chlamydia, "\nFeline Leukemia:", self.felineLeukemia) 
        
    def updateVaccine(self, DRC, Rabies, Chlamydia, FelineLeukemia):
        self.drc = DRC
        self.rabies = Rabies
        self.chlamydia = Chlamydia
        self.felineLeukemia = FelineLeukemia
        super().printClient()
        print("\nUpdated Vaccine History", "\nDRC:", self.drc, "\nRabies:", self.rabies, "\nChlamydia", self.chlamydia, "\nFeline Leukemia:", self.felineLeukemia) 
        
        
#----------Starts here-------------

vaccineDicDog = {
    "DHLPP" : False,
    "Rabies" : False,
    "Bordatella" : False,
    "Coronavirus" : False,
    "Lyme" : False
}

vaccineDicCat = {
    "DRC" : False,
    "Rabies" : False,
    "Chlamydia" : False,
    "FelineLeukemia" : False
}


animalType = str(input("Client's kind (dog/cat): "))
clientName = str(input("Client's Name: "))
clientSurname = str(input("Client's Surname: "))
clientAge = int(input("Client's Age: "))


if animalType.upper() == "DOG": 
    newClient = Dogs(clientName.capitalize(), clientSurname.capitalize(), clientAge)
    newClient.vaccineHistory()
    
    vaccineList = list(input("\n\nPlease enter the vaccinations made (for DHLPP(D), Rabies(R), Bordatella(B), Coronavirus(C), Lyme(L) put space between letters): ")) 
    
    for i in vaccineList:
        if i.upper() == "D":
            vaccineDicDog.update({"DHLPP": True})
        elif i.upper() == "R":
            vaccineDicDog.update({"Rabies": True})
        elif i.upper() == "B":
            vaccineDicDog.update({"Bordatella": True})
        elif i.upper() == "C":
            vaccineDicDog.update({"Coronavirus": True})
        elif i.upper() == "L":
            vaccineDicDog.update({"Lyme": True})
        elif i == " ":
            continue
        else:
            print("Wrong vaccine type")
        
    newClient.updateVaccine(**vaccineDicDog)
        
        
elif animalType.upper() == "CAT": 
    newClient = Cats(clientName.capitalize(), clientSurname.capitalize(), clientAge)
    newClient.vaccineHistory()
    
    vaccineList = list(input("Please enter the vaccinations made (for DRC(D), Rabies(R), Chlamydia(C), Feline Leukemia(F) put space between letters): ")) 
    
    for i in vaccineList:
        if i.upper() == "D":
            vaccineDicCat.update({"DRC": True})
        elif i.upper() == "R":
            vaccineDicCat.update({"Rabies": True})
        elif i.upper() == "C":
            vaccineDicCat.update({"Chlamydia": True})
        elif i.upper() == "F":
            vaccineDicCat.update({"FelineLeukemia" : True})
        elif i == " ":
            continue
        else:
            print("Wrong vaccine type")
    
    newClient.updateVaccine(**vaccineDicCat)
    
else:
    print("Wrong attempt..") 
