# 🫀 Sistema de Triagem Cardíaca com Inteligência Artificial

Projeto final desenvolvido para a disciplina de Inteligência Artificial do curso de Tecnologia em Análise e Desenvolvimento de Sistemas - IFPB Campus Esperança.

## 👥 Equipe
* Denis Willian
* Ruan Gouveia

## 🎯 Sobre o Projeto
O objetivo deste projeto é auxiliar na triagem preliminar de riscos cardiovasculares utilizando **Aprendizado de Máquina Supervisionado (Classificação)**. 

O modelo foi treinado com o algoritmo de **Árvore de Decisão (Decision Tree)** utilizando o consagrado dataset de Cleveland (UCI Machine Learning Repository). O sistema analisa diversos indicadores clínicos (colesterol, pressão arterial, frequência cardíaca, entre outros) para classificar o paciente em "Baixo Risco" ou "Alto Risco".

Além do modelo preditivo, o projeto entrega uma **interface gráfica interativa** que permite a simulação de atendimentos clínicos em tempo real.

## 📂 Estrutura do Repositório
* `main.py`: Script principal contendo o carregamento de dados, treinamento do modelo, geração de métricas e a interface gráfica.
* `dados/`: Pasta contendo o dataset `processed.cleveland.data`.

## 🛠️ Tecnologias e Bibliotecas
* **Linguagem:** Python 3.12
* **Manipulação de Dados:** Pandas & NumPy
* **Inteligência Artificial:** Scikit-Learn
* **Visualização:** Matplotlib & Seaborn
* **Interface de Usuário:** Gradio

## 🚀 Como Executar o Projeto Localmente

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/Denis166dev/Projeto-dis-IA.git
   
2. **Instale as dependências:**
   ```bash
   pip install pandas numpy scikit-learn matplotlib seaborn gradio

3. **Execute o sistema:**
   ```bash
   python main.py
