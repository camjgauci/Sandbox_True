
def main():
  get_name()


def get_name():
    name = input("What is your Name?")
    name = "".join(name.split())
    count = 0
    if len(name) > 1:
        print(name[::2])
    else:
        print("Not a valid name")


main()






