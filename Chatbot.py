
# -*- coding: utf-8 -*-
#Define uma clasee com várias funções, e tudo que estiver dentro da será executado quando chamarmos a funçao dentro da classe, desse exemplo; resposta()
#Comandos que serão executados quando chamar a função, captura a resposta e processa-a;


import webbrowser
import wikipedia
import requests
import numpy as np
import time
import json
import sys
import os
import subprocess as s
from time import strftime
from datetime import datetime
from BuscaWeb import BuscaWeb
from busca_web import busca_web
import random
from pyfirmata import Arduino, util
import pyautogui as pi
from pygame import mixer
from time import strftime
import time

Uno = Arduino('/dev/ttyACM0')
interagir = util.Iterator(Uno)
interagir.start()
luzdasala = Uno.get_pin('d:3:p')


class Chatbot():    
    def __init__(self, nome):
        try:
            memoria = open(nome+'.json','r')
        except FileNotFoundError:        
            memoria = open(nome+'.json','w')
            memoria.write('[["Douglas","Bianca"],{"vinx": "Olá, em que posso ajudálo?","oi": "Olá, qual o seu nome?","tchau": "tchau","abra o midia player":"executa C:\Program Files\Windows Media Player\wmplayer"}]')
            memoria.close()
            memoria = open(nome+'.json','r')
        self.nome = nome
        self.conhecidos, self.frases = json.load(memoria)
        memoria.close()
        self.historico = [None,]
        
        
    def escuta(self,frase=None):
        if frase == None:
            frase = input('>: ')
        frase = str(frase)
        if 'executa ' in frase:
            return frase
        frase = frase.lower()
        return frase

    
    def pensa(self,frase):
        respostas = ['Pois não?','Em que posso ajudá- lo?','Pode falar...','Estou ouvindo','Eu...','E aí, o que manda?','Sim, estou aqui']
        ultimaFrase = self.historico[-1]
        quartos = ['200','201','202','203','204','205','206','207','208','209','210','211','212','213','214','215','216','217','218','219','220','221','222','223','224','225','226','227','228','229','230','231','232','233','234','235','236','237','238','239','240','241','242','243','244','245','246','247','248','249','250']
        self.contador = 0

        #analisando sensor
        #if frase == True:
            #return 'ligado'
        #elif frase == False:
            #return 'desligado'

        ##############   analisando nomes e respondendo
        if frase == 'oi lisa':
            return 'Olá, qual o seu nome?'
            
        elif ultimaFrase == 'Olá, qual o seu nome?':
            nome = self.pegaNome(frase)
            frase = self.respondeNome(nome)
            return frase

        ##########
        elif frase == 'meu id':
            self.id = ultimaFrase

        #nesta parte é onde ensinamos respostas ao chatbot#########################       
        elif frase == 'lisa aprenda':
            return 'Qual a frase?'

        elif ultimaFrase == 'Qual a frase?' and frase in self.frases:
            self.chave = frase
            return 'Esta frase já está cadastrada, deseja alterá-la?'

        elif ultimaFrase == 'Qual a frase?':
            self.chave = frase
            return 'Qual a resposta?'

        elif ultimaFrase == 'Esta frase já está cadastrada, deseja alterá-la?':
            if frase == 'sim' or frase == 's':
                return 'Qual a resposta?'
            else:
                return 'Aprendizado cancelado'

        elif ultimaFrase == 'Qual a resposta?':
            resp = frase
            self.frases[self.chave] = resp
            self.gravaMemoria()
            return 'Aprendido'
        
        #Fazendo um check-out#####################################
        elif frase == 'fazer check-out' or frase == '/command12':
            return 'De qual quarto deseja fazer um check-out?'

        elif ultimaFrase == 'De qual quarto deseja fazer um check-out?':
            if frase in self.frases:
                self.chave = frase
                return 'Confirma o check-out?'
            else:
                if frase.isnumeric():
                    return 'Não ha check-in nesse quarto.'
                else:
                    return 'Dados informados inválidos'

        elif ultimaFrase == 'Confirma o check-out?':
            if frase == 'sim' or frase == 's':
                resp = 'vazio'
                self.frases[self.chave] = resp
                self.gravaMemoria()
                return 'Check-out realizado com sucesso.'
            else:
                return 'Check-out cancelado'


        #usando o arduíno para ligar e desligar luzes #####################################
        elif frase == '/command1':
            if self.frases[frase] == '1':
                Uno.digital[3].write(1)
                self.chave = frase
                salao1 = '0'
                self.frases[self.chave] = salao1
                self.gravaMemoria()
                return 'luz 1 do salao ligada'
            elif self.frases[frase] == '0':
                Uno.digital[3].write(0)
                self.chave = frase
                salao1 = '1'
                self.frases[self.chave] = salao1
                self.gravaMemoria()
                return 'luz 1 do salao desligada'
        
        elif frase == '/command2':
            if self.frases[frase] == '1':
                Uno.digital[4].write(1)
                self.chave = frase
                salao2 = '0'
                self.frases[self.chave] = salao2
                self.gravaMemoria()
                return 'luz 2 do salao ligada'
            elif self.frases[frase] == '0':
                Uno.digital[4].write(0)
                self.chave = frase
                salao2 = '1'
                self.frases[self.chave] = salao2
                self.gravaMemoria()
                return 'luz 2 do salao desligada'

        elif frase == '/command3':
            if self.frases[frase] == '1':
                Uno.digital[5].write(1)
                self.chave = frase
                salao3 = '0'
                self.frases[self.chave] = salao3
                self.gravaMemoria()
                return 'luz 3 do salao ligada'
            elif self.frases[frase] == '0':
                Uno.digital[5].write(0)
                self.chave = frase
                salao3 = '1'
                self.frases[self.chave] = salao3
                self.gravaMemoria()
                return 'luz 3 do salao desligada'

        elif frase == '/command4':
            if self.frases[frase] == '1':
                Uno.digital[6].write(1)
                self.chave = frase
                frenteBar = '0'
                self.frases[self.chave] = frenteBar
                self.gravaMemoria()
                return 'luz da frente do bar ligada'
            elif self.frases[frase] == '0':
                Uno.digital[6].write(0)
                self.chave = frase
                frenteBar = '1'
                self.frases[self.chave] = frenteBar
                self.gravaMemoria()
                return 'luz da frente do bar desligada'

        elif frase == '/command5':
            if self.frases[frase] == '1':
                Uno.digital[7].write(1)
                self.chave = frase
                corredor1 = '0'
                self.frases[self.chave] = corredor1
                self.gravaMemoria()
                return 'luz 1 do corredor ligada'
            elif self.frases[frase] == '0':
                Uno.digital[7].write(0)
                self.chave = frase
                corredor1 = '1'
                self.frases[self.chave] = corredor1
                self.gravaMemoria()
                return 'luz 1 do corredor desligada'

        elif frase == '/command6':
            if self.frases[frase] == '1':
                Uno.digital[8].write(1)
                self.chave = frase
                corredor1 = '0'
                self.frases[self.chave] = corredor1
                self.gravaMemoria()
                return 'luz 2 do corredor ligada'
            elif self.frases[frase] == '0':
                Uno.digital[8].write(0)
                self.chave = frase
                corredor1 = '1'
                self.frases[self.chave] = corredor1
                self.gravaMemoria()
                return 'luz 2 do corredor desligada'

        elif frase == '/command7':
            if self.frases[frase] == '1':
                Uno.digital[9].write(1)
                self.chave = frase
                corredor1 = '0'
                self.frases[self.chave] = corredor1
                self.gravaMemoria()
                return 'luz 1 do restaurante ligada'
            elif self.frases[frase] == '0':
                Uno.digital[9].write(0)
                self.chave = frase
                corredor1 = '1'
                self.frases[self.chave] = corredor1
                self.gravaMemoria()
                return 'luz 1 do restaurante desligada'

        elif frase == '/command8':
            if self.frases[frase] == '1':
                Uno.digital[10].write(1)
                self.chave = frase
                corredor1 = '0'
                self.frases[self.chave] = corredor1
                self.gravaMemoria()
                return 'luz 2 do restaurante ligada'
            elif self.frases[frase] == '0':
                Uno.digital[10].write(0)
                self.chave = frase
                corredor1 = '1'
                self.frases[self.chave] = corredor1
                self.gravaMemoria()
                return 'luz 2 do restaurante desligada'
        ##########################

        #nesta parte é onde cadastramos pessoas#######################
        elif frase == 'fazer check-in' or frase == '/command9':
            return 'Certo, digite o número do quarto.'

        #+++++++ CANCELA VENDAS ++++++++++
        elif frase == 'cancelar venda' or frase == '/command10':
            return 'O número do quarto?'
        elif ultimaFrase == 'O número do quarto?':
            if frase in quartos and frase in self.frases:
                self.chaveQuarto = frase
                return 'Qual o ítem será cancelado?'
            else:
                if frase.isnumeric():
                    return 'Não há check-in nesse quarto'
                else:
                    return 'Dados informados inválidos'

        elif ultimaFrase == 'Qual o ítem será cancelado?':
            cardapio = {'pc camarão':70,'pc calabresa':40,'pc fritas':25,'drink':20,'suco':10,'cerveja':7,'refrigerante':5}
            self.item = frase
            if self.item in cardapio:
                self.valor = int(cardapio[self.item])
                return 'Qual a quantidade?'
            else:
                return 'Este ítem não contém na lista'

        elif ultimaFrase == 'Qual a quantidade?':
            self.quantidade = frase
            if (self.quantidade).isnumeric():
                self.quantidade = int(self.quantidade)
                self.valorvenda = self.quantidade * self.valor
                self.total = int(self.total)
                self.total -= int(self.valorvenda)
                self.quantidade = str(self.quantidade)
                self.valor = str(self.valor)
                self.total = str(self.total)
                self.valorvenda = str(self.valorvenda)
                dataEhoraV = datetime.now()
                self.anoV = str(dataEhoraV.year)
                self.mesV = str(dataEhoraV.month)
                self.diaV = str(dataEhoraV.day)
                self.horaV = str(strftime('%H:%M'))
                self.frases[self.chaveQuarto] += ('\n'+'\n'+'Venda cancelada' + '\n' + 'Ítem: ' + self.item + '\n' + 'Valor por unidade: ' + 'R$ ' + self.valor + ',00' + '\n' + 'Quantidade: ' + self.quantidade + '\n' + 'Valor da venda: ' + 'R$ ' + self.valorvenda + ',00' + '\n' + 'Data e hora: ' + self.diaV + '/' + self.mesV + '/' + self.anoV + ' > ' + self.horaV + '\n'+ '\n' + 'Total: R$ ' + self.total+',00').title()
                self.gravaMemoria()
                return 'Venda cancelada'
            else:
                return 'Valores informados inválidos'

        #+++++++ VENDAS ++++++
        elif frase == 'venda' or frase == '/command13':
            return 'Qual o número do quarto?'
        elif ultimaFrase == 'Qual o número do quarto?':
            if frase in quartos and frase in self.frases:
                self.chaveQuarto = frase
                return 'Qual o ítem?'
            else:
                if frase.isnumeric():
                    return 'Não há check-in nesse quarto'
                else:
                    return 'Dados informados inválidos'
        #+++++++++

        elif ultimaFrase == 'Certo, digite o número do quarto.':
            if frase in quartos and frase in self.frases:
                if self.frases[frase] == 'vazio':
                    self.chaveQuarto = frase
                    return 'Informe o nome completo do responsável do quarto.'
                else:
                    self.chaveQuarto = frase
                    return 'Este quarto já está cadastrado, digite 1 para alterá- lo ou 2 para vendas'
            elif frase in quartos:
                self.chaveQuarto = frase
                return 'Informe o nome completo do responsável do quarto.'
            else:
                return 'Valores informados inválidos'

        elif ultimaFrase == 'Este quarto já está cadastrado, digite 1 para alterá- lo ou 2 para vendas' and frase == '1':
            return 'Informe o nome completo do responsável do quarto.'
        elif ultimaFrase == 'Este quarto já está cadastrado, digite 1 para alterá- lo ou 2 para vendas' and frase == '2':
            return 'Qual o ítem?'

        #+++++++++
        elif ultimaFrase == 'Qual o ítem?':
            cardapio = {'pc camarão':70,'pc calabresa':40,'pc fritas':25,'drink':20,'suco':10,'cerveja':7,'refrigerante':5}
            self.item = frase
            if self.item in cardapio:
                self.valor = int(cardapio[self.item])
                return 'Quantidade?'
            else:
                return 'Este ítem não contém na lista'

        elif ultimaFrase == 'Quantidade?':
            self.quantidade = frase
            if (self.quantidade).isnumeric():
                self.quantidade = int(self.quantidade)
                self.valorvenda = self.quantidade * self.valor
                try:
                    self.total = str(self.total)
                except:
                    with open('arquivo.txt','r') as arquivo:
                        texto = arquivo.readlines()
                        string = self.chaveQuarto
                        for i in texto:
                            if string in i:
                                total = str(texto[5:])
                                self.total = total
                self.total = int(self.total)
                self.total += int(self.valorvenda)
                self.quantidade = str(self.quantidade)
                self.valor = str(self.valor)
                self.total = str(self.total)
                self.valorvenda = str(self.valorvenda)
                dataEhoraV = datetime.now()
                self.anoV = str(dataEhoraV.year)
                self.mesV = str(dataEhoraV.month)
                self.diaV = str(dataEhoraV.day)
                self.horaV = str(strftime('%H:%M'))
                self.frases[self.chaveQuarto] += ('\n'+'\n'+'Venda' + '\n' + 'Ítem: ' + self.item + '\n' + 'Valor por unidade: ' + 'R$ ' + self.valor + ',00' + '\n' + 'Quantidade: ' + self.quantidade + '\n' + 'Valor da venda: ' + 'R$ ' + self.valorvenda + ',00' + '\n' + 'Data e hora: ' + self.diaV + '/' + self.mesV + '/' + self.anoV + ' > ' + self.horaV + '\n'+ '\n' + 'Total: R$ ' + self.total+',00').title()
                self.gravaMemoria()
                chave = self.chaveQuarto
                total = self.total
                reescreva = str(chave +' '+ total)

                with open('arquivo.txt','w') as arquivo:
                    arquivo.write(reescreva)
                return 'Venda realizada com sucesso'
            else:
                return 'Valores informados inválidos'
        #################

        elif ultimaFrase == 'Informe o nome completo do responsável do quarto.':
            self.chaveNome = frase
            return 'Acompanhantes? Se "não", digite "0", se "sim", digite o primeiro nome de cada acompanhante, exemplo: maria pedro lucas ana'

        elif ultimaFrase == 'Acompanhantes? Se "não", digite "0", se "sim", digite o primeiro nome de cada acompanhante, exemplo: maria pedro lucas ana':
            self.chaveAcompanhantes = str(frase)
            return 'Deseja confirmar o check-in?'

        elif ultimaFrase == 'Deseja confirmar o check-in?':
            if 's' or 'sim' in frase:
                dataEhora = datetime.now()
                self.ano = str(dataEhora.year)
                self.mes = str(dataEhora.month)
                self.dia = str(dataEhora.day)
                self.hora = str(strftime('%H:%M'))
                self.item = ''
                self.quantidade = ''
                self.diaV = ''
                self.mesV = ''
                self.anoV = ''
                self.horaV = ''
                self.total = '0'
                self.frases[self.chaveQuarto] = ('Número do quarto: ' + self.chaveQuarto + '\n' + 'Responsável: ' + self.chaveNome + '.\n' + 'Acompanhantes: ' + self.chaveAcompanhantes + '.\n' + 'Data e hora do check-in: ' + self.dia + '/' + self.mes + '/' + self.ano + ' > ' + self.hora + self.item +self.quantidade + self.diaV + self.mesV + self.anoV + self.horaV + '\n' + 'Total: ' + self.total).title()
                self.gravaMemoria()
                return 'Check-in realizado com sucesso!'
            elif 'n' or 'nao' or 'não' in frase:
                return 'Certo, o cadastro foi cancelado!'

        ### Conferir quarto ########################################
        elif frase == 'conferir quarto' or frase == '/command11':
            return 'Certo, qual é o quarto?'
        elif ultimaFrase == 'Certo, qual é o quarto?':
            if frase.isnumeric() and frase in self.frases:
                return self.frases[frase]

        ###########################################     
        #Nesta parte, você pode programar ações para que o programe execute somente antes de chamá-lo pelo nome
        elif frase == 'bot':
            comandos = str(random.choice(respostas))
            return comandos

        elif ultimaFrase in respostas:
            if frase in self.frases:
                return self.frases[frase]

            elif frase == 'tchau':
                return 'tchau'
            
            else:            
                try:  #Nesta parte, se a frase digitada for uma equação numérica, o chatbot tentará resolve-la ##########
                    if ' x ' in frase:
                        frase = frase.replace(' x ','*')
                    resp = str(eval(frase))
                    return resp

                except:
                    #Caso nenhum processo anterior seja executado, o chatbot usará a api do google para te retornar uma resposta
                    #existem limitações
                    cb = BuscaWeb()
                    resultado = cb.start(frase)
                    chave = str(resultado[0])
            
                    if(chave == "nenhum resultado"):
                        if 'traduza para o inglês ' in frase:
                            frase = frase.replace('traduza para o inglês ','')
                            time.sleep(1)
                            pi.hotkey('shift','2')
                            pi.typewrite('ytranslatebot >> ' + frase)
                            pi.click(790, 416, button='left', duration=3)
                            time.sleep(1)
                            return 'pronto'
			#usa wikipedia para tentar encontrar uma resposta
                        elif 'quem é ' in frase:
                            frase2 = frase.replace('quem é ','')
                            frase3 = frase2.title()
                            
                            if ' De ' in frase3:
                                frase4 = frase3.replace(' De ',' de ')
                                frase5 = frase4.replace(' ','_')
                                novaChave = ('https://pt.wikipedia.org/wiki/'+frase5)
                                return novaChave
                            else:
                                frase4 = frase3.replace(' ','_')
                                novaChave = ('https://pt.wikipedia.org/wiki/'+frase4)
                                return novaChave

                        elif 'quem foi ' in frase:
                            frase2 = frase.replace('quem foi ','')
                            frase3 = frase2.title()

                            if ' De ' in frase3:
                                frase4 = frase3.replace(' De ',' de ')
                                frase5 = frase4.replace(' ','_')
                                novaChave = ('https://pt.wikipedia.org/wiki/'+frase5)
                                return novaChave
                            else:
                                frase4 = frase3.replace(' ','_')
                                novaChave = ('https://pt.wikipedia.org/wiki/'+frase4)
                                return novaChave


                        elif 'o que é ' in frase:
                            frase2 = frase.replace('o que é ','')
                            frase3 = frase2.replace(' ','_')
                            novaChave = ('https://pt.wikipedia.org/wiki/'+frase3)
                            return novaChave


                        #verificando se é uma música que deseja tocar, procurando no youtube ##################
                        elif 'tocar ' in frase:
                            frase = frase.replace('tocar ','')
                            try:
                                mixer.init()
                                mixer.music.load('/home/doug/Música/'+frase+'.mp3')
                                mixer.music.play()
                                return 'pronto'
                                
                            except:
                                pi.click(651, 727, button='left', duration=0.30)
                                pi.hotkey('shift','2')
                                pi.typewrite('vid ' + frase)
                                pi.click(684, 586, button='left', duration=3)
                                time.sleep(2)
                                pi.click(684, 586, button='left')
                                time.sleep(2)
                                pi.click(684, 586, button='left')
                                return 'pronto'

                        elif 'fechar som' or 'fechar música' in frase:
                            pi.click(660, 696, button='left', duration=0.30)
                            return 'pronto'


                        elif 'traduza para o inglês ' in frase:
                            frase = frase.replace('traduza para o inglês ','')
                            time.sleep(1)
                            pi.hotkey('shift','2')
                            pi.typewrite('ytranslatebot >> ' + frase)
                            pi.click(748, 547, button='left', duration=4)
                            time.sleep(2)
                            return 'pronto'

                        elif 'traduza para o português ' in frase:
                            frase = frase.replace('traduza para o português ','')
                            time.sleep(1)
                            pi.hotkey('shift','2')
                            pi.typewrite('ytranslatebot >> ' + frase)
                            pi.click(748, 547, button='left', duration=4)
                            time.sleep(2)
                            return 'pronto'

                        elif 'como fazer ' in frase:
                            frase = frase.replace('como fazer ','')
                            pi.click(648, 726, button='left', duration=0.30)
                            pi.hotkey('shift','2')
                            pi.typewrite('vid ' + frase)
                            pi.click(748, 547, button='left', duration=4)
                            time.sleep(2)
                            pi.click(748, 547, button='left')
                            time.sleep(2)
                            pi.click(748, 547, button='left')
                            return 'pronto'

			
			#retorna uma frase caso nada tenha sido encontrado
                        else:
                            respostas1 = ['Não encontrei nada em minhas fontes...','Desculpe, não achei nada relativo...','Acho que essa eu não vou conseguir te responder.',]
                            respostas2 = str(random.choice(respostas1))
                            return (respostas2)
                
                    else:   #retorna pesquisa do google
                        return(resultado[0])

        else:            
            #Nesta parte, se a frase digitada for uma equação numérica, o chatbot tentará resolve-la ##########
            try:
                if ' x ' in frase:
                    frase = frase.replace(' x ','*')
                resp = str(eval(frase))
                return resp
            except:      
                return 'Comando não reconhecido'



    def pegaNome(self,nome):
        if 'o meu nome é ' in nome:
            nome = nome[500:]
        nome = nome.title()
        return nome


    def respondeNome(self,nome):
        if nome in self.conhecidos:
            frase = 'Oi '
        else:
            frase = 'Muito prazer '
            self.conhecidos.append(nome)
            self.gravaMemoria()
        return frase+nome


    def gravaMemoria(self):
        memoria = open(self.nome+'.json','w')
        json.dump([self.conhecidos,self.frases],memoria)
        memoria.close()
                       
		
    def fala(self,frase):          
        if 'executa ' in frase:
            plataforma = sys.platform
            comando = frase.replace('executa ','')
            if 'win' in plataforma:
                os.startfile(comando)
            if 'linux' in plataforma:
                try:
                    s.Popen(comando)
                except FileNotFoundError:
                    s.Popen(['xdg-open',comando])
            
        else:
            print(frase)
        self.historico.append(frase)
       
