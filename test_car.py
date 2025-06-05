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

