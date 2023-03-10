# Detecção de Fraudes em Tempo Real

<div align="center">
    <image src="images/credit.jpg" width=50%>
</div>

💳 Uma abordagem em tempo real baseada em Machine Learning para detecção de fraudes em um sistema de pagamentos online, com fluxo end-to-end e arquitetura AWS.

## Contexto do Negócio 💼
A detecção de fraudes é um desafio significativo para muitas empresas ao redor do mundo. A fraude pode assumir várias formas, desde o roubo de cartões de crédito, bem como roubo da identidade de terceiros, até a falsificação de transações financeiras. A detecção de fraudes em tempo hábil é essencial para minimizar as perdas financeiras oriundas dessa prática, protegendo a reputação da empresa e a integridade dos clientes.

## Problema de Negócio ❔
A empresa **"Europe Online Store"** possui um e-commerce onde vende produtos digitais por toda a Europa. As fraudes representam um desafio para a compania, dada a crescente onda dessa prática nos últimos meses. Com isso, o time de negócios elaborou, em conjunto com o time de Ciência de Dados, o planejamento para construir uma solução de detecção em tempo real dessas transações má intencionadas, bloqueando-as e tomando as devidas providências para impedir essa prática, como o bloqueio de contas, notificações ao time comercial, entre outros.

## Objetivo 🎯
Considerando o problema mencionado, o objetivo deste projeto é **construir uma solução escalável, de ponta-a-ponta, para detectar em tempo real transações fraudulentas** em um sistema online de pagamentos. Para tal fim, serão utilizadas técnicas de machine learning, criando uma modelagem preditiva capaz de identificar padrões em transações fraudulentas. Ademais, esse modelo será integrado em uma arquitetura escalável, respeitando as boas práticas de desenvolvimento de software e MLOPs. Como meta do projeto, o modelo deverá ser superior a um baseline aleatório, bem como possuir taxas de acerto de transações fraudulentas e precisão na detecção dessas transações superior ao estado atual da empresa.

## Metodologia Utilizada 📝
Na construção do projeto, será utilizada a metodologia [CRISP-DM](https://www.ibm.com/docs/en/spss-modeler/saas?topic=dm-crisp-help-overview) (traduzido como "Processo Padrão Inter-Indústrias para Mineração de Dados"), sendo um processo construtivo-investigativo na resolução de problemas de negócio em Ciência de Dados.

<div align="center">
    <image src="images/crispdm.png" width=40%>
    <br> Imagem de Especialização em Data Science e Big Data (UFPR), disponível em Moodle.
</div>

## Conjunto de Dados 📊
A base de dados utilizada será a [Credit Card Fraud Detection (Kaggle)](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud). O conjunto de dados contém transações feitas por cartões de crédito em setembro de 2013 por titulares de cartões europeus. Este conjunto de dados apresenta transações que ocorreram em dois dias, onde temos 492 fraudes em 284.807 transações. O conjunto de dados é altamente desequilibrado, a classe positiva (fraudes) representa 0,172% de todas as transações.

Infelizmente, por motivos de sigilo, o nome das features foi mascarado na base original. Portanto, serão atribuídos nomes fictícios para cada uma delas, para fins do projeto. Segue abaixo uma lista contendo as colunas e suas respectivas descrições:

| Coluna     | Tipo do Dado | Descrição          |
|------------|--------------|--------------------|
| `amount`   | `float`      | Valor da transação |
| `time`     | `datetime`   | Data da transação  |

## Principais KPIs e Métricas 📈
Após conversas com o time de negócios e os principais stakeholders envolvidos no projeto, foram definidas as principais KPIs referentes ao modelo a ser construído:

- **Taxa de detecção das transações fraudulentas** (deve ser maximizada);
- **Taxa de falsos positivos na detecção das transações fraudulentas** (deve ser minimizada);
- **Tempo de processamento** que o modelo leva pra realizar e devolver as predições, em segundos (deve ser minimizado);
- **Prejuízo evitado** do total de transações impedidas de serem fraudadas (em R$), considerando o `amount` total somado;

Considerando as principais KPIs envolvidas, o time de Ciência de Dados escolheu as seguintes métricas para guiar a construção dos modelos:
- **Revocação** (`recall`): taxa de detecção das transações fraudulentas em relação ao total de fraudes;
- **Precisão** (`precision`): taxa de acerto das transações fraudulentas em relação ao total transações definidas como fraude;
- **F1 Score Balanceado** (`f1-score`): média harmônica entre a precisão e a revocação, em relação às transações fraudulentas, considerando ainda o balanceamento das classes;
- **KS** (*Kolmogorov–Smirnov*): métrica que determina o grau de separação das classes, muito utilizado em problemas de classificação binária; 

## Planejamento do Projeto 🔎
Após a definição do nosso objetivo, a próxima etapa é o planejamento das atividades a serem realizadas.

- **Objetivos da Sprint 1**
    - Processo de extração e processamento da base de dados a ser utilizada (*Extract, Transform, Load, ETL*);
    - Pré-processamento dos dados, limpeza e padronização da base (*data cleaning*);
    - Agendamento do processo utilizando Airflow;
- **Objetivos da Sprint 2**
    - Análise exploratória (EDA) na base de dados;
    - Elaboração e validação de hipóteses de negócio;
- **Objetivos da Sprint 3**
    - Criação de um modelo base (baseline) na detecção de fraudes;
    - Criação de um modelo protótipo (prototipação rápida utilizando LightGBM) para detecção de fraudes;
    - Criar um MVP do projeto, contendo o modelo protótipo disponibilizado através de uma API.
- **Objetivos da Sprint 4**
    - Tratar valores faltantes (se existirem) na base de dados (*data imputation*);
    - Tratar desbalanceamento das classes (*imbalance classification*);
    - Testar vários modelos e escolher o mais promissor (*model selection*);
- **Objetivos da Sprint 5**
    - Criar novas features a partir das informações existentes (*feature engineering*);
    - Selecionar as melhores features para o 
    modelo escolhido (*feature selection*);
    - Refinar o modelo selecionado (*hyperparameter tuning*);
    - Ajuste e análise do *threshold* a ser escolhido;
- **Objetivos da Sprint 6**
    - Apresentação do modelo e alinhamento com o time de negócio e os stakeholders envolvidos (*storytelling*);
    - Ajustes finais no modelo, adaptações e possíveis melhorias;
    - Disponibilização do modelo através de uma API (*model deployment*);

## Resultados Obtidos 🏆
