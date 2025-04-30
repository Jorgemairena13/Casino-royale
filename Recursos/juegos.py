import random
import time
import os


def limpiar_pantalla():
    os.system('cls')


class Juegos:
    def __init__(self, nombre, apuesta_min, apuesta_max, saldo_inicial):
        self.nombre = nombre                        
        self.apuesta_min = apuesta_min              
        self.apuesta_max = apuesta_max              
        self.saldo_jugador = saldo_inicial          
        self.apuesta_actual = 0                     
        self.resultado = None                       
        self.multiplicador_pago = 0.0               
        self.historial = []                         
         

class Maquina_slots(Juegos):
    def __init__(self, nombre, apuesta_min, apuesta_max, saldo_inicial):
        super().__init__(nombre, apuesta_min, apuesta_max, saldo_inicial)
    
    def mostrar_info(self):
        print(self.nombre)
        print(self.apuesta_min)
        print(self.apuesta_max)
        print(self.saldo_jugador)

    # Plantilla completa de la máquina ASCII, con marcadores para los carretes
    def maquina_slots(self,r,credito,ultima_tirada):
        return f"""
   
╔══════════════════════════════════════════════════════════════════════╗
║                      💥  MÁQUINA TRAGAPERRAS DEL BAR  💥             ║
║━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━║
║                                                                      ║
║             ╔═════════╗   ╔═════════╗   ╔═════════╗                  ║
║             ║   {r[0][0]}    ║   ║   {r[1][0]}    ║   ║   {r[2][0]}    ║                  ║
║             ║   {r[0][1]}    ║   ║   {r[1][1]}    ║   ║   {r[2][1]}    ║                  ║
║             ║   {r[0][2]}    ║   ║   {r[1][2]}    ║   ║   {r[2][2]}    ║                  ║
║             ╚═════════╝   ╚═════════╝   ╚═════════╝                  ║
║                                                                      ║
║━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━║
║ 💰 PREMIOS 💰                                                        ║
║  ────────────────────────────────────────────────────────────────    ║
║    3 x 🍒  = 10 créditos        3 x 🔔 = 20 créditos                 ║
║    3 x 💎 = 100 créditos        3 x 🤑 = 200 créditos                ║
║    3 x 🍀 =  50 créditos        3 x 🏆 = 200 créditos                ║
║━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━║
║ 💳 CRÉDITOS: {credito:<4}                  🎯 Último resultado: {ultima_tirada}           ║
╠══════════════════════════════════════════════════════════════════════╣
║                      🎲  [ PULSA ENTER PARA TIRAR ]  🎲              ║
╚══════════════════════════════════════════════════════════════════════╝
"""



    def animar_maquina(self,saldo_pasar,iteraciones=40, delay=0.01):
        """Anima los carretes dentro del marco ASCII."""
        ultima = None
        premio = 0
        SIMBOLOS = ['🍒','🔔','💎','🍀','🤑','🏆']
        APARICIONES = [40,30,20,30,15,10]
   
        # Bucle con las iteraciones para animar la maquina
        for _ in range(iteraciones):
            # Lista con los emojis ramdom que vamos a usar
            reels = [[random.choices(SIMBOLOS, weights=APARICIONES, k=1)[0] for _ in range(3)]for _ in range(3)]

            limpiar_pantalla()
            # Mostramos la maquina de slots 
            print(self.maquina_slots(reels,saldo_pasar,premio))

            # Guardamos la lista
            ultima = reels

            # Damos una pausa
            time.sleep(delay)
        # Muestra el resultado final fijo
        limpiar_pantalla()
        print(self.maquina_slots(ultima,saldo_pasar,premio))
        
        
        # Si los 3 son iguales damos mas premio 
        if ultima[0][1] == ultima[1][1] == ultima[2][1]:
            
            if ultima[0][1] == '🍒':
                premio = 10
            elif ultima[0][1] == '🔔':
                premio = 20
            elif ultima[0][1] == '💎':
                premio = 100
            elif ultima[0][1] == '🏆':
                premio = 200
            elif ultima[0][1] == '🍀':
                premio = 50
            elif ultima[0][1] == '🤑':
                premio = 200

        # Comparamos que los 2 de la izquierda sean iguales
        elif ultima[0][1] == ultima[1][1]:
            # Segun como sea damos un premio
            if ultima[0][1] == '🍒':
                premio += 5
            elif ultima[0][1] == '🔔':
                premio += 10
            elif ultima[0][1] == '💎':
                premio += 50
            elif ultima[0][1] == '🏆':
                premio += 100
            elif ultima[0][1] == '🍀':
                premio += 25
            elif ultima[0][1] == '🤑':
                premio += 100
            

        # Comparamos los 2 del lado derecho si son iguales
        elif ultima[1][1] == ultima[2][1]:
            # Si es igual damos estos premios
            if ultima[1][1] == '🍒':
                premio = 5
            elif ultima[1][1]  == '🔔':
                premio = 10
            elif ultima[1][1]  == '💎':
                premio = 50
            elif ultima[1][1]  == '🏆':
                premio = 100
            elif ultima[1][1]  == '🍀':
                premio = 25
            elif ultima[1][1]  == '🤑':
                premio = 100
            print(f"¡GANASTE {premio} CRÉDITOS!")
        else:
            print("¡Inténtalo de nuevo!")
        
        return premio


