while True: 
    try:
        numero = int(input("Enter an int number: "))
        print(5/numero)
        break
    except (ValueError, ZeroDivisionError):
        print("Valor errado ou não é possível dividir por 0")
    except:
        print("Desculpe, algo errado aconteceu...")
       
        