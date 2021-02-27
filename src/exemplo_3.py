import numpy as np
from matplotlib import pyplot as plt
from pyfmi import load_fmu

# Carregando o modelo
modelo = load_fmu("../fmu/rc_serie.fmu") # Carrega o fmu

# Parametros da Simulacao
t_inicio = 0.0 # Inicio simulacao
t_fim   = 10.0 # Fim simulacao

modelo.time = t_inicio # Seta o tempo atual do modelo

modelo.initialize() # Inicializa o modelo

modelo.set('c', 200e-6) # Seta o valor da capacitancia
modelo.set('x', 0.0) # Seta o valor inicial da Tensao

# Resultados
x = modelo.continuous_states # Recebe os valores atuais da simulacao

vref  = [modelo.get_variable_valueref('x') , modelo.get_variable_valueref('u')] # Referencias
 
resultados = [modelo.get_real(vref)] # Vetor de resultados
resultados_t = [t_inicio] # Vetor de tempo dos resultados

# Simulacao
t = t_inicio # Tempo atual
dt = 0.001 # Passo de tempo
while (t + dt) <= t_fim: # Loop ate o tempo final
    
    dx = modelo.get_derivatives() # Recebe as derivadas do modelo

    t += dt # Incrementa o tempo

    modelo.time = t # Define o tempo do modelo

    x += dt*dx # Incrementa a variavel do modelo

    # Feedback
    if(x < 0.7): # Limiar inferior
        modelo.set('u', 10.0)
    if(x > 9.3): # Limiar superior
        modelo.set('u', 0.0)

    # Define o valor da variavel do modelo
    modelo.continuous_states = x

    resultados_t += [t] # Armazena o tempo
    resultados += [modelo.get_real(vref)] # Armazena os resultados
    


# Vetores de resultados
v = np.array(resultados)[:,0]
u = np.array(resultados)[:,1]
t = resultados_t

# Plot
plt.plot(t,v, color='b') # plot da tensao no capacitor (linha)
plt.plot(t, u, color='k') # plot da tensao da fonte (linha)

plt.legend(["Capacitor", "Fonte"]) # Legenda

#plt.scatter(t,v, color='b', marker='.') # plot da tensao no capacitor (ponto)
#plt.scatter(t, u, color='k', marker='.') # plot da tensao da fonte (ponto)

plt.title("Circuito RC") # Titulo
plt.xlabel("Tempo [s]") # Eixo x
plt.ylabel("Tensão [v]") # Eixo y

plt.grid() # ativa a grade

plt.show() # mostra o grafico