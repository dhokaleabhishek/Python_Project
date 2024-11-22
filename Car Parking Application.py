class CarParking:
    SUV_price = 20
    hatchback = 10
    SUV_count = 0
    hatchback_count = 0
    total_cash = 0
    def __init__(self):
        self.name = input("car_name")
        print("Car type are : SUV || hatchback")
        self.type = input("car_type")
        print("Car Parking price per hour are : SUV : $20 || hatchback : $10 ")
        self.time = float(input("parking_time"))
        if self.type == "SUV":
            self.amount = CarParking.SUV_price * self.time
            CarParking.total_cash += self.amount
            CarParking.SUV_count += 1

        elif self.type == "hatchback":
            self.amount = CarParking.hatchback * self.time
            CarParking.total_cash += self.amount
            CarParking.hatchback_count += 1


    def display(self):
        print("------------------ Parking Ticket -------------------")
        print("Car Name : = ",self.name)
        print("Car Type : = ",self.type)
        print(f"Car Parking Time : = {self.time} hours")
        print("Car Parking Fees : = $",self.amount)
        print("---------------------------------------------------")

    @classmethod
    def Catalog(cls):
        print("***************** Parking Details *********************")
        print("Cash Available : = $", cls.total_cash)
        print("number of SUV's : = ", cls.SUV_count)
        print("number of hatchback's : = ", cls.hatchback_count)
        print("******************************************************")

print("---------------------------Car Parking Application---------------------------")
CarParking.Catalog()
n = 1
while n !=0:
    dict1 = {1: "Parking", 2: "Catalog", 0: "Exit"}
    for k, v in dict1.items():
        print(f"{k} = {v}")
    n = int(input("Enter choice : "))

    if n == 1:
        c1 = CarParking()
        c1.display()
    elif n == 2:
        CarParking.Catalog()
    elif n == 0:
        CarParking.Catalog()
        print("EXIT")
    else:
        print("INVALID INPUT !!\n-------------------Enter Again-------------------")
        pass

