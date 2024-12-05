# CSC110
# Project 4 - geometry module file
# Hwansu Kim (Billy)
# 10/19/2021


from math import pi


# Function definition for calculating a circle's circumference.
def circleCircum(radius):
    circumference = 2 * pi * radius
    return circumference


# Function definition for calculating a circle's area.
def circleArea(radius):
    area = pi * radius ** 2
    return area


# Function definition for calculating a sphere's volume.
def sphereVolume(radius):
    volume = (4 / 3) * pi * radius ** 3
    return volume


# Function definition for calculating a sphere's surface area.
def sphereSurfArea(radius):
    surfArea = 4 * pi * radius ** 2
    return surfArea


# Function definition for calculating a square's perimeter.
def squarePerim(sideLength):
    perimeter = 4 * sideLength
    return perimeter


# Function definition for calculating a square's area.
def squareArea(sideLength):
    area = sideLength ** 2
    return area


# Function definition for calculating a cube's volume.
def cubeVolume(sideLength):
    volume = sideLength ** 3
    return volume


# Function definition for calculating a cube's surface area.
def cubeSurfArea(sideLength):
    surfArea = 6 * sideLength ** 2
    return surfArea