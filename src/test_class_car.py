import unittest
from src.car import Car, FuelOverflowError, NotEnoughFuelError

class TestCase(unittest.TestCase):
    def setUp(self):
        self.car = Car(model="BMW X5", fuel_capacity=80)

    def tearDown(self):
        pass

    def test_drive(self):
        self.car.refuel_car(10)
        self.car.drive(20)
        with self.assertRaises(NotEnoughFuelError):
            self.car.drive(80000)

    def test_refuel(self):
        self.car.refuel_car(20)
        self.assertEqual(self.car.get_current_fuel_level(), 20)
        with self.assertRaises(FuelOverflowError):
            self.car.refuel_car(80)
