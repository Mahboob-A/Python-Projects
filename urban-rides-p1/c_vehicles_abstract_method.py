
# 170124, Wednesday, 04.00 pm 

# abstract classes for vehicles 

from abc import ABC, abstractmethod


class Vehicle(ABC): 

    vehicle_base_speeds = {
        'car' : 60, 
        'bike' : 45, 
        'cng' : 25
    }

    vehicle_status = {
        'available' : 'available', 
        'occupied' : 'occupied', 
        'running' : 'running'
    }

    def __init__(self, vehicle_type, vehicle_name, number_plate, base_fare_rate, driver): 
        self.vehicle_type = vehicle_type 
        self.vehicle_name = vehicle_name
        self.number_plate = number_plate 
        self.base_fare_rate = base_fare_rate
        self.driver = driver  # driver object 
        self.car_base_speed = self.vehicle_base_speeds[vehicle_type]
        self.driver_licence = None
        self.status = 'available'

    @abstractmethod
    def start_driving(self): 
        pass 

    @abstractmethod
    def trip_finished(self): 
        pass 

    


class Car(Vehicle): 
    def __init__(self, vehicle_type, vehicle_name, number_plate, base_fare_rate, driver): 
        super().__init__(vehicle_type, vehicle_name, number_plate, base_fare_rate, driver)

    def start_driving(self): 
        self.status = 'unavailable' 
        print(f'{self.vehicle_type}: {self.vehicle_name} started!')
    
    def trip_finished(self): 
        self.status = 'available' 
        print(f'{self.vehicle_type}: {self.vehicle_name} trip finished!')



class Bike(Vehicle): 
    def __init__(self, vehicle_type, vehicle_name, number_plate, base_fare_rate, driver): 
        super().__init__(vehicle_type, vehicle_name, number_plate, base_fare_rate, driver)

    def start_driving(self): 
        self.status = 'unavailable' 
        print(f'{self.vehicle_type}: {self.vehicle_name} started!')
    
    def trip_finished(self): 
        self.status = 'available' 
        print(f'{self.vehicle_type}: {self.vehicle_name} trip finished!')



class Cng(Vehicle): 
    def __init__(self, vehicle_type, vehicle_name, number_plate, base_fare_rate, driver): 
        super().__init__(vehicle_type, vehicle_name, number_plate, base_fare_rate, driver)

    def start_driving(self): 
        self.status = 'unavailable' 
        print(f'{self.vehicle_type}: {self.vehicle_name} started!')
    
    def trip_finished(self): 
        self.status = 'available' 
        print(f'{self.vehicle_type}: {self.vehicle_name} trip finished!')
