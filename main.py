import csv

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

print('Type "exit" at any time to exit')

while not done:
    word = input("Enter a word to translate (hello, thank you, sorry): ").strip().lower()
    if word == "exit":
        done = True
    elif word in translations:
        print(f'The translation of "{word}" is "{translations[word]}"')
    else:
        print(f'"{word}" is not currently in our dictionary, thank you for your patience while we update our vocabulary database.')


