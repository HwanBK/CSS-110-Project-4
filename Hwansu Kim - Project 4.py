# CSC110
# Project 4 - Main File
# Hwansu Kim (Billy)
# 10/19/2021


import geometry


# Function definition for displaying a circle's circumference and area, by using user inputs for arguments and calling
# the geometry module's functions for calculations.
def displayCircleResults(radius, unit):
    print()
    print("Circle results")
    print("-" * 14)
    print(format("Circumference:", "<15s"), format(round(geometry.circleCircum(radius), 2), ">20.2f"), "linear", unit)
    print(format("Area:",          "<15s"), format(round(geometry.circleArea(radius),   2), ">20.2f"), "square", unit)
    print()


# Function definition for displaying a sphere's volume and surface area, by using user inputs for arguments and calling
# the geometry module's functions for calculations.
def displaySphereResults(radius, unit):
    print("Sphere results")
    print("-" * 14)
    print(format("Volume:",       "<15s"), format(round(geometry.sphereVolume(radius),   2), ">20.2f"), "cubic",  unit)
    print(format("Surface area:", "<15s"), format(round(geometry.sphereSurfArea(radius), 2), ">20.2f"), "square", unit)
    print()


# Function definition for displaying a square's perimeter and area, by using user inputs for arguments and calling
# the geometry module's functions for calculations.
def displaySquareResults(sideLength, unit):
    print("Square results")
    print("-" * 14)
    print(format("Perimeter:", "<15s"), format(round(geometry.squarePerim(sideLength), 2), ">20.2f"), "linear", unit)
    print(format("Area:",      "<15s"), format(round(geometry.squareArea(sideLength),  2), ">20.2f"), "square", unit)
    print()


# Function definition for displaying a cube's volume and surface area, by using user inputs for arguments and calling
# the geometry module's functions for calculations.
def displayCubeResults(sideLength, unit):
    print("Cube results")
    print("-" * 12)
    print(format("Volume:",       "<15s"), format(round(geometry.cubeVolume(sideLength),   2), ">20.2f"), "cubic", \
          unit)
    print(format("Surface area:", "<15s"), format(round(geometry.cubeSurfArea(sideLength), 2), ">20.2f"), "square", \
          unit)


# Function definition that gathers and returns user input for size(radius/side length) and the unit of measurement.
def getUserInput():
    userSize = float(input("Enter size for radius/side: "))
    userUnitOfMeasure = input("Enter unit of measure, e.g., inches: ")
    return userSize, userUnitOfMeasure


def main():
    size, unitOfMeasure = getUserInput()
    displayCircleResults(size, unitOfMeasure)
    displaySphereResults(size, unitOfMeasure)
    displaySquareResults(size, unitOfMeasure)
    displayCubeResults(size, unitOfMeasure)


main()


# SUMMARY

#    I started this project by using the call hierarchy diagram, that was provided, to take note of which functions
# would be defined in the main project file and which ones would be defined in the geometry module file. In the geometry
# module file, I first imported just the pi function from the math module, since it's all that's needed; importing
# the entire module seemed unnecessary. Then, I started by defining the first set of functions for the geometry module,
# individually testing the functions after creating them  to ensure the equations for each function where correct and
# were properly returning an output. After repeating this for every defined function until all of them were defined and
# working properly, I moved onto the main project file. When importing the geometry module into the main file, I
# initially typed "from geometry import *", but as I was calling the geometry module's functions I thought that just
# seeing the function name would be confusing and harder to read/understand; so, I went back and changed the import
# code to "import geometry" so that when I call on the functions from geometry, I'd be typing geometry.functionName,
# so that someone who reads the code would be able to immediately understand that cubeVolume() is from the imported
# geometry module. After all the functions were defined and I tested to ensure all arguments were properly passing
# to the appropriate parameters, I went on to tidy up the alignment of the output/UI; the biggest problem is that
# with the way I've aligned and formatted the output, there's a limit to the input's character count before the
# alignment breaks, a problem that's been persisting for that past couple projects.
#    For testing, I manually tested individual units of the program as I coded, ensuring each individual function
# was properly working before moving onto the next set of code. In regards to the geometry module's functions, I tested
# and compared all the function's output to calculations I did outside the program, on a calculator, to ensure the
# equations were properly coded. After finishing the main project file and geometry module, I created the optional
# PyUnit test script, which I honestly wish I had done before working on the main project file and after finishing
# the geometry module file. With the test script I tested all the types of numerical values I could think of: positive
# and negative integers, zero, and positive and negative floating-point numbers. The test script, although it took a
# fair bit of time to code and test the test script itself, saved a ton of time when it came time to test the overall
# project, since I no longer had to manually input and test every single valid and invalid input when I made changes
# or edits to the main project file. And as far as what doesn't work, inputting anything that isn't an integer or
# floating-point number in the userSize input, such as the string "nine", breaks the program; but, since we have learned
# that we can redirect users back to the input or give them a warning message to input specific data types only via
# selection statements, I already have an idea of how to fix this issue. Unfortunately, selection statements aren't a
# part of this project's week's material.
#    Project 4 was great additional practice for defining and calling functions, adding onto the previous week's
# material; as well as creating and importing modules. Although, the best part of the project was honestly the extra
# credit; the test script proved to be extremely useful and time efficient and as I was creating test cases for each
# function I really concentrated on which values and types of values to test; whereas when I used to manually test
# I would just try a couple random values or just testing the boundary cases, like with Project 2's brownie
# calculations. And for future projects I like to create or design the tests as soon as possible, following test-driven
# development.


# TEST CASES

# -userSize Input (Also applies to geometry.py tests)
#   +All integer type values work. (Test cases in TestGeometry)
#     -Tested positive integer values for all geometry module functions.
#     -Tested negative integer values for all geometry module functions.
#     -Tested 0 for all geometry module functions.
#   +All floating-point type values work. (Test cases in TestGeometry)
#     -Tested positive floating-point values for all geometry module functions.
#     -Tested negative floating-point values for all geometry module functions.
#   +String type inputs will break the program with a ValueError.
#     -Spelling out a numerical value; "Nine".
#     -Inputting a mathematical operation; (1 + 2).
#     -Numbers with commas; 102,204.
#     -Providing no input will also result in a ValueError, due to Python recognizing no input as an empty string.

# -userUnitOfMeasure Input
#   +No input will break the program.
#     -Although, inputs that are not units of measure, such as "apple pies", will result in outputs that don't make
#      sense logically; i.e. 706 square apple pies, when the calculation is finding the area of a circle.

# -Output
#   +Alignment will break if the output exceeds the soft-limit for character count.

# -geometry.py/TestGeometry.py
#   +Coded equations tested and compared to calculations done, outside of the program, with a calculator; expected
#    values in test cases from external calculations.
#   +AssertionError if the expected calculation is not the same as the function's output. (Tested for the sake of it).
