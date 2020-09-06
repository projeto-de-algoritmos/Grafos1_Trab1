def verificaVizinhos(meugrafo, verticePai):
    for i in meugrafo.vertices[verticePai].vizinhos:
        if meugrafo.vertices[i].estado == True:
                # print("Pai: ",verticePai,meugrafo.vertices[verticePai].numero, "Remover:",i,meugrafo.vertices[i].numero)
                
                if meugrafo.vertices[verticePai].quantidade_numeros()!=1:
                    meugrafo.vertices[verticePai].rm_numero(int(meugrafo.vertices[i].numero[0]))
                
                else:
                    # print("-----------------")
                    # print(verticePai, meugrafo.vertices[verticePai].numero)
                    meugrafo.vertices[verticePai].add_estado(True)
                    meugrafo.preenchidos+=1
                    
                    return


def buscaSolucao(meuGrafo):
    for j in range(9):
        for i in range(0,81):
            if meuGrafo.vertices[i].estado == False:
                verificaVizinhos(meuGrafo, i)
            else:
                pass
        