menu = """

[1] Depositar
[2] Sacar 
[3] Estrato
[0] Sair

"""


saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUE = 3

while True:
  
   opcao = int(input(menu))
   
   if opcao == 1:
    deposito = float(input("Digite valor do deposito"))
    if deposito <= 0:
      print("Deposito falhou! efetue um Deposito maior que R$1 real")
      #break
 
    else:
     saldo += deposito
     efetuado = f"Deposito realizado com sucesso de R${deposito:.2f} Reais"
     print(f"{efetuado}, saldo atual R${saldo:.2f} Reais")
     extrato.append(efetuado)
    


   if opcao == 2:
      saque = int(input("Digite valor que deseja sacar"))
      numero_saques += 1
      if saque > saldo:
       print("saldo insuficiente tente novamente")
       #break

      elif numero_saques > LIMITE_SAQUE:
       print("Quatidade de saques atigiu o limite")
       #break

      elif saque > limite:
       print(f"Saque ultrapassou o limite : R${limite} Reais")

      elif saque < 1:
       print("saque falhou! valor invalido")
       #break

      else:
       print(f"Saldo atual R${saldo} Reais")
       saldo -= saque
       efetuado = f"Saque realizado com sucesso de R${saque:.2f} Reais"
       print(f"{efetuado:}, saldo atual {saldo:.2f} Reais")
       extrato.append(efetuado)


   if opcao == 3:
    print("###############Extrato#################")
    for i in extrato:
     print(i)
    print(f"saldo: R${saldo:.2f}")
    print("#####################################")

   if opcao == 0:
    break
    
   else:
    print("Operação invalida")
