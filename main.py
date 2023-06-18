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
          pygame.draw.circle(tela, branco,(coordenada), 5) 
          print(item)     
              
              
          texto=font.render(item, True, (branco))
          tela.blit(texto,(coordenada))                
          if estrelas>1:
              pygame.draw.line(tela, branco, (coordenadas[-2]),(coordenadas[-1]),2)
            
       
        if event.type== pygame.KEYDOWN and event.key == pygame.K_F12:
            tela.blit(fundo,(0,0))
            estrelas=0


        if event.type == pygame.QUIT:
            running = False
        elif event.type== pygame.KEYDOWN and event.key == pygame.K_ESCAPE:  
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
    