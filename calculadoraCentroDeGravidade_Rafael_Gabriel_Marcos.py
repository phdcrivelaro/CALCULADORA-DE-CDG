import math
print("====/ Código feito por Rafael Bandini, Gabriel José e Marcos Liberatti /====\n")
while True:
    ind = 0
    areaFormas = 0
    menosAreaFormas = 0
    momentoEstaticoAddY = 0
    momentoEstaticoRemovY = 0
    momentoEstaticoAddX = 0
    momentoEstaticoRemovX = 0
    figurasAdd = int(input("Quantas figuras de adição?\n\n"))
    figurasRemov = int(input("\nQuantas de remoção?\n\n"))
    centroGx = 0
    centroGy = 0
    # adicao
    for i in range(0, figurasAdd):
        ind += 1
        print("==============/ figura:", ind, " /==============")
        tipoFigura = int(input("Qual o tipo de figura de adição?\n"
                               "1 - quadrado ou retângulo\n"
                               "2 - triangulo\n"
                               "3 - circulo\n"
                               "4 - semicirculo\n"
                               "5 - ¼ de circulo\n\n"))
        #quadrado ou triangulo
        if tipoFigura == 1 or tipoFigura == 2:
            base = str(input("\nQuais são os pontos de início e fim em X? (separar por vírgula)\n\n")).split(",")
            baseConta = float(base[1]) - float(base[0])
            altura = str(input("\nQuais são os pontos de início e fim em Y? (separar por vírgula)\n\n")).split(",")
            alturaConta = float(altura[1]) - float(altura[0])
            area = baseConta * alturaConta
            #quadrado
            if tipoFigura == 1:
                centroGx = (baseConta / 2) + float(base[0])
                centroGy = (alturaConta / 2) + float(altura[0])
            #triangulo
            else:
                area = area / 2
                anguloReto = str(input("\nQuais as coordenadas do ângulo reto? (separar por virgula)\n\n")).split(",")
                if float(anguloReto[0]) > float(base[0]):
                    centroGx = (-baseConta / 3) + float(anguloReto[0])
                else:
                    centroGx = (baseConta / 3) + float(anguloReto[0])
                if float(anguloReto[1]) > float(altura[0]):
                    centroGy = (-alturaConta / 3) + float(anguloReto[1])
                else:
                    centroGy = (alturaConta / 3) + float(anguloReto[1])
            momentoEstaticoAddX += centroGx * area
            momentoEstaticoAddY += centroGy * area
            areaFormas += area
        #circulo e derivados
        elif tipoFigura == 3 or tipoFigura == 4 or tipoFigura == 5:
            centroCirculo = str(input("\nQuais as coordenadas do centro da figura? (separar por vírgula)\n\n")).split(",")
            raio = int(input("\nQual o raio da figura?\n\n"))
            area = math.pi * (raio ** 2)
            if tipoFigura == 3:
                centroGx = float(centroCirculo[0])
                centroGy = float(centroCirculo[1])
            #semicirculo
            elif tipoFigura == 4:
                area = area/2
                direction = int(input("\nPara qual direção esta o semicírculo?\n"
                                      "1 - esquerda\n"
                                      "2 - baixo\n"
                                      "3 - direita\n"
                                      "4 - cima\n\n"))
                if direction == 1 or direction == 3:
                    centroGy = float(centroCirculo[1])
                    if direction == 1:
                        centerX = -4 * raio / (3 * math.pi)
                    else:
                        centerX = 4 * raio / (3 * math.pi)
                    centroGx = float(centroCirculo[0]) + centerX
                elif direction == 2 or direction == 4:
                    centroGx = float(centroCirculo[0])
                    if direction == 2:
                        centerY = -4 * raio / (3 * math.pi)
                    else:
                        centerY = 4 * raio / (3 * math.pi)
                    centroGy = float(centroCirculo[0]) + centerY
            else:
                area = area/4
                direction = int(input("\nEm qual quadrante esta o ¼ de círculo?\n"
                                      "1 - primeiro\n"
                                      "2 - segundo\n"
                                      "3 - terceiro\n"
                                      "4 - quarto\n\n"))
                if direction == 1 or direction == 2:
                    centroGy = float(centroCirculo[1]) + (4 * raio / (3 * math.pi))
                    if direction == 1:
                        centerX = 4 * raio / (3 * math.pi)
                    else:
                        centerX = -4 * raio * (3 * math.pi)
                    centroGx = float(centroCirculo[0]) + centerX
                elif direction == 3 or direction == 4:
                    centroGy = float(centroCirculo[1]) - (4 * raio / (3 * math.pi))
                    if direction == 3:
                        centerX = -4 * raio / (3 * math.pi)
                    else:
                        centerX = 4 * raio / (3 * math.pi)
                    centroGx = float(centroCirculo[0]) + centerX
            momentoEstaticoAddX += centroGx * area
            momentoEstaticoAddY += centroGy * area
            areaFormas += area
    # subtracao
    for i in range(0, figurasRemov):
        ind += 1
        print("==============/ figura:", ind, "/==============")
        tipoFigura = int(input("Qual o tipo de figura de remoção?\n"
                               "1 - quadrado ou retângulo\n"
                               "2 - triangulo\n"
                               "3 - círculo\n"
                               "4 - semicírculo\n"
                               "5 - ¼ de círculo\n\n"))
        if tipoFigura == 1 or tipoFigura == 2:
            base = str(input("\nQuais são os pontos de início e fim em X? (separar por vírgula)\n\n")).split(",")
            baseConta = float(base[1]) - float(base[0])
            altura = str(input("\nQuais são os pontos de início e fim em Y? (separar por vírgula)\n\n")).split(",")
            alturaConta = float(altura[1]) - float(altura[0])
            area = baseConta * alturaConta
            #quadrado
            if tipoFigura == 1:
                centroGx = (baseConta / 2) + float(base[0])
                centroGy = (alturaConta / 2) + float(altura[0])
            else:
                area = area / 2
                anguloReto = str(input("\nQuais as coordenadas do ângulo reto? (separar por vírgula)\n\n")).split(",")
                if float(anguloReto[0]) > float(base[0]):
                    centroGx = (-baseConta / 3) + float(anguloReto[0])
                else:
                    centroGx = (baseConta / 3) + float(anguloReto[0])
                if float(anguloReto[1]) > float(altura[0]):
                    centroGy = (-alturaConta / 3) + float(anguloReto[1])
                else:
                    centroGy = (alturaConta / 3) + float(anguloReto[1])
            momentoEstaticoRemovX += centroGx * area
            momentoEstaticoRemovY += centroGy * area
            menosAreaFormas += area
        elif tipoFigura == 3 or tipoFigura == 4 or tipoFigura == 5:
            centroCirculo = str(input("\nQuais as coordenadas do centro da figura? (separar por vírgula)\n\n")).split(",")
            raio = float(input("\nQual o raio da figura?\n\n"))
            area = math.pi * (raio ** 2)
            if tipoFigura == 3:
                centroGx = float(centroCirculo[0])
                centroGy = float(centroCirculo[1])
            elif tipoFigura == 4:
                area = area/2
                direction = int(input("\nPara qual direção esta o semicírculo?\n"
                                      "1 - esquerda\n"
                                      "2 - baixo\n"
                                      "3 - direita\n"
                                      "4 - cima\n\n"))
                if direction == 1 or direction == 3:
                    centroGy = float(centroCirculo[1])
                    if direction == 1:
                        centerX = -4 * raio / (3 * math.pi)
                    else:
                        centerX = 4 * raio / (3 * math.pi)
                    centroGx = float(centroCirculo[0]) + centerX
                else:
                    centroGx = float(centroCirculo[0])
                    if direction == 2:
                        centerY = -4 * raio / (3 * math.pi)
                    else:
                        centerY = 4 * raio / (3 * math.pi)
                    centroGy = float(centroCirculo[1]) + centerY
            else:
                area = area/4
                direction = int(input("\nEm qual quadrante esta o ¼ de círculo?\n"
                                      "1 - primeiro\n"
                                      "2 - segundo\n"
                                      "3 - terceiro\n"
                                      "4 - quarto\n\n"))
                if direction == 1 or direction == 2:
                    centroGy = float(centroCirculo[1]) + (4 * raio / (3 * math.pi))
                    if direction == 1:
                        centerX = 4 * raio / (3 * math.pi)
                    else:
                        centerX = -4 * raio * (3 * math.pi)
                    centroGx = float(centroCirculo[0]) + centerX
                elif direction == 3 or direction == 4:
                    centroGy = float(centroCirculo[1]) - (4 * raio / (3 * math.pi))
                    if direction == 3:
                        centerX = -4 * raio / (3 * math.pi)
                    else:
                        centerX = 4 * raio / (3 * math.pi)
                    centroGx = float(centroCirculo[0]) + centerX
            momentoEstaticoRemovX += centroGx * area
            momentoEstaticoRemovY += centroGy * area
            menosAreaFormas += area
    areaTotal = (areaFormas - menosAreaFormas)
    momentoEstaticoTotalY = momentoEstaticoAddY - momentoEstaticoRemovY
    momentoEstaticoTotalX = momentoEstaticoAddX - momentoEstaticoRemovX
    centroGyFinal = momentoEstaticoTotalY / areaTotal
    centroGxFinal = momentoEstaticoTotalX / areaTotal
    print("\n==============/ Dados obtidos por sua figura constituída de", ind, "figuras/==============")
    print("Área total..............." + str(areaTotal) + "\n")
    print("Momento estático em X...." + str(momentoEstaticoTotalX) + "\n")
    print("Momento estático em Y...." + str(momentoEstaticoTotalY) + "\n")
    print("xG......................." + str(centroGxFinal) + "\n")
    print("yG......................." + str(centroGyFinal) + "\n")
    print(f"({centroGxFinal:.1f},{centroGyFinal:.1f})")
    sair = input("Digite 'SAIR' para parar ou pressione ENTER↵ para continuar\n")
    if sair.upper() == "SAIR":
        break
