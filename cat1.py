# for _ in range(3):
#     print("meow")

# print("meow \n"*3,end="")

# user_input = int(input("What's n? "))
# while True:
#     if user_input>0:
#         break
#     user_input = int(input("What's n? "))
# # print("meow\n"*user_input,end="")

# for i in range(user_input):
#     print("meow") 


def main():
    meow(positive_number())
    

def meow(n):
    for i in range(n):
        print("meow")

def positive_number():
    while True:
        n = int(input("What's n? "))
        if n>=0:
            return n

main()