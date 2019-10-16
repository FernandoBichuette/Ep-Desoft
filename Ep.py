
import random

def soma_pontos(cartas):
    total = 0
    for carta in cartas:
        if carta > 1 and carta < 11:
            total += carta
    
    for carta in cartas:
        if carta == 1:
            if (total + 11) > 21:
                total += 1
            else:
                total += 11
                
    return total
    
 
carteira=int(input('Quanto de dinheiro você?: ')) 

aposta=int(input('Qual aposta?: '))  

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
            baralho[As]=1
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
        
        
        if carteira <=0:
            print("você perdeu o jogo")
            print("GAME OVER")
            break
        
        
        if sum(player) < 21:
            
            a = True
            
            while a:
                
                if sum(player) > 21:
                    print("Você perdeu. A casa ganhou")
                    break
            
                elif sum(player) == 21:
                    ganho = aposta*1.5
                    carteira=carteira+ganho
                    print("21, você venceu! seu saldo é " + str(carteira))
                    break
            
                if sum(carta_da_mesa) == 21:
                    print("A casa ganhou, você perdeu")
                    break
                    
                elif sum(carta_da_mesa) > 21:
                    print('A casa perdeu')
                    break
                    
                pergunta= str(input('Você quer ficar[hit] ou sair[sair]?: '))
                
                if pergunta=='fim':
                    a=False 
                
                if pergunta == 'hit':
                    player.append(random.choice(list(baralho.values())))
                    ab=True
                    mudoucarta=False
                    print("Você tem agora o total " + str(soma_pontos(player)) + " com as seguintes cartas ", player)
                    while ab:
                        if soma_pontos(player) > 21 and not(mudoucarta):                            
                            mudoucarta=True
                            continue
                        if mudoucarta:
                            ganho = -aposta
                            carteira=carteira+ganho
                            print("você perdeu " + str(soma_pontos(player)) + ". seu saldo é " + str(carteira))
                            a=False
                        ab=False
                    
                    
                    if soma_pontos(player) == 21:
                        ganho = aposta
                        carteira=carteira+ganho
                        print("você venceu por 21. seu saldo é " + str(carteira))
                        aposta=int(input("nova aposta?: "))
                        a=False
                        
                if pergunta == 'sair':    
                    if soma_pontos(player) < soma_pontos(carta_da_mesa):
                            print('A casa venceu!')
                            ganho = -aposta
                            carteira=carteira+ganho
                            print("você perdeu " +str(soma_pontos(player))+". seu saldo é " + str(carteira))
                            aposta=int(input("nova aposta?: "))
                            a=False
                    else:
                        ganho = aposta
                        carteira=carteira+ganho
                        print("você venceu " +str(soma_pontos(player))+". seu saldo é " + str(carteira))
                        aposta=int(input("nova aposta?: "))
                        #eae
                        a=False
                   
     
        if pergunta=='fim':
            print('Seu dinheiro total é igual ' + str(carteira) )
            break
    
    else:
        print('Você não pode jogar')         
