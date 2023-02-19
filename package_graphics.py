Pack.py
from graph import circle,rectangle,cuboid,sphere
r=int(input("Enter the radius of circle:"))
circle(r)
l=int(input("Enter the length of rectangle:"))
b=int(input("Enter the breadth of rectangle:"))
rectangle(l,b)
l1=int(input("Enter the length of cuboid:"))
b1=int(input("Enter the breadth of cuboid:"))
h1=int(input("Enter the height of cuboid:"))
cuboid(l1,b1,h1)
r1=int(input("Enter the radius of sphere:"))
sphere(r1)

graph.py
def circle(r):
    areac =3.14*r*r
    print("Area of circle is:", areac)
    peric = 2*3.14*r
    print("Perimeter of circle is:", peric)
def rectangle(l,b):
    arear =l*b
    print("Area of Rectangle is:",arear)
    perir =2*(l+b)
    print("Perimeter of Rectangle is:",perir)
def cuboid(l,b,h):
    areacub = 2*((l*b) + (b*h) + (h*l))
    print("Area of Cuboid is:", areacub)
    pericub = 4*(l+b+h)
    print("Perimeter of Cuboid is:", pericub)
def sphere(r):
    areas = 4*3.14*r*r
    print("Area of Sphere is:", areas)
    peris = 6.2832*r
    print("Perimeter of Sphere is:", peris)
