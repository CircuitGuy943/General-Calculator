# This program is supposed to receive a valid equation e.g. 1+2*5 and complete it in BIDMAS (Brackets, Indices,
# Division, Multiplication, Addition and Subtraction) order then return the result all through a window.
import tkinter as tk
from tkinter import ttk

prev_result = ""

def calculate():
    global prev_result
    count1 = 1
    count2 = 1
    num1 = ""
    num2 = ""
    float_try = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", ]
    equation = "qwe" + entry_variable.get() + "qwe"

    while "^" in equation:
        place_of_op = equation.index("^")
        while equation[place_of_op - count1] in float_try:
            num1 = str(equation[place_of_op - count1]) + num1
            count1 = count1 + 1
        while equation[place_of_op + count2] in float_try:
            num2 = num2 + str(equation[place_of_op + count2])
            count2 = count2 + 1
        result = float(num1) ** float(num2)
        equation = equation.replace(str(num1) + "^" + str(num2), str(result), 1)
        count1 = 1
        count2 = 1
        num1 = ""
        num2 = ""
    while "*" in equation:
        place_of_op = equation.index("*")
        while equation[place_of_op - count1] in float_try:
            num1 = str(equation[place_of_op - count1]) + num1
            count1 = count1 + 1
        while equation[place_of_op + count2] in float_try:
            num2 = num2 + str(equation[place_of_op + count2])
            count2 = count2 + 1
        result = float(num1) * float(num2)
        equation = equation.replace(str(num1) + "*" + str(num2), str(result), 1)
        count1 = 1
        count2 = 1
        num1 = ""
        num2 = ""
    while "/" in equation:
        place_of_op = equation.index("/")
        while equation[place_of_op - count1] in float_try:
            num1 = str(equation[place_of_op - count1]) + num1
            count1 = count1 + 1
        while equation[place_of_op + count2] in float_try:
            num2 = num2 + str(equation[place_of_op + count2])
            count2 = count2 + 1
        result = float(num1) / float(num2)
        equation = equation.replace(str(num1) + "/" + str(num2), str(result), 1)
        count1 = 1
        count2 = 1
        num1 = ""
        num2 = ""
    while "-" in equation:
        place_of_op = equation.index("-")
        while equation[place_of_op - count1] in float_try:
            num1 = str(equation[place_of_op - count1]) + num1
            count1 = count1 + 1
        while equation[place_of_op + count2] in float_try:
            num2 = num2 + str(equation[place_of_op + count2])
            count2 = count2 + 1
        result = float(num1) - float(num2)
        equation = equation.replace(str(num1) + "-" + str(num2), str(result), 1)
        count1 = 1
        count2 = 1
        num1 = ""
        num2 = ""
    while "+" in equation:
        place_of_op = equation.index("+")
        while equation[place_of_op - count1] in float_try:
            num1 = str(equation[place_of_op - count1]) + num1
            count1 = count1 + 1
        while equation[place_of_op + count2] in float_try:
            num2 = num2 + str(equation[place_of_op + count2])
            count2 = count2 + 1
        result = float(num1) + float(num2)
        equation = equation.replace(str(num1) + "+" + str(num2), str(result), 1)
        count1 = 1
        count2 = 1
        num1 = ""
        num2 = ""
    if equation != prev_result:
        prev_result = equation
        my_label = ttk.Label(root, text="Your New Answer Is: " + str(round(float(equation[3:-3]), 4)) + " !").pack(side="top")
    elif equation == prev_result:
        prev_result = equation

root = tk.Tk()
root.title("Advanced Calculator")
root.geometry("500x500")
root.resizable(0, 0)
root.attributes("-alpha", 1)
root.attributes("-topmost", 1)

entry_variable = tk.StringVar()
my_entry = ttk.Entry(root, textvariable=entry_variable).pack(side="top")

my_button = ttk.Button(root, text="Calculate!", command=calculate).pack(side="top")

root.mainloop()