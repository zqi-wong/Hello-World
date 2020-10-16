class Car():

    def __init__(self,make,model,year):

        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("this car has "+ str(self.odometer_reading) + 
        " miles on it.")

    def update_odometer(self):
        self.odometer_reading += int(input())
    