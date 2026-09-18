# age = input("what is your age? ")
# if age == "9-12":
#     print("you are a child")
# elif age == "18-23":
#     print("you are an adult")
# else:
#     print("you are old")

# print("what class do u want to check?")
# class_name = input("math, programming, science, english? ")

# if class_name == "math":
#     math_grade = input("what is your math grade? ")
#     if math_grade == "B-":
#         print("you are doing alr")
#     else:
#         print("you need to work on math")
# elif class_name == "programming":
#     programing_grade = input("what is your programming grade? ")
#     if programing_grade == "A":
#         print("you are doing great")
#     else:
#         print("you need to work on programming")
# elif class_name == "science":
#     science_grade = input("what is your science grade? ")
#     if science_grade == "C":
#         print("you need to work on science")
#     else:
#         print("you are doing okay in science")
# elif class_name == "english":
#     english_grade = input("what is your english grade? ")
#     if english_grade == "f":
#         print("you need to work on english")
#     else:
#         print("you are doing okay in english")
# else:
#     print("invalid class")



height = float(input("what is your height? "))
if height < 4.5:
    print("you are short")
elif height < 5.0:
    print("you are of average height")
else:
    print("you are tall")

weight = float(input("what is your weight? "))
if weight <100:
    print("you need to eat")
    if weight <160-190:
        print("your alright")
else:
    print("you are fattt ")