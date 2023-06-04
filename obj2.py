class Gun:
    """We are crete a class gun with different functionalities"""
    cart = 0
    bullet = "==>"
    ammo = 120
    def __init__(self, name):
        self.name = name
        
    def guntype(self):
        
        print(f"Hi, I am name is {rifle.name}, and I am an automatic rifle with ammo of {Gun.ammo} and a cartridge of {Gun.cart} rounds") 
    def reload(self):
        Gun.ammo -= 30
        Gun.cart += 30
        print(f"you have just reloaded you have {Gun.ammo} ammo remaining!")
    def fire(self):
        for fire in range(1, 31):
            Gun.cart -= 1
        print(Gun.bullet)

rifle = Gun("P90")


rifle.guntype()
rifle.reload()
rifle.fire()  
rifle.fire()
rifle.fire()
rifle.fire()
rifle.fire()
rifle.fire()
rifle.fire()
rifle.fire()
rifle.fire()
rifle.fire()
rifle.fire()
rifle.fire()
rifle.reload()
    
        