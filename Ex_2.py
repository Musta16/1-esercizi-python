n1_String = input("Inserisci il primo numero: ") #chiedo l'inserimento di un numero
while not n1_String.isnumeric(): #ciclo controllo l'effettivo inserimento di un numero
    print("Il valore inserito non è un numero! Valore inserito: ", n1_String)
    n1_String = input("Inserisci il primo numero: ")
n1 = float(n1_String) #converto la Stringa di numeri in un Float

op = input("inserisci operatore (+, -, *, /): ") #chiedo l'inserimento di un simbolo
while op != "+" and op != "-" and op != "*" and op != "/": #ciclo controllo l'effettivo inserimento
    print("Il valore inserito non è un simbolo d'operazione! Valore inserito: ", op)
    op = input("inserisci operatore (+, -, *, /): ")

n2_String = input("Inserisci il secondo numero: ") #chiedo l'inserimento di un numero
while not n2_String.isnumeric(): #ciclo controllo l'effettivo inserimento di un numero
    print("Il valore inserito non è un numero! Valore inserito: ", n2_String)
    n2_String = input("Inserisci il secondo numero: ")
n2 = float(n2_String) #converto la Stringa di numeri in un Float

if (op == "+"):
    print("Il risultato è: ", n1 + n2)
elif (op == "-"):
    print("Il risultato è: ", n1 - n2)
elif (op == "*"):
    print("Il risultato è: ", n1 * n2)
elif (op == "/"):
    print("Il risultato è: ", n1 / n2)
else:
    print("Non hai inserito un operatore corretto!")
