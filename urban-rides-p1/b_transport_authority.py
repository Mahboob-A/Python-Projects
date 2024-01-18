
# 170124, Wednesday, 04.00 pm 

import random 
import string 
from time import sleep 
class TransportAuthority: 
    def __init__(self): 
        self.__licenceDb = {}


    def create_licence_helper(self): 
        upper_chrars = random.choices(string.ascii_uppercase, k=3)
        digits = random.randint(101, 999)
        dirving_licence = f"{upper_chrars[0]}{upper_chrars[1]}{digits}{upper_chrars[2]}"
        return dirving_licence 

    def driving_test(self, email): 

        if email in self.__licenceDb.keys(): 
            print(f'This email address {email} is already registered with us and the driver is a Licenced Driver. Please provide another email, or login to your account.')
            return False 

        score = random.randint(1, 101)
        if score >= 33: 
            while True: 
                dirving_licence = self.create_licence_helper()
                if dirving_licence not in self.__licenceDb.values(): 
                    break
            self.__licenceDb[email] = dirving_licence

            print(f'SUCCESS: You have passed the driving test! Your score is: {score}.')
            return dirving_licence
        else: 
            print(f'FAILED: You have failed the driving test. Your score is: {score}. You need minimum of 33 to pass the test!')
            return False 

    def validate_licence(self, licence): 
        if licence in self.__licenceDb.values(): 
            return True 
        return False 


    

transport_authority = TransportAuthority()

if __name__ == '__main__': 
    while True: 
        sleep(5)
        email  = random.choice(string.ascii_uppercase)
        email += '@gmail.com'
        print(email)
        transport_authority.driving_test(email)
        print()
