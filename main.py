# This is a sample Python script.
import os


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Get the value of the PORT environment variable
    port = os.environ.get('PORT')

    if port is not None:
        print(f"PORT environment variable value: {port}")
    else:
        print("PORT environment variable is not set")
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
