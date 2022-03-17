nCiclo_String = input("Quanti numeri vuoi inserire? ") #chiedi di inserite un numero
while not nCiclo_String.isnumeric(): #ciclo un controllo sull'input
   print("Il valore inserito non è un numero intero! Valore inserito: ", nCiclo_String)
   nCiclo_String = input("Quanti numeri vuoi inserire? ")
nCiclo = int(nCiclo_String) #coverto la string di numeri in int

i = 0
sum = 0
while (i < nCiclo):
   n_String = input("Inserisci un numero: ")
   while not n_String.isnumeric():
      print("Il valore inserito non è un numero intero! Valore inserito: ", n_String)
      n_String = input("Inserisci un numero: ")
   n = int(n_String)
   sum += n
   i += 1

print("La somma dei numeri inseriti è :", sum)
