### Objetivo
# Projeto de Controle PID Analógico com Arduino

Este projeto implementa um **sistema de controle de tensão analógico** usando um **controlador PID analógico com amplificadores operacionais**, uma **planta RC (resistor + capacitor)** e um **Arduino UNO** para monitoramento da resposta do sistema.

---

## 🎯 Objetivo

Controlar a tensão de saída de uma carga RC utilizando um controlador PID analógico, com o auxílio do Arduino para leitura e visualização da saída do sistema em tempo real.

---

## ⚙️ Componentes Utilizados

- 1 × Arduino UNO
- 3 × Amplificadores operacionais (op-amp)
- 1 × Carga RC (resistor + capacitor)
- Vários resistores e capacitores para configurar as constantes do PID
- Fonte de alimentação (pilhas ou banco de energia)
- Jumpers e protoboard
- Potenciômetro ou divisor de tensão para setpoint (referência)

---

## 🧠 Estrutura do Sistema

### 🔲 1. **Controlador PID Analógico**

Implementado com três amplificadores operacionais:
- **Proporcional (P)**: resistor em malha direta.
- **Integrador (I)**: capacitor na realimentação.
- **Derivativo (D)**: capacitor na entrada.

A combinação desses três blocos produz um sinal de controle analógico baseado no erro entre a tensão de referência e a saída da planta.

---

### 🔲 2. **Planta: Circuito RC**

Simula um sistema físico simples onde:
- A tensão de entrada (do PID) controla a carga no capacitor.
- A saída é a tensão no capacitor, que representa a variável controlada.

---

### 🔲 3. **Arduino UNO**

- Lê a **tensão da planta** (pino A0).
- Envia os dados ao **monitor serial** para acompanhamento em tempo real.
- (Opcional) Pode ser utilizado futuramente para aplicar controle digital, PWM ou comunicação com Python/PC.

---

## 🖥️ Código Arduino

```cpp
const int sensorPin = A0;
float Vref = 5.0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  int raw = analogRead(sensorPin);
  float voltage = (raw / 1023.0) * Vref;

  Serial.print("Tensao: ");
  Serial.print(voltage);
  Serial.println(" V");

  delay(100);
}
```

![Diagrama do controlador PID](images/image.png)


## Amplificador Operacional – Entradas e Saídas

### `in+` e `in–`

Esses são os **terminais de entrada** de um amplificador operacional:

| Símbolo | Nome                  | Função                                                                 |
|---------|-----------------------|------------------------------------------------------------------------|
| `in+`   | Entrada **não-inversora** (+) | Aumenta a saída quando sua tensão é maior que `in–`.              |
| `in–`   | Entrada **inversora** (–)     | Reduz a saída quando sua tensão é maior que `in+`.                |

A saída do amplificador tenta amplificar a diferença entre essas entradas:

> Onde `A` é o ganho (idealmente muito alto).

V_out = A(V_in+ - V_in-)
### `out+` e `out–`

Normalmente, amplificadores operacionais como o **LM741** possuem **apenas uma saída (`out`)**.

Porém, em amplificadores diferenciais ou de instrumentação, pode haver:

| Símbolo | Nome                        | Função                                 |
|---------|-----------------------------|----------------------------------------|
| `out+`  | Saída positiva              | Representa a parte positiva de uma saída diferencial |
| `out–`  | Saída negativa (ou GND)     | Referência ou terminal negativo        |

No caso do **LM741**:
- Ele **não possui `out+` nem `out–`**, apenas um único terminal de saída (`out`, pino 6).

---

## Pinagem do LM741 (DIP 8)

Out |1 8| NC
In– |2 7| +Vcc
In+ |3 6| Out
-V |4 5| NC

| Pino | Nome    | Função                          |
|------|---------|---------------------------------|
| 1    | Offset  | Compensação de offset (opcional)|
| 2    | `in–`   | Entrada inversora               |
| 3    | `in+`   | Entrada não-inversora           |
| 4    | `–V`    | Alimentação negativa            |
| 5    | Offset  | Compensação de offset (opcional)|
| 6    | `out`   | Saída                           |
| 7    | `+V`    | Alimentação positiva            |
| 8    | NC      | Sem conexão                     |

---

## Portas de Offset

Pinos 1 e 5 do LM741 são usados para **compensar erro de offset** com um **potenciômetro de 10 kΩ**:

- Liga-se um potenciômetro entre os pinos 1 e 5.
- O pino central do potenciômetro vai para o terminal **–Vcc**.
- Isso permite ajustar a saída para ser 0 V quando as entradas estão iguais.

> No **Tinkercad**, esse ajuste pode ser ignorado, pois a simulação já compensa esse erro automaticamente.

---

