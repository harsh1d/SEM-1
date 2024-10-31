# class squirrel:#
#creating instance
class squ:
    color = 'brown'
    size = 'small'
    behaviour = ['frantic','nervous']
    num_legs = 4
    tail = 1
    def __init__(self,color=None,size=None):
        if color != None : self.color = color
        if size != None : self.size = size
        
    def make_noise(self):
        return "Squeak!"
    
    def show_info(self):
        print("This is a %s %s squirrel."% (self.color, self.size))
        print("It has %d legs and a %d tail."% (self.num))
        print("The squirrel behaves like this:%s"% ', '.join(self.behaviour))

nutsy = squ()
print(nutsy.make_noise())
nutsy.show_info()   
fluffy = squ('grey', 'large')
fluffy.tail = 2
print(fluffy.make_noise())
fluffy.show_info()  
