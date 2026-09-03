from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

text = """
class Car:
    A simple class to represent a car.

    # The Constructor Method (Initializer)
    def __init__(self, make, model, year):
        self.make = make         # Instance attribute
        self.model = model       # Instance attribute
        self.year = year         # Instance attribute
        self.odometer = 0        # Default instance attribute

    # A regular method to get a clean description of the car
    def get_descriptive_name(self):
        return f"{self.year} {self.make} {self.model}"

    # A method to update data inside the object
    def drive(self, miles):
        if miles > 0:
            self.odometer += miles
        else:
            print("You can't roll back an odometer!")


# --- Using the Class (Creating Objects) ---

# 1. Create a new instance (object) of the Car class
my_car = Car("Toyota", "Camry", 2024)

# 2. Access attributes using dot notation
print(my_car.make)   # Output: Toyota
print(my_car.model)  # Output: Camry

# 3. Call methods on the object
description = my_car.get_descriptive_name()
print(description)   # Output: 2024 Toyota Camry

# 4. Modify attributes through a method
my_car.drive(150)
print(f"Current Odometer: {my_car.odometer} miles")  # Output: Current Odometer: 150 miles
"""

# Initialize the splitter
splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=300,
    chunk_overlap=0,
)

# Perform the split
chunks = splitter.split_text(text)

print(len(chunks))
print(chunks[1])