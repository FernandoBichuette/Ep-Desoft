# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 18:50:42 2019

@author: Fernando
"""

import random

baralho={'rei':10,
       'dama':10,
       'valete':10,
       'As':1,
       '2':2,
       '3':3,
       '4':4,
       '5':5,
       '6':6,
       '7':7,
       '8':8,
       '9':9,
       '10':10} 

carta_da_mesa=[]
player=[]

while len(carta_da_mesa) != 2:
    carta_da_mesa.append(random.choice(list(baralho.values())))
    if len(carta_da_mesa) == 2:
        print('A mesa tem X e ',carta_da_mesa[1])

while len(player) !=2:
    player.append(random.choice(list(baralho.values())))
    if len(player)==2:
        print("Você tem ",player)

# Para casa
if sum(carta_da_mesa) == 21:
    print("A casa ganhou, você perdeu")
elif sum(carta_da_mesa) > 21:
    print('A casa perdeu')
    
while sum(player) < 21:
    
    pergunta= str(input('Você quer ficar[stay] ou continuar[hit]:'))
    
    if pergunta == 'hit':
        player.append(random.choice(list(baralho.values())))
        print("Você tem agora o total " + str(sum(player)) + " com as seguintes cartas ", player)
    
    if pergunta == 'stay':
        carta_da_mesa.append(random.choice(list(baralho.values())))
        print('A mesa tem X e ',carta_da_mesa[1])
        print("Você tem ",player)

    if pergunta == 'sair':
        if sum(player) < sum(carta_da_mesa):
            print('A casa venceu!')
            
        else:
            print('Você venceu')
            break
        
if sum(player) > 21:
    print("Você perdeu. A casa ganhou")
        
elif sum(player) == 21:
    print("21 , você venceu!")        
        
        
        
        
        
        
        
        
        
        
        
        
            
    
    
    
    
    