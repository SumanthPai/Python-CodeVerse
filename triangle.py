class Triangle:
    number_of_sides=3
    def __init__(self,angle1,angle2,angle3):
        self.angle1=angle1
        self.angle2=angle2
        self.angle3=angle3

    def checkangles(self):
        if((self.angle1+self.angle2+self.angle3)==180):
            print("True")
            return True
        else:
            print("False")
            return False

my_triangle=Triangle(60,60,60)
my_triangle.checkangles()
res=my_triangle.number_of_sides
print(str(res))
                         
                         
