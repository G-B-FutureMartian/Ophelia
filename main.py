from random import choice 
from time import sleep


#word = "Huh"

def inWord(word):
  if "hi" or "hello" in word:
    #print("Hello")
    sleep(1)

class Ophelia:
  name = "Ophelia"
  firstGreetings = [ # Greetings for when first meeting chatbot
    "Hi.",
    "Hi!",
    "Hi, I'm Ophelia.",
    "Hello.",
    "Hello!",
    "Hello, my name is Ophelia."
  ]

  # this is where all the Responses will go.
  # Response types include:
  # greetings
  greetings = [
    "Hi.",
    "Hello"
  ]
  
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
    chatBot = Ophelia

  if botChoice == "Noah":
    chatBot = Noah
  word = "placeholder"
  while word != 'exit' or 'Exit':
    print(botTemplate + choice(chatBot.greetings))
    word = input("You: ")
    word = word.upper()
    inWord(word)
  
if __name__ == "__init__":
  print("Hi")