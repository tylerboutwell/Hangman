word = "computer"

print("Enter your name:")
username = input()
print("Welcome " + username)

word_array = []
for i in word:
    word_array.append(i)

word_status = []
for i in range(len(word_array)):
    word_status.append("_")

for i in range(7):
    print("Guess the word: ")
    for i in word_status:
        print(i, end=" ")
    print()
    print("Enter a letter:")
    user_letter = input()
    if len(user_letter) != 1:
        print("You must enter 1 letter!")
