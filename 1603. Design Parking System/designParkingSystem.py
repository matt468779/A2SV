class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.limits = [big, medium, small]
        self.parking = [0] * 3

    def addCar(self, carType: int) -> bool:
        self.parking[carType-1] += 1
        return self.parking[carType-1] <= self.limits[carType-1]


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
