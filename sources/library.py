import numpy as np
import matplotlib.pyplot as plt
import os
import sys

file_out = open('./outputs/' + os.path.basename(sys.argv[0]).split('.')[0] + '.txt', "w")

def print_out(text):
    print(text)
    file_out.write(text + '\n')

def plotar_histograma_cinzas(data, title, path):
    plt.clf()
    plt.hist(data, bins=256, range=(0, 255), density=True)
    plt.title(title)
    plt.xlabel("Intensidade de pixel")
    plt.ylabel("Frequência")
    plt.savefig(path)

def plotar_histograma_ruido(data, title, path):
    plt.clf()
    plt.hist(data, bins=256, range=(-255, 255), density=True)
    plt.title(title)
    plt.xlabel("Intensidade de pixel")
    plt.ylabel("Frequência")
    plt.savefig(path)

def plotar_comparacao_histograma(original_img, processo_img, titles, path):
    # 
    original_depths = np.ndarray.flatten(np.asarray(original_img))
    processo_depths = np.ndarray.flatten(np.asarray(processo_img))

    # Limpar relatórios
    plt.clf()
    fig, ax = plt.subplots(2, 2)

    # Mostra as imagens original e processada lado a lado
    ax[0, 0].set_title(titles[0])
    ax[0, 0].imshow(original_img)

    ax[0, 1].set_title(titles[1])
    ax[0, 1].imshow(processo_img)
    
    ax[1, 0].set_title(titles[2])
    ax[1, 0].hist(original_depths, bins=255)
    
    ax[1, 1].set_title(titles[3])
    ax[1, 1].hist(processo_depths, bins=255)

    #
    fig.tight_layout()

    #
    plt.savefig(path)