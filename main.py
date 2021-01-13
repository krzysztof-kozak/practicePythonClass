from math import ceil
from copy import copy


class Person:
    def __init__(self, name, age):
        print("Pozdrowienia od konstruktora!")
        self.name = name
        self.age = age
        self.semester = 7
        self.address = None

    def set_address(self, address: object):
        self.address = address

    @property
    def hello(self):
        print("Hello!")

    def greet_user(self, user):
        print(f'Hello {user}')

    def intruduce_self(self):
        print(f'Hello, my name is {self.name} and I am {self.age} years old')

    def grow_older(self, number_of_years=1):
        self.age += number_of_years

    def get_age_in_months(self):
        return self.age * 12

    def get_study_year_info(self):
        return ceil(self.semester / 2)

class Address:
    def __init__(self, street_name, street_number, city, postal_code):
        self.street_name = street_name
        self.street_number = street_number
        self.city = city
        self.postal_code = postal_code

    def get_full_address(self):
        return (self.street_name, self.street_number, self.city, self.postal_code)


# Można, ale nie trzeba, nazywać swoje argumenty
# Dzięki nazywaniu argumentów można np. zmieniać ich kolejność (pog!)
some_house = Address(
    street_name='Roscoe', street_number=5, city='New York', postal_code=555)
dude = Person("Alfred", 79)

dude.intruduce_self()
dude.grow_older()
dude.intruduce_self()

my_age_in_months = dude.get_age_in_months()
my_study_year = dude.get_study_year_info()

print(my_age_in_months)
print(my_study_year)

dude.hello
another_dude = copy(dude)

another_dude.grow_older(50)
dude.intruduce_self()

# Można też stowrzyć odpowiednią właściwość obiektu pt. address oraz napisać metodę, która będzie wyznaczać ten adres, co w sumie teraz zrobię, a linijki poniżej zakomentuje.

# dude.address = some_house
# another_dude.address = some_house

print(dude.address)  # Homeless LOL!

dude_with_address = Person("Richard", 19)
dude_with_address.set_address(some_house)

print(dude_with_address.address.get_full_address()) # Not homeless!
