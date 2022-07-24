#Task 1 - Motorbike
from datetime import datetime

moterbike_value = 2000

def bike_depreceation(bike_value):
    '''
    This function calculates the value of a bike per year until it's value if £1000.
    It does this by taking the initial value of a bike then reducing the value by
    10% per year.
    
    :param bike_value: int - the inital value of the bike.
    
    Prints the value of the bike each year until it is worth £1,000.
    '''

    while bike_value > 1000:
        print(round(bike_value, 2))
        bike_value *= 0.9
  
bike_depreceation(moterbike_value)

#Expanding the above to make it a method of a bike object

class MotorBikes:
    '''
    Attributes
    ----------
    (class)total_motorbikes_created: int
    name: str - the name of the bike
    make: str - the make of the bike
    model_year: int - the year the bike was made
    model_type: str - the model of the bike
    production_value: int - the value of the bike when it was made

    Methods
    -------
    current_value(): calculates the current value of the Motorbike by depreciating
    the production value of the bike by 10% per year since the bike was produced.
    '''

    total_motorbikes_create = 0

    def __init__(self, name, make, model_year, model_type, production_value):
        self.name = name
        self.make = make
        self.model_year = model_year
        self.model_type = model_type
        self.production_value = production_value
        MotorBikes.total_motorbikes_create += 1

    def current_value(self):
        '''
        This function determines the current value of the bike based on the current year.
        '''
        bike_age = datetime.today().year - self.model_year
        current_value = self.production_value
        print(self.name, 'is', bike_age, 'years old.')
        while bike_age > 0:
            current_value *= 0.9
            bike_age -= 1

        return f'The current value of {self.name} is £{round(current_value, 2)}'

bens_bike = MotorBikes('Ben\'s Bike', 'Kawasaki', 2005 ,'Ninja 1000', 15000)

bens_bike.current_value()
