from yeelight import discover_bulbs, Bulb

bulbs = discover_bulbs()

bulb = Bulb(bulbs[0]['ip'])


cor = input("Bota a cor ai mané: ")
while (True):
    if cor == "roxo":
        bulb.set_rgb(153,51,153)
    elif cor == "vermelho":
        bulb.set_rgb(255,0,0)
    elif cor == "azul":
        bulb.set_rgb(0,0,255)
    elif cor == "branco":
        bulb.set_rgb(255,255,255)
    
    cor = input("Bota a cor ai mané: ")



