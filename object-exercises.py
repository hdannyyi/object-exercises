class Person: 
    def __init__(self, name, email, phone, friends):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
    
    def add_friend(self, other_person):
        self.friends.append(other_person)

    def greet(self, other_person):
        print('Hello {}, I am {}!'.format(other_person.name, self.name))

    def print_contact_info(self):
        print('{}\'s email: {}, {}\'s phone number: {}'.format(self.name, self.email, self.name, self.phone) )
##1 Basics
sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948', [])
jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456', [])

sonny.greet(jordan)
jordan.greet(sonny)
print(sonny.email, sonny.phone)
print(jordan.email, jordan.phone)
sonny.print_contact_info()
jordan.add_friend(sonny)

##2 Make your own class
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def print_info(self):
        print('{} {} {}'.format(car.year, car.make, car.model))

car = Vehicle('Nissan', 'Leaf', '2015')
car.print_info()