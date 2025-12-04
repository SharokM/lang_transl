translations = {
  "hello":"hola",
  "thank you":"gracias",
  "sorry":"lo siento",
  "connect":"instalar",
  "save":"guardar",
  "scroll":"desplazar",
  "paste":"lo pegar",
  "close":"cerrar",
  "open":"abrir"
}

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


