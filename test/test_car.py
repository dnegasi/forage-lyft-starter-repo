import unittest
from datetime import datetime
import datetime

from engine.model.calliope import Calliope
from engine.model.glissade import Glissade
from engine.model.palindrome import Palindrome
from engine.model.rorschach import Rorschach
from engine.model.thovex import Thovex
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery


class TestCalliope(unittest.TestCase):
    def test_battery_needs_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
    def test_engine_should_be_serviced(self):    
        current_mileage = 30001
        last_service_mileage = 0

        capulet = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(capulet.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 29999
        last_service_mileage = 0

        capulet = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(capulet.needs_service())

    def test_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year = current_date.year -3)

        spindler = SpindlerBattery(last_service_date, current_date)
        self.assertTrue(spindler.needs_service())

    def test_battery_should_not_be_serviced(self):
        current_date = 0
        last_service_date = 0

        spindler = SpindlerBattery(last_service_date, current_date)
        self.assertFalse(spindler.needs_service())


class TestGlissade(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_mileage = 60001
        last_service_mileage = 0

        willoughby = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(willoughby.needs_service())

    def engine_should_not_be_serviced(self):
        current_mileage = 0
        last_service_mileage = 0

        willoughby = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(willoughby.needs_service())

    def test_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year =current_date.year -3)

        spindler = SpindlerBattery(last_service_date, current_date)
        self.assertTrue(spindler.needs_service())

    def test_battery_should_not_be_serviced(self):
        current_date = 0
        last_service_date = 0

        spindler = SpindlerBattery(last_service_date, current_date)
        self.assertFalse(spindler.needs_service())
        


class TestPalindrome(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        warning_light_is_on = True

        sternman = SternmanEngine(warning_light_is_on)
        self.assertTrue(sternman.needs_service())

    def test_engine_should_not_be_serviced(self):
        warning_light_is_on = False

        sternman = SternmanEngine(warning_light_is_on)
        self.assertFalse(sternman.needs_service())

    def test_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year = current_date.year -3)

        spindler = SpindlerBattery(current_date,last_service_date)
        self.assertTrue(spindler.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year -1)

        current_date = 0
        last_service_date = 0 

        spindler = SpindlerBattery(current_date, last_service_date)
        self.assertFalse(spindler.needs_service())


class TestRorschach(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_mileage = 60001
        last_service_mileage = 0

        willoughby = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(willoughby.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 0
        last_service_mileage = 0

        willoughby = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(willoughby.needs_service())


    def test_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year =current_date -5)

        spindler = SpindlerBattery(current_date,last_service_date)
        self.assertTrue(spindler.needs_service())

    def test_battery_should_not_be_serviced(self):
        current_date = 0
        last_service_date = 0

        nubbin = NubbinBattery(current_date,last_service_date)
        self.assertFalse(nubbin.needs_service())


class TestThovex(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_mileage = 30001
        last_service_mileage = 0

        capulet = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(capulet.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 29999
        last_service_mileage = 0

        capulet = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(capulet.needs_service())

    def test_battery_should_be_serviced(self):
        current_date =datetime.today().date()
        last_service_date = current_date.replace(year =current_date.year -5)
        

        nubbin = NubbinBattery(last_service_date, current_date)
        self.assertTrue(nubbin.needs_service())

    def test_battery_should_not_be_serviced(self):
        current_date = 0
        last_service_date = 0

        nubbin = NubbinBattery(last_service_date, current_date)
        self.assertFalse(car.needs_service())


if __name__ == '__main__':
    unittest.main()
