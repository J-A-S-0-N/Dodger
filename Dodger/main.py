import random
import keyboard
from os import system
from time import sleep

chri = "#"
enemy = "|"

def printall():
    print(map1)
    print(map2)
    print(map3)
    print(map4)
    print(map5)
    print(map6)
    print(map7)
    print(map8)
    print(map9)
    print(map10)
    print(player)


def map(player_posx, enemy_posx):
    global map1
    map1 = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    global map2
    map2 = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    global map3
    
    map3 = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    global map4
    
    map4 = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    global map5

    map5 = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    global map6

    map6 = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    global map7
    map7 = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    global map8
    
    map8 = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    global map9

    map9 = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    global map10 
    map10 = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    global player
    
    player = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    if player_posx == 0:
        player[0] = chri
        sleep(0.01)    
    if player_posx == 1:
        player[1] = chri
    if player_posx == 2:
        player[2] = chri
    if player_posx == 3:
        player[3] = chri
    if player_posx == 4:
        player[4] = chri
    if player_posx == 5:
        player[5] = chri
    if player_posx == 6:
        player[6] = chri
    if player_posx == 7:
        player[7] = chri
    if player_posx == 8:
        player[8] = chri
    if player_posx == 9:
        player[9] = chri
    
    if enemy_posx == 0:
        map1[0] = enemy
    if enemy_posx == 1:
        map1[1] = enemy
    if enemy_posx == 2:
        map1[2] = enemy
    if enemy_posx == 3:
        map1[3] = enemy
    if enemy_posx == 4:
        map1[4] = enemy
    if enemy_posx == 5:
        map1[5] = enemy
    if enemy_posx == 6:
        map1[7] = enemy
    if enemy_posx == 7:
        map1[8] = enemy
    if enemy_posx == 8:
        map1[9] = enemy
def ran():
    global pos
    pos = random.randint(0,10)

def main():
    ran()
    map(5, 0)
    global current_pos
    current_pos = 5
    while True:
        if current_pos == -1:
            currrent_pos += 1
        if current_pos == 10:
            current_pos -= 1
        map(current_pos, pos)
        printall()
        if keyboard.is_pressed("a"):
            current_pos -= 1
        if keyboard.is_pressed("d"):
            current_pos += 1
        system("cls")
        sleep(0.001)
        


if __name__ == "__main__":
    main()