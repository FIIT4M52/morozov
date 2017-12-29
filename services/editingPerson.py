from models.person import Person

#fetch person from database

person = Person()


def enter_person_data():
    for data in person.__dict__:
        person.__setattr__(data, input(f"Enter your {data}: "))
    
    person.crud() #UPDATE


enter_person_data()

#load person to database

# only for test
print("-/-/-/-//-/-/-/-/_test_/-/-/-/-//-/-/-/-")
print(person.name)