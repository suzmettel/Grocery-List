#To Do List
#1/10/24
#Suzanna M, Lam M

#Intialize
print("""Welcome to the grocery list. 
          You can add an item (0), 
          View the list (1), 
          Mark a task as done (2), 
          Remove an item (3),
          Clear all items(4),
          Sort items in list (5),
          Count number of items (6),
          and Quit Program (7)""")
grocery=[]

#Function
def add():
    item1=input("What do you want to add: ")
    grocery.append(item1)

def view():
    print(grocery)

def mark():
    ans=input("select a item from the list to mark as done: ")
    i=grocery.index(ans)
    grocery[i]=ans+" X"

def remove():
    thing2=input("What item do you want to remove: ")
    i=grocery.index(thing2)
    grocery.pop(i)

def clear():
    grocery.clear()

def exit():
    print("Goodbye.")
    quit()

def sort():
    grocery.sort()

def count():
    number=len(grocery)
    print(number)

def groceryList():
    user=int(input("Which option: "))
    if (user==0):
        add()
    elif (user==1):
        view()
    elif (user==2):
        mark()
    elif (user==3):
        remove()
    elif(user==4):
        clear()
    elif(user==5):
        sort()
    elif(user==6):
        count()
    elif(user==7):
        exit()
    else:
        print("Please enter a number from 0-4")
        groceryList()
    groceryList()

#Main
groceryList()