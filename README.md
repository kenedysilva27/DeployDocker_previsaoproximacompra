# **Estudo de Caso: Previsão do Valor Gasto por Clientes após uma Campanha de Marketing**

O objetivo deste estudo de caso é construir um modelo de regressão linear para prever o valor gasto por clientes na primeira compra após uma campanha de marketing cuja ação é o disparo de e-mail bem como a efetividade desta campanha para a a empresa. 
A base de dados contém informações coletadas durante a campanha, e usaremos essas informações para fazer previsões do valor gasto.

Base de Dados
A base de dados foi elaborada com dados do ChatGPT e contém as seguintes colunas:

Idade: Idade do cliente.
Gênero: Gênero do cliente (0 para masculino, 1 para feminino).
Renda Mensal: Renda mensal do cliente em reais.
N° de E-mails Enviados: Número de e-mails da campanha que foram enviados ao cliente.
N° de E-mails Abertos: Número de e-mails da campanha que o cliente abriu.
Tempo no Site (min): Tempo total (em minutos) que o cliente passou no site após a campanha.
Valor Gasto: Valor gasto pelo cliente na primeira compra após a campanha.

Metodologia
Modelagem: Utilização de regressão linear para construir o modelo preditivo.

Avaliação do Modelo: Métricas como R² Score e Erro Médio Absoluto (EMA) foram utilizadas para avaliar o desempenho do modelo.

Resultados
R² Score: Mede a proporção da variabilidade nos dados que é explicada pelo modelo. Em torno de 0,81
Erro Médio Absoluto (MAE): Calcula a média das diferenças absolutas entre os valores preditos e reais. O erro está em torno de 40,44

Conclusão

O modelo se provou capaz de prever com uma margem aceitável de precisão o valor gasto por clientes após uma campanha de marketing baseada em e-mail.
