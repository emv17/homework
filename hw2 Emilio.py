###############################
# GRADE
###A	90%-100%4.0
##B	80%-89%	3.0
##C	70%-79%	2.0
##D	60%-69%	1.0
##F	0%-59%	0.0
# Given the score (0 to 100) received on a test, print the letter grade.
# You can just give the letter, no need for the +/-
#
# The score should be taken from user input.
#
# In case you have been at Hampshire long enough to forget how grades work,
# you can use the first table on this wikipedia page:
# https://en.wikipedia.org/wiki/Academic_grading_in_the_United_States

### YOUR CODE HERE ###

grade = input("enter your grade")

print("grade entered:", grade)

index = 0

if grade == "100":
    print("A")
    
elif len(grade) < 2:
         print("F")
    
elif len(grade) > 2:
        print("invalid grade")

else:
    if grade[index] == "5" or grade == "10":
        print("F")
    elif grade[index] == "6":
        print("D")
    elif grade[index] == "7":
        print("C")
    elif grade[index] == "8":
        print("B")
    elif grade[index] == "9":
        print("A")
    
   

###############################
# AREA
#
# Take user input to determine the name of a shape (rectangle or triangle)
#
# Depending on the shape name, create as many variables as needed and set their
# values based on user input.
#
# Print the area of the shape.

### YOUR CODE HERE ###

shape = input("Name a Shape")

index = 0,1

if shape == "rectangle":
   height_rectangle = int(input("height?"))
   length_rectangle = int(input("length?"))
   print("area: ",length_rectangle * height_rectangle)

elif shape == "triangle":
    base_triangle = int(input("base?"))
    height_triangle = int(input("height?"))
    print("area: ",(base_triangle * height_triangle)/2)

else:
    print("don't know that one")


