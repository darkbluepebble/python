# classes

class Animal():
    name="Amy"
    noise="Grunt"
    size="Large"
    color="Brown"
    hair="Covers body"

    def set_color(self,clr):
        print(self.color)
        self.color=clr
        return self.color +" "+clr
        
    def get_color(self):
        return self.color

    @property
    def make_noise(self):
        print(self.noise)
        return self.noise

"""
dog=Animal()
dog.make_noise()
dog.size="small"
dog.color="black"
dog.hair="hairless"
 """

class Dog(Animal):
    name="Luck"
    
    """color="brown"
    def get_color(self):
        print(self.name)
        return self.color """

    
obj=Dog()
obj.color="white"
obj.name="Jon Snow"

obj.make_noise

obj.set_color("blue")
print(obj.set_color("blue"))
