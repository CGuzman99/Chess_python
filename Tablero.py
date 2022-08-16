import numpy as np
from Pieza import *

#Crea una matriz de 8x8 donde se encuentran las piezas
def crearCasillas() :
	casillas = crearMatriz()
	crearPiezas(casillas)
	return casillas
#Crea una arreglo de 2 dimensiones
def crearMatriz() :
	casillas = []
	for i in range(0,8) :
		casillas.append([])
		for j in range(0,8) : 
			casillas[i].append(None)
	return casillas
#Crea las piezas
def crearPiezas(casillas) :
	for i in range(0,8) :
		for j in range(0,8) :
			if j==0 :
				if i==0 or i==7 :
					casillas[i][j] = Torre()
					casillas[i][j].asignarProp('N',i,j)
				elif i==1 or i==6 :
					casillas[i][j] = Caballo()
					casillas[i][j].asignarProp('N',i,j)
				elif i==2 or i==5 :
					casillas[i][j] = Alfil()
					casillas[i][j].asignarProp('N',i,j)
				elif i==3 :
					casillas[i][j] = Dama()
					casillas[i][j].asignarProp('N',i,j)
				else :
					casillas[i][j] = Rey()
					casillas[i][j].asignarProp('N',i,j)
			elif j==7 :
				if i==0 or i==7 :
					casillas[i][j] = Torre()
					casillas[i][j].asignarProp('B',i,j)
				elif i==1 or i==6 :
					casillas[i][j] = Caballo()
					casillas[i][j].asignarProp('B',i,j)
				elif i==2 or i==5 :
					casillas[i][j] = Alfil()
					casillas[i][j].asignarProp('B',i,j)
				elif i==3 :
					casillas[i][j] = Dama()
					casillas[i][j].asignarProp('B',i,j)
				else :
					casillas[i][j] = Rey()
					casillas[i][j].asignarProp('B',i,j)
			elif j==1 :
				casillas[i][j] = Peon()
				casillas[i][j].asignarProp('N',i,j)
			elif j==6 :
				casillas[i][j] = Peon()
				casillas[i][j].asignarProp('B',i,j)

def cambiarTurno(Turno) :
	t = Turno
	if t=='B' :
		t = 'N'
	else :
		t = 'B'
	return t

def mover(tab,pieza,x,y) :
	tablero = tab
	if pieza!=None :
		tablero[x][y]==pieza
		tablero[pieza.pos_x][pieza.pos_y] = None
		if tablero[x][y]!=None :
			tablero[x][y].setPos(x,y)
	return tablero
#Deermina si hay jaque
def Jaque(tablero,Turno) :
	rey = None
	for i in range(0,8) :
		for j in range(0,8) :
			if tablero[i][j]!=None and tablero[i][j].color==Turno and tablero[i][j].toString()=="Rey" :
				rey = tablero[i][j]
				break
		if rey!=None :
			break
	for i in range(0,8) :
		for j in range(0,8) :
			if tablero[i][j]!=None and tablero[i][j].movimientoValido(tablero,rey.pos_x,rey.pos_y) :
				return True
	return False
#Determina si es jaque mate
def JaqueMate(tablero,Turno) :
	jm = False
	if Jaque(tablero,Turno) :
		rey = None
		for i in range(0,8) :
			for j in range(0,8) :
				if tablero[i][j]!=None and tablero[i][j].color==Turno and tablero[i][j].toString()=="Rey" :
					rey = tablero[i][j]
					break
			if rey!=None :
				break
		for i in range(rey.pos_x-1,rey.pos_x+2) :
			jm = False
			for j in range(rey.pos_y-1,rey.pos_y+2) :
				if i>=0 and i<8 and j>=0 and j<8 :
					for x in range(0,8) :
						for y in range(0,8) :
							if (i!=rey.pos_x or j!=rey.pos_y) and tablero[x][y]!=None and tablero[x][y].color!=rey.color and tablero[x][y].movimientoValido(tablero,i,j) :
								jm = True
				if jm :
					break
			if not jm :
				break
	return jm
