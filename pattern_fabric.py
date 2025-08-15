
from abc import ABC, abstractmethod

from logger import get_logger

logger = get_logger(__name__)


class Vehicle(ABC):
    @abstractmethod
    def start_engine(self) -> None:
        pass


class Car(Vehicle):
    def __init__(self, make: str, model: str) -> None:
        self.make = make
        self.model = model

    def start_engine(self) -> None:
        logger.info("%s %s: Двигун запущено", self.make, self.model)


class Motorcycle(Vehicle):
    def __init__(self, make: str, model: str) -> None:
        self.make = make
        self.model = model

    def start_engine(self) -> None:
        logger.info("%s %s: Мотор заведено", self.make, self.model)


class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make: str, model: str) -> Vehicle:
        pass

    @abstractmethod
    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        pass

class USVehicleFactory(VehicleFactory):
    REGION_SUFFIX = "US Spec"

    def create_car(self, make: str, model: str) -> Vehicle:
        return Car(make, f"{model} ({self.REGION_SUFFIX})")

    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        return Motorcycle(make, f"{model} ({self.REGION_SUFFIX})")


class EUVehicleFactory(VehicleFactory):
    REGION_SUFFIX = "EU Spec"

    def create_car(self, make: str, model: str) -> Vehicle:
        return Car(make, f"{model} ({self.REGION_SUFFIX})")

    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        return Motorcycle(make, f"{model} ({self.REGION_SUFFIX})")


def main() -> None:
    us_factory = USVehicleFactory()
    eu_factory = EUVehicleFactory()

    vehicle1 = us_factory.create_car("Ford", "Mustang")
    vehicle2 = eu_factory.create_motorcycle("Yamaha", "MT-07")

    vehicle1.start_engine()
    vehicle2.start_engine()


if __name__ == "__main__":
    main()
