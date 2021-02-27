# =====================================================================================
# Carrega o FMU e realiza a simulacao de acordo com os 
# parametros definidos neste código (tensao de entrada, resistencia, capacitancia, 
# tempo inicial, tempo final e numero de pontos) - sobrescreve os valores contidos no 
# modelo (padrão).
#
# A tensao de entrada (termo nao homogeneo da edo) pode ser um degrau (u) ou uma senoide (u_2),
# basta comentar/descomentar a linha que cria a variavel input.
# 
# Plota os graficos com os resultados, podendo escolher entre plotar as 
# linhas, os pontos, ou os dois juntos (basta comentar/descomentar as linhas de plot).
# =====================================================================================

import numpy as np
import math
from matplotlib import pyplot as plt
from pyfmi import load_fmu

# Carregando o modelo
modelo = load_fmu("../fmu/rc_serie.fmu") # Carrega o fmu

# Funcoes para a tensao da fonte
def u(time): # Degrau
    
    if(time>=0.5):
        return 10.0
    
    else:
        return 0.0

def u_2(time): # Senoide

    a = 10.0 # Amplitude (volts)
    f = 8.0 # Frequencia (hertz)
    p = 0.0 # Fase (radianos)
    o = 0.0 # Offset (volts)

    return a * np.sin(2.0*math.pi*f*time + p) + o

# Parametros do modelo
#input = ('u', u) # Define a funcao de entrada do modelo (Degrau)
input = ('u', u_2) # Define a funcao de entrada do modelo (Senoide)

modelo.set('c', 10e-6) # Valor da Capacitancia
modelo.set('x', 0) # Valor inicial de x

opts = modelo.simulate_options() # Get opcoes da simulacao do modelo
opts['ncp'] = 5000 # Altera o numero de pontos

# Simulacao do Modelo
resultados = modelo.simulate(start_time=0, final_time=1, input=input, options=opts) # Simula o modelo de acordo com os valores enviados

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
