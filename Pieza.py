class Pieza :
	def _init_(self,s) :
		self.string = None
		self.color = None
		self.posInicial = True
		self.pos_x = 0
		self.pos_y = 0

	def setPos(self,x,y) :
		self.pos_x = x
		self.pos_y = y
		self.posInicial = False
	def toString(self) :
		return self.string
	def getImageName(self) :
		s = self.string+self.color+".png"
		return s

class Alfil(Pieza) :
	def _init_(self) :
		Pieza._init_(self)

	def asignarProp(self,c,x,y) :
		self.string = "Alfil"
		self.color = c
		self.pos_x = x
		self.pos_y = y
		self.posInicial = True
	
	def movimientoValido(self,tablero,x,y) :
		dif_x = self.pos_x-x
		dif_y = self.pos_y-y
		if abs(dif_x)!=abs(dif_y) :
			return False
		for i in range(self.pos_x,x,int(dif_x/abs(dif_x))) :
			for j in range(self.pos_y,y,int(dif_y/abs(dif_y))) :
				if abs(self.pos_x-i)==abs(self.pos_y-j) and tablero[i][j]!=None  :
					if tablero[i][j].color==self.color and abs(self.pos_x-i)<=abs(dif_x) :
						return False
					elif tablero[i][j].color!=self.color and abs(self.pos_x-i)<abs(dif_x) :
						return False
		return True

class Caballo(Pieza) :
	def _init_(self,c,x,y) :
		Pieza._init_(self)

	def asignarProp(self,c,x,y) :
		self.string = "Caballo"
		self.color = c
		self.pos_x = x
		self.pos_y = y
		self.posInicial = True

	def movimientoValido(self,tablero,x,y) :
		dif_x = self.pos_x-x
		dif_y = self.pos_y-y
		if ((dif_x**2)+(dif_y**2))!=5 :
			return False
		elif tablero[x][y]!=None and tablero[x][y].color==self.color :
			return False
		return True

class Torre(Pieza) :
	def _init_(self) :
		Pieza._init_(self)

	def asignarProp(self,c,x,y) :
		self.string = "Torre"
		self.color = c
		self.pos_x = x
		self.pos_y = y
		self.posInicial = True

	def movimientoValido(self,tablero,x,y) :
		dif_x = self.pos_x-x
		dif_y = self.pos_y-y
		if self.pos_x!=x and self.pos_y!=y :
			return False
		elif self.pos_x==x :
			for j in range(self.pos_y,y,int(dif_y/abs(dif_y))) :
				if tablero[x][j]!=None :
					return False
		elif self.pos_y==y :
			for i in range(self.pos_x,x,int(dif_x/abs(dif_x))) :
				if tablero[i][y]!=None :
					return False
		elif tablero[x][y]!=None and tablero[x][y].color==self.color :
			return False
		return True

class Dama(Pieza) :
	def _init_(self) :
		Pieza._init_(self)

	def asignarProp(self,c,x,y) :
		self.string = "Dama"
		self.color = c
		self.pos_x = x
		self.pos_y = y
		self.posInicial = True

	def movimientoValido(self,tablero,x,y) :
		dif_x = self.pos_x-x
		dif_y = self.pos_y-y
		if abs(dif_x)!=abs(dif_y) and self.pos_x!=x and self.pos_y!=y :
			return False
		elif self.pos_x==x and dif_y!=0 :
			for j in range(self.pos_y,y,int(dif_y/abs(dif_y))) :
				if tablero[x][j]!=None :
					return False
		elif self.pos_y==y and dif_x!=0 :
			for i in range(self.pos_x,x,int(dif_x/abs(dif_x))) :
				if tablero[i][y]!=None :
					return False
		
		elif abs(dif_x)==abs(dif_y) and dif_x!=0 and dif_y!=0 : 
			for i in range(self.pos_x,x,int(dif_x/abs(dif_x))) :
				for j in range(self.pos_y,y,int(dif_y/abs(dif_y))) :
					if abs(self.pos_x-i)==abs(self.pos_y-j) and tablero[i][j]!=None  :
						if tablero[i][j].color==self.color and abs(self.pos_x-i)<=abs(dif_x) :
							return False
						elif tablero[i][j].color!=self.color and abs(self.pos_x-i)<abs(dif_x) :
							return False
		elif tablero[x][y]!=None and tablero[x][y].color==self.color :
			return False
		return True

class Rey(Pieza) :
	def _init_(self) :
		Pieza._init_(self)

	def asignarProp(self,c,x,y) :
		self.string = "Rey"
		self.color = c
		self.pos_x = x
		self.pos_y = y
		self.posInicial = True

	def movimientoValido(self,tablero,x,y) :
		if abs(self.pos_x-x)>1 and abs(self.pos_y-y)>1 :
			return False
		elif tablero[x][y]!=None and tablero[x][y].color==self.color :
			return False
		for i in range(0,8) :
			for j in range(0,8) :
				if tablero[i][j]!=None and tablero[i][j].color!=self.color :
					if tablero[i][j].toString()!="Rey" and tablero[i][j].movimientoValido(tablero,x,y) :
						return False
		return True

class Peon(Pieza) :
	def _init_(self) :
		Pieza._init_(self)

	def asignarProp(self,c,x,y) :
		self.string = "Peon"
		self.color = c
		self.pos_x = x
		self.pos_y = y
		self.posInicial = True

	def movimientoValido(self,tablero,x,y) :
		dif_x = self.pos_x-x
		dif_y = self.pos_y-y

		if dif_x==0 and abs(dif_y)==2 :
			if self.posInicial :
				if dif_y>0 and tablero[x][y+1]==None and tablero[x][y]==None :
					return True
				elif tablero[x][y-1]==None and tablero[x][y]==None :
					return True
		elif dif_x==0 and abs(dif_y)==1 :
			if tablero[x][y]==None :
				return True
		elif abs(dif_x)==1 and abs(dif_y)==1 :
			if tablero[x][y]!=None and tablero[x][y].color!=self.color :
				return True;
		return False
			