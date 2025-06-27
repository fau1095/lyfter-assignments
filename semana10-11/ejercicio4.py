

class Human:
    def __init__(self, torso):
        self.torso = torso
        
    def describe(self):
        print("This is a human with the following body parts:")
        print(f"Head        -> {self.torso.head}")
        print(f"Right Arm   -> {self.torso.right_arm}")
        print(f"Left Arm    -> {self.torso.left_arm}")
        print(f"Right Leg   -> {self.torso.right_leg}")
        print(f"Left Leg    -> {self.torso.left_leg}")
        
    def is_complete(self):
        return all([
        self.torso.head,
        self.torso.right_arm and self.torso.right_arm.hand,
        self.torso.left_arm and self.torso.left_arm.hand,
        self.torso.right_leg and self.torso.right_leg.feet,
        self.torso.left_leg and self.torso.left_leg.feet
    ])

class Torso:
    def __init__(self, head, right_arm, left_arm, right_leg, left_leg):
        self.head = head
        self.right_arm = right_arm
        self.left_arm = left_arm
        self.right_leg = right_leg
        self.left_leg = left_leg
        
class Head:
    def __str__(self):
        return "Head with a pair of eyes, a nose, and a mouth"
            
class Arm:
    def __init__(self, hand):
        self.hand = hand

    def __str__(self):
        return f"An arm that ends in {self.hand}"
    
class Hand:
	def __str__(self):
		return "a hand with 5 fingers"
class Leg:
    def __init__(self, feet):
        self.feet = feet
    def __str__(self):
        return f"A leg that ends in a {self.feet}"

class Foot:
    def __str__(self):
        return "foot with toes and a heel"    
    
 
left_foot = Foot()
right_foot = Foot()
left_leg = Leg(left_foot)
right_leg = Leg(right_foot)
head = Head()
right_hand = Hand()
right_arm = Arm(right_hand)
left_hand = Hand()
left_arm = Arm(left_hand)
torso = Torso(head, right_arm, left_arm, right_leg, left_leg)
human = Human(torso)
human.describe()

print("Human is complete!" if human.is_complete() else "Human is missing parts.")