print("Lista")
dt= ["Joana", "Diana", "Dayanne", "Dora", "Fernanda", "Raqueka",] 
while True: 
print("Menu")
print("------------------Arquivo lista---------------------")
print("1) mostrar arquivo) 2 Cadastrar) 3 lista) 0u 4 para sair ) 5 para alterar o nome) 6 para alterar) 7 para apagar")
escolha = input("Escolha um número : ") 
if escolha== "!": 
  print(dt) 
elif escolha== "2": 
  nome= input("Entre com o nome:") 
  dt.append(nome) 
  dt.pop(5) 
  dt.remove("Fernanda") 
elif escolha== "3":
     for x in dt: print(x) 
elif escolha== "4": 
  print("Sair do programa") 
  break 
elif escolha == "5": 
  nome = input("Escolhab um nome para alterar:") 
  for c in range(len(dt)): 
    novonome = imput("Qual é o novo nome:") 
    dt(c) = novonome 
    break 
else: print("Não encontrado") 
