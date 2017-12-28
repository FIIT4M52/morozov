from models.person import Person
import json
import os


class PersonService:
    lastPersonId = 0

    def createNewPerson(self, name, lastName, phone, login, password,calification):                      
        self.lastPersonId += 1
        person = Person(self.lastOrderId, name, lastName, phone, login, password,calification)
        jsonString = json.dumps(person)
        with open("Person" + str(person.id) + ".txt", "w") as text_file:
            text_file.write(jsonString)
        return person
