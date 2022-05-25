tasks = [
    {'name' : 'Write email to Jan', 'completed' : True},
    {'name' : 'Sweep front porch', 'completed' : True},
    {'name' : 'Call mom', 'completed' : False}
]


def list_tasks():
    """List out task."""
    for index, task in enumerate(tasks):
        print(str.format('{}: {} (Completed: {})', index, task['name'], task['completed']))


def task_text():
    """Add new task as dictionary to the task list."""
    new_task = {'name': input("What task would you like to add: "), 'completed': False}
    tasks.append(new_task)

    # Using the above task_text variable, create a dictionary named new_task and set completed to False

    # Then, add new_task to the tasks list


# You will need a function to handle removing a task.
    # When this function is run, list out the tasks. Hint! There is already a function that handles this

    # Here, create a variable that uses input. The user should be able to input the index number of the task to be removed. Hint! You will need to wrap the input() function within the int() function so the user's input is read as a number.

    # Here, delete the task in the tasks list based on the above variable

def remove_task():
    """Select task in list by index number and remove task."""
    del tasks[int(input('Task number to remove: '))]     


# You will need a function to handle marking a task complete.
    # When this function is run, list out the tasks. Hint! There is a function that already does this for you.

    # Here, create a variable that uses input. The user should be able to input the index number of the task to be marked complete. Hint! You will need to wrap the input() function within the int() function so the user's input is read as a number.

    # Mark the task complete in the tasks list based on the variable you created above. Hint! you will need to use two sets of square brackets to find the index and set the appropriate key to True 

def completed_task():
    """Select task in list by index number then select key completed and change the value to true."""
    tasks[int(input('Task number you would like to complete: '))]['completed'] = True

def unmark_task():
    """Select task in list by index number then select key completed and change the value to false."""
    tasks[int(input('Task number you would like to complete: '))]['completed'] = False

menu_text = """
====================
1. List the tasks
2. Add a task
3. Remove a task
4. Mark task complete
5. Mark task not complete
6. Quit

What would you like to do? """

program_is_running = True

while program_is_running:
    decision = input(menu_text)
    if decision == '1':
        list_tasks()

    # Add elif statements for inputs 2, 3, and 4
    elif decision == '2':
        list_tasks()
        task_text()
        
    elif decision == '3':
        list_tasks()
        remove_task()
    elif decision == '4':
        list_tasks()
        completed_task()

    elif decision == '5':
        list_tasks()
        unmark_task()

    elif decision == '6':
        program_is_running = False
        
    else:
        print('please choose a valid option')


