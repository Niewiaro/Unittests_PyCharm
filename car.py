class Car:
    def __init__(self, speed: int = 0, fuel: int = 0) -> None:
        self.speed = speed
        self.odometer = 0
        self.time = 0
        self.fuel = fuel

    def say_state(self) -> None:
        print("I'm going {} kph!".format(self.speed))

    def accelerate(self) -> None:
        self.speed += 5

    def brake(self) -> None:
        if self.speed < 5:
            self.speed = 0
        else:
            self.speed -= 5

    def step(self) -> None:
        self.odometer += self.speed
        self.time += 1
        self.fuel -= self.speed // 10  # Assuming 1 unit of fuel per 10 km

    def refuel(self, amount: int) -> None:
        if amount < 0:
            print("Cannot refuel with a negative amount.")
            return
        self.fuel += amount
        print(f"Refueled {amount} units. Current fuel: {self.fuel} units.")

    def average_speed(self) -> float:
        try:
            return self.odometer / self.time
        except ZeroDivisionError:
            return 0.0


def main() -> None:
    my_car = Car()
    print("I'm a car!")
    while True:
        action = input("Whar should I do ? [A}ccelerate, "
                       "[B]rake, show [O]dometer, "
                       "show average [S]peed"
                       "or [R]efuel?").upper()
        if action not in "ABOSR" or len(action) != 1:
            print("I don't know how to do that")
            continue
        if action == 'A':
            my_car.accelerate()
        elif action == 'B':
            my_car.brake()
        elif action == 'O':
            print("The car has driven {} "
                  "kilometers".format(my_car.odometer))
        elif action == 'S':
            print("The car's average speed was {} "
                  "kph".format(my_car.average_speed()))
        elif action == 'R':
            try:
                amount = int(input("How much fuel should I add? "))
                my_car.refuel(amount)
            except ValueError:
                print("Please enter a valid number.")
        my_car.step()
        my_car.say_state()


if __name__ == "__main__":
    main()
