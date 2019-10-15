# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 18:50:42 2019

@author: Fernando
"""

import random

carteira=[]
carteira.append(int(input('Quanto de dinheiro você?: ')))  

aposta=int(input('Qual aposta?: '))  

if aposta >= 0.3*carteira[0]:
    
    game=True
    while game: 
        
        print("O jogo começa!\n")
        
        carta_da_mesa=[]
        player=[]
        
        baralho={}
        i=0
        while i < 4:
            
            
            if i == 0:
                istr='de Ouros'
            if i == 1:
                istr='de Paus'
            if i ==2:
                istr='de Copas'
            if i == 3:
                istr='de Espadas'
            
            rei= "rei " + istr
            dama='dama '+istr
            valete='valete '+istr
            As='As '+istr
            dois='2 '+ istr
            tres='3 '+ istr
            quatro='4 '+ istr
            cinco='5 '+ istr
            seis='6 '+istr
            sete='7 '+istr
            oito='8 '+istr
            nove='9 '+istr
            dez='10 '+istr
            
            
            baralho[rei]=10
            baralho[dama]=10
            baralho[valete]=10
            baralho[As]=11
            baralho[dois]=2
            baralho[tres]=3
            baralho[quatro]=4
            baralho[cinco]=5
            baralho[seis]=6
            baralho[sete]=7
            baralho[oito]=8
            baralho[nove]=9
            baralho[dez]=10
            
            i+=1
            
        
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
        
            
        if sum(player) < 21:
            
            a = True
            
            while a==True:
            
                pergunta= str(input('Você quer ficar[hit] ou sair[sair]?: '))
                
                
                if pergunta == 'hit':
                    player.append(random.choice(list(baralho.values())))
                    print("Você tem agora o total " + str(sum(player)) + " com as seguintes cartas ", player)
                    if sum(player) > 21:
                        
                        a=False
                    
                    elif sum(player) == 21:
                        
                        a=False
                        
                if pergunta == 'sair':    
                    if sum(player) < sum(carta_da_mesa):
                            print('A casa venceu!')
                            a=False
                    else:
                        ganho=carteira+aposta
                        carteira.append(ganho)
                        total=sum(carteira)
                        print('Você venceu'+str(total))
                        
                        a=False
                   
        
                
        if sum(player) > 21:
            print("Você perdeu. A casa ganhou")
                
        elif sum(player) == 21:
            ganho=aposta + aposta*1.5
            carteira.append(ganho)
            total=sum(carteira)
            print("21, você venceu!"+str(total))        
            
    else:
        print('Você não pode jogar')        
        
        
        
        
        
        
        
        
        
        
            
    
    
    
    
    