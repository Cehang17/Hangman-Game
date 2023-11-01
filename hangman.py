import random
name_list = ["Oliver","Jake",	"Noah","Jack","Connor","Liam","John","Harry",
             "Callum","Mason","Robert","Jaacob","Kyle","William","Thomas",
             "Joe","Ethan","David","George","Reece","Michael","Richard",
             "Oscar","Rhys","Alexander","Joseph","James","Charlie","Charles",
             "Damian","Daniel","Amelia","Margaret","Emma","Mary","Samantha",
             "Olivia","Patricia","Isla","Bethany","Sophia","Jennifer","Emily",
             "Elizabeth","Poppy","Joanne","Ava","Linda","Megan","Mia","Barbara",
             "Isabella","Victoria","Susan","Lauren","Abigail","Lily","Michelle",
             "Madison","Jessica","Sophie","Tracy","Charlotte","Sarah","Lillia"]

word = random.choice(name_list).lower()
life = 5
guessedletters = ""
while life != 0:
  realword = ""
  for letter in word:
    if letter in guessedletters:
      realword = realword + letter
    else:
      realword = realword + "_ "
  print(realword)

  if realword == word:
    print(f"Congratulations! You found the word ({word.capitalize()}).")
    break

  guess = input("Guess a letter: ").lower()
  guessedletters = guessedletters + guess
  if guess not in word:
    life -= 1
    print("The letter you entered is not in the word")
    print("")
    if life == 0:
      print("you have no life left")
      print(f"True word was {word}.")
      break
    if life == 1:
      print(f"You have only {life} life left")
      continue
    print(f"You have {life} lifes left ")

