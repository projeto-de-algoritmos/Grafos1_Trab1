import sys
import grafo as Grafo
import funcoes


square = [['00','01','02','9','10','11','18','19','20'],
          ['03','04','05','12','13','14','21','22','23'],
          ['06','07','08','15','16','17','24','25','26'],
          ['27','28','29','36','37','38','45','46','47'],
          ['30','31','32','39','40','41','48','49','50'],
          ['33','34','35','42','43','44','51','52','53'],
          ['54','55','56','63','64','65','72','73','74'],
          ['57','58','59','66','67','68','75','76','77'],
          ['60','61','62','69','70','71','78','79','80']]


def main(argv):
    try:
        filename = argv[1]
    except IndexError:
        print ('Usage: python sudoku.py filename')
        sys.exit(-1)
    
    grafo = Grafo.Grafo()

    fp = open(filename, 'r')
    data = fp.read().split('\n')
    data.remove('')
    sudoku = []
    # Preenchendo a tabela do jogo
    for line in data:
        sudoku.append(line.split(' '))
    
    # Criando os vertices
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 'x':
                cor = [1,2,3,4,5,6,7,8,9]
                no = Grafo.Vertice(cor)
                no.add_estado(False)
                # print(no.numero)
                grafo.add_vertice(no)
                # g.add_node(nodes[i][j], color=[1,2,3,4,5,6,7,8,9], status=False)
            else:
                no = Grafo.Vertice(list(sudoku[i][j]))
                grafo.preenchidos += 1
                no.add_estado(True)
                grafo.add_vertice(no)

    # Percorre as linhas
    for i in range(0,81,9):
        # percorrer cada coluna da linha
        for k in range(9):
            # Percorre (numero de colunas)-1
            for j in range(1,9):

                # print(i+j)
                grafo.add_vizinho_do_vertice(i+k, i+j)
    
    #posição na lista de nos
    p=0
    #Numero de linhas
    for i in range(9):
        #numero de colunas
        for j in range(9):
            #linhas
            for k in range(0,81,9):
                grafo.add_vizinho_do_vertice(p, j+k)
            p+=1
    #Adicionando os vizinhos dos quadrados 3x3
    for i in range(9):
        for j in range(8):
            for k in range(j,8):
                
                grafo.add_vizinho_do_vertice(int(square[i][j]), int(square[i][k+1]))
               
        funcoes.buscaSolucao(grafo)
        
    grafo.imprime_tabela()

    # grafo.imprime_vertices()

if __name__ == '__main__':
    main(sys.argv)

    


