def main():
    user_input = input("Please paste your input string here: ")
    user(user_input)

def user(user_input):
    dots = "..."
    str = dots.join(user_input.split())
    print(str)

main()
