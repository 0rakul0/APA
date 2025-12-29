# Implementação e Análise Experimental de Algoritmos SSSP

Este repositório contém a implementação e a análise experimental de algoritmos determinísticos para o problema de **Single-Source Shortest Path (SSSP)** em **grafos dirigidos ponderados**, conforme apresentado no artigo:

> *Implementação e Análise Experimental de Algoritmos para Caminhos Mínimos em Grafos Dirigidos*  
> Jefferson Silva dos Anjos — CEFET/RJ (2025)

O trabalho compara algoritmos clássicos com uma abordagem alternativa baseada em **propagação de fronteiras**, inspirada em resultados recentes da literatura que quebram a chamada *sorting barrier*.

---

## 📌 Objetivo

Avaliar empiricamente:

- **Corretude** dos caminhos mínimos
- **Tempo de execução**
- **Impacto da remoção da ordenação global**

para os seguintes métodos:

- Bellman–Ford
- Dijkstra
- Simulador baseado em fronteiras (sem sorting global)

---

## 📐 Problema SSSP

Dado um grafo dirigido ponderado \( G = (V, E) \) com pesos não negativos e um vértice fonte \( s \), o problema **SSSP** consiste em calcular o menor custo de caminho de \( s \) até todos os vértices alcançáveis.

Aplicações clássicas incluem:

- Redes de computadores
- Sistemas de transporte
- Logística
- Roteamento

---

## 🧠 Algoritmos Implementados

### 1. Bellman–Ford
- Relaxações globais sucessivas
- Suporta pesos negativos
- Complexidade:  
  O(|V| × |E|)

### 2. Dijkstra
- Estratégia gulosa
- Uso de fila de prioridade (ordenção global)
- Complexidade:  
  𝑂(|𝐸| + |𝑉| log |𝑉|)

### 3. Simulador por Propagação de Fronteiras
- Não utiliza fila de prioridade
- Evita ordenação global (*sorting barrier*)
- Propaga relaxações apenas sobre uma **fronteira ativa**
- Controlado por um parâmetro `K` (número de relaxações locais)

Essa abordagem é conceitualmente alinhada aos resultados de Duan et al. (2025), embora seja uma versão simplificada e experimental.

---

## 🧪 Metodologia Experimental

- Grafo dirigido ponderado construído manualmente
- Múltiplos caminhos alternativos
- Presença de ciclos leves
- Comparação direta entre:
  - Distâncias
  - Caminhos mínimos
  - Tempo de execução

A visualização dos caminhos permite verificar intuitivamente a corretude das soluções.

---

## 🗂 Estrutura do Projeto

```text
.
├── SSSP_deterministico.py   # Script principal
├── grafo.png                # Visualização gerada automaticamente
├── README.md                # Este arquivo
````

---

## ▶️ Como Executar

### Requisitos

* Python 3.9+
* Bibliotecas:

  * `networkx`
  * `matplotlib`

Instalação:

```bash
pip install networkx matplotlib
```

### Execução

```bash
python SSSP_deterministico.py
```

---

## 📤 Saídas Geradas

### Terminal

* Distâncias mínimas por algoritmo
* Caminho mínimo até o destino escolhido
* Tempo de execução (em segundos)

Exemplo:

```text
=== DISTÂNCIAS ===
Bellman–Ford: {0: 0, 4: 1.5, 3: 2.5, 5: 3.3, ...}
Dijkstra    : {0: 0, 4: 1.5, 3: 2.5, 5: 3.3, ...}
Simulador   : {0: 0.0, 4: 1.5, 3: 2.5, 5: 3.3, ...}

=== TEMPO DE EXECUÇÃO (segundos) ===
Bellman–Ford: 0.000261
Dijkstra    : 0.000297
Simulador   : 0.000048
```

### Arquivo Gráfico

* `grafo.png` contendo:

  * Grafo original
  * Caminho mínimo por algoritmo

---

## 📊 Resultados Observados

* Todos os algoritmos encontram **o mesmo caminho mínimo**
* O simulador baseado em fronteiras apresentou:

  * **Menor tempo de execução**
  * Menor propagação de relaxações redundantes
* Evidência empírica de que a ordenação global **não é estritamente necessária**

---

## 📌 Conclusões

* A remoção da ordenação global pode gerar ganhos práticos relevantes
* Estratégias baseadas em **controle de fronteira** são promissoras
* O simulador confirma, em pequena escala, resultados teóricos recentes
* O trabalho abre espaço para:

  * Grafos maiores
  * Execução paralela
  * Uso de GPU
  * Integração com GNNs e aprendizado profundo

---

## 📚 Referências

* Bellman, R. (1958). *On a routing problem*
* Dijkstra, E. W. (1959). *A note on two problems in connexion with graphs*
* Cormen et al. (2009). *Introduction to Algorithms*
* Duan et al. (2025). *Breaking the sorting barrier for directed SSSP*

---

## 👤 Autor

**Jefferson Silva dos Anjos**
CEFET/RJ — Programa de Pós-graduação em Ciência da Computação
📧 [jefferson.anjos.1@aluno.cefet-rj.br](mailto:jefferson.anjos.1@aluno.cefet-rj.br)

