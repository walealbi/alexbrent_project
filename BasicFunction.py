import pandas as pd
from rapidfuzz import fuzz, process

srch_data = pd.read_csv('./srch_library_db.csv')
data = pd.read_csv('./library_db.csv')


def add_book():
  book_title = input("Enter title: ")
  df =pd.DataFrame(data)
  new_row = {'ID':'', 'img_url':'', 'book_title': book_title, 'notes':''}
  df.loc[len(df)] = new_row
  df = df._append(new_row, ignore_index=True)


def menu():
  print("Your Library\n")
  print("1. Manually Add a Book")
  print("2. View your Library")
  print("3. Search our Database")
  print("4. Exit")

def view_library():
  df =pd.DataFrame(data)
  print(df)
  
def search(): 
  def fuzzy_find(df, search_term, n=1):
      matches = process.extract(search_term, df["book_title"], scorer=fuzz.token_set_ratio, limit=n)
      first_match = matches[0] # grab only first match, ignore n for now
      text = first_match[0] # the text of the first match
      match_score = first_match[1] # the similarity score of the first match
      index = first_match[2] # the index in the data frame of the first match
      print(f"searched for {search_term}\nbest match: {text}, {index}, {match_score}")
      return text, index, match_score
  df = pd.read_csv('srch_library_db.csv')   #  read the csv file into a data frame
  match_percent = 50
  
  while True:
      # 1) ask the user for the title search term 
      search_term = input("What title do you want to search for? ")
      # 2) ask for a quality threshold (our match %), give it a default of 50. I the user just hits return, keep the existing value otherwise update it
      new_match_percent_str = input(f"What quality threshold do you want, currently {match_percent} ")
      if new_match_percent_str:
          match_percent = int(new_match_percent_str) 
      # 3) call fuzzy find to find the best match for the term, get the text and score
      text, index, match = fuzzy_find(df, search_term)
      # 4) print the summary of the found book if the match score is greater than or equal to our threshold, else print a no good match found statement
      if match >= match_percent:
          print(f"The closest we have is {text}")
      else:
          print(f"match of {match} is lower than {match_percent}, no good match found!")


while 1:
   menu()
   menu_input = int(input("\nPlease enter a number corresponding to your menu option:"))
   print("\nYou selected option:", menu_input)
   if menu_input == 4:
      print("Exiting...")
      break
   elif menu_input == 2:
      view_library()
   elif menu_input == 1:
      add_book()
   elif menu_input == 3:
      while 1:
         search()
   else:
      print("Invalid option, try again")