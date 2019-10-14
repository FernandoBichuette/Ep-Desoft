# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 18:50:42 2019

@author: Fernando
"""

import random

carta={rei,
       dama,
       valete,
       As} 

carta_da_mesa=[]
player=[]

while len(carta_da_mesa) != 2:
    carta_da_mesa.append(random.randint(1,11))
    if len(carta_da_mesa) == 2:
        print('A mesa tem X e ',carta_da_mesa[1])

while len(player) !=2:
    player.append(random.randint(1,11))
    if len(player)==2:
        print("Você tem ",player)

# Para casa
if sum(carta_da_mesa) == 21:
    print("A casa ganhou, você perdeu")
elif sum(carta_da_mesa) > 21:
    print('A casa perdeu')
    
while sum(player) < 21:
    
    pergunta= str(input('Você quer ficar[stay] ou continuar[hit]'))
    
    if pergunta == 'hit':
        player.append(random.randint(1, 11))
        print("Você tem agora o total " + str(sum(player)) + " com as seguintes cartas ", player)
    
    if pergunta == 'stay':
        carta_da_mesa.append(random.randint(1,11))
        print('A mesa tem X e ',carta_da_mesa[1])
        print("Você tem ",player)

    else:
        print("Você tem agora o total " + str(sum(carta_da_mesa)) + " com as seguintes cartas ", carta_da_mesa[1])

        print("Você tem agora o total " + str(sum(player)) + " com as seguintes cartas ", player)
        
        if sum(player) < sum(carta_da_mesa):
            print('A casa venceu!')
            
        else:
            print('Você venceu')
            break
        
if sum(player) > 21:
    print("Você perdeu. A casa ganhou")
        
elif sum(player) == 21:
    print("21 , você venceu!")        
        
        
        
        
        
        
        
        
        
        
        
        
            
    
    
    
    
    