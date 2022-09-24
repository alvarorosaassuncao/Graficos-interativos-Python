import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1,6) #conta de 1 a 5 
dados = np.random.randint(20,30,5)

plt.style.use('ggplot') # muda o estilo do grafico

plt.ion() #Deixa o grafico interativo

for i in range(10):
    dados = np.random.randint(20,30,5)
    plt.cla() #limpa os dados do grafico
    plt.clf() #limpa os dados anteriores
    plt.bar(x, dados)
    plt.pause(2)
plt.ioff()
plt.bar(x, dados)
plt.pause(5) #se usa quando esta com modo interativo ligado

plt.ioff() # desliga o modo interativo
plt.show() #mantem o grafico na tela
