class animal:
    """We are generating a new class"""
    
    types = 0
    
    def __init__(self, name):
        """We are creating the animal at this point"""
        self.name = name
        print(f"I am a {self.name}.")
        
        animal.types += 1
    @classmethod
    def sold(cls):
        
        animal.types -= 1
        print(f"We have {animal.types:d} numbers of pet left in shed")
    @classmethod
    def diff_types(cls):
        print(f"We have {animal.types} different kinds of animals")
        

pet=animal("Cat")

pet=animal("Dog")

pet=animal("Hound")

print(pet)

animal.diff_types()
animal.types()
