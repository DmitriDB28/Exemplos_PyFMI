# =====================================================================================
# Carrega o FMU e realiza a simulacao de acordo com os 
# parametros definidos no modelo (resistencia, capacitancia, 
# tempo inicial, tempo final e numero de pontos).
#
# Plota os graficos com os resultados, podendo escolher entre plotar as 
# linhas, os pontos, ou os dois juntos (basta comentar/descomentar as linhas de plot).
# =====================================================================================

import numpy as np
from matplotlib import pyplot as plt
from pyfmi import load_fmu

# Carregando o modelo
modelo = load_fmu("../fmu/rc_serie.fmu") # Carrega o fmu

# Simulando
resultados = modelo.simulate() # Simula o FMU

# Resultados
v = resultados['x'] # vetor da solucao (tensao no capacitor)
t = resultados['time'] # vetor de tempo
u = resultados['u'] # vetor da funcao de entrada (tensao da fonte)

# Plot
plt.plot(t,v, color='b') # plot da tensao no capacitor (linha)
plt.plot(t,u-v, color='r') # plot da tensao no resistor (linha)
plt.plot(t, u, color='k') # plot da tensao da fonte (linha)

plt.legend(["Capacitor", "Resistor", "Fonte"]) # Legenda

#plt.scatter(t,v, color='b', marker='.') # plot da tensao no capacitor (ponto)
#plt.scatter(t,u-v, color='r', marker='.') # plot da tensao no resistor (ponto)
#plt.scatter(t, u, color='k', marker='.') # plot da tensao da fonte (ponto)

plt.title("Circuito RC") # Titulo
plt.xlabel("Tempo [s]") # Eixo x
plt.ylabel("Tensão [v]") # Eixo y

plt.grid() # ativa a grade

plt.show() # mostra o grafico
