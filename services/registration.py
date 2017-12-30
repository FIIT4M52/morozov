from models.person import Person
import json
import os


class PersonService:
    lastPersonId = 0

    def createNewPerson(self, name, lastName, phone, login, password,calification):
        self.lastPersonId += 1
        person = Person(self.lastOrderId, name, lastName, phone, login, password, 0, "no eny role")
        jsonString = json.dumps(person)
        with open("Person" + str(person.id) + ".txt", "w") as text_file:
            text_file.write(jsonString)
        return person

    def getPersonById(self, personId):
        with open("Person" + str(personId) + ".txt", "r") as text_file:
            jsonString = text_file.read()
        return json.loads(jsonString)

    def savePerson(self, personId, person):
        jsonString = json.dumps(person)
        with open("Person" + str(personId) + ".txt", "w") as text_file:
            text_file.write(jsonString)

    def deletePerson(self, personId):
        with open("Person" + str(personId) + ".txt", "w") as text_file:
            os.remove(os.path.abspath(text_file.name))

    def enterPersonData(self, person):
        id = person.id
        for data in person.__dict__:
            person.__setattr__(data, input(f"Enter your {data}: "))
        self.savePerson(id, person)