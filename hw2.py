current_year = 2021
class Person:
    '''Doctring'''
    __total_person = 0

    def __init__(self,birht_year, name , **kwargs ):
        Person.__total_person += 1
        self.__birth_year = birht_year
        self.__name = name
        self.language = kwargs.get('language')
        self.year = current_year - self.__birth_year

    def get_age(self):
        self.year = current_year - self.__birth_year
        if self.year > 0:
            print(f'Your age {self.year}')
        else:
            print(f'Your age {self.year}')

    def birthday(self, birth_year):
        self.__birth_year = birth_year
        if birth_year > current_year:
            print("Man, are you seriously? we are not future")
        elif birth_year < 2004:
            print("You have 18. You can smoking and driking for many time, while your liver not died:)")
        elif birth_year > 2004:
            print("You haven't 18 now")

    def get_name(self):
        return self.__name

    def change_name(self,name):
        self.__name = name

    def get_total_person(self):
        return Person.__total_person

    def talk(self):
        print("Hello, World!")

    def is_adult(self):
        year = current_year - self.__birth_year
        if year > 17:
            is_adult = True
            print(is_adult)
        else:
            is_adult = False
            print(is_adult)




class Teacher(Person):
    '''Docstring'''
    def talk(self):
        print("Greetings, I'm your teacher")
    def teach(self):
        print("Lesson started by Teacher")


p1 = Person(2004,'Islam',language='spanish')
p2 = Person(2003,'Esen',language='english')
p3 = Person(2006, 'Baatyr',language='russian')
p4 = Teacher(2024,'Bekbolsun',language='turkey')
p5 = Teacher(1999, 'Nurlan')
p6 = Teacher(1998, 'Darikha')
print(p1.get_total_person())
