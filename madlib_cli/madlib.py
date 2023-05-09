import re

file = "assets/madlib.txt"

def opening():
    print("""
  **************************************
  ** Welcome to the Madlib Experience!**
  ***************************************
  """)

def word_list(arr):
    word_array = []
    for i in arr:
        response = input(f'Please enter a {i}:')
        word_array.append(response)
    return word_array


def read_template(template):
    with open(template,'r') as read_file:
        read_text = read_file.read()
        return read_text



if __name__ == "__main__":
    opening()
    template = read_template("assets/madlib.txt")


