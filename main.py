import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import gradio as gr
import os

print("Iniciando o sistema de IA...")
caminho_arquivo = 'dados/processed.cleveland.data'

colunas = [
    'idade', 'sexo', 'tipo_dor_peito', 'pressao_arterial', 'colesterol',
    'glicemia_jejum', 'eletrocardiograma', 'freq_cardiaca_max',
    'angina_exercicio', 'depressao_st', 'inclinacao_st', 'num_vasos', 'talio', 'diagnostico'
]

df = pd.read_csv(caminho_arquivo, names=colunas, na_values='?')

df = df.dropna()
df['diagnostico'] = df['diagnostico'].apply(lambda x: 1 if x > 0 else 0)

X = df.drop('diagnostico', axis=1)
y = df['diagnostico']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)

print("Treinando o modelo de Árvore de Decisão...")
modelo = DecisionTreeClassifier(max_depth=5, random_state=42)
modelo.fit(X_train, y_train)

previsoes = modelo.predict(X_test)
acuracia = accuracy_score(y_test, previsoes)
print(f"\n--- RESULTADOS ---")
print(f"Acurácia do Modelo: {acuracia * 100:.2f}%")
print("------------------\n")

print("Gerando e salvando a Matriz de Confusão...")

pasta_destino = 'matriz_confusao'

if not os.path.exists(pasta_destino):
    os.makedirs(pasta_destino)

plt.figure(figsize=(6, 4))
matriz = confusion_matrix(y_test, previsoes)
sns.heatmap(matriz, annot=True, fmt='d', cmap='Blues',
            xticklabels=['Sem Doença', 'Com Doença'],
            yticklabels=['Sem Doença', 'Com Doença'])

plt.title('Matriz de Confusão')
plt.ylabel('Real')
plt.xlabel('Previsto')
plt.tight_layout()

caminho_completo = os.path.join(pasta_destino, 'matriz_confusao.png')

plt.savefig(caminho_completo)
plt.close()

print(f"Gráfico salvo com sucesso em: {caminho_completo}\n")


def prever_doenca(idade, sexo, tipo_dor_peito, pressao_arterial, colesterol, glicemia_jejum, eletrocardiograma,
                  freq_cardiaca_max, angina_exercicio, depressao_st, inclinacao_st, num_vasos, talio):
    dados_paciente = np.array(
        [[idade, sexo, tipo_dor_peito, pressao_arterial, colesterol, glicemia_jejum, eletrocardiograma,
          freq_cardiaca_max, angina_exercicio, depressao_st, inclinacao_st, num_vasos, talio]])
    resultado = modelo.predict(dados_paciente)

    if resultado[0] == 1:
        return "Alto Risco de Doença Cardíaca Detectado!"
    else:
        return "Baixo Risco de Doença Cardíaca."


interface = gr.Interface(
    fn=prever_doenca,
    inputs=[
        gr.Number(label="Idade"),
        gr.Radio(choices=[0, 1], label="Sexo (0=Feminino, 1=Masculino)"),
        gr.Radio(choices=[0, 1, 2, 3], label="Tipo de Dor no Peito (0 a 3)"),
        gr.Number(label="Pressão Arterial em repouso"),
        gr.Number(label="Colesterol mg/dl"),
        gr.Radio(choices=[0, 1], label="Açúcar no sangue em jejum > 120"),
        gr.Radio(choices=[0, 1, 2], label="Eletrocardiograma em repouso"),
        gr.Number(label="Frequência Cardíaca Máxima"),
        gr.Radio(choices=[0, 1], label="Angina induzida por exercício"),
        gr.Number(label="Depressão de ST induzida"),
        gr.Radio(choices=[0, 1, 2], label="Inclinação do segmento ST"),
        gr.Radio(choices=[0, 1, 2, 3], label="Número de vasos principais coloridos"),
        gr.Radio(choices=[1, 2, 3], label="Resultado do teste de Tálio"),
    ],
    outputs=gr.Text(label="Resultado da Previsão da Inteligência Artificial"),
    title="🩺 Sistema Inteligente de Triagem Cardíaca",
    description="Preencha os dados clínicos para a IA classificar o risco de doença cardíaca."
)

if __name__ == "__main__":
    print("Iniciando a interface visual. Acesse o link local (http://127.0.0.1:7860) fornecido abaixo:")
    interface.launch(inbrowser=True)