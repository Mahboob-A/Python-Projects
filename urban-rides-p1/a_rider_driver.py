
# 16-2 Create User with password verification
# 150124, Tuesday, 05.30 pm 

import hashlib 
import random

from b_transport_authority import transport_authority
from c_vehicles_abstract_method import Car, Bike, Cng
from d_ride_manager import ride_manager
from string import ascii_uppercase, ascii_lowercase


class User: 
    ''' Base class for Rider and Driver for Urban Rides App '''

    def __init__(self, name, email, password, location): 
        self.name = name 
        self.email = email.lower()
        self.location = location
        self.hashed_password = hashlib.md5(password.encode()).hexdigest()

        if not self.user_exists(): 
            with open('/home/ubuntu/myvscode/py-oop-recap/urban-rides-p1/users.txt', 'a') as f: 
                f.write(f"{self.email} {self.hashed_password}\n")
            f.close()
            print(f'USER Type: {self.__class__.__name__}. Name: {self.name} is created!\n')
        else: 
            print(f'ERR: USER Type: {self.__class__.__name__} Name: {self.name} already exists!\n')

    def set_location(self, location): 
        self.location = location 

    def get_location(self): 
        return self.location

    def user_exists(self): 
        '''Method to check if same user with same email already exists '''
        with open('/home/ubuntu/myvscode/py-oop-recap/urban-rides-p1/users.txt', 'r') as f:
            lines = f.readlines()
            for line in lines: 
                if self.email in line: 
                    return True 
            return False 
            

    @staticmethod
    def login(user_email, password):         
        stored_password_hash = ''

        with open('/home/ubuntu/myvscode/py-oop-recap/urban-rides-p1/users.txt', 'r') as f:
            lines = f.readlines()
            user_email = user_email.lower()
            for line in lines: 
                if user_email in line: 
                    stored_password_hash = line.split(' ')[1].strip()  # delete any leading or trailing whitespaces 
                    break
        f.close()

        provided_password_hash = hashlib.md5(password.encode()).hexdigest()

        if stored_password_hash == provided_password_hash: 
            print('user is valid')
        else: 
            print('user is not valid')


class Rider(User): 
    def __init__(self, balance, name, email, password, location): 
        super().__init__(name=name, email=email, password=password, location=location)
        self.balance = balance 


    def request_trip(self, destination): 
        pass 

    def start_a_trip(self, fare, destination): 
        pass 



class Driver(User): 
    def __init__(self, name, email, password, location): 
        super().__init__(name=name, email=email, password=password, location=location)
        self.licence = None 
        self.valid_driver = False 
        self.earnings = 0 
        self.driver_vehicle_type = ''
    
    def take_driving_test(self): 
        # driving test from Transport Authority. Result is published in the Transport Authority. 
        result = transport_authority.driving_test(self.email)
        if result is not False: # a dirving_licence value is reutrned 
            self.licence = result # add the licence 
            self.valid_driver = True 
            print(f'Your licence number is: {self.licence}')
            print('You can now add your vehicle in ProRide!\n')
        else: 
            print('Please try again!\n') 

    def register_a_vehicle(self, vehicle_type, vehicle_name, number_plate, rate): 
        if self.valid_driver: 
            new_vehicle = None 
            if vehicle_type == 'car': 
                new_vehicle = Car(vehicle_type=vehicle_type, vehicle_name=vehicle_name, number_plate=number_plate, base_fare_rate=rate, driver=self)
            elif vehicle_type == 'bike': 
                new_vehicle = Bike(vehicle_type=vehicle_type, vehicle_name=vehicle_name, number_plate=number_plate, base_fare_rate=rate, driver=self)
            elif vehicle_type == 'cng': 
                new_vehicle = Cng(vehicle_type=vehicle_type, vehicle_name=vehicle_name, number_plate=number_plate, base_fare_rate=rate, driver=self)
            else: 
                print(f"'{vehicle_type}' is not a valid vehicle in ProRide. Please register with either Car, Bike or Cng.\n")

            if new_vehicle: 
                # add the driver licence to the vehicle 
                new_vehicle.driver_licence = self.licence

                # add the vehicle type to driver object 
                self.driver_vehicle_type = vehicle_type 

                # add the vehicle to central regisry 
                ride_manager.add_a_vehicle(vehicle_type=vehicle_type, vehicle=new_vehicle, driver_name=self.name)
                print('You will be able to accept ride based on availability!\n')
        else: 
            print(f'Driver: {self.name} with email {self.email} is not a Licenced Driver. Please Take Driving Test before adding your vehicle in ProRide.\n')


    def start_a_trip(self, fare, destination): 
        self.earnings += fare 
        self.location = destination 





if __name__ == '__main__': 
    #tom = User('Tom', 'tom@gmail.com', 'iamtom', 'Kharibona')
    #jerry = User('Jerry', 'jerry@gmail.com', 'iamjerry', 'Rng')

    #User.login('jerry@gmail.com', 'iamjerry')

    rider1 = Rider(balance=random.randint(101, 501), name=random.choice(ascii_uppercase), 
            email=random.choice(ascii_lowercase)+'@gmail.com', password='123', location=random.randint(10, 30)
    )
    #print(dir(rider1))

    driver1 = Driver(name=random.choice(ascii_uppercase), 
            email=random.choice(ascii_lowercase)+'@gmail.com', password='123', location=random.randint(10, 300)
    )
    driver1.take_driving_test()
    driver1.register_a_vehicle('car', 'Tata Nixon', 'ABC123', 50)

    ride_manager.find_a_vehicle(rider=rider1, vehicle_type='car', rider_destination=10)
    
    #print(ride_manager.get_available_cars())






