
### significado de cada atributo:

1. **Idade:** Idade do paciente em anos.
2. **Sexo:** 0 = Feminino; 1 = Masculino. *(Doenças cardíacas apresentam incidências diferentes dependendo do sexo biológico).*
3. **Tipo de Dor no Peito:** Vai de 0 a 3.
   * *0 = Angina Típica (dor no peito causada por falta de sangue).*
   * *1 = Angina Atípica.*
   * *2 = Dor não anginosa (pode ser muscular).*
   * *3 = Assintomático (nenhuma dor).*
4. **Pressão Arterial em Repouso:** É a pressão máxima (sistólica) medida quando o paciente chega ao hospital. Valores acima de 130 ou 140 indicam hipertensão.
5. **Colesterol:** Colesterol sérico em mg/dl. Valores saudáveis ficam abaixo de 200. Acima de 240 já é considerado perigoso.
6. **Açúcar no Sangue em Jejum:** Mede se o paciente tem indícios de diabetes. (0 = Falso/Abaixo de 120; 1 = Verdadeiro/Acima de 120).
7. **Eletrocardiograma em repouso:** Mede a atividade elétrica do coração de 0 a 2. Sendo 0 "Normal" e 2 "Provável Hipertrofia (coração aumentado)".
8. **Frequência Cardíaca Máxima:** O pico de batimentos do paciente durante um teste de esteira. Pessoas saudáveis alcançam batimentos altos (ex: 160-180); corações fracos não conseguem acelerar muito.
9. **Angina induzida por exercício:** Se o paciente sente dor no peito *somente* quando faz esforço (0 = Não; 1 = Sim).
10. **Depressão de ST induzida:** Um valor numérico lido no eletrocardiograma. Quanto mais próximo de 0.0, mais saudável o coração reagiu ao esforço.
11. **Inclinação do segmento ST:** Também lido no eletro. Mede o quão rápido o coração "se recupera" após o pico do batimento (0, 1 ou 2).
12. **Número de vasos principais coloridos:** Vai de 0 a 3. O médico injeta um contraste e faz um raio-X. O número indica quantas artérias principais estão com algum entupimento. O ideal é 0.
13. **Resultado do teste de Tálio:** Mede o fluxo sanguíneo para o músculo cardíaco (1 = Normal; 2 = Defeito Fixo; 3 = Defeito Reversível).

---

### Exemplo Paciente Saudável:

* **Idade:** `30`
* **Sexo:** `1` *(Masculino)*
* **Tipo de Dor no Peito:** `3` *(Assintomático - sem dor)*
* **Pressão Arterial em repouso:** `115` *(Pressão normal 11 por 7)*
* **Colesterol mg/dl:** `165` *(Muito bom, abaixo de 200)*
* **Açúcar no sangue em jejum > 120:** `0` *(Falso, sem diabetes)*
* **Eletrocardiograma em repouso:** `0` *(Normal)*
* **Frequência Cardíaca Máxima:** `175` *(Coração forte, aguenta esforço)*
* **Angina induzida por exercício:** `0` *(Não sente dor na esteira)*
* **Depressão de ST induzida:** `0` *(Eletro perfeito na esteira)*
* **Inclinação do segmento ST:** `1` *(Recuperação normal)*
* **Número de vasos principais coloridos:** `0` *(Zero veias entupidas)*
* **Resultado do teste de Tálio:** `1` *(Fluxo de sangue normal)*