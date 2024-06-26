import pandas as pd

def add_book():
  title_input = input("Enter title of book: ")
  author_input = input("Enter author of book: ")
  type_input = input("Enter type of book (paper, digital, or audio): ")
    # data of Player and their performance
  data = {
        'title': [title_input],
        'author': [author_input],
        'type': [type_input]
    }
  
    # Make data frame of above data
  df = pd.DataFrame(data)
  
    # append data frame to CSV file
  df.to_csv('myShelf.csv', mode='a', index=False, header=False)
  
    # print message
  print("Book added to your collection.")

def view_library():
  df = pd.read_csv('myShelf.csv')
  print(df)

def menu_input():
  print("1. Add book")
  print("2. View library")
  while True:
     menu_input = input("Please enter a number corresponding to your menu option:")
     print("You selected option:", menu_input)
     if menu_input == "1":
       add_book()
       break
     elif menu_input == "2":
         view_library()
         break 

menu_input()
