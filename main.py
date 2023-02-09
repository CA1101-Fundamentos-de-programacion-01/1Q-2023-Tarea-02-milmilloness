def calcularDispositivoBebe(edad, peso, altura):
  if(0 <= edad <= 1 and 0 <= peso <= 13 and 0 <= altura <= 75):
    print("Portabebé")
  elif(1 <= edad <= 4 and 9 <= peso <= 18 and 75 <= altura <= 110):
    print("Silla")