import pygame,sys
from pygame.locals import *
from tkinter import *
from tkinter import messagebox as MessageBox
from Tablero import *
from Pieza import *

#Dibuja los componentes de la ventana
def paint(ventana,tablero,string,Turno) :
	pygame.init()

	BLACK = (0,0,0)
	WHITE = (255,255,255)
	LIGHT_GRAY = (64,64,64)
	DARK_GRAY = (192,192,192)
	D_W = (139,115,85)
	L_W = (238,197,145)
	inicio_tab_x = 150
	inicio_tab_y = 150
	ancho_tab = 400
	alto_tab = 400
	ventana.fill(WHITE)
	fuente = pygame.font.SysFont(None,24)

	#Imprime el turno en la parte superior
	if Turno=='B' :
		txt = "Turno: piezas blancas"
	else :
		txt = "Turno: piezas negras"
	texto = fuente.render(txt,True,BLACK,WHITE)
	textoRect = texto.get_rect()
	textoRect.topleft = (inicio_tab_x+(ancho_tab/4),inicio_tab_y-50)
	ventana.blit(texto,textoRect)
	pygame.draw.rect(ventana,D_W,(inicio_tab_x,inicio_tab_y,ancho_tab,alto_tab))
	
	#Imprime las casillas y las piezas del juego
	for i in range(0,8) :
		for j in range(0,8) :
			if ((i+j)%2)==0 :
				pygame.draw.rect( ventana,L_W,(inicio_tab_x+(i*50),inicio_tab_y+(j*50),50,50) )
			if( tablero[i][j]!=None ) :
				imgRect = pygame.Rect(inicio_tab_x+(i*50),inicio_tab_y+(j*50),50,50)
				img = pygame.image.load( tablero[i][j].getImageName() )
				ventana.blit(img,imgRect)
		
		#Imprime las etiqetas de los renglones y las columnas del tablero
		texto = fuente.render(str(i+1),True,BLACK,WHITE )
		textoRect = texto.get_rect()
		textoRect.topleft = (inicio_tab_x-35,inicio_tab_y+alto_tab-35-(i*50))
		textoRect.size = (20,20)
		ventana.blit(texto,textoRect)
		
		texto = fuente.render( chr(i+65),True,BLACK,WHITE )
		textoRect = texto.get_rect()
		textoRect.topleft = (inicio_tab_x+20+(i*50),inicio_tab_y+alto_tab+15)
		textoRect.size = (20,20)
		ventana.blit(texto,textoRect)

	#Imprime la pieza selecionada
	st = fuente.render(string,True,BLACK,WHITE)
	stRect = st.get_rect() 
	stRect.topleft = (20,20)
	stRect.size = (20,50)
	ventana.blit(fuente.render("",True,WHITE,WHITE),stRect)
	ventana.blit(st,stRect)

def test() :
	MessageBox.showinfo(None,"Jaque Mate")

pygame.init()

inicio_tab_x = 150
inicio_tab_y = 150
ancho_tab = 400
alto_tab = 400

#Crea la ventana
ventana = pygame.display.set_mode((700,700),0,32)
pygame.display.set_caption('Ajedrez en python')
#Crea las casillas
tablero = crearCasillas()
string = ""
pieza = None
Turno = 'B'

while not JaqueMate(tablero,Turno) :
	paint(ventana,tablero,string,Turno)
	event = pygame.event.wait()
	#Lee los eventos realizados con el mouse
	if event.type==pygame.MOUSEBUTTONDOWN :
		x = int( (event.pos[0]-(event.pos[0]%50)-inicio_tab_x)/50 )
		y = int( (event.pos[1]-(event.pos[1]%50)-inicio_tab_y)/50 )
		if x>=0 and x<8 and y>=0 and y<8 :
			if tablero[x][y]!=None and tablero[x][y].color==Turno :
				pieza = tablero[x][y]
				string = pieza.toString()
			elif pieza!=None and pieza.color==Turno :
				#if Jaque(tablero,Turno) :	
				if pieza.toString()=="Rey" and (pieza.pos_x!=x or pieza.pos_y!=y) and pieza.movimientoValido(tablero,x,y) :
					tablero[x][y] = pieza
					tablero[pieza.pos_x][pieza.pos_y] = None
					tabler[x][y].setPos(x,y)
					Turno = cambiarTurno(Turno)
					paint(ventana,tablero,string,Turno)
				#else :
				if (pieza.pos_x!=x or pieza.pos_y!=y) and pieza.movimientoValido(tablero,x,y) :
					#tablero = mover(tablero,pieza,x,y)
					tablero[x][y] = pieza
					tablero[pieza.pos_x][pieza.pos_y] = None
					tablero[x][y].setPos(x,y)
					Turno = cambiarTurno(Turno)
					paint(ventana,tablero,string,Turno)
	elif event.type==pygame.MOUSEBUTTONUP :
		x = int( (event.pos[0]-(event.pos[0]%50)-inicio_tab_x)/50 )
		y = int( (event.pos[1]-(event.pos[1]%50)-inicio_tab_y)/50 )
		if x>=0 and x<8 and y>=0 and y<8 :
			if tablero[x][y]!=None and tablero[x][y]==Turno :
				pieza = tablero[x][y]
				string = pieza.toString()
			elif pieza!=None and pieza.color==Turno :
				if Jaque(tablero,Turno) :
					if pieza.toString()=="Rey" and (pieza.pos_x!=x or pieza.pos_y!=y) and pieza.movimientoValido(tablero,x,y) :
						tablero[x][y] = pieza
						tablero[pieza.pos_x][pieza.pos_y] = None
						tabler[x][y].setPos(x,y)
						Turno = cambiarTurno(Turno)
						paint(ventana,tablero,string,Turno)
				else :
					if (pieza.pos_x!=x or pieza.pos_y!=y) and pieza.movimientoValido(tablero,x,y) :
						#tablero = mover(tablero,pieza,x,y)	
						tablero[x][y] = pieza
						tablero[pieza.pos_x][pieza.pos_y] = None
						tablero[x][y].setPos(x,y)				
						Turno = cambiarTurno(Turno)
						paint(ventana,tablero,string,Turno)
	#Termina el juego si la ventana es cerrada
	elif event.type==QUIT :
		pygame.quit()
		sys.exit()

	pygame.display.update()

root = Tk()
Button(root,text="Aceptar",command=test).pack()
#root.mainloop()
for event in pygame.get_event() :
	if event.type==QUIT :
		pygame.quit()
		sys.exit()