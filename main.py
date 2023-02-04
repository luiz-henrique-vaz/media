nota1 = float(input('digite n1(0-10): '))      
nota2 = float(input('digite n2(0-10): '))

media = (nota1 + nota2) / 2
print('Media das notas:' + str(media))
if (media < 7):
  print('Reprovado')
else:
  if media != 10:
     print('Aprovado')
  else:
      print('Aprovado com distinção')
