import csv

translations = {

}

with open("translations.csv", "r") as words:
    reader = csv.DictReader(words, delimiter=",")
    for line in reader:
        english = line["English"].lower()
        spanish = line["Spanish"].lower()
        french = line["French"].lower()
        translations[english] = [spanish, french]
        print(line["English"], line["French"], line["Spanish"])


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


