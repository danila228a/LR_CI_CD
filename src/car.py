# car.py
class FuelOverflowError(Exception):
    """Ошибка при попытке залить слишком много топлива."""

    message = "Вы пытаетесь залить слишком много бензина!"


class NotEnoughFuelError(Exception):
    """Ошибка при попытке проехать на пустом баке."""

    message = "Не доедем жеж..."


class Car:
    def init(self, model: str, fuel_capacity: float) -> None:
        self._model = model
        self._max_fuel_capacity: float = fuel_capacity
        self._fuel_in_tank: float = 0

    def get_current_fuel_level(self) -> float:
        return self._fuel_in_tank

    def refuel_car(self, fuel_quantity: float):
        if self._max_fuel_capacity - self._fuel_in_tank < fuel_quantity:
            raise FuelOverflowError  # ruff рекомендует без скобок
        self._fuel_in_tank += fuel_quantity

    def drive(self, distance_km: float):
        fuel_burned: float = 8 * (distance_km / 100)
        if self._fuel_in_tank < fuel_burned:
            raise NotEnoughFuelError  # без скобок
        self._fuel_in_tank -= fuel_burned
        return self.get_current_fuel_level()
