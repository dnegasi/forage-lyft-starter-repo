from abc import ABC

from car import Car
class Battery(Car):
      def needs_service(self):
        return True