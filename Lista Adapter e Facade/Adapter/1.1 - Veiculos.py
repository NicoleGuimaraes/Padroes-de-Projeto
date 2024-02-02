from abc import ABC, abstractmethod

# Interface para os tipos de veículos
class Vehicle(ABC):
    @abstractmethod
    def manufacture(self):
        pass

# Fábrica abstrata para veículos
class VehicleFactory(ABC):
    @abstractmethod
    def produce_car(self) -> Vehicle:
        pass

    @abstractmethod
    def produce_motorcycle(self) -> Vehicle:
        pass

    @abstractmethod
    def produce_truck(self) -> Vehicle:
        pass

# Implementações concretas de veículos
class Car(Vehicle):
    def manufacture(self):
        print("Produzindo um carro.")

class Motorcycle(Vehicle):
    def manufacture(self):
        print("Produzindo uma motocicleta.")

class Truck(Vehicle):
    def manufacture(self):
        print("Produzindo um caminhão.")

# Fábrica concreta de veículos elétricos
class ElectricVehicleFactory(VehicleFactory):
    def produce_car(self) -> Vehicle:
        return Car()

    def produce_motorcycle(self) -> Vehicle:
        return Motorcycle()

    def produce_truck(self) -> Vehicle:
        return Truck()

# Fábrica concreta de veículos a combustível
class FuelVehicleFactory(VehicleFactory):
    def produce_car(self) -> Vehicle:
        return Car()

    def produce_motorcycle(self) -> Vehicle:
        return Motorcycle()

    def produce_truck(self) -> Vehicle:
        return Truck()

# Uso das fábricas
def main():
    electric_factory = ElectricVehicleFactory()
    fuel_factory = FuelVehicleFactory()

    car1 = electric_factory.produce_car()
    motorcycle1 = electric_factory.produce_motorcycle()
    truck1 = electric_factory.produce_truck()

    car2 = fuel_factory.produce_car()
    motorcycle2 = fuel_factory.produce_motorcycle()
    truck2 = fuel_factory.produce_truck()

    car1.manufacture()
    motorcycle1.manufacture()
    truck1.manufacture()

    car2.manufacture()
    motorcycle2.manufacture()
    truck2.manufacture()

if __name__ == "__main__":
    main()