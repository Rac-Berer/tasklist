# import modules
import datetime as dt
import os
import pickle

# Design the task class
class Task:
    def __init__(self, name, due_date=None, category="General", notes=""):
        self.name = name
        self.due_date = due_date
        self.category = category
        self.completed = False
        self.notes = notes # Optional notes for the task
        
    def change_name(self, new_name):
        self.name = new_name

    def change_due_date(self, new_date):
        self.due_date = new_date

    def complete(self):
        self.completed = True

# Initialize the tasks list
tasks = []
predefined_categories = ["Daily Essentials", "Personal Development", "Household Chores", "Social", "Finance", "Errands", "Leisure"]

# Building the Menu
menu = {
    1: "Add New Task",
    2: "View All Tasks",
    3: "Mark Task as Completed",
    4: "Mark Task as Incomplete",
    5: "Delete Task",
    6: "Save Tasks",
    7: "Load Tasks",
    8: "Sort Tasks",
    9: "Filter Tasks",
    10: "Edit Task Notes",
    11: "Quit"
}
# Printing the Menu options
print('\nTask List Menu')
for key, value in menu.items():
    print(f'{key} -- {value}')

choice = input('Please enter your selection: ')

# Implementing the Functions and adding a new task
def add_task():
    predefined_tasks = [
        ("Brush teeth", "Daily Essentials"),
        ("Drink water", "Daily Essentials"),
        ("Go to bed at set time", "Daily Essentials"),
        ("Plan meals", "Daily Essentials"),
        ("Take a shower", "Daily Essentials"),
        ("Take medication", "Daily Essentials"),
        ("Wake up at set time", "Daily Essentials"),
        ("Attend a workshop", "Personal Development"),
        ("Cook a new recipe", "Personal Development"),
        ("Draw or paint", "Personal Development"),
        ("Do yoga", "Personal Development"),
        ("Exercise", "Personal Development"),
        ("Go for a walk", "Personal Development"),
        ("Meditate", "Personal Development"),
        ("Practice a hobby", "Personal Development"),
        ("Practice a language", "Personal Development"),
        ("Practice gratitude", "Personal Development"),
        ("Practice mindfulness", "Personal Development"),
        ("Read a book", "Personal Development"),
        ("Try a new activity", "Personal Development"),
        ("Write in a journal", "Personal Development"),
        ("Do laundry", "Household Chores"),
        ("Dust furniture", "Household Chores"),
        ("Organize closet", "Household Chores"),
        ("Take out the trash", "Household Chores"),
        ("Vacuum living room", "Household Chores"),
        ("Wash dishes", "Household Chores"),
        ("Attend an event", "Social"),
        ("Call a friend", "Social"),
        ("Connect with a colleague", "Social"),
        ("Help a neighbor", "Social"),
        ("Host a game night", "Social"),
        ("Plan a meetup", "Social"),
        ("Respond to messages", "Social"),
        ("Donate to charity", "Finance"),
        ("Pay bills", "Finance"),
        ("Review budget", "Finance"),
        ("Review investments", "Finance"),
        ("Transfer money to savings", "Finance"),
        ("Grocery shopping", "Errands"),
        ("Mail a letter", "Errands"),
        ("Make an appointment", "Errands"),
        ("Personal shopping", "Errands"),
        ("Refill prescriptions", "Errands"),
        ("Take pet to the vet", "Errands"),
        ("Go to a concert", "Leisure"),
        ("Listen to music", "Leisure"),
        ("Plan a trip", "Leisure"),
        ("Play a game", "Leisure"),
        ("Visit a museum", "Leisure"),
        ("Volunteer for a cause", "Leisure"),
        ("Watch a show or movie", "Leisure"),
    ]

    print("\nWould you like to add a predefined task or create a new one?")
    print("1. Choose from predefined tasks")
    print("2. Enter a new task")

    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        print("\nSelect a predefined task:")
        for i, (name, category) in enumerate(predefined_tasks, start=1):
            print(f"{i}. {name} ({category})")

        task_choice = input("Enter the number of the predefined task: ")

        if task_choice.isdigit():
            task_choice = int(task_choice)
            if 1 <= task_choice <= len(predefined_tasks):
                name, category = predefined_tasks[task_choice - 1]
            else:
                print("Invalid choice.")
                return
        else:
            print("Invalid input.")
            return
    elif choice == "2":
        name = input("Enter task name: ")
        

        print("\nChoose a category from the list:")
        for i, category in enumerate(predefined_categories, start=1):
            print(f"{i}. {category}")

        category_choice = input("Enter the number corresponding to your chosen category: ")
        category = predefined_categories[int(category_choice) - 1] if category_choice.isdigit() else "General"

    else:
        print("Invalid choice. Returning to menu.")
        return
    due_date = input("Enter due date (MM-DD-YYYY) or press Enter to skip: ")
    if due_date:
        try:
            dt.datetime.strptime(due_date, "%m-%d-%Y")
        except ValueError:
            print("Invalid date format. Please use MM-DD-YYYY.")
            return
    notes = input("Enter any additional notes for this task (or leave blank): ")
    new_task = Task(name, due_date if due_date else None, category, notes)
    tasks.append(new_task)
    save_tasks()
    print(f"Task '{name}' added to category '{category}' with notes: '{notes}'")


# Viewing all tasks
def view_tasks():
    print("\nAll Tasks by Category:")

    if not tasks:
        print("No tasks available.")
        return

    categorized_tasks = {}
    for task in tasks:
        categorized_tasks.setdefault(task.category, []).append(task)

    # Ensure only manually added tasks are displayed
    # for category, task_list in categorized_tasks.items():
        # print(f"\nCategory: {category}")
        # for i, task in enumerate(task_list, start=1):
            # due_date_display = task.due_date if task.due_date is not None else "No due date assigned"
            # print(f"  {i}. {task.name} - Due: {due_date_display} - Completed: {task.completed}")


    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task.name} (Category: {task.category}, Due: {task.due_date or 'No due date'} - Completed: {task.completed})")
        if task.notes:
            print(f"   Notes: {task.notes}")




 # Function to edit task notes
def edit_task_notes():
    view_tasks()  # Display tasks before editing

    try:
        index = int(input("Enter the task number to edit notes: ")) - 1
        if 0 <= index < len(tasks):  # Ensure index is valid
            task = tasks[index]
            print(f"Current notes for '{task.name}': {task.notes}")
            new_notes = input("Enter new notes (or leave blank to keep existing): ")

            if new_notes.strip():
                task.notes = new_notes
                print(f"Notes updated for '{task.name}'.")
            else:
                print("No changes made.")

            save_tasks()  # Save changes
        else:
            print("Invalid task number. Please try again.")
    except ValueError:
        print("Please enter a valid task number.")



# Marking Tasks as completed
def complete_task():
    view_tasks() # Show all tasks before marking as completed
    if not tasks:
        print('No tasks available to mark as completed.')
        return
    index = int(input('Enter the task number to mark as completed: ')) - 1
    if 0 <= index < len(tasks): # Ensure index is within range
        tasks[index].complete()
        save_tasks()  # Save tasks after marking one as completed
        print("Task marked as completed.")
    else:
        print('Invalid task number. Please try again.')

# Marking Tasks as incomplete
def incomplete_task():
    view_tasks() # Show all tasks before marking as incomplete
    if not tasks:
        print('No tasks available to mark as incomplete.')
        return
    index = int(input('Enter the task number to mark as incomplete: ')) - 1
    if 0 <= index < len(tasks): # Ensure index is within range
        tasks[index].completed = False
        save_tasks()  # Save tasks after marking one as incomplete
        print("Task marked as incomplete.")
    else:
        print("Invalid task number.")


# Deleting Tasks by Category
def delete_task_by_category():
    # Get a list of categories
    predefined_categories = set(task.category for task in tasks)
    print("\nAvailable Categories:")
    for i, category in enumerate(predefined_categories, 1):
        print(f"{i}. {category}")

    # User selects a category
    try:
        category_index = int(input('Enter the category number to view tasks: ')) - 1
        selected_category = list(predefined_categories)[category_index]

        # Filter tasks by chosen category
        category_tasks = [task for task in tasks if task.category == selected_category]

        # Show tasks from selected category
        if category_tasks:
            print(f"\nTasks in '{selected_category}':")
            for i, task in enumerate(category_tasks, 1):
                print(f"{i}. {task.name}")

            # User selects a task to delete
            task_index = int(input('Enter the task number to delete: ')) - 1
            if 0 <= task_index < len(category_tasks):
                deleted_task = category_tasks.pop(task_index)
                tasks.remove(deleted_task)
                print(f"Task '{deleted_task.name}' from category '{selected_category}' deleted successfully.")
            else:
                print('Invalid task number. Please try again.')

        else:
            print(f"No tasks found in category '{selected_category}'.")

    except (ValueError, IndexError):
        print('Invalid input. Please try again.')




# Save Tasks
def save_tasks():
    try:
        with open('tasks.dat', 'wb') as file:
            pickle.dump(tasks, file)
        print("Tasks saved successfully.")
    except Exception as e:
        print(f"Error saving tasks: {e}")

# Load Tasks
def load_tasks():
    global tasks
    try:
        with open('tasks.dat', 'rb') as file:
            tasks = pickle.load(file)
        print("Tasks loaded successfully.")
    except FileNotFoundError:
        print("No saved tasks found.")
    except Exception as e:
        print(f"Error loading tasks: {e}")


# Sorting and Filtering Tasks
def sort_tasks(by):
    if by == "name":
        sorted_tasks = sorted(tasks, key=lambda task: task.name.lower())
    elif by == "due_date":
        sorted_tasks = sorted(tasks, key=lambda task: task.due_date if task.due_date else "")
    elif by == "completed":
        sorted_tasks = sorted(tasks, key=lambda task: task.completed, reverse=True)
    elif by == "category":
        sorted_tasks = sorted(tasks, key=lambda task: task.category.lower())
    else:
        print("Invalid sorting option.")
        return

    print("\nSorted Tasks:")
    for i, task in enumerate(sorted_tasks, start=1):
        due_date_display = task.due_date if task.due_date else "No due date"
        print(f"{i}. {task.name} - Category: {task.category} - Due: {due_date_display} - Completed: {task.completed}")





# Filtering Tasks
def filter_tasks(selected_categories, filter_status=None):
    
            
    
    selected_categories = []
    if category_choices:
        choices = category_choices.split(",")  # Split input into a list
        for choice in choices:
            if choice.strip().isdigit():
                choice = int(choice.strip())
                if 1 <= choice <= len(predefined_categories):
                    selected_categories.append(predefined_categories[choice - 1])
                else:
                    print(f"Invalid category number: {choice}")
            else:
                print(f"Invalid input: {choice}")

    if not selected_categories:
        print("No valid categories selected. Returning to menu.")
        return
    print(f"Selected categories for filtering: {', '.join(selected_categories)}")

    # Optional: Allow filtering by completion status as well
    print("\nWould you like to filter by task completion status?")
    print("1. Completed tasks")
    print("2. Incomplete tasks")
    print("3. Skip status filtering")

    status_choice = input("Enter the number corresponding to your choice: ")

    filtered_tasks = [task for task in tasks if task.category in selected_categories]

    if status_choice == "1":
        filtered_tasks = [task for task in filtered_tasks if task.completed]
    elif status_choice == "2":
        filtered_tasks = [task for task in filtered_tasks if not task.completed]

    if not filtered_tasks:
        print(f"No tasks found in selected categories: {', '.join(selected_categories)} with selected filters.")
        return

    print("\nFiltered Tasks:")
    for i, task in enumerate(filtered_tasks, start=1):
        due_date_display = task.due_date if task.due_date else "No due date"
        print(f"{i}. {task.name} - Category: {task.category} - Due: {due_date_display} - Completed: {task.completed}")





# Main Application Loop
def display_menu():
    print('Task List Menu')
    for key, value in menu.items():
        print(f'{key} -- {value}')

while choice != '11':  # Updated to match "Quit"

    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        complete_task()
    elif choice == '4':  # Mark Task as Incomplete
        incomplete_task()        
    elif choice == '5':
        delete_task_by_category()
    elif choice == '6':
        save_tasks()
        print("Tasks saved successfully.")
    elif choice == '7':
        load_tasks()
        print("Tasks loaded successfully.")

    elif choice == '8':  # Sorting tasks
        print("\nChoose a sorting method:")
        sorting_options = {
            1: "name",
            2: "due_date",
            3: "completed",
            4: "category"
        }
    
        for key, value in sorting_options.items():
            print(f"{key}. {value.replace('_', ' ').title()}")  # Display options in user-friendly format
    
        sort_choice = input("Enter the number corresponding to your sorting method: ")
    
        if sort_choice.isdigit():
            sort_choice = int(sort_choice)
            if sort_choice in sorting_options:
                sort_by = sorting_options[sort_choice]  # Get the correct sorting key
                sort_tasks(sort_by)
            else:
                print("Invalid choice. Returning to menu.")
        else:
            print("Invalid input. Returning to menu.")
    elif choice == '9':  # Filtering tasks
        print("\nChoose categories to filter by. Select multiple numbers (comma-separated):")

        # Ensure predefined_categories is accessible
        if 'predefined_categories' not in globals():
            print("Error: predefined_categories is not defined globally.")

        for i, category in enumerate(predefined_categories, start=1):
            print(f"{i}. {category}")

        category_choices = input("Enter the numbers corresponding to the categories (e.g., 1,3,5) or press Enter to skip: ")

        selected_categories = []
        if category_choices:
            choices = category_choices.split(",")  # Convert input into a list
            for choice in choices:
                if choice.strip().isdigit():
                    choice = int(choice.strip())
                    if 1 <= choice <= len(predefined_categories):
                        selected_categories.append(predefined_categories[choice - 1])
                    else:
                        print(f"Invalid category number: {choice}")
                else:
                    print(f"Invalid input: {choice}")

        if not selected_categories:
            print("No valid categories selected. Returning to menu.")
            continue

        filter_tasks(selected_categories)
        
    elif choice == '10':  # Edit task notes
        edit_task_notes()

    input('Press enter to return to menu: ')
    display_menu()
    choice = input('Please enter your selection: ')