class Car:
  
  #attribute
  wheel_number = 4
  gas_type = "Gasoline"
  
  def __init__(self, year):
      # This is the constructor method, it is called when we create an instance of the class
      print(f"Creating a new {year} car...")
      self.year = year  # instance attribute
      self.wheel_number = Car.wheel_number  # instance attribute, can be overridden for specific instances

  def confirmation_message(self):
      print("Car created successfully!")
      
  def car_capabilities(self, miles, crashes):
      print(f"This car is able to drive {miles} miles, withstand {crashes} crashes, and has a total of {self.wheel_number} wheels.")    
      
  def upgrade_engine(self):
    if self.gas_type == "Gasoline":
      print("Upgrading engine to Diesel...")
      self.gas_type = "Diesel"
    else:
      print("Engine is already Diesel.")     


#here we create an instance of the class Car, e.g. we make my_car an object of the class Car    
my_car = Car("2025") # This will call the constructor method __init__ when we create the instance and assign the value "2025" to the year attribute of the class Car
my_bigger_car = Car("2024")
my_car.confirmation_message()
my_bigger_car.confirmation_message()

my_bigger_car.wheel_number = 8  # This will not change the class attribute, only the instance attribute

#here we assign the values to the attributes of the class Car
my_car.car_capabilities(350000, 3) #This will call the method car_capabilities from the class Car and assign the values to the parameters miles and crashes
my_bigger_car.car_capabilities(275000, 6) 

my_bigger_car.upgrade_engine()  # This will change the gas_type attribute of my_car


print("First car:")
print(my_car.gas_type)
print("Upgraded car:")
print(my_bigger_car.gas_type)