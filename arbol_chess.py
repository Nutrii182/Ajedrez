import chess
import random
import time

board = chess.Board()

aux = []
aux2 = []
aux3 = []
auxHijos = []
auxTiros = []

class arbol():

    def __init__(self, coordenada, peso, tipo):
        self.coordenada = coordenada
        self.peso = peso
        self.tipo = tipo
        self.hijos = []



    def eliminar_nodo(self, nodo):
        for hijos in nodo.hijos:
            nodo.hijos.pop()
            return self.eliminar_nodo(nodo)



    def insertar_coor(self,nodo,coordenada):
        for x in aux:
            self.busquedaEliminarArbolRepetidos(nodo.hijos,self.clave(x))
            nodo.hijos.append(arbol(self.clave(x),random.randrange(10), 1))



        for x in range(len(aux)):
            e = self.busquedaOrigen(nodo, aux[x][0:2])
            e.hijos.append(arbol(aux[x][0:4],random.randrange(10), 1))



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

        indice_ficha = self.ObteniendoPesoFicha(hijos)
        indice_tiro = self.ObteniendoPesoTiro(nodo, hijos, indice_ficha)
        tiro = self.encontrandoFicha(nodo.hijos, indice_ficha, indice_tiro)

        if tiro != None:
            print("Tiro de maquina (Negras): ",tiro)
            print("Moviminetos ----> ",board.legal_moves.count())


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



    def encontrandoFicha(self, hijos, indice_ficha, indice_tiro):
        for x in range(len(hijos)):
            if hijos[x].peso == indice_ficha:
                return self.encontrandoTiro(hijos[x].hijos, indice_tiro)



    def encontrandoTiro(self, hijos, indice_tiro):
        tiroFinal =[]
        for x in range(len(hijos)):
            if hijos[x].peso == indice_tiro:
                tiroFinal.append(hijos[x].coordenada)
                return max(tiroFinal)



    def clave(self,ubicacion):
        a = ubicacion[0:2]
        return a



    def jugadas(self):
        v = board.legal_moves
        for x in v:
            aux.append(str(x))



    def imprimir(self,nodo,nivel):
    	print(nivel,nodo.coordenada,nodo.peso)
    	for n in nodo.hijos:
    		self.imprimir(n,nivel+"-")


n = arbol("raiz",0,0)

while(True):

    print("\n------------------------------------ \n")
    start_time = time.time()
    print("Tiempo de ejecución --> ", time.time() - start_time)

    n.heuristica(n, n.hijos)

    print("\n")
    print(board.unicode())
    print("\n")
    #n.imprimir(n,"-")

    n.Limpiar(n)
    n.eliminar_nodo(n)

    print("Tira el jugador (Blancas) ")
    a = input("Donde desea tirar: ")
    x = chess.Move.from_uci(a)
    board.push(x)


    if board.is_check():
        print('Jaque a la maquina')
    else:
        pass

    if board.is_checkmate():
        print('Jaque Mate a la maquina')
        board.is_game_over()
    else:
        pass
