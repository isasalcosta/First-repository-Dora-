venda = int(input("Digite o valor da venda"))
if venda < 500:
  print("Sem desconto")
elif venda > 500 and < 1000:
  print("Desconto de 5%", venda*0.95)
elif venda >=1000 and venda < 5000: 
  print("Desconto de 10%", venda*0.90)
else:
  print("Desconto de 15%"< venda *0.85)
