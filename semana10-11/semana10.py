class Circle:
    
    def __init__(self, radius):
        self.radius = radius
        
    def get_area(self):
        return 3.14 * (self.radius ** 2)

    def __str__(self):
        return f"Circle with radius: {self.radius}, area: {self.get_area()}"
    
print("Circle example:")
circle = Circle(5)
print(circle)
    
# -------------------------------------- #  

class Person():
	def __init__(self, name):
		self.name = name
		self.age = 0
		age = 56

person_1 = Person("John")
age = 34

print(person_1.age)

# -------------------------------------- #  

class Bus:
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []
    
    def board_passenger(self, person):
        if len(self.passengers) < self.capacity:
            self.passengers.append(person)
            print(f"{person.name} boarded. Total passengers: {len(self.passengers)}")
        else:
            print("Bus is full!")
    
    def unboard_passenger(self):
        if self.passengers:
            person = self.passengers.pop()
            print(f"{person.name} unboarded. Total passengers: {len(self.passengers)}")
        else:
            print("No passengers to unboard!")        
    
    def __str__(self):
        return f"Bus with capacity {self.capacity} and current passengers: {[p.name for p in self.passengers]}"    


print("Bus example:")
bus = Bus(5)
print(bus)
bus.board_passenger(person_1)
bus.board_passenger(Person("Mark"))
bus.board_passenger(Person("Stephanie"))
print(bus)
bus.board_passenger(Person("Cody"))
bus.board_passenger(Person("Trish"))
bus.board_passenger(Person("Shawn"))
print(bus)
bus.unboard_passenger()
bus.unboard_passenger()
print(bus)
bus.unboard_passenger()
bus.unboard_passenger()
bus.unboard_passenger()
print(bus)
bus.unboard_passenger()