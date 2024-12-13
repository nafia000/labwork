import graphics
import graphics.rectangle
import graphics.circle
from graphics.three_d_graphics.cuboid import cuboidarea,cuboidvolume
from graphics.three_d_graphics.sphere import *
length=float(input("Enter Length of Rectangle:"))
width=float(input("Enter Width of Rectangle:"))
print("Rectangle Area :",graphics.rectangle.area(length,width))
print("Rectangle Perimeter :",graphics.rectangle.perimeter(length,width))
radius=float(input("Enter Radius of Circle:"))
print("Circle Area :",graphics.circle.area(radius))
print("Circle Perimeter :",graphics.circle.perimeter(radius))
length=float(input("Enter Length of Cuboid:"))
width=float(input("Enter Width of Cuboid:"))
height=float(input("Enter Height of Cuboid:"))
print("Cuboid Area :",cuboidarea(length,width,height))
print("Cuboid Volume :",cuboidvolume(length,width,height))
radius=float(input("Enter Radius of Sphere:"))
print("Sphere Area :",area(radius))
print("Sphere Volume :",volume(radius))
