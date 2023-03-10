[![Open in colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gprzy/real-time-fraud-detection/blob/main/fraud_detection.ipynb)
[![GitHub license](https://img.shields.io/github/license/microsoft/ML-For-Beginners.svg)](https://github.com/gprzy/real-time-fraud-detection/blob/main/LICENSE)

# Detecção de Fraudes em Tempo Real

<div align="center">
    <image src="images/credit.jpg" width=50%>
</div>

💳 Uma abordagem baseada em Aprendizagem de Máquina para detecção em tempo real de fraudes em um sistema online de pagamentos. Fluxo de ponta-a-ponta e arquitetura AWS.

## Contexto do Negócio 💼
A **detecção de fraudes** é um desafio significativo para muitas empresas ao redor do mundo. A fraude pode assumir várias formas, desde o roubo de cartões de crédito, bem como roubo da identidade de terceiros, até a falsificação de transações financeiras. A detecção de fraudes em tempo hábil é essencial para minimizar as perdas financeiras oriundas dessa prática, protegendo a reputação da empresa e a integridade dos clientes.

## Problema de Negócio ❔
A empresa **"Europe Online Store"** possui um e-commerce onde vende produtos digitais por toda a Europa. As fraudes representam um desafio para a compania, dada a crescente onda dessa prática nos últimos meses. Com isso, o time de negócios elaborou, em conjunto com o time de Ciência de Dados, o planejamento para construir uma solução de detecção em tempo real dessas transações má intencionadas, bloqueando-as e tomando as devidas providências para impedir essa prática, como o bloqueio de contas, notificações ao time comercial, entre outros.

## Objetivo 🎯
Considerando o problema mencionado, o objetivo deste projeto é **construir uma solução escalável, de ponta-a-ponta, para detectar em tempo real transações fraudulentas** em um sistema online de pagamentos. Para tal fim, serão utilizadas técnicas de machine learning, criando uma modelagem preditiva capaz de identificar padrões em transações fraudulentas. Ademais, esse modelo será integrado em uma arquitetura escalável, respeitando as boas práticas de desenvolvimento de software e MLOPs. Como meta do projeto, o modelo deverá ser superior a um baseline aleatório, bem como possuir taxas de acerto de transações fraudulentas e precisão na detecção dessas transações superior ao estado atual da empresa.

## Lista de Tópicos 📌
1. [Metodologia Utilizada](#metodologia-utilizada-📝)
2. [Um Problema com Detecção de Fraudes: Desbalanceamento!](#)
3. [Quais Informações são Relevantes?](#)
4. [Abordagem Escolhida](#abordagem-escolhida-⌚)
5. [Ciclo de Vida de um Modelo de Machine Learning](#)
6. [Arquitetura Proposta](#arquitetura-proposta-🗜)
7. [Escolha da Arquitetura](#escolha-da-arquitetura)
8. [Como Monitorar a Performance do Modelo em Produção?](#escolha-da-arquitetura)
9. [Conjunto de Dados](#conjunto-de-dados-📊)
10. [Principais KPIs e Métricas](#principais-kpis-e-métricas-📈)
11. [Visão Geral do Projeto](#visão-geral-do-projeto-🔎)
12. [Escolha das Ferramentas/Tecnologias em Cada Etapa](escolha-das-ferramentas-tecnologias-em-cada-etapa)
13. [Planejamento do Projeto](#planejamento-do-projeto)
14. [Resultados Obtidos](#resultados-obtidos-🏆)
15. [Considerações Finais](#resultados-obtidos-🏆)

## Metodologia Utilizada 📝
Na construção do projeto, será utilizada a metodologia [CRISP-DM](https://www.ibm.com/docs/en/spss-modeler/saas?topic=dm-crisp-help-overview) (traduzido como "Processo Padrão Inter-Indústrias para Mineração de Dados"), sendo um processo construtivo-investigativo na resolução de problemas de negócio em Ciência de Dados.

<div align="center">
    <image src="images/crispdm.png" width=40%>
    <br> Imagem de Especialização em Data Science e Big Data (UFPR), disponível em <a href="https://moodle.com/pt/">Moodle</a>.
</div>

## Um Problema com Detecção de Fraudes: Desbalanceamento! ⚖
É muito comum em problemas de detecção de fraudes que o evento de interesse (no nosso caso, a fraude) ocorra com uma frequência muito menor que os eventos da classe majoritária. Essa característica, em aprendizagem de máquina, é conhecida como **desbalanceamento de classes**, gerando diversas implicações na criação de modelos. Os modelos apresentam um "viés" para classificar as classes como pertencentes à classe majoritária, gerando pouco ou até mesmo nenhum apredizado. Contornar esse problema é uma tarefa desafiadora, existindo diversas técnicas que podem ajudar nesse contexto; entre tais técnicas, temos estratégias de:
- **Undersampling** ⬇ <br> É a redução do número de instâncias da classe majoritária, para que as classes se igualem em quantidade. Alguns exemplos de técnicas possíveis de serem utilizadas, dessa categoria, são:
    - `RandomUnderSampler`;
    - `TomekLinks`;
    - `NearMiss`;
- **Oversampling** ⬆ <br> Processo contrário ao apresentado acima. Se refere a inserção de instâncias pertencentes à classe minoritária, seguindo alguma estratégia, como por exemplo inserção de dados sintéticos. Alguns exemplos de técnicas dessa categoria são:
    - `RandomOverSampler`;
    - `SMOTE` (Synthetic Minority Over-sampling Technique);
    - `ADASYN` (Adaptive Synthetic Sampling);

A escolha da técnica específica depende das particularidades do problema sendo abordado. É comum, em problemas de detecção de fraude, a mistura de diversas técnicas, entre elas a criação de **stacks** de modelos, *ensembles* treinados com variedades balanceadas dos dados originais, utilizando técnicas semelhantes às descritas acima, fornecendo uma capacidade preditiva superior. No geral, os modelos são também treinados utilizando separações estratificadas de dados, ou seja, mantendo as proporções das classes, para não aumentar ainda mais o desbalanceamento. Existem, ainda, outros métodos complementares nos quais pesos específicos são atribuídos à classe minoritária, visando compensar a menor quantidade.

## Quais Informações são Relevantes? ℹ
Em detecção de fraudes, existe uma gama de informações que em geral são úteis e relevantes para se descobrir atividades fraudulentas. Segue abaixo algumas delas:

- **Endereço IP do dispositivo de origem** 💻 <br> As instituições financeiras podem verificar o endereço IP do dispositivo usado para fazer a transação e verificar se ele está geograficamente próximo ao endereço de faturamento do cartão de crédito. Além disso, eles podem verificar se o endereço IP está em uma lista de endereços conhecidos por atividades fraudulentas;

- **Localização geográfica** 🌎 <br> As instituições financeiras também podem verificar a localização geográfica da transação e verificar se ela está em uma área conhecida por atividades fraudulentas, como mencionado no tópico anterior;

- **Valor da transação** 💰 <br> Valores muito altos ou muito baixos em relação à transação média do usuário podem ser indicadores de atividade fraudulenta. Em suma, anomalias nos valores usuais daquele cliente;

- **Tipo de transação** 💱 <br> As instituições financeiras podem verificar o tipo de transação que está sendo realizada e se ela é consistente com o histórico de transações do usuário. Ainda, transações de um tipo específico podem aumentar a probabilidade de ocorrência de uma fraude, especialmente padrões de trocas abruptas do tipo transacional;

- **Padrões de gastos** 📈 <br> As instituições financeiras podem verificar se o padrão de gastos do usuário mudou recentemente ou se há transações incomuns que não estão em conformidade com o histórico de gastos do usuário. Esse item é complementar ao que se refere ao valor da transação, visando obter informações a respeito dos padrões de gasto do cliente e o quanto as transações distoam desse padrão;

- **Histórico de transações** 📶 <br> O histórico de transações do usuário pode ser verificado para identificar transações suspeitas ou atividades incomuns. No mais, a análise do histórico também fornece exemplos de padrões em históricos trnasacionais não fraudulentos;

- **Tipo de cartão de crédito** 💳 <br> Algumas instituições financeiras consideram o tipo de cartão de crédito usado para fazer a transação e se ele é consistentemente usado para fazer compras caras ou incomuns, fornecendo possivelmente uma maior probabilidade de fraude;

- **Frequência de uso** 🕐 <br> A frequência de uso do cartão de crédito também pode ser um indicador de atividade fraudulenta, especialmente se houver um aumento repentino no uso do cartão;

Todos os itens acima referem-se, em geral, à quebras abruptas no padrão de gasto de um cliente, ou então diretamente à atividades tipicamente suspeitas. No geral, as informações acima referem-se à features que buscam quantificar anomalias, quebras de frequência, diferenças nos gastos usuais, e, por fim, compondo esses itens suspeitos para gerar uma classificação final.

## Abordagem Escolhida 🧭
Existem inúmeras abordagens diferentes para diferentes tipos de problemas de negócio, computação e aprendizagem de máquina. No tocante ao nosso problema de detecção de fraudes, mais especificamente em relação ao modelo de aprendizagem de máquina subjacente, temos algumas possíveis abordagens distintas, entre elas:

- **Em Tempo Real** (*real-time*) ⏱ <br> A abordagem mais adequada para detecções de fraude em tempo hábil, em relação à aprendizagem de máquina, é a **real-time**, pois precisamos detectar as fraudes antes que ocorram, de maneira rápida. Uma maneira comum de realizar isso é enviando uma requisição à um modelo previamente treinado, que irá nos dizer se uma determinada transação é ou não uma transação fraudulenta, ou então qual a probabilidade que seja fraudulenta de fato;

- **Em Lotes** (*batch*) 📦 <br> A abordagem em *batch*, nesse caso em específico, não é indicada, uma vez que realizaríamos predições em lotes de dados, geralmente periodicamente, podendo descobrir as fraudes após estas já terem ocorrido. 

- **Em Fluxos** (*stream*) ⏩ <br> Primeiramente, é importante fazer uma distinção: o conceito de "stream" para a Engenharia de Dados, em relação à fluxos de dados, é diferente da definição de "stream" no contexto de modelos de aprendizagem de máquina. A primeira refere-se à um tipo especial de processamento de dados em tempo real, mais especificamente relacionados à ordem sequencial e contínua dos dados. A última, refere-se a tipos particulares de modelos capazes de se adaptarem às mudanças nos dados ao longo do tempo (i.e. data drift), reduzindo as necessidades de retreino e potencialmente aperfeiçoando seu desempenho ao longo do tempo. Dito isto, a abordagem em stream é uma alternativa interessante e possível, caso feita em tempo real, de maneira semelhante à abordagem em tempo real. Contudo, como não se obteve nenhuma informação adicional de que os dados das transações estão sofrendo mudanças de padrão e comportamento, optamos por utilizar os modelos tradicionais (treinados em batch) ao invés dos modelos em stream. Uma das razões é a maior complexidade de implementação, validação e monitoramento desses modelos, bem como o fato dos dados não estarem sofrendo mudanças significativas. Por fim, o processo de retreino periódico pode ser benéfico em termos de compreensão de negócio, e deve ser feito cuidadosamente. Muitas vezes é preferível realizá-lo manualmente ao invés de uma forma automatizada, devido à natureza do problema abordado. 

- **Qual será o fluxo geral da detecção das fraudes?** <br> Um modelo de aprendizagem de máquina será previamente treinado com os dados históricos das transações fraudulentas, e então disponibilizado através de uma API, sendo solicitado pelas aplicações, em tempo real, para classificar uma determinada transação, guiando os próximos passos a serem evitados de maneira a mitigar a fraude. Abaixo, segue um diagrama simples para ilustrar esse fluxo geral:

<div align="center">
    <image src="images/fraud_detection_general_flow.png" width=60%>
    <br> Fluxo Geral de Detecção de Fraudes. Diagrama criado utilizando <a href="https://mermaid.js.org/">Mermaid.js</a>.
</div>

## Ciclo de Vida de um Modelo de Machine Learning 🌱
Todo modelo de aprendizagem de máquina, assim como qualquer solução de software, possui um ciclo de vida com algumas etapas aproximadamente definidas. Ao pensar na solução proposta, o time de dados considerou todas essas etapas e buscou aplicar as boas práticas de MLOPs nos diferentes escopos da solução. Segue uma imagem abaixo para ilustrar esse ciclo de vida dos modelos de aprendizagem de máquina:

<div align="center">
    <image src="images/mlops.png" width=50%>
    <br> Imagem disponível em <a href="https://nealanalytics.com/expertise/mlops/">Neal Analytics</a>.
</div>

## Arquitetura Proposta 🗜
Considerando o problema definido, objetivo levantado e a abordagem escolhida, bem como o fato de que a empresa atualmente já possui aplicações que utilizam serviços em nuvem da [AWS (Amazon Web Services)](https://aws.amazon.com/pt/), o time de dados concluiu, juntamente com o time de negócios, que seria uma boa escolha manter essa escolha por motivos relacionados a facilidade de manutenção, compartilhamento de conhecimentos e padronização de processos.

Segue abaixo um diagrama geral com os serviços da AWS a serem utilizados em diferentes etapas do processo de detecção de fraudes em tempo real: 

<div align="center">
    <image src="./images/aws_fraud_detection_architecture/aws_fraud_detection_architecture.png" width=70%>
    <br> Arquitetura proposta utilizando a <a href="https://aws.amazon.com/pt/">Amazon Web Services (AWS)</a>. Diagrama feito utilizando a ferramenta <a href="https://app.diagrams.net/">draw.io</a>
</div>

<br>

Descrevendo brevemente os componentes da arquitetura acima, temos:
- **Loja Online: Sistema Web** 🛍 <br> Aplicação Web correspondente à loja online de venda de produtos digitais, onde os usuários interagem diretamente e realizam suas compras. Onde também as tentativas de fraude são realizadas;

- **Loja Online: Sistema Mobile** 📲 <br> Aplicação opcional, dado que no problema de negócio original não foi incluída a aplicação mobile. Uma solução interessante seria testar o modelo em navegadores (ou onde as aplicações sejam mais estáveis), para então expandir para outros dispositivos;

- [Amazon API Gateway](https://aws.amazon.com/pt/api-gateway/) ⚙ <br> O **Amazon API Gateway** é um serviço totalmente gerenciado que torna mais fácil o desenvolvimento, a publicação, a manutenibilidade, o monitoramento e a segurança de APIs, de maneira escalável. O papel do API Gateway nessa arquitetura é fornecer uma interface de programação de aplicativos (API) para que os clientes possam enviar solicitações para o sistema de detecção de fraudes, atuando como o portão principal de entrada;

- [AWS Lambda](https://aws.amazon.com/pt/lambda/) ⚙ <br> O **AWS Lambda** é um serviço de computação sem servidor (*serverless*) que nos permite executar código sem provisionar ou gerenciar servidores. O papel do Lambda nessa arquitetura é atuar como um intermediário entre o API Gateway e o Amazon SageMaker, recebendo uma solicitação de detecção de fraude e realizando a requisição diretamente no endpoint do SageMaker, encaminhando o resultado obtido novamente à aplicação;

- [Amazon SageMaker](https://aws.amazon.com/pt/sagemaker/) ⚙ <br> O **Amazon SageMaker** é um serviço de aprendizado de máquina totalmente gerenciado que permite criar, treinar e implantar modelos de aprendizado de máquina de maneira escalável. O papel do SageMaker nessa arquitetura é hospedar o modelo de detecção de fraude, permitindo que o AWS Lambda realize predições em tempo real. Adicionalmente, o SageMaker também permite o monitoramento e versionamento de modelos;

- [Amazon Kinesis Data Firehose](https://docs.aws.amazon.com/firehose/latest/dev/what-is-this-service.html) ⚙ <br> O **Amazon Kinesis Data Firehose** é um serviço de streaming de dados gerenciado que facilita o carregamento escalável de informações em destinos de armazenamento e análise. O papel do Kinesis Data Firehose nessa arquitetura é capturar e processar dados de entrada em tempo real, antes de serem armazenados no Amazon S3, buscando monitorar rapidamente as transações realizadas;

- [Amazon S3](https://aws.amazon.com/pt/s3/) ⚙ <br> O **Amazon S3** é um serviço de armazenamento de objetos que oferece escalabilidade, disponibilidade e durabilidade de dados. O papel do Amazon S3 é armazenar tanto os modelos de detecção de fraude a serem utilizados no endpoint do SageMaker (*model registry*), quanto armazenar os dados processados pelo Kinesis Data Firehose, referentes às transações realizadas nas aplicações;

- [Amazon QuickSight](https://aws.amazon.com/pt/quicksight/) ⚙ <br> O **Amazon QuickSight** é um serviço de business intelligence (BI) que permite criar visualizações de dados e relatórios interativos. Esse serviço é algo opcional na arquitetura, pois não é essencial para seu funcionamento, contudo é extremamente útil e proveitoso, caso utilizado em conjunto com os demais componentes. O papel do QuickSight nessa arquitetura é fornecer ferramentas de análise de dados para que os usuários possam explorar informações armazenadas no Amazon S3, obtendo insights valiosos referentes às transações fraudulentas;

## Escolha da Arquitetura 🚀
Existem inúmeras maneiras de se realizar tarefas semelhantes utilizando os diversos serviços em nuvem disponíveis, tais como máquinas EC2, instâncias de contâineres, kubernetes, entre diversos outros serviços de computação. Contudo, precisamos escolher um que apresente um bom balanço entre custo/benefício. A escolha dos componentes levou em consideração critérios para se criar uma infraestrutura altamente escalável, dispoível e resiliente, que realiza predições em tempo real, com um fluxo de dados em tempo real e de processamento rápido, eficiente e confiável. No mais, tabém foi considerado um bom custo benefício, por exemplo na escolha do AWS Lambda, que é cobrado de acordo com seu tempo de execução. Segue abaixo os serviços utilizados e seus respectivos benefícios em relação à detecção de fraudes em tempo real:

- **Amazon API Gateway** ✔ <br> Um dos principais benefícios do API Gateway é que ele pode gerenciar automaticamente o tráfego de solicitações de entrada e dimensionar automaticamente para lidar com picos de tráfego, sem que você precise gerenciar infraestrutura. A ideia é fornecer uma maneira centralizada e eficiente para trabalhar com as requisições de detecção de fraude;

- **Lambda** ✔ <br> Uma das principais vantagens do Lambda é a sua capacidade de escalabilidade por padrão, ou seja, pode lidar com qualquer volume de solicitações sem se preocupar em provisionar servidores. Ademais, paga-se pelo tempo de execução do código, o que o torna um serviço econômico. No contexto do problema aqui apresentado, sua escalabilidade e versatilidade é uma vantagem, direcionando as requisições diretamente para o endpoint do modelo e também para o processamento dos dados pelo Kinesis;

- **Amazon SageMaker** ✔ <br> Uma das principais vantagens do SageMaker provém da sua capacidade de treinar e implantar modelos de forma rápida e escalável, tornando-o ideal para ambientes em que a rapidez e a precisão são cruciais, como na detecção de fraudes em tempo real. Adicionalmente, ele permite o retreino de modelos, qie pode ser necessário dado a natureza do problema abordado;

- **Amazon S3** ✔ <br> Uma das principais vantagens do Amazon S3 é sua grande escalabilidade. Ele pode armazenar e recuperar quantidades massivas de dados de forma eficiente e segura, podendo também ser facilmente integrado a outros serviços da AWS. Ademais, a durabilidade dos dados é alta, com um histórico de disponibilidade de 99,999999999% dos objetos armazenados;

- **Amazon Kinesis Data Firehose** ✔ <br> Uma das principais vantagens do Kinesis Data Firehose refere-se à sua capacidade de processar dados em tempo real, enviando-os para vários destinos e permitindo que o sistema possa ser adaptável a diferentes necessidades de análise e armazenamento. No exemplo aqui abordado, é crucial o acompanhamento em tempo real das transações realizadas;

- **Amazon QuickSight** ✔ <br> Uma das principais vantagens do QuickSight é sua facilidade de uso, oferecendo uma interface simples e intuitiva para visualização e análise de dados. Ademais, o QuickSight é capaz de se integrar com outros serviços da AWS, tornando-o uma solução eficiente para analisar grandes quantidades de dados em tempo real. É de suma importância poder visualizar de maneira eficiente os dados transacionais, possíveis padrões em fraudes e histórico dos clientes;

## Como Monitorar a Performance do Modelo em Produção? 🔭
Como mencionado, utilizaremos o Amazon SageMaker para monitoramento do modelo. O SageMaker, possui diversas ferramentas que nos permitem acompanhar métricas específicas e analisar o comportamento dos modelos em produção; abaixo, seguem as principais:

- [Amazon CloudWatch](https://aws.amazon.com/pt/cloudwatch/) 👁 <br> É uma ferramenta de monitoramento da AWS que fornece métricas e logs em tempo real. O SageMaker integra com o CloudWatch para monitorar o uso de recursos, como CPU, memória e utilização de rede do modelo em produção;

- [SageMaker Model Monitor](https://aws.amazon.com/pt/sagemaker/model-monitor/) 📉 <br> O Model Monitor é uma ferramenta de monitoramento automático que permite monitorar e detectar desvios em tempo real em relação ao comportamento esperado do modelo. Ele usa técnicas estatísticas e de aprendizado de máquina para detectar anomalias;

- [SageMaker Clarify](https://aws.amazon.com/pt/sagemaker/clarify/?sagemaker-data-wrangler-whats-new.sort-by=item.additionalFields.postDateTime&sagemaker-data-wrangler-whats-new.sort-order=desc) 💡 <br> O Clarify é uma ferramenta que ajuda a garantir que o modelo esteja operando de maneira balanceada e livre de viés. Ele fornece uma série de métricas e diagnósticos que permitem avaliar a equidade do modelo em relação a diferentes grupos.

No que diz respeito ao modelo em si, **como podemos saber quando o modelo está obsoleto?** Ou então, em outras palavras, **como saber se a performance do modelo está satisfatória?**

Em aprendizagem de máquina, existe um fenômeno chamado **data-drift**, quando os dados utilizados para treinar um modelo sofrem mudanças significativas ao longo do tempo, de tal maneira que a amostra utilizada para treinar o modelo já não é mais representativa do fenômeno modelado. Para detectar o data-drift, e também avaliar a performance do modelo em produção, podemos:
    
- **Avaliar a variação das principais métricas** do modelo ao longo do tempo (e.g. acurácia, revocação, precisão);
- **Avaliar a diferença entre as distribuições passada e atual**, por exemplo através de um gráfico, visando observar se a distribuição mudou, tornando necessário retreinar o modelo;
- **Testes estatísticos**, como o teste de hipótese de Kolmogorov-Smirnov, o t-test e o teste de Qui-Quadrado podem ser usados para detectar data drift. Esses testes comparam as distribuições dos dados históricos e atuais e determinam se a diferença é estatisticamente significativa;
- Quaisquer outros métodos de detecção de anomalias e diferenças entre os dados passados e atuais, utilizando diversas técnicas estatísticas e de aprendizagem de máquina;

## Conjunto de Dados 📊
A base de dados utilizada será a [Credit Card Fraud Detection (Kaggle)](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud). O conjunto de dados contém **transações feitas por cartões de crédito** em setembro de 2013 por titulares de cartões europeus. Este conjunto de dados apresenta transações que ocorreram em dois dias, onde temos 492 fraudes em 284.807 transações. O conjunto de dados é altamente desequilibrado, a classe positiva (fraudes) representa 0,172% de todas as transações.

Infelizmente, por motivos de sigilo, o nome das features foi mascarado na base original. Portanto, serão atribuídos nomes fictícios para cada uma delas, para fins do projeto. Segue abaixo uma lista contendo as colunas e suas respectivas descrições:

| Nome Original | Nome Fictício/Atualizado | Tipo | Descrição |
|--------|-----------------|--------------|-----------|
| `V1` | `bandeira_origem_v1` | `float64` | Bandeira do cartão utilizado na transação pela origem |
| `V2` | `bandeira_destino_v2` | `float64` | Bandeira do cartão utilizado na transação pelo destino |
| `V3` | `tipo_transacao_v3` | `float64` | Tipo de transação realizada |
| `V4` | `tipo_transacao_2_v4` | `float64` | Segundo tipo de transação realizada |
| `V5` | `banco_origem_v5` | `float64` | Banco da conta de origem utilizada na transação |
| `V6` | `banco_destino_v6` | `float64` | Banco da conta de destino utilizada na transação |
| `V7` | `longitude_v7` | `float64` | Coordenada de longitude da transação |
| `V8` | `latitude_v8` | `float64` | Coordenada de latitude da transação |
| `V9` | `periodo_do_dia_transacao_v9` | `float64` | Período do dia em que a transação foi realizada |
| `V10` | `data_transacao_dia_da_semana_v10` | `float64` | Dia da semana em que a transação foi realizada |
| `V11` | `data_transacao_mes_v11` | `float64` | Mês em que a transação foi realizada |
| `V12` | `dist_origem_destino_v12` | `float64` | Distância geográfica entre a origem e o destino da transação |
| `V13` | `valor_saldo_anterior_origem_v13` | `float64` | Valor do saldo anterior da conta de origem |
| `V14` | `valor_saldo_anterior_destino_v14` | `float64` | Valor do saldo anterior da conta de destino |
| `V15` | `tipo_cartao_v15` | `float64` | Tipo de cartão utilizado na transação |
| `V16` | `debito_credito_v16` | `float64` | Indica se a transação foi de débito ou crédito |
| `V17` | `tempo_conta_origem_v17` | `float64` | Tempo de existência da conta de origem |
| `V18` | `tempo_conta_destino_v18` | `float64` | Tempo de existência da conta de destino |
| `V19` | `grupo_ip_origem_v19` | `float64` | Grupo de endereços de IP da origem da transação |
| `V20` | `pais_origem_v20` | `float64` | País de origem da transação |
| `V21` | `pais_destino_v21` | `float64` | País de destino da transação |
| `V22` | `grupo_cep_origem_v22` | `float64` | Grupo de CEPs da origem da transação |
| `V23` | `grupo_cep_destino_v23` | `float64` | Grupo de CEP do destinatário da transação |
| `V24`  | `data_expiracao_v24` | `float64` | Data de expiração do cartão de crédito utilizado na transação |
| `V25`  | `limiar_fraude_v25` | `float64` | Limiar de decisão para a identificação de fraude |
| `V26`  | `bandeira_cartao_origem_v26` | `float64` | Bandeira do cartão de crédito utilizado na transação |
| `V27`  | `grupo_sistema_operacional_origem_v27` | `float64` | Grupo do sistema operacional utilizado na transação |
| `V28`  | `taxa_incidencia_fraudes_no_passado_v28` | `float64` | Taxa de incidência de fraudes no passado para o usuário |
| `Time` | `tempo` | `float64` | Número de segundos decorridos entre a transação atual e a primeira transação no conjunto de dados |
| `Amount` | `valor` | `float64` | Valor da transação, em dólares |
| `Fraud` | `fraude` | `int64` | Indicador binário de fraude, onde 1 representa uma transação fraudulenta e 0 representa uma transação legítima |

## Principais KPIs e Métricas 📈
Após conversas com o time de negócios e os principais stakeholders envolvidos no projeto, foram definidas as principais KPIs referentes ao modelo a ser construído:

- **Taxa de detecção das transações fraudulentas** (deve ser maximizada);
- **Taxa de falsos positivos na detecção das transações fraudulentas** (deve ser minimizada);
- **Tempo de processamento** que o modelo leva pra realizar e devolver as predições, em segundos (deve ser minimizado);
- **Prejuízo evitado** do total de transações impedidas de serem fraudadas (em R$), considerando o `amount` total somado;

Considerando as principais KPIs envolvidas, o time de Ciência de Dados escolheu as seguintes **métricas** para guiar a construção dos modelos:
- **Revocação** (`recall`) <br> Taxa de detecção das transações fraudulentas em relação ao total de fraudes;
- **Precisão** (`precision`) <br> Taxa de acerto das transações fraudulentas em relação ao total transações definidas como fraude;
- **F1 Score Balanceado** (`f1`) <br> Média harmônica entre a precisão e a revocação, em relação às transações fraudulentas, considerando ainda o balanceamento das classes;
- **KS** (*Kolmogorov–Smirnov*) <br> Métrica que determina o grau de separação das classes, muito utilizado em problemas de classificação binária;

## Visão Geral do Projeto 🔎
O projeto, de maneira geral, segue as seguintes etapas:
- **Obtenção dos dados** <br> Fluxo de ETL, limpeza e pré-processamento dos dados, seguido da automatização do processo;
- **Análise de dados** <br> Engloba EDA, validação de hipóteses, entre outros;
- **Criação do modelo** <br> Parte mais experimental do processo, englobando *model selection*, *feature engineering*, *feature selection*, *hyperparameter tuning*, entre outros;
- **Disponibilização do modelo** <br> Produtificação do modelo, empacotamento, conteinerização, construção da API e disponibilização;

## Escolha das Ferramentas/Tecnologias em Cada Etapa 🛠

## Planejamento do Projeto 🔬
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

## Resultados Obtidos (80% de acerto!) 🏆
Os resultados abaixo são referentes ao modelo de detecção de fraude, utilizando um `LGBMClassifier`. O modelo foi treinado com dados balanceados, utilizando `SMOTE`, e então testado nos dados originais. Ademais, os hiperparâmetros do modelo foram otimizados através de uma otimização Bayesiana, e por fim foi escolhido um threshold que maximizasse seu desempenho. Segue abaixo as métricas obridas, respectivamente a matriz de confusão, a curva ROC AUC e o KS:

<div align="center">
    <image src="images/metrics/cm.png" width=50%>
    <br> Matriz de Confusão do Modelo de Detecção de Fraudes.
</div> <br>

<div align="center">
    <image src="images/metrics/roc.png" width=50%>
    <br> Curva ROC AUC do Modelo de Detecção de Fraudes.
</div> <br>

<div align="center">
    <image src="images/metrics/ks.png" width=50%>
    <br> KS do Modelo de Detecção de Fraudes.
</div> <br>

**O modelo foi capaz de detectar corretamente 80% das transações fraudulentas, com uma precisão de 89%**. A precisão e revocação de detecção das transações não fraudulentas foi de aproximadamente 100%.

## Considerações Finais 💡
O modelo apresentou um ótimo desempenho, com um bom equiíbrio entre acertos e falsos positivos. Com isso, o modelo cumpre com as metras a ele atreladas, apresentando um desempenho superior ao estado atual de detecção de fraudes no setor de risco da empresa, bem como em um tempo menor e de maneira mais eficiente!
