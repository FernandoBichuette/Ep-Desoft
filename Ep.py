
import random

carteira=int(input('Quanto de dinheiro você?: ')) 

aposta=float(input('Qual aposta?: '))  

if aposta >= 0.3*carteira:
    
    game=True
    while game: 
        print('\n------------------')
        print("O jogo começa!")
        print('------------------\n')
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
        
                           
        while sum(carta_da_mesa) < 17:
            carta_da_mesa.append(random.choice(list(baralho.values())))
            print('A mesa pegou mais uma cartas',carta_da_mesa)
        

                            
        # Para casa
        if sum(carta_da_mesa) == 21:
            print("A casa ganhou, você perdeu")
            continue            
        
        elif sum(carta_da_mesa) > 21:
            print('A casa perdeu')
            continue
            
        
        if sum(player) > 21:
            print("Você perdeu. A casa ganhou")
            continue
                            
        elif sum(player) == 21:
            ganho = aposta*1.5
            carteira=carteira+ganho
            print("21, você venceu! " + str(carteira))   
            continue
        
        elif carteira <=0:
            print("você perdeu o jogo")
            print("GAME OVER")
            break                
        
        
        a = True 
        
        while a==True:           
                # Para casa
                if sum(carta_da_mesa) == 21:
                    print("A casa ganhou, você perdeu")
                                
                elif sum(carta_da_mesa) > 21:
                    print('A casa perdeu')
                    break
                    
                
                if sum(player) > 21:
                    print("Você perdeu. A casa ganhou")
                    break
                                    
                elif sum(player) == 21:
                    ganho = aposta*1.5
                    carteira=carteira+ganho
                    print("21, você venceu! " + str(carteira))   
                    break
                
                elif carteira <=0:
                    print("você perdeu o jogo")
                    print("GAME OVER")
                    break 
                pergunta= str(input('Você quer ficar[hit] ou sair[sair]?: '))
                
            
                if pergunta == 'hit':
                    player.append(random.choice(list(baralho.values())))
                    print("Você tem agora o total " + str(sum(player)) + " com as seguintes cartas ", player)
                
                    if sum(player) > 21:

                        ganho = -aposta
                        carteira=carteira+ganho
                        print("você perdeu " + str(carteira))
                        a=False
                    
                    elif sum(player) == 21:
                        ganho = aposta
                        carteira=carteira+ganho
                        print("você venceu " + str(carteira))
                        aposta=int(input("nova aposta?: "))
                        a=False
                        
                if pergunta == 'sair':    
                    if sum(player) < sum(carta_da_mesa):
                            print('A casa venceu!')
                            ganho = -aposta
                            carteira=carteira+ganho
                            print("você perdeu " + str(carteira))
                            aposta=int(input("nova aposta?: "))
                            a=False
                    else:
                        ganho = aposta
                        carteira=carteira+ganho
                        print("você venceu " + str(carteira))
                        aposta=int(input("nova aposta?: "))
                        #eae
                        a=False
    
     
        if aposta == str():
            print('Seu dinheiro total é igual ' + str(carteira) )
            break
    
    else:
        print('Você não pode jogar')        
        