#!/usr/bin/ python
'''
Python v3.7
August 7, 2019
Homework 6 - Kassandra Bethune
hw6.py
GitHub URL: https://github.com/FatalRoot/hw6
'''

infile = r"C:\Users\Kass\Documents\todo.txt"
# open and read todo.txt
with open(infile, 'r+') as todo_file:
    lines = todo_file.readlines()

#create dict to store data from for loop
task_dict = {}

for line in lines:
    task = line.split(",")[0].strip()
    priority = line.split(",")[1].strip()
    task_dict[task] = priority

#view items in todo list
def view_items(input_dict):
    for key, val in input_dict.items():
        print(key, val)

#add new items to todo list
def add_task(input_dict, new_key, new_value):
    input_dict[new_key] = new_value

#remove items from list
def remove_task(input_dict, task_name):
    if task_name in task_dict.keys():
        del task_dict[task_name]
    else:
        print('Task not found in todo list.')

#save items to list
def save_todo(infile, input_dict):
    with open(infile, 'w') as fh:
        for key, value in input_dict.items():
            fh.write('{},{}\n'.format(key, value))

#provide options to user and start while loop
while(True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()

    #if user selects 1, call view_items function
    if (strChoice.strip() == '1'):
        view_items(task_dict)

    #if user selects 2, call add_task function
    elif(strChoice.strip() == '2'):
        new_key = input('Enter a new task name: ')
        new_value = input('Enter the new task\'s priority from low to high: ')
        add_task(task_dict, new_key, new_value)

    #if user selects 3, call remove_task function
    elif(strChoice.strip() == '3'):
        remove_key = input('Enter the task name to remove: ')
        remove_task(task_dict, remove_key)

    #if user selects 4, call save_todo function
    elif(strChoice.strip() == '4'):
        save_todo(infile, task_dict)

    #if user selects 5, break out of while loop and close file
    elif(strChoice.strip() == '5'):
        break
        todo_file.close()
