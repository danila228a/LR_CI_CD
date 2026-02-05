class NotEnoughFuelError(Exception):
    """
    Недостаточно топлива для поездки.
    """


class TooMuchFuelError(Exception):
    """
    Пытаетесь залить больше, чем вмещает бак.
    """


class Car:
    def __init__(self, model: str, fuel_capacity: float) -> None:
        """
        Инициализация автомобиля.

        Args:

            model: марка и модель автомобиля.
            fuel_capacity: объём топливного бака в литрах.
        """
        self._model = model
        self._fuel_capacity: float = fuel_capacity
        self._fuel_in_tank: float = 0.0

    def get_current_fuel_level(self) -> float:
        """
        Возвращает текущий уровень топлива в баке.
        """
        return self._fuel_in_tank

    def refuel_car(self, fuel_quantity: float) -> None:
        """
        Заправка автомобиля.

        Args:

            fuel_quantity: количество топлива для заправки (литры).

        Raises:

            TooMuchFuelError: если пытаемся залить больше, чем вмещает бак.
        """
        if self._fuel_capacity < fuel_quantity:
            msg = "Вы пытаетесь залить слишком много бензина!"
            raise TooMuchFuelError(msg)

        self._fuel_in_tank += fuel_quantity

    def drive(self, distance_km: float) -> float:
        """
        Поездка на заданное расстояние.

        Args:

            distance_km: расстояние в километрах.

        Returns:

            Оставшееся топливо в баке.

        Raises:

            NotEnoughFuelError: если топлива не хватает на поездку.
        """
        # Считаем, что расход 8 литров на 100 км
        fuel_burned: int = int(8 * (distance_km / 100))

        if self._fuel_in_tank < fuel_burned:
            msg = "Не доедем же жеж..."
            raise NotEnoughFuelError(msg)

        self._fuel_in_tank -= fuel_burned
        return self._fuel_in_tank
 __init__(self, model: str, fuel_capacity: float) -> None:
        """Инициализация автомобиля.

        Args:
            model: марка и модель автомобиля.
            fuel_capacity: объём топливного бака в литрах.
        """
        self._model = model
        self._fuel_capacity: float = fuel_capacity
        self._fuel_in_tank: float = 0

    def get_current_fuel_level(self) -> float:
        """Возвращает текущий уровень топлива в баке."""
        return self._fuel_in_tank

    def refuel_car(self, fuel_quantity: float) -> None:
        """Заправка автомобиля.

        Args:
            fuel_quantity: количество топлива для заправки (литры).

        Raises:
            TooMuchFuelError: если пытаемся залить больше, чем вмещает бак.
        """
        if self._fuel_capacity < fuel_quantity:
            msg = "Вы пытаетесь залить слишком много бензина!"
            raise TooMuchFuelError(msg)

        self._fuel_in_tank += fuel_quantity

    def drive(self, distance_km: float) -> float:
        """Поездка на заданное расстояние.

        Args:
            distance_km: расстояние в километрах.

        Returns:
            Оставшееся топливо в баке.

        Raises:
            NotEnoughFuelError: если топлива не хватает на поездку.
        """
        # Считаем, что расход 8 литров на 100 км
        fuel_burned: int = int(8 * (distance_km / 100))  # noqa: FIX002

        if self._fuel_in_tank < fuel_burned:
            msg = "Не доедем же жеж..."
            raise NotEnoughFuelError(msg)

        self._fu

