from random import choice
from time import sleep


word = "Huh"
def inWord():
  if "hi" or "hello" in word:
    #print("Hello")
    sleep(1)

class Ophelia:
  name = "Ophelia"
  greetings = [
    "Hi.",
    "Hi!",
    "Hi, I'm Ophelia.",
    "Hello.",
    "Hello!",
    "Hello, my name is Ophelia."
  ]

  
  # this is where all the Responses will go.
  Hello = {
    "Hi."
    "Hello"
  }
  
class Noah:
  name = "Noah"
  greetings = [
    "Howdy!",
    "Howdy, I'm Noah",
    "My name be Noah",
    
  ]
  Responses = [
    "Hello!",
    "Hi."
    ]

class Responses:
  Ophelia

def test(bot):
  if bot == "Ophelia":
    testBot = Ophelia
  if bot == "Noah":
    testBot = Noah


if __name__ == "__main__":
  print("What bot do you want to chat to?\nChoices will be listed:")
  sleep(1)
  botChoice = input("Noah or Ophelia? ")
  botTemplate = "{0}: ".format(botChoice)
  if botChoice == "Ophelia":
    Standard = Ophelia
  print(botTemplate + choice(Standard.greetings))


  if botChoice == "Noah":
    Standard = Noah
    print(choice(Standard.greetings))

  while word != 'exit' or 'Exit':
   print(Standard.Responses.Hello)
   word = input("You: ")
   word = word.upper()
   if word ==  "exit":
    break
   else:
     inWord()
  
if __name__ == "__init__":
  print("Hi")