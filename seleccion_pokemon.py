from random import randint

class Seleccion_pokemon:
    def __init__(self, pokemon):
        self.pokemon = pokemon

    def inicial(self):
        nivel = 5
        if self.pokemon == 1:
            #puntos de salud
            vi = randint(1, 20)
            EB = 45
            ataque = 49
            defensa = 49
            vel = 45
            ps = ((vi + 2 * EB)* (nivel/100))+10+nivel
            #puntos de ataque
            vi2 = randint(1, 20)
            atq = ((vi2 + 2 * ataque)*(nivel/100))+5
            #puntos de defensa
            vi3 = randint(1, 20)
            defe = ((vi3 + 2 * defensa)*(nivel/100))+5
            #puntos de ataque especial
            vi4 = randint(1, 20)
            atq_especial = ((vi4 + 2 * ataque)*(nivel/100))+5
            #puntos de defensa especial
            vi5 = randint(1, 20)
            def_especial = ((vi5 + 2 * defensa)*(nivel/100))+5
            #velocidad
            vi6 = randint(1, 20)
            velocidad = ((vi6 + 2 * vel)*(nivel/100))+5
            

            print('Su pokemon es: BULBASAUR')
            apodo = input('Ingrese apodo: ')
            print(f"Nivel-----------: {nivel} ")
            print('Movimientos-----: ')
            print('Datos de combate. ')
            print(f"Puntos de salud-: {ps} ")
            print(f"Ataque----------: {atq}")
            print(f"Defensa---------: {defe}")
            print(f"Ataque especial-: {atq_especial}")
            print(f"Defensa especial: {def_especial}")
            print(f"Velocidad-------: {velocidad}")
            input('Presione cualquier tecla para continuar...')

        elif self.pokemon == 2:
            #puntos de salud
            vi = randint(1, 20)
            EB = 39
            ataque = 52
            defensa = 43
            vel = 65
            ps = ((vi + 2 * EB)* (nivel/100))+10+nivel
            #puntos de ataque
            vi2 = randint(1, 20)
            atq = ((vi2 + 2 * ataque)*(nivel/100))+5
            #puntos de defensa
            vi3 = randint(1, 20)
            defe = ((vi3 + 2 * defensa)*(nivel/100))+5
            #puntos de ataque especial
            vi4 = randint(1, 20)
            atq_especial = ((vi4 + 2 * ataque)*(nivel/100))+5
            #puntos de defensa especial
            vi5 = randint(1, 20)
            def_especial = ((vi5 + 2 * defensa)*(nivel/100))+5
            #velocidad
            vi6 = randint(1, 20)
            velocidad = ((vi6 + 2 * vel)*(nivel/100))+5
            

            print('Su pokemon es: BULBASAUR')
            apodo = input('Ingrese apodo: ')
            print(f"Nivel-----------: {nivel} ")
            print('Movimientos-----: ')
            print('Datos de combate. ')
            print(f"Puntos de salud-: {ps} ")
            print(f"Ataque----------: {atq}")
            print(f"Defensa---------: {defe}")
            print(f"Ataque especial-: {atq_especial}")
            print(f"Defensa especial: {def_especial}")
            print(f"Velocidad-------: {velocidad}")
            input('Presione cualquier tecla para continuar...')

        elif self.pokemon == 3:
            #puntos de salud
            vi = randint(1, 20)
            EB = 44
            ataque = 48
            defensa = 65
            vel = 43
            ps = ((vi + 2 * EB)* (nivel/100))+10+nivel
            #puntos de ataque
            vi2 = randint(1, 20)
            atq = ((vi2 + 2 * ataque)*(nivel/100))+5
            #puntos de defensa
            vi3 = randint(1, 20)
            defe = ((vi3 + 2 * defensa)*(nivel/100))+5
            #puntos de ataque especial
            vi4 = randint(1, 20)
            atq_especial = ((vi4 + 2 * ataque)*(nivel/100))+5
            #puntos de defensa especial
            vi5 = randint(1, 20)
            def_especial = ((vi5 + 2 * defensa)*(nivel/100))+5
            #velocidad
            vi6 = randint(1, 20)
            velocidad = ((vi6 + 2 * vel)*(nivel/100))+5
            

            print('Su pokemon es: BULBASAUR')
            apodo = input('Ingrese apodo: ')
            print(f"Nivel-----------: {nivel} ")
            print('Movimientos-----: ')
            print('Datos de combate. ')
            print(f"Puntos de salud-: {ps} ")
            print(f"Ataque----------: {atq}")
            print(f"Defensa---------: {defe}")
            print(f"Ataque especial-: {atq_especial}")
            print(f"Defensa especial: {def_especial}")
            print(f"Velocidad-------: {velocidad}")
            input('Presione cualquier tecla para continuar...')
        
        else:
            print('Esta opcion no esta disponible')