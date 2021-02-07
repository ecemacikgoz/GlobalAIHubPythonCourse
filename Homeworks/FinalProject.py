# I don't actually understand the way you ask the question but here I go.

class Employees:
  def __init__(self, name, surname, age, language = []):
    self.name = name
    self.surname = surname
    self.age = age
    self.language = language
        
  def addLanguage(self,newLang):
    print("Adding new language")
    self.language.append(newLang)

  def showLanguage(self):
    print(self.name, "can speak:")
    for l in self.language:
      print(l)


class Managers(Employees):
  def __init__(self, name, surname, age, language):
    super().__init__(name, surname, age, language)


def main():
  emp1 = Employees("Ayşe", "Sarıyer", 23, ["English", "German", "Turkish"])
  emp2 = Employees("Fatma", "Çakmak", 29, ["English", "Turkish"])
  emp3 = Managers("Hayriye", "Bölükoğlubaşı", 37, ["French", "Turkish", "English"])
  emp4 = Employees("Heidi", "Yılmaz", 42, ["English", "Turkish"])
  emp5 = Managers("Sabriye", "Pınar", 69, ["Turkish", "Spanish", "Italian"])
  emp6 = Employees("Meliha", "Kaplan", 35, ["English", "Turkish", "German"])

  dic = [emp1.name, emp2.name, emp3.name, emp4.name, emp5.name, emp6.name]

  whose = str(input("Enter the employee whose information you want to learn: "))

  if whose == emp1.name:
    emp1.showLanguage()
  elif whose == emp2.name:
    emp2.showLanguage()
  elif whose == emp3.name:
    emp3.showLanguage()
  elif whose == emp4.name:
    emp4.showLanguage()
  elif whose == emp5.name:
    emp5.showLanguage()
  elif whose == emp6.name:
    emp6.showLanguage()
  else:
    print("There is no employee under the name", whose)

main()
