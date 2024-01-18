
# 180124, Thursday, 02.30 pm 

class RideManager: 
    def __init__(self): 
        self.__availableCars = []
        self.__availableBikes = []
        self.__availableCngs = []
    

    def get_available_cars(self):
        return self.__availableCars

    def handle_vehicle_assignment(self, car, rider, vehicle_type, rider_destination): 
        print(f'SUCCESS: Nearby car found!')

        rider_driver_distance = abs(rider_destination - car.driver.location)

        # within > 20 and <= 30 | reject the car find request by driver 
        if rider_driver_distance > 20:
            print(f'REJECTED: DRIVER: {car.driver.name}. CAR: {car.vehicle_name} rejected your request!')
            print('Searching other nearby cars!\n')
            return False 

        if rider_driver_distance <= 20:
            print(f'ACCEPTED: CAR: {car.vehicle_name}. DRIVER: {car.driver.name} accepted your request!')
            print(f'DRIVER: {car.driver.name} is at location: {car.driver.location}. He is {rider_driver_distance} km. away from you!')
            estimated_time = ''
            if rider_driver_distance <= 5:
                estimated_time = 'Within 5 minutes'
            elif rider_driver_distance > 5 and rider_driver_distance <= 10: 
                estimated_time = 'Within 10 minutes'
            elif rider_driver_distance > 10 and rider_driver_distance <= 15: 
                estimated_time = 'Within 15 minutes'
            else: 
                estimated_time = 'Within 20 minutes'
    
            print(f"ESTIMATED TIME: The driver is likely to reach to your location: {rider_destination} from driver's location: {car.driver.location} - {estimated_time}\n")
            return True         
    

    def find_a_vehicle(self, rider, vehicle_type, rider_destination):
        if vehicle_type == 'car': 
            if len(self.__availableCars) == 0:
                print(f"INCONVENIENCE: This CAR vehicle type is not availavle at this time!")
                return False 

            vehicle_found = False 
            for car in self.__availableCars: 
                if abs(rider_destination - car.driver.location) <= 30:
                    result = self.handle_vehicle_assignment(car=car, rider=rider, vehicle_type=vehicle_type, rider_destination=rider_destination)
                    if result: 
                        vehicle_found = True 
                        break
                    else: 
                        continue # the rider might have rejected the ride | continue other nearby cars 
            
            if not vehicle_found: 
                print(f"INCONVENIENCE: No nearby 'CAR' vehicle type is available at this time at your location: {rider_destination}!\n")
                
                


    def add_a_vehicle(self, vehicle_type, vehicle, driver_name): # vehicle = vehicle object 
        if vehicle_type == 'car': 
            self.__availableCars.append(vehicle)
        elif vehicle_type == 'bike': 
            self.__availableBikes.append(vehicle)
        else: 
            self.__availableCngs.append(vehicle)
        print(f'Driver Name: {driver_name}. Email: {vehicle.driver.email}. {vehicle_type.title()}: {vehicle.vehicle_name} - successfully added to the central registry!')



ride_manager = RideManager()