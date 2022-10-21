from random import choice 
from Play import *

def run_game(): 
    """arranca el juego"""
    display_game()
    while True:
        #una nueva partida 
        user_play = get_user_play()#JUGADA DEL USUARIO
        comp_play = random_play()#JUGADA DEL ORDENADOR 
        display_match(user_play, comp_play)#MUESTRO JUGADA
        winner = get_winner(user_play, comp_play)#AVERIGUO VENCEDOR 
        if winner == None: #Empate 
            display_tie(user_play, comp_play)
        else:
            display_victory(winner)
        #PREGUNTO AL USUARIO Y SU QUIERE SALIR
        #SALGO PITANDO CON UN BREAK
        resp = another_match()
        if resp == False:
            #me las piro 
            break
    print(choice(["Vuelve a tu agujero!\n"]))

    

def another_match():
    while True:
        nueva_partida = (input("Quieres jugar otra vez? S/N")).upper()
        print("S.Continuas?\n")
        print("N.Lo dejas\n")
        play_again = None
        if nueva_partida == "S":
            print("Let's Rock Baby\n")
            play_again = True
        elif nueva_partida == "N":
            play_again = False
        else:
            print("Escoge una opción correcta")
        return play_again

def display_match(play1, play2):
    print(f'{play1.description()} vs {play2.description()} FIGHT! \n')

def display_game():
    print("\n\n\t\tRock Paper Scissors\n\n")
#muestra el nombre del juego 


def get_user_play():
#Le pregunta al usuario que quiere jugar y lo devuelve
#Creamos instancias de las jugadas 
    res = get_user_response()
    if res == 1:
        return Rock()
    elif res == 2:
        return Paper()
    else: 
        return Scissors()
        
def get_user_response():
    #Menú de opciones y te da a escoger una. 
    #Devuelve una cadena lo que ha elegido
    response = None
    while True:
        print("Chose your play:")
        print("1. Rock🪨")
        print("2. Paper🧻")
        print("3 Scissors ✂️ ")
        raw = input("Enter 1, 2 or 3\n")
        #validar raw
        raw = raw.strip()
        if raw == "1":
            response = 1
            break
        elif raw == "2":
            response =2 
            break
        elif raw == "3":
            response = 3
        else: 
            continue
        return response

def random_play():
    #Selecciona una jugada al azar para competidr con el usuario 
    return choice([Paper(),Rock(),Scissors()]) #choice devuelve una instancia de paper, rock y scissors

def get_winner(play1, play2):
    winner = ''
    final = play1.compare(play2)
    if final == Result.gana:
        print(f"Gana:{play1}")
        winner = play1
    elif final == Result.igual:
        print("Empate")
        winner = None
    else:
        winner = play2
        print(f"Gana: {play2}")
    return winner
#Obtiene el vencedor o None si hay empate
    

def display_tie(play1, play2):
    #imprime que ha habido un empate 
    print(f'Empate entre dos {play1.description()}')

def display_victory(winner):
    #muestra que winner ha ganado 
    print (f"Ha ganado {winner.description}")


if __name__=='__main__':
    #forma de decir aquí empieza mi programa 
    run_game()