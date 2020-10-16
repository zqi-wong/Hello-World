from car import Car

my_new_car = Car('audi','a4',2016) 
print(my_new_car.get_descriptive_name())
i = 0
while i<= 5:
    my_new_car.update_odometer()
    my_new_car.read_odometer()
    i = 1+i
