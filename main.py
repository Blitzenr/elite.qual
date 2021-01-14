import random

# The bot is intended to be completely useless, maybe other than for humor (:
print("Welcome to the totally useless chat bot! The bot that will never solve your problems!")


response = input("What would you like help with? ")
print("May I help you with " + response + "?") 

# Giving the user answer choices, if one is picked, a certain response will be triggered
# Line 17, 20 and 23 from https://stackoverflow.com/questions/73663/how-to-terminate-a-python-script/73673#73673
response2 = input("Yes or No? ")
if response2 == ("Yes"):
  print("Good!")
elif response2 == ("No"):
  print("Understandable, have a great day!")
  raise SystemExit 
elif response2 == ("no"):
  print("Understandable, have a great day!")
  raise SystemExit
elif response2 == ("n"):
  print("Understandable, have a great day!")
  raise SystemExit

# The bot attempts to help you but utterly fails, terminating the process.
# Line 24 from https://stackoverflow.com/questions/73663/how-to-terminate-a-python-script/73673#73673
if response == input("Ok, let's get started. Could you better explain your issues? "):
 print("Splendid!") 
print("Sorry I cannot help you with " + response + "!")
print("Goodbye! Find a more useful bot!")
raise SystemExit 

# New Change 










