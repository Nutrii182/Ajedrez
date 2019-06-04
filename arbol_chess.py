import chess
import random

board = chess.Board()
aux = []
aux2 = []
auxHijos = []
auxTiros = []

class arbol():

    def __init__(self,coordenada,peso):
    	self.coordenada = coordenada
    	self.peso = peso
    	self.hijos = []

    def eliminar_nodo(self, nodo):
        for hijos in nodo.hijos:
            nodo.hijos.pop()
            return self.eliminar_nodo(nodo)

    def insertar_coor(self,nodo,coordenada):
        for x in aux:
            self.busquedaEliminarArbolRepetidos(nodo.hijos,self.clave(x))
            nodo.hijos.append(arbol(self.clave(x),random.randrange(10)))


        for x in range(len(aux)):
            e = self.busquedaOrigen(nodo, aux[x][0:2])
            e.hijos.append(arbol(aux[x][0:4],random.randrange(10)))


    def busquedaOrigen(self, nodo, nodo_buscar):
        if(nodo.coordenada == nodo_buscar):
            return nodo
        else:
            for x in nodo.hijos:
                e = self.busquedaOrigen(x, nodo_buscar)
                if(e != None):
                    return e


    def busquedaEliminarArbolRepetidos(self, hijos, busqueda):
        for x in range(len(hijos)):
            if(hijos[x].coordenada == busqueda):
                return hijos.pop(x)


    def heuristica(self, nodo, hijos):
        self.jugadas()
        self.insertar_coor(nodo, aux)
        self.tiros(nodo.hijos)

        indice_ficha = self.ObteniendoPesoFicha(hijos)
        indice_tiro = self.ObteniendoPesoTiro(nodo, hijos, indice_ficha)

        #print(indice_ficha)
        #print(indice_tiro)

        tiro = self.tiro(nodo.hijos, indice_ficha, indice_tiro)
        print(tiro)
        #print(tiro)

        if tiro == None:
            self.Limpiar(nodo)
            self.eliminar_nodo(nodo)
            self.heuristica(nodo, hijos)

        else:
            x = chess.Move.from_uci(tiro)
            board.push(x)

            if board.is_check():
                print('Jaque al Jugador')
            else:
                pass

            if board.is_checkmate():
                print('Jaque Mate al jugador')
                board.is_game_over()
            else:
                pass


    def Limpiar(self, nodo):
        for x in range(len(aux)):
            aux.pop()

        for x in range(len(aux2)):
            aux2.pop()

        for x in range(len(auxHijos)):
            auxHijos.pop()

        for x in range(len(auxTiros)):
            auxTiros.pop()


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
                return self.prueba(hijos[x].hijos, indice_tiro)


    def prueba(self, hijos, indice_tiro):
        tiroFinal =[]
        for x in range(len(hijos)):
            if hijos[x].peso == indice_tiro:
                tiroFinal.append(hijos[x].coordenada)
                #print("-> ",tiroFinal)
                return max(tiroFinal)


    def imprimir(self,nodo,nivel):
    	print(nivel,nodo.coordenada,nodo.peso)
    	for n in nodo.hijos:
    		self.imprimir(n,nivel+"-")


    def clave(self,ubicacion):
        a = ubicacion[0:2]
        return a


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
    		aux.append(str(x))



n = arbol("raiz",0)

while(True):


    n.heuristica(n, n.hijos)
    #n.imprimir(n,"-")

    print("\n")
    print(board.unicode())
    print("\n")

    n.Limpiar(n)
    n.eliminar_nodo(n)

    print("Tira el jugador: ")
    a = input("Donde desea tirar: ")
    x = chess.Move.from_uci(str(a))
    board.push(x)

    if board.is_check():
        print('Jaque')
    else:
        pass

    if board.is_checkmate():
        print('Jaque Mate al jugador')
        board.is_game_over()
    else:
        pass

    #h2h4 f1g3 tiros posisbles de principio


#print(chess.Piece(2, 0))
#print(chess.square_distance(2,2))
#print(board.piece_at(56))
#print(board.piece_type_at(3))

#random.choice(aux)
