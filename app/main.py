class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people.update({self.name: self})


def create_person_list(people: list) -> list:
    for person in people:
        Person(person["name"], person["age"])

    for person in people:
        new_person = Person.people[person["name"]]
        if "wife" in person and person["wife"]:
            new_person.wife = Person.people.get(person["wife"])
        if "husband" in person and person["husband"]:
            new_person.husband = Person.people.get(person["husband"])

    return list(Person.people.values())