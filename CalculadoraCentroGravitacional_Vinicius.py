import math

def read_coordinates(prompt):
    coordinates = input(prompt).split("-")
    return list(map(int, coordinates))

def read_float(prompt):
    return float(input(prompt))

def read_integer(prompt):
    return int(input(prompt))

while True:
    areaFormas = 0
    menosAreaFormas = 0
    momentoEstaticoAddY = 0
    momentoEstaticoRemovY = 0
    momentoEstaticoAddX = 0
    momentoEstaticoRemovX = 0
    
    figurasAdd = read_integer("Quantas figuras de adicao?\n")
    figurasRemov = read_integer("Quantas de remocao?\n")
    
    # adicao
    for i in range(figurasAdd):
        tipoFigura = read_integer("Qual o tipo de figura de adicao?\n"
                                  "1- quadrado ou retângulo\n"
                                  "2- triangulo\n")
        
        if tipoFigura == 1 or tipoFigura == 2:
            base = read_coordinates("Quais as coordenadas em X da base? (separar por -)\n")
            baseConta = base[1] - base[0]
            altura = read_coordinates("Quais as coordenadas em Y da altura? (separar por -)\n")
            alturaConta = altura[1] - altura[0]
            area = baseConta * alturaConta
            
            if tipoFigura == 1:
                centroGx = (baseConta / 2) + base[0]
                centroGy = (alturaConta / 2) + altura[0]
            else:
                area = area / 2
                anguloReto = read_coordinates("Quais as coordenadas do angulo reto? (separar por -)\n")
                if anguloReto[0] > base[0]:
                    centroGx = (-baseConta / 3) + anguloReto[0]
                else:
                    centroGx = (baseConta / 3) + anguloReto[0]
                if anguloReto[1] > altura[0]:
                    centroGy = (-alturaConta / 3) + anguloReto[1]
                else:
                    centroGy = (alturaConta / 3) + anguloReto[1]
            momentoEstaticoAddX += centroGx * area
            momentoEstaticoAddY += centroGy * area
            areaFormas += area
        
        # circulo e derivados
        elif tipoFigura == 3 or tipoFigura == 4 or tipoFigura == 5:
            centroCirculo = read_coordinates("Quais as coordenadas do centro da figura? (separar por -)\n")
            raio = read_float("Qual o raio da figura?\n")
            area = math.pi * (raio ** 2)
            
            if tipoFigura == 3:
                centroGx = centroCirculo[0]
                centroGy = centroCirculo[1]
            elif tipoFigura == 4:
                area = area / 2
                direction = read_integer("Para qual direcao esta o semicirculo?\n"
                                         "1 - esquerda\n"
                                         "2 - baixo\n"
                                         "3 - direita\n"
                                         "4 - cima\n")
                if direction == 1 or direction == 3:
                    centroGy = centroCirculo[1]
                    if direction == 1:
                        centerX = -4 * raio / (3 * math.pi)
                    else:
                        centerX = 4 * raio / (3 * math.pi)
                    centroGx = centroCirculo[0] + centerX
                else:
                    centroGx = centroCirculo[0]
                    if direction == 2:
                        centerY = -4 * raio / (3 * math.pi)
                    else:
                        centerY = 4 * raio / (3 * math.pi)
                    centroGy = centroCirculo[1] + centerY
            else:
                area = area / 4
                direction = read_integer("Em qual quadrante esta o ¼ de circulo?\n"
                                         "1 - primeiro\n"
                                         "2 - segundo\n"
                                         "3 - terceiro\n"
                                         "4 - quarto\n")
                if direction == 1 or direction == 2:
                    centroGy = centroCirculo[1] + (4 * raio / (3 * math.pi))
                    if direction == 1:
                        centerX = 4 * raio / (3 * math.pi)
                    else:
                        centerX = -4 * raio * (3 * math.pi)
                    centroGx = centroCirculo[0] + centerX
                elif direction == 3 or direction == 4:
                    centroGy = centroCirculo[1] - (4 * raio / (3 * math.pi))
                    if direction == 3:
                        centerX = -4 * raio / (3 * math.pi)
                    else:
                        centerX = 4 * raio / (3 * math.pi)
                    centroGx = centroCirculo[0] + centerX
            momentoEstaticoAddX += centroGx * area
            momentoEstaticoAddY += centroGy * area
            areaFormas += area
    
    # subtracao
    for i in range(figurasRemov):
        tipoFigura = read_integer("Qual o tipo de figura de remocao?\n"
                                  "1- quadrado ou retângulo\n"
                                  "2- triangulo\n"
                                  "3- circulo\n"
                                  "4- semicirculo\n")
        if tipoFigura == 1 or tipoFigura == 2:
            base = read_coordinates("Quais as coordenadas em X da base? (separar por -)\n")
            baseConta = base[1] - base[0]
            altura = read_coordinates("Quais as coordenadas em Y da altura? (separar por -)\n")
            alturaConta = altura[1] - altura[0]
            area = baseConta * alturaConta
            
            if tipoFigura == 1:
                centroGx = (baseConta / 2) + base[0]
                centroGy = (alturaConta / 2) + altura[0]
            else:
                area = area / 2
                anguloReto = read_coordinates("Quais as coordenadas do angulo reto? (separar por -)\n")
                if anguloReto[0] > base[0]:
                    centroGx = (-baseConta / 3) + anguloReto[0]    
                else:
                    centroGx = (baseConta / 3) + anguloReto[0]
                if anguloReto[1] > altura[0]:
                    centroGy = (-alturaConta / 3) + anguloReto[1]
                else:
                    centroGy = (alturaConta / 3) + anguloReto[1]
            momentoEstaticoRemovX += centroGx * area
            momentoEstaticoRemovY += centroGy * area
            menosAreaFormas += area
        
        elif tipoFigura == 3 or tipoFigura == 4 or tipoFigura == 5:
            centroCirculo = read_coordinates("Quais as coordenadas do centro da figura? (separar por -)\n")
            raio = read_float("Qual o raio da figura?\n")
            area = math.pi * (raio ** 2)
            
            if tipoFigura == 3:
                centroGx = centroCirculo[0]
                centroGy = centroCirculo[1]
            elif tipoFigura == 4:
                area = area / 2
                direction = read_integer("Para qual direcao esta o semicirculo?\n"
                                         "1 - esquerda\n"
                                         "2 - baixo\n"
                                         "3 - direita\n"
                                         "4 - cima\n")
                if direction == 1 or direction == 3:
                    centroGy = centroCirculo[1]
                    if direction == 1:
                        centerX = -4 * raio / (3 * math.pi)
                    else:
                        centerX = 4 * raio / (3 * math.pi)
                    centroGx = centroCirculo[0] + centerX
                else:
                    centroGx = centroCirculo[0]
                    if direction == 2:
                        centerY = -4 * raio / (3 * math.pi)
                    else:
                        centerY = 4 * raio / (3 * math.pi)
                    centroGy = centroCirculo[1] + centerY
            else:
                area = area / 4
                direction = read_integer("Em qual quadrante esta o ¼ de circulo?\n"
                                         "1 - primeiro\n"
                                         "2 - segundo\n"
                                         "3 - terceiro\n"
                                         "4 - quarto\n")
                if direction == 1 or direction == 2:
                    centroGy = centroCirculo[1] + (4 * raio / (3 * math.pi))
                    if direction == 1:
                        centerX = 4 * raio / (3 * math.pi)
                    else:
                        centerX = -4 * raio * (3 * math.pi)
                    centroGx = centroCirculo[0] + centerX
                elif direction == 3 or direction == 4:
                    centroGy = centroCirculo[1] - (4 * raio / (3 * math.pi))
                    if direction == 3:
                        centerX = -4 * raio / (3 * math.pi)
                    else:
                        centerX = 4 * raio / (3 * math.pi)
                    centroGx = centroCirculo[0] + centerX
            momentoEstaticoRemovX += centroGx * area
            momentoEstaticoRemovY += centroGy * area
            menosAreaFormas += area
            
    areaTotal = areaFormas - menosAreaFormas
    momentoEstaticoTotal = momentoEstaticoAddY - momentoEstaticoRemovY
    print(areaTotal)
    print(momentoEstaticoTotal)
    centroGyFinal = momentoEstaticoTotal / areaTotal
    print(centroGyFinal)
    
    sair = input("Digite 'SAIR' para parar ou pressione ENTER para continuar\n")
    if sair.upper() == "SAIR":
        break
