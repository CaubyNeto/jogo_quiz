print("Bem-vindo ao Grande Quiz do Python!")
jogar = input("Você quer jogar? Digite sim ou não: ")

if jogar.lower() != "sim":
    quit()
print("Certo. Vamos jogar.")

def pergunta1():
    resposta = ""
    fora_de_resposta = False
    contagem_de_resposta = 0
    
    while resposta != "1991" and not(fora_de_resposta):
        resposta = input("Quando o Python foi criado? ")
        if resposta != "1991":
            print("Incorreto. Tente novamente.")
        contagem_de_resposta += 1
        if contagem_de_resposta == 5:
            fora_de_resposta = True
            
    if fora_de_resposta:
        print("Incorreto. É 1991.")
    else:
        print("Correto!")
pergunta1() 
    
