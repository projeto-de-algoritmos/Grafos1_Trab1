
"""
Created on September 2020

@author: Marcos Adriano, Moacir Mascarenha

"""
import numpy as np
import sys
import os





sys.path.append(os.path.join(os.path.dirname(__file__), "../"))

import src.sudoku  as sudoku
import interface
if __name__ == "__main__":
    
    m = interface.Menu()
    entrada = np.block(m.inicio())

    chave = 1
    if chave == 1:
        input = np.block([[5, 3, 0, 0, 7, 0, 0, 0, 0], [6, 0, 0, 1, 9, 5, 0, 0, 0], [0, 9, 8, 0, 0, 0, 0, 6, 0],
             [8, 0, 0, 0, 6, 0, 0, 0, 3], [4, 0, 0, 8, 0, 3, 0, 0, 1], [7, 0, 0, 0, 2, 0, 0, 0, 6],
             [0, 6, 0, 0, 0, 0, 2, 8, 0], [0, 0, 0, 4, 1, 9, 0, 0, 5], [0, 0, 0, 0, 8, 0, 0, 7, 9]])

        input_2 = np.block([[5, 3, 0, 0, 7, 0, 0, 0, 0], [6, 0, 0, 1, 9, 5, 0, 0, 0], [0, 9, 8, 0, 0, 0, 0, 6, 0],
             [8, 0, 0, 0, 6, 0, 0, 0, 3], [4, 0, 0, 8, 0, 3, 0, 0, 1], [7, 0, 0, 0, 2, 0, 0, 0, 6],
             [0, 6, 0, 0, 0, 0, 2, 8, 0], [0, 0, 0, 4, 1, 9, 0, 0, 5], [0, 0, 0, 0, 8, 0, 0, 7, 9]])

    elif chave == 2:
        input = np.block([[0, 0, 0, 0, 7, 0, 0, 1, 0], [0, 6, 8, 0, 5, 9, 0, 0, 0], [4, 9, 7, 0, 0, 0, 0, 0, 5],
                      [0, 0, 0, 0, 6, 0, 0, 8, 0], [9, 0, 0, 0, 0, 0, 0, 0, 7], [0, 3, 0, 0, 8, 0, 9, 6, 4],
                       [6, 2, 3, 0, 9, 0, 0, 0, 0], [0, 7, 0, 0, 0, 8, 0, 4, 0],[0, 0, 0, 0, 0, 2, 0, 0, 0]])

        input_2 = np.block([[0, 0, 0, 0, 7, 0, 0, 1, 0], [0, 6, 8, 0, 5, 9, 0, 0, 0], [4, 9, 7, 0, 0, 0, 0, 0, 5],
                      [0, 0, 0, 0, 6, 0, 0, 8, 0], [9, 0, 0, 0, 0, 0, 0, 0, 7], [0, 3, 0, 0, 8, 0, 9, 6, 4],
                       [6, 2, 3, 0, 9, 0, 0, 0, 0], [0, 7, 0, 0, 0, 8, 0, 4, 0],[0, 0, 0, 0, 0, 2, 0, 0, 0]])

    else:
    # SUDOKU MAIS DIFICIL DO MUNDO
    # http://detudoblogue.blogspot.com/2012/07/sudoku.html
        input = np.block([[8, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 3, 6, 0, 0, 0, 0, 0], [0, 7, 0, 0, 9, 0, 2, 0, 0],
                      [0, 5, 0, 0, 0, 7, 0, 0, 0], [0, 0, 0, 0, 4, 5, 7, 0, 0], [0, 0, 0, 1, 0, 0, 0, 3, 0],
                       [0, 0, 1, 0, 0, 0, 0, 6, 8], [0, 0, 8, 5, 0, 0, 0, 1, 0],[0, 9, 0, 0, 0, 0, 4, 0, 0]])

        input_2 = np.block([[8, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 3, 6, 0, 0, 0, 0, 0], [0, 7, 0, 0, 9, 0, 2, 0, 0],
                      [0, 5, 0, 0, 0, 7, 0, 0, 0], [0, 0, 0, 0, 4, 5, 7, 0, 0], [0, 0, 0, 1, 0, 0, 0, 3, 0],
                      [0, 0, 1, 0, 0, 0, 0, 6, 8], [0, 0, 8, 5, 0, 0, 0, 1, 0], [0, 9, 0, 0, 0, 0, 4, 0, 0]])

    

    solLarg = list(sudoku.resolve(entrada, busca='largura'))[1]
    solProf = list(sudoku.resolve(entrada, busca='profundidade'))[1]

    print("                    " + " ----------------------- ")
    print("               " + "SOLUÇÃO COM ALGORITMO EM LARGURA")
    print("                    " + " ----------------------- ")

    sudoku.printsudoku(solLarg)
    print("                    " + " ----------------------- ")
    print("               " + "SOLUÇÃO COM ALGORITMO EM PROFUNDIDADE")
    print("                    " + " ----------------------- ")
    sudoku.printsudoku(solProf)
    print("------------------------------------------------------------------- ")
    print("------------------------------------------------------------------- ")
    print("------------------------------------------------------------------- ")
    
    m.imprimeResultado(solLarg,"Busca/Largura")
    m.imprimeResultado(solProf,"Busca/Profundidade")

    exit(0)
