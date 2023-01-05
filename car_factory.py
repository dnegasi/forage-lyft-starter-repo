from abc import ABC

from car import Car
class CarFactory(Car):
    def create_calliope(self):
        current_date = ""
        last_service_date = ""
        current_mileage = 0
        last_service_mileage = 0
    def create_glissade(self):
        current_date = ""
        last_service_date = ""
        current_mileage = 0
        last_service = 0
    def create_pallindrome(self):
        current_date = ""
        last_service_date = ""
        warning_light_on = True        
    def create_rorschach(self):    
        current_date = ""
        last_service_date = ""
        current_mileage = 0
        last_service_mileage = 0
    def create_thovex(self):
        current_date = ""
        last_service_date = ""
        current_mileage = 0
        last_service_mileage =0    