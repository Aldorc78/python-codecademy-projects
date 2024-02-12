#program that simulates a match of scrabble
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

#using dict comprehension to create a dict out of the list above
letter_to_points = {letter:points for letter,points in zip(letters,points)}

#Adding a new space char to the dict so spaces has the value of 0
print(letter_to_points)
letter_to_points[" "] = 0
print(letter_to_points)

#creating a function that iterates trough every char of a string and sums every point of the word
def score_word(word):
  word = word.upper() #making every letter upper case
  point_total = 0
  for letter in word: 
    point_total += letter_to_points.get(letter,0)
  return point_total

#checking if function works
print("testing")
brownie_points = score_word("BRoWNIe")
print(brownie_points, "\n")

#creating a list containing results of a match with player name as a key and a list of the words said by that player
player_to_words = {"player1": ["BLUE","TENNIS","EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"], "Lexi Con": ["ERASER", "BELLY", "HUSKY" ], "Prox Reader": ["ZAP", "COMA", "PERIOD"] }

#iterating trough every word in every player to sum the total points of each player
player_to_points = {}
def update_point_totals():   
  for player, phrases in player_to_words.items():
      
      player_points = 0
      for word in phrases:
        player_points += score_word(word)
      player_to_points[player] = player_points 

update_point_totals()
print(player_to_points)

#function that take in a player and a word, and add that word to the list of words played by player
def play_word(player, word):
  list_of_words = player_to_words[player]
  list_of_words.append(word)
  player_to_words[player] = list_of_words

#testing play_word function
play_word("player1", "HOLA")     
print(player_to_words, "\n")
print("updating points")
update_point_totals()
print(player_to_points)