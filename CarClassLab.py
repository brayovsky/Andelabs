class Car(object):
 def __init__(self,name='General',model='GM',cartype='Saloon'):
    self.name=name
    self.model=model
    self.cartype=cartype
    self.speed = 0
    if(self.name == 'Porshe' or self.name == 'Koenigsegg'):
      self.num_of_doors = 2
    else:
      self.num_of_doors = 4
    if(self.cartype == 'trailer'):
      self.num_of_wheels = 8
    else:
      self.num_of_wheels = 4
    
 def is_saloon(self):
    if(self.cartype != 'trailer'):
      return True
    else:
      return False
      
 def drive(self,power):
   if(self.is_saloon()):
     self.speed = 10**power
     return self
   else:
     self.speed = 77
     return self