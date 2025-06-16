import numpy as np
import matplotlib.pyplot as plt

# Parâmetros do circuito
R = 1e3
C = 1e-6
dt = 1e-4
Tmax = 0.5
Vref = 1.0
hyst = 0.05
V_on = 5.0
V_off = 0.0

# Inicializações
vout = 0
vin = V_on
estado = True

# Configura o gráfico
plt.ion()
fig, ax = plt.subplots()
line_vout, = ax.plot([], [], label="Vout")
line_vin, = ax.plot([], [], label="Vin", linestyle="--")
ax.set_xlim(0, Tmax * 1000)
ax.set_ylim(0, 5.5)
ax.set_xlabel("Tempo (ms)")
ax.set_ylabel("Tensão (V)")
ax.set_title("Controle por Histerese - Tempo Real")
ax.legend()
ax.grid(True)

# Vetores para plotagem
t_data = []
vout_data = []
vin_data = []

t = 0
while t < Tmax:
    # Atualiza controle
    if vout < Vref - hyst:
        estado = True
    elif vout > Vref + hyst:
        estado = False
    vin = V_on if estado else V_off

    # Atualiza planta
    dv = (vin - vout) / (R * C)
    vout += dv * dt

    # Salva dados
    t_data.append(t * 1000)
    vout_data.append(vout)
    vin_data.append(vin)

    # Atualiza gráfico
    line_vout.set_data(t_data, vout_data)
    line_vin.set_data(t_data, vin_data)
    ax.set_xlim(0, max(50, t * 1000))
    plt.pause(0.001)

    t += dt

plt.ioff()
plt.show()
