from tkinter import *
import random
import pytest
import csv



csv_file_names = "C:\\Users\\cjcri\\OneDrive\\Documents\\BYU_I\\cse111\\Personal_program\\names.csv"
csv_file_expressions =  "C:\\Users\\cjcri\\OneDrive\\Documents\\BYU_I\\cse111\\Personal_program\\expressions.csv"


def main():
    root.mainloop()


def student_name(csv_file_names):
    with open(csv_file_names) as f:
        reader = csv.reader(f)
        chosen_row = random.choice(list(reader))
        return chosen_row[0]

def expression(csv_file_expressions):
     with open(csv_file_expressions) as f:
        reader = csv.reader(f)
        chosen_row = random.choice(list(reader))
        return chosen_row[0]

def on_button_click():
    random_name_perclick = student_name(csv_file_names)
    random_expression_perclick = expression(csv_file_expressions)
    result_label.config(text=f"{random_name_perclick} what is the value of {random_expression_perclick}?")



root = Tk()
root.geometry('300x300')

l = Label(root, text="Today's Hero is!")
l.pack()

result_label = Label(root, text="")
result_label.pack()

button = Button(root, text="Click Me", command=on_button_click)
button.pack()

root.mainloop()


if __name__ == "__main__":
    main()