#argumwnt the real value


#define create a fuction 

# def say_hellow():
#     print("hello")

#     #call the fuction
# say_hellow()


#arguments and prameters
#functions that is goimg to be calld orvet
# def greet(name):
#     # name is the parameter, which is a placeholder
#     #print out the name
#     print("hello", name)
#           #call ya funttions 
# greet("john")


#why are functions for 
#reusing code
#braking problems in to smaller pieces
# print("wellcome")
# print("pick an option")
# print("goodbye")

#  def show_menu():
#     print("wellcome")
#     print("pick an option")
#     print("goodbye")

    #print vs return
    #afuction that print 
#     def hello_world():
#         print("hello ")
#         this shows the text to the user 

#         #a fuction the returns a value
#         def hello():
#             return "hello world"
# msg = hello()
# print(msg)

# #call culater fuctions the uses 2 parameters
# def calculate(num1, num2):
#     operation=input("enter an operation (+, -, *, /): ")
#     #if or el on what to do 
#     print or return the result 



def play_again():
    #ansewr to the question if the user wants to play again
    question=input("do you want to play again? (y/n): ")
    if question=="y":
        play_again()
    else:
        print("goodbye")