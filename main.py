import csv

def intro():
    print("Welcome to the English-German-Filipino Translator! \n\nEnter a word then press 'Enter'.")
    print('\nType "exit" at any time to exit')


translations = {
}

with open("english_german_filipino_200.csv", "r") as words:
    reader = csv.DictReader(words, delimiter=",")
    for line in reader:
        english = line["English"].lower()
        german = line["German"].lower()
        filipino = line["Filipino"].lower()
        translations[english] = [german, filipino]
        print(line["English"], line["German"], line["Filipino"])


done = False


intro()

def exit():
    print("\nThank you for using the translator. Goodbye!")

while not done:
    word = input("Enter a word to translate \n(E.g. hello, thank you, sorry): ").strip().lower()
    if word == "exit":
        exit()
        done = True
    elif word in translations:
        print(f'\nThe translation of "{word}" in German is: \n"{translations[word] [0]}"')
        print(f'\nThe translation of "{word}" in Filipino is: \n"{translations[word] [1]}"')
    else:
        print(f'\n"{word}" is not currently in our dictionary, thank you for your patience while we update our vocabulary database.')


