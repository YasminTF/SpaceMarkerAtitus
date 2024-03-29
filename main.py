from funcoes import criarBaseDados
import pygame 
import winsound 
import time
from tkinter import simpledialog

pygame.init()
pygame.mixer.music.load("Space_Machine_Power.mp3")
pygame.mixer.music.play(-1)
pygame.font.init()
font = pygame.font.Font(None, 30)
branco= (255,255,255)
tamanho =(1500,800)
clock= pygame.time.Clock()
tela = pygame.display.set_mode(tamanho)
pygame.display.set_caption("Space Marker")
icone = pygame.image.load("logo.png")
pygame.display.set_icon(icone)
fundo = pygame.image.load("image.jpeg")

running = True
estrelas = 0
coordenada = []
coordenadas = []
nomeEstrela=[]
coordenadaEnome=[]
dicionario = {coordenadaEnome[i]: coordenadaEnome[i+1] for i in range(0, len(coordenadaEnome), 2)}
tela.fill(branco)
tela.blit(fundo,(0,0))
criarBaseDados()
while running: 
    for event in pygame.event.get():  
        if event.type==pygame.MOUSEBUTTONUP:
          coordenada = pygame.mouse.get_pos()
          item= simpledialog.askstring("Space" ,  "Nome da estrela:")
          if item =="":
             print("DESCONHECIDO")
             item= ("DESCONHECIDO" +str(coordenada))
          if item == None:
            break 
          
          estrelas = estrelas +1 
          coordenadas.append(coordenada)
          nomeEstrela.append(item) 
          coordenadaEnome.append(coordenada)
          coordenadaEnome.append(item) 
          pygame.draw.circle(tela, branco,(coordenada), 5)                           
          texto=font.render(item, True, (branco))
          tela.blit(texto,(coordenada))                
          if estrelas>1:
              pygame.draw.line(tela, branco, (coordenadas[-2]),(coordenadas[-1]),2)
              
        if event.type== pygame.KEYDOWN and event.key == pygame.K_F10:
            with open('banco_dados.txt', 'w') as arquivo:
                pass
   
            dicionario = {coordenadaEnome[i]: coordenadaEnome[i+1] for i in range(0, len(coordenadaEnome), 2)}
            print(dicionario)
            arquivo = open('banco_dados.txt','a')
            arquivo.write(str(dicionario))
            arquivo.close()
            break
        
        if event.type== pygame.KEYDOWN and event.key == pygame.K_F11:
            estrelas=2
            try:
              with open('banco_dados.txt', 'r') as file:
                dados = eval(file.read())
                
                for coordenada, nome in dados.items():
                    pygame.draw.circle(tela, branco, coordenada, 5) 
                    coordenadas.append(coordenada)
                    texto = font.render(nome, True, branco)
                    tela.blit(texto, (coordenada[0] + 12, coordenada[1] + 12))
                    coordenadaEnome.append(coordenada)
                    coordenadaEnome.append(nome)                   
                    coordenada = list(dados.keys())
                    for i in range(len(coordenada) - 1):
                        coordenada_atual = coordenada[i]
                        proxima_coordenada = coordenada[i+1]
                        pygame.draw.line(tela, branco, coordenada_atual, proxima_coordenada, 1)
                        pygame.display.flip()
            except:
                print("Nenhum save encontrado, por favor salve apertando a tecla F10")  
                
                
        if event.type== pygame.KEYDOWN and event.key == pygame.K_F12:
            with open('banco_dados.txt', 'w') as arquivo:
                pass
            coordenadaEnome= []
            tela.blit(fundo,(0,0))
            estrelas=0
            
        if event.type == pygame.QUIT:
            with open('banco_dados.txt', 'w') as arquivo:
                pass
            
               
            dicionario = {coordenadaEnome[i]: coordenadaEnome[i+1] for i in range(0, len(coordenadaEnome), 2)}
            print(dicionario)
            arquivo = open('banco_dados.txt','a')
            arquivo.write(str(dicionario))
            arquivo.close()
           
            running = False

        elif event.type== pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            with open('banco_dados.txt', 'w') as arquivo:
                pass
            
            dicionario = {coordenadaEnome[i]: coordenadaEnome[i+1] for i in range(0, len(coordenadaEnome), 2)}
            print(dicionario)
            arquivo = open('banco_dados.txt','a')
            arquivo.write(str(dicionario))
            arquivo.close()

            running= False
        
    texto = font.render("Pressione F10 para Salvar os Pontos", True, (branco))
    tela.blit(texto,(10,10))
    texto2 = font.render("Pressione F11 para Carregar os Pontos", True, (branco))
    tela.blit(texto2,(10,30))
    texto3 = font.render("Pressione F12 para Deletar os Pontos", True, (branco))
    tela.blit(texto3,(10,50))
          
    time.sleep(0.01)
    pygame.display.flip()
pygame.display.update()        