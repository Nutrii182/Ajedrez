import chess
import random

board = chess.Board()
aux = []
aux2 = []

class arbol():

    def __init__(self,coordenada):
    	self.coordenada = coordenada
    	#self.pesos = {'P': 1, 'N': 2,'B': 3, 'R': 4, 'Q': 5, 'K': 6}
    	#self.heuristica = heuristica
    	self.hijos = []

    '''
    def valida_tiro(self, x):
    	if x == 'g1h3':
    		return 'Nh3'
    	elif x == 'g1f3':
    		return 'Nf3'
    	elif x == 'b1c3':
    		return 'Nc3'
    	elif x == 'b1a3':
    		return 'Na3'
    	else:
    		return x'''

    def insertar_coor(self,nodo,coordenada):
        for x in aux:
            self.busqueda_arbol(nodo.hijos,self.clave(x))
            nodo.hijos.append(arbol(self.clave(x)))


    def busqueda_arbol(self, hijos, busqueda):
        for x in range(len(hijos)):
            if(hijos[x].coordenada == busqueda):
                return hijos.pop(x)

    def imprimir(self,nodo,nivel):
    	print(nivel,nodo.coordenada)
    	for n in nodo.hijos:
    		self.imprimir(n,nivel+"-")

    def clave(self,ubicacion):
    		a = ubicacion[0:2]
    		return a

    '''def tiros(self,hijos):
    	for x in hijos:
    		for y in aux:
    			if self.clave(y) == x.coordenada:
    				aux2.append(y)'''

    def tiros(self,hijos):
        for x in hijos:
            for c in range(len(aux)):
                if x.coordenada == self.clave(aux[c]):
                    if aux[c] in aux2:
                        pass
                    else:
                        aux2.append(aux[c])
                else:
                    break

    def jugadas(self):
    	v = board.legal_moves
    	for x in v:
    		#aux.append(self.valida_tiro(str(x))
    		aux.append(str(x))
    	#ran = random.choice(aux)
    	#if ran in aux:
    	#	board.push_san(ran)

n = arbol("raiz")
n.jugadas()
n.insertar_coor(n,aux)

#print(n.busqueda_arbol(n.hijos,"g1"))

n.tiros(n.hijos)
n.imprimir(n,"-")

#print(aux)
#print('')
#print("\n->",aux2)

#print("\n")
#print(board)
