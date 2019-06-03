# las blancas es la PC (TRUE)(1)
# las negras somo nosotros (FALSE)(0)

import chess
import random

board = chess.Board()
aux = []
aux2 = []

auxHijos = []
auxTiros = []

tiroFinal = []


figuras = {'P': 1, 'N': 2,'B': 3, 'R': 4, 'Q': 5, 'K': 6}

class arbol():

    def __init__(self,coordenada,peso):
    	self.coordenada = coordenada
    	self.peso = peso
    	self.hijos = []


    def insertar_coor(self,nodo,coordenada):
        for x in aux:
            self.busquedaEliminarArbolRepetidos(nodo.hijos,self.clave(x))
            nodo.hijos.append(arbol(self.clave(x),random.randrange(10)))

###########################

        #insertando el tercer nivel

        for x in range(len(aux)):
            e = self.busquedaOrigen(nodo, aux[x][0:2]) #se puede hacer esto we en aux(aproveche que tenemos los datos ahi) <indice,lo que quiero cortandolo>
            e.hijos.append(arbol(aux[x][0:4],random.randrange(10))) # en donde nos retorne lo que encontro el nodo ahi insertamos ahora lo que queremos <indice,lo que quiero cortandolo>


    def busquedaOrigen(self, nodo, nodo_buscar): # la funcion que busqueda en el ejemplo del primer arbol que te mostre funciono que es lo que pensaste de regresar el nodo
        if(nodo.coordenada == nodo_buscar):
            return nodo
        else:
            for x in nodo.hijos:
                e = self.busquedaOrigen(x, nodo_buscar)
                if(e != None):
                    return e

###########################

    def busquedaEliminarArbolRepetidos(self, hijos, busqueda):
        for x in range(len(hijos)):
            if(hijos[x].coordenada == busqueda):
                return hijos.pop(x)


#########################

    def heuristica(self, nodo, hijos):
        indice_ficha = self.ObteniendoPesoFicha(hijos)
        indice_tiro = self.ObteniendoPesoTiro(nodo, hijos, indice_ficha)

        print(indice_ficha)
        print(indice_tiro)

        self.tiro(nodo.hijos, indice_ficha, indice_tiro)

        print(tiroFinal[0])


    def ObteniendoPesoFicha(self, hijos):
        for x in range(len(hijos)):
            auxHijos.append(hijos[x].peso)
        return max(auxHijos)


    def ObteniendoPesoTiro(self, nodo, hijos, num_buscar_max):
        for x in range(len(hijos)):
            for y in range(len(hijos[x].hijos)):
                if (hijos[x].peso == num_buscar_max):
                    auxTiros.append(hijos[x].hijos[y].peso)
        return max(auxTiros)


    def tiro(self, hijos, indice_ficha, indice_tiro):
        for x in range(len(hijos)):
            if hijos[x].peso == indice_ficha:
                self.prueba(hijos[x].hijos, indice_tiro)
                return

    def prueba(self, hijos, indice_tiro):
        for x in range(len(hijos)):
            if hijos[x].peso == indice_tiro:
                tiroFinal.append(hijos[x].coordenada)



#########################

    def imprimir(self,nodo,nivel):
    	print(nivel,nodo.coordenada,nodo.peso)
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



n = arbol("raiz",0)
n.jugadas()
n.insertar_coor(n,aux)

#print(n.busqueda_arbol(n.hijos,"g1"))

n.tiros(n.hijos)
n.imprimir(n,"-")

print("\n")
n.heuristica(n, n.hijos)
print("\n")

print(board)
print("\n")

#print(chess.Piece(2, 0))
#print(chess.square_distance(2,2))
#print(board.piece_at(56))
#print(board.piece_type_at(3))

#random.choice(aux)
