import numpy as np
import matplotlib.pyplot as plt

# Parâmetros do circuito RC
R = 1e3         # 1k Ohm
C = 1e-6        # 1uF
dt = 1e-4       # Passo de tempo
Tmax = 0.5      # Tempo total
N = int(Tmax / dt)

# Parâmetros PID
Kp = 15.0
Ki = 200.0
Kd = 0.0002

# Referência
Vref = 1.0
vout = 0
vin = 0
integral = 0
erro_anterior = 0

# Vetores para plotagem
t_data = []
vout_data = []
vin_data = []

# Inicializa gráfico
plt.ion()
fig, ax = plt.subplots()
line_vout, = ax.plot([], [], label='Vout')
line_vin, = ax.plot([], [], label='Vin', linestyle='--')
ax.set_xlim(0, Tmax * 1000)
ax.set_ylim(0, 5.5)
ax.set_xlabel("Tempo (ms)")
ax.set_ylabel("Tensão (V)")
ax.set_title("Controle PID em Tempo Real - Circuito RC")
ax.grid(True)
ax.legend()

# Loop de simulação
t = 0
while t < Tmax:
    erro = Vref - vout
    integral += erro * dt
    derivada = (erro - erro_anterior) / dt
    erro_anterior = erro

    # Controle PID
    vin = Kp * erro + Ki * integral + Kd * derivada

    # Saturação do atuador (fonte limitada entre 0 e 5V)
    vin = np.clip(vin, 0, 5)

    # Simulação do RC
    dv = (vin - vout) / (R * C)
    vout += dv * dt

    # Atualiza dados
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
