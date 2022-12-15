# main function.
from pip._vendor.distlib.compat import raw_input


def main():
    print("Enter your name")
    name = raw_input('Your name: ')
    print('Hello ' + name + ', how are you?')
main()