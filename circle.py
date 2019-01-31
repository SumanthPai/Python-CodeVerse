import traceback
class InvalidRadiusError(Exception):
    pass
def area(r):
    area=3.14*r*r
    print("Area of the circle is %d"%(area))
radius=0

def usrinput():
    try:
        radius=int(input("Enter the radius:\n"))
    except ValueError:
        print("Input cannot be string")

    try:
        if radius<=0:
            raise InvalidRadiusError
            input()
        else:
            area(radius)
    except InvalidRadiusError:
        print("Invalid Radius Error : Radius should be greater than Zero\n")
        traceback.print_exc()

        
usrinput()
