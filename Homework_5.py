# Homework 5

#1
def pre_minimal(*args):
    s= [*args]
    s.sort()
    return(s[s.count(s[0])])

# print(pre_minimal(1,1,1,3,2,4,5))

#2

class Person:
    """ Class Description """
    def __init__(self, full_name = '', year = 2021):
        self.full_name = full_name
        self.year = year

        if ((self.full_name.find(' ') == -1) or (len(self.full_name.split())) < 2):
            raise NameError('Invalid name')

        import datetime
        now = datetime.datetime.now()
        if (now.year < self.year) or (self.year < 1900):
            raise NameError('Invalid year')

    def name_from_fn(self):
        return((self.full_name.split())[0])

    def surname_from_fn(self):
        return((self.full_name.split())[1])

    def age_in(self):
        import datetime
        now = datetime.datetime.now()
        return(now.year - self.year)

    def __str__(self):
        return f'Person object with Full name = {self.full_name} and Year = {self.year}'

#2.1
class Employee(Person):
    """ Class Description """
    def __init__(self, full_name = '', year = 2021, position = '', experience = None, salary = None):
        Person.__init__(self, full_name , year )
        self.experience = experience
        self.salary = salary
        self.position = position

        assert ((self.experience is None) or (self.experience > 0))\
               and ((self.salary is None) or (self.salary > 0)),\
            'Invalid value experience or salary'

    def experience_val(self):
        if self.experience < 3:
            return f'Junior {self.position}'
        if self.experience <= 6:
            return f'Middle {self.position}'
        if self.experience > 6:
            return f'Senior {self.position}'

    def increase_salary(self, increase=1):
        self.salary += increase
        return self.salary

    def __str__(self):
        return f'Employee object with Full name = {self.full_name} and Year = {self.year},' \
               f' position = {self.position}, experience = {self.experience}, ' \
               f'salary = {self.salary}'


class ITEmployee(Employee):
    """ Class Description """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.skill = []

    def add_skill(self, new_skill):
        self.skill.append(new_skill)

    def add_skills(self, *args):
        for a in args:
            args = str(args)
            self.skill.append(a)

    def __str__(self):
        return f'Employee object with Full name = {self.full_name} and Year = {self.year},' \
               f' position = {self.position}, experience = {self.experience}, ' \
               f'salary = {self.salary} skill = {self.skill}'


#3
class Rectangular:
    """  Class Description  """
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2

    def perimeter(self):
        return self.side1 * 2 + self.side2 *2

    def square(self):
        return self.side1 * self.side2

#3.2
class Student:
    def __init__(self, name ='', surame='', speciality='', start_year=None):
        self.name = name
        self.surname = surame
        self.speciality = speciality
        self.start_year = start_year
        self.score =[]
    def new_score(self, *args):
        for a in args:
            self.score.append(a)

    def average_score(self):
        sum = 0
        for a in self.score:
            sum += a
        midl = sum/(len(self.score))
        return (round(midl, 2))

    def year_in(self):
        import datetime
        now = datetime.datetime.now()
        return (now.year - self.start_year)

    def __str__(self):
        return f'Class Student: {self.name} {self.surname} {self.speciality} {self.start_year}, score: {self.score}'


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distanse_to_start(self):
        d = (self.x**2 + self.y**2)**0.5
        return d
    def distanse_to_other(self, other):
        d = ((self.x-other.x) ** 2 + (self.y-other.y) ** 2) ** 0.5
        return d
    def __str__(self):
        return f'class Point X:{self.x}, Y:{self.y}'


if __name__ == "__main__":
    # a = Point(3,4)
    # b = Point(3, 6)
    # print(Point.distanse_to_other(a,b))
    # print(a)
    # a = Student('Ivan','Ivanov', 'QA', 2018)
    # a.new_score(9, 10, 11, 10, 12, 8, 9)
    # print(a)



