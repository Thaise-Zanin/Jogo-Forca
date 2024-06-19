#Nomes: Alice Bohnen Segatto, Thaise Chaves Zanin. RA: 1136046, 1136629

import os, time

def limparTela(tempo):
    time.sleep(tempo)
    os.system("cls")

def palavraOculta(palavraChave, letrasCorretas, letrasJogadas):
    palavraOculta = " "
    for letra in palavraChave:
        if letra in letrasCorretas or letra in letrasJogadas:
           palavraOculta += letra
        else:
           palavraOculta += "*"
    return palavraOculta

def desenharForca(erros):
    if erros == 0:
        print("  +---+")
        print("      |")
        print("      |")
        print("      |")
        print("      |")
        print("    __|__ ")
    elif erros == 1:
        print("  +---+")
        print("  O   |")
        print("      |")
        print("      |")
        print("      |")
        print("    __|__ ")
    elif erros == 2:
        print("  +---+")
        print("  O   |")
        print("  |   |")
        print("      |")
        print("      |")
        print("    __|__ ")
    elif erros == 3:
        print("  +---+")
        print("  O   |")
        print(" /|   |")
        print("      |")
        print("      |")
        print("    __|__")
    elif erros == 4:
        print("  +---+")
        print("  O   |")
        print(" /|\  |")
        print("      |")
        print("      |")
        print("    __|__")
    elif erros == 5:
        print("  +---+")
        print("  O   |")
        print(" /|\  |")
        print(" /    |")
        print("      |")
        print("    __|__")
    elif erros == 6:
        print("  +---+")
        print("  O   |")
        print(" /|\  |")
        print(" / \  |")
        print("      |")
        print("    __|__")
limparTela(0)


def jogoDaForca():
   limparTela(1)
   print("  Bem-vindos ao Jogo da Forca!  ")
   limparTela(2)
   nomeDesafiante = input("Insira o nome do Desafiante: ")
   nomeCompetidor = input("Insira o nome do Competidor: ")
   limparTela(2)

   print("Desafiante por favor insira a palavra chave e três dicas")
   limparTela(3)

   palavraChave = input("Insira a palavra chave: ")
   dica1 = input("Insira a Dica1: ")
   dica2 = input("Insira a Dica2: ")
   dica3 = input("Insira a Dica3: ")

   erros = 0
   letrasCorretas = []
   letrasJogadas = []
   tentativasRestantes = 6
   dicasRestantes = 3
   limparTela(3)

   print(f"{nomeCompetidor} a palavra chave tem: ", '*' * len(palavraChave))

   while '*' in palavraOculta(palavraChave, letrasCorretas, letrasJogadas) and tentativasRestantes > 0:
      print("Digite (0) para jogar")
      print("Digite (1) para solicitar dica")
      opcao = input("")
      if opcao == "1":
         if dicasRestantes == 3:
            print(f"Dica: {dica1}")
            dicasRestantes -= 1
         elif dicasRestantes == 2:
            print(f"Dica: {dica2}")
            dicasRestantes -=1
         elif dicasRestantes == 1:
            print(f"Dica: {dica3}")
            dicasRestantes -=1
         else:
            print("Você já usou todas as dicas!")
            
       
      elif opcao == "0":
          letra = input("Digite uma letra: ")
          if len(letra) == 1:
             letrasJogadas.append(letra)
             print("Letras Jogadas: ", letrasJogadas)   
             if letra in palavraChave:  
                letrasCorretas.append(letra)
                print("Palavra: ", palavraOculta(palavraChave, letrasCorretas, letrasJogadas)) 
                print("Você acertou uma letra!")        
             if '*' not in palavraOculta(palavraChave, letrasCorretas, letrasJogadas):   
                print(f"Parabéns {nomeCompetidor}, você ganhou!")
                print("Você deseja jogar novamente (2) ou deseja sair (3)")
                opcaoFinal = input("")
                if opcaoFinal == "2":
                    print("Reiniciando jogo...")
                    jogoDaForca()
                elif opcaoFinal == "3":
                    print("Encerrando jogo..")
                    limparTela(1)
                    quit()
                else:
                    print("Opção Inválida.")
                break
             
             elif letra not in palavraChave: 
                tentativasRestantes -= 1
                erros += 1
                print(f"Letra incorreta! Você tem mais {tentativasRestantes} tentativas restantes.")
                print(f"Total de erros: {erros}")
                desenharForca(erros)
          else:
                print("Opção Inválida. Por favor, insira apenas uma letra.")
      else:
          print("Opção Inválida")

   if tentativasRestantes == 0:
       print(f"A palavra chave era: {palavraChave}")
       print(f"Suas tentativas acabaram, você perdeu {nomeCompetidor}.")
       print(f"Parabéns {nomeDesafiante} você ganhou!")
       print("Você deseja jogar novamente (2) ou deseja sair (3)")
       opcaoFinal = input("")
       if opcaoFinal == "2":
          print("Reiniciando jogo...")
          jogoDaForca()
       elif opcaoFinal == "3":
          print("Encerrando jogo..")
          limparTela(1)
          quit()
       else:
          print("Opção Inválida.")

jogoDaForca()