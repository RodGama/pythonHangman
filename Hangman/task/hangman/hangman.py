# Write your code here
import random

print("H A N G M A N ")
acao = input("Type \"play\" to play the game, \"exit\" to quit:").strip()
while acao not in ["play", "exit"]:
    acao = input("Type \"play\" to play the game, \"exit\" to quit:").strip()

while acao == "play":
    word_list = ["python", "java", "kotlin", "javascript"]
    resp = random.choice(word_list)
    resp_1 = resp
    tentativas = 0
    palavra_cript = '-' * (len(resp))
    letras_tentadas = set()
    while tentativas < 8:
        print(" ")
        print(palavra_cript)
        #  print()
        letra = input('Input a letter : ')
        #  letra = str(input("Input a letter: > "))
        if letra == "" or letra == " ":
            print("It is not an ASCII lowercase letter")
        elif len(letra) > 1:
            print("You should input a single letter")
        elif not letra.isalpha():
            print("It is not an ASCII lowercase letter")
        elif letra.isupper():
            print("It is not an ASCII lowercase letter")
        elif letra.isnumeric():
            print("It is not an ASCII lowercase letter")
        elif letra in letras_tentadas:
            print("You already typed this letter")
        elif letra.lower() in resp:
            for char in range(resp_1.count(letra)):
                palavra_cript = palavra_cript[:resp_1.find(letra)] + letra + palavra_cript[resp_1.find(letra) + 1:]
                resp_1 = resp_1.replace(letra, "-", 1)
            letras_tentadas.add(letra)
        else:
            print("No such letter in the word")
            tentativas = tentativas + 1
            letras_tentadas.add(letra)

        if "-" not in palavra_cript:
            break

    if palavra_cript != resp:
        print("You are hanged!")
    else:
        print(resp)
        print("You guessed the word!")
        print("You survived!")
    print("")
    acao = input("Type \"play\" to play the game, \"exit\" to quit:").strip()

    while acao not in ["play", "exit"]:
        acao = input("Type \"play\" to play the game, \"exit\" to quit:").strip()
