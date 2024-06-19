import pandas as pd
from rapidfuzz import fuzz, process




def add_book(search_term, srch_data, mylib):
  row = search(search_term, srch_data)
  if row is None:
     print("No title found.")
  else:
      mylib = mylib._append([mylib, row], ignore_index=True)
      print("Book added to your library!")


def run_menu_functions(srch_data, mylib):
  print("Your Library\n")
  print("1. Manually Add a Book")
  print("2. View your Library")
  print("3. Search our Database")
  print("4. Exit")

  while True:
   menu_input = input("\nPlease enter a number corresponding to your menu option:")
   print("\nYou selected option:", menu_input)
   if menu_input == "4":
      print("Exiting...")
      #save mylib back to csv dataframe_ always ignore index
      break
   elif menu_input == "2":
      view_library(mylib)
   elif menu_input == "1":
      search_term = input("Enter search_term: ")
      add_book(search_term, srch_data, mylib)
   elif menu_input == "3":
      search_term = input("Enter search_term: ")
      search(search_term, srch_data)
   else:
      print("Invalid option, try again")
  

def view_library(srch_data):
  print(srch_data)

def fuzzy_find(srch_data, search_term, n=1):
   matches = process.extract(search_term, srch_data["book_title"], scorer=fuzz.token_set_ratio, limit=n)
   first_match = matches[0] # grab only first match, ignore n for now
   text = first_match[0] # the text of the first match
   match_score = first_match[1] # the similarity score of the first match
   index = first_match[2] # the index in the data frame of the first match)
   return text, index, match_score
  
def search(search_term, srch_data): 

   
   match_percent = 50



   # 2) call fuzzy find to find the best match for the term, get the text and score
   text, index, match = fuzzy_find(srch_data, search_term)
   # 3) print the summary of the found book if the match score is greater than or equal to our threshold, else print a no good match found statement
   if match >= match_percent:
         row = srch_data.loc[index]
         text = row["book_title"]
         print(f"The closest we have is {text}")
         return row
   else:
         print(f"match of {match} is lower than {match_percent}, no good match found!")
         return None

# main
srch_data = pd.read_csv('./srch_library_db.csv')
mylib = pd.read_csv('./library_db.csv')
# search_term = input("Enter search_term: ")
# search(search_term, srch_data)
run_menu_functions(srch_data, mylib)