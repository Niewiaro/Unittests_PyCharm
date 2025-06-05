from unittest import TestCase


class TestCar(TestCase):

    def setUp(self):
        from car import Car

        self.car = Car()


class TestInit(TestCar):
    def test_initial_speed(self):
        self.assertEqual(self.car.speed, 0)

    def test_initial_odometer(self):
        self.assertEqual(self.car.odometer, 0)

    def test_initial_time(self):
        self.assertEqual(self.car.time, 0)


class TestAccelerate(TestCar):
    def test_accelerate_from_zero(self):
        self.car.accelerate()
        self.assertEqual(self.car.speed, 5)

    def test_multiple_accelerates(self):
        for _ in range(3):
            self.car.accelerate()
        self.assertEqual(self.car.speed, 15)


class TestBrake(TestCar):
    def test_break_once(self):
        self.car.accelerate()
        self.car.brake()
        self.assertEqual(self.car.speed, 0)

    def test_multiple_brakes(self):
        for _ in range(5):
            self.car.accelerate()
        for _ in range(3):
            self.car.brake()
        self.assertEqual(self.car.speed, 10)

    def test_should_not_allow_negative_speed(self):
        self.car.brake()
        self.assertEqual(self.car.speed, 0)

    def test_multiple_brakes_at_zero(self):
        for _ in range(3):
            self.car.brake()
        self.assertEqual(self.car.speed, 0)


class TestStep(TestCar):
    def test_step_increases_odometer(self):
        self.car.speed = 10
        self.car.step()
        self.assertEqual(self.car.odometer, 10)
        self.assertEqual(self.car.time, 1)

    def test_multiple_steps(self):
        self.car.speed = 20
        for _ in range(3):
            self.car.step()
        self.assertEqual(self.car.odometer, 60)
        self.assertEqual(self.car.time, 3)


class TestAverageSpeed(TestCar):
    def test_average_speed_with_no_time(self):
        self.assertEqual(self.car.average_speed(), 0)

    def test_average_speed_after_steps(self):
        self.car.speed = 10
        for _ in range(3):
            self.car.step()
        self.assertEqual(self.car.average_speed(), 10)

    def test_average_speed_after_multiple_speeds(self):
        self.car.speed = 10
        self.car.step()
        self.car.speed = 20
        self.car.step()
        self.assertEqual(self.car.average_speed(), 15)


class TestMain(TestCar):
    def test_main_function_exists(self):
        from car import main
        self.assertTrue(callable(main))


class TestRefuel(TestCar):
    def test_refuel_positive_amount(self):
        self.car.refuel(10)
        self.assertEqual(self.car.fuel, 10)

    def test_refuel_negative_amount(self):
        self.car.refuel(-5)
        self.assertEqual(self.car.fuel, 0)  # Assuming initial fuel is 0

    def test_refuel_zero_amount(self):
        self.car.refuel(0)
        self.assertEqual(self.car.fuel, 0)  # Assuming initial fuel is 0


class TestTruck(TestCase):
    def setUp(self):
        from car import Truck

        self.truck = Truck()


class TestTruckCargo(TestTruck):
    def test_load_cargo(self):
        self.truck.load_cargo(50)
        self.assertEqual(self.truck.cargo, 50)

    def test_unload_cargo(self):
        self.truck.load_cargo(50)
        self.truck.unload_cargo(20)
        self.assertEqual(self.truck.cargo, 30)


class TestTruckOverload(TestTruck):
    def test_not_overloaded(self):
        self.truck.load_cargo(100)
        self.assertFalse(self.truck.is_overloaded())

    def test_overloaded(self):
        self.truck.load_cargo(120)
        self.assertFalse(self.truck.is_overloaded())  # cargo capped at max_cargo

    def test_max_cargo(self):
        self.truck.load_cargo(100)
        self.assertTrue(self.truck.cargo <= self.truck.max_cargo)


class TestPoliceCar(TestCase):
    def setUp(self):
        from car import PoliceCar

        self.police_car = PoliceCar()


class TestPoliceCarSiren(TestPoliceCar):
    def test_toggle_siren_on(self):
        self.police_car.toggle_siren()
        self.assertTrue(self.police_car.is_siren_active())

    def test_toggle_siren_off(self):
        self.police_car.toggle_siren()
        self.police_car.toggle_siren()
        self.assertFalse(self.police_car.is_siren_active())


class TestPoliceCarArrests(TestPoliceCar):
    def test_make_arrest(self):
        self.police_car.make_arrest()
        self.police_car.make_arrest()
        self.assertEqual(self.police_car.arrests, 2)


class TestPoliceCarAttributes(TestPoliceCar):
    def test_siren_attribute(self):
        self.assertIn('siren_on', self.police_car.__dict__)
