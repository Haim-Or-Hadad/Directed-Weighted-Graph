import math


class coordinates:

    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def x(self):
        return self.x()

    def y(self):
        return self.y()

    def z(self):
        return self.z()

    def distance(self,  other):
        dx = self.x - other.x
        dy = self.y - other.y
        dz = self.z - other.z
        return math.sqrt(dx**2 + dy**2 + dz**2)

    def __display__(self):
        print("x=%d,y=%d,z=%d" %(self.x,self.y, self.z))



# coor1 = coordinates(5,6,7)
# coor2 = coordinates(1,2,3)
# coor3 = coordinates()
#
# coor1.__display__()
# coor2.__display__()
# coor3.__display__()
#
# print(coor1.distance(coor2))