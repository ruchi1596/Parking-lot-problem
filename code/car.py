class Car(object):
    """
    This is class which represents details of a car.
   
    reg = Car Registration Number
    age = Age of Driver 

    """

    def __init__(self):
        self._reg = None
        self._age = None

    @property
    def reg(self):
        return self._reg

    @reg.setter
    def reg(self, value):
        self._reg = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value

    @classmethod
    def create(cls, reg, age):
        car_obj = cls()
        car_obj.reg = reg
        car_obj.age = age
        return car_obj
