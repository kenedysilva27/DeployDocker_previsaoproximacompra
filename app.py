import pandas as pd
import streamlit as st
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error

st.set_page_config(page_title="Previsão de Próxima Compra", page_icon="🛒", layout="wide")
st.markdown(
    """
    <style>
    .reportview-container {
        background: #f0f5f5; /* Cor de fundo ajustável */
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title('🛒 Previsão de Próxima Compra')

@st.cache_data
def carregar_base():
    base = pd.read_csv('base_marketing_realistic.csv', sep=',')
    base.columns = ['Idade', 'Gênero', 'Renda_Mensal', 
                    'Nu_de_E-mails_Enviados', 'Num_de_E-mails_Abertos', 
                    'Tempo_no_Site_min', 'Valor_Gasto']
    return base

base = carregar_base()

# Preprocessamento dos dados
X = base.drop(['Valor_Gasto'], axis=1)
y = base['Valor_Gasto']

scaler = StandardScaler()
X_preprocessado = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_preprocessado, y, test_size=0.2, random_state=42)

modelo = LinearRegression()
modelo.fit(X_train, y_train)

# Função para realizar a predição
def realizar_predicao(idade, genero, renda_mensal, nu_emails_enviados, nu_emails_abertos, tempo_no_site):
    novo_cliente = scaler.transform([[idade, genero, renda_mensal, nu_emails_enviados, nu_emails_abertos, tempo_no_site]])
    predicao_valor_gasto = modelo.predict(novo_cliente)[0]
    return realizar_predicao

y_pred = modelo.predict(X_test)
r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)

st.markdown("---")
st.header("Resultados do Modelo")
st.metric(label="Pontuação R2 (Capacidade das características dos parâmetros explicarem o valor a ser gasto)", value=f"{r2:.2f}")
st.metric(label="Erro Médio Absoluto (Média de erros para mais ou para menos)", value=f"{mae:.2f}")
st.markdown("---")

st.header("Preencha os Parâmetros")

idade = st.number_input('Idade', min_value=18, max_value=69, value=30, step=1)
genero = st.selectbox('Gênero', options=['Masculino', 'Feminino'])
renda_mensal = st.number_input('Renda Mensal', min_value=1412, max_value=5000, value=5000, step=500)
nu_emails_enviados = st.number_input('Número de E-mails Enviados', min_value=1, max_value=10, value=3, step=1)
nu_emails_abertos = st.number_input('Número de E-mails Abertos', min_value=0, max_value=10, value=1, step=1)
tempo_no_site = st.number_input('Tempo no Site (min)', min_value=0, max_value=59, value=25, step=5)


if st.button('Ver Previsão'):
    predicao = realizar_predicao(idade, 0 if genero == 'Masculino' else 1, renda_mensal, nu_emails_enviados, nu_emails_abertos, tempo_no_site)
    st.subheader(f"Valor Gasto Previsto: R${predicao:.2f}")

    if predicao > base['Valor_Gasto'].mean():
        st.markdown('<p style="color: green;">O valor previsto está acima da média histórica de gastos.</p>', unsafe_allow_html=True)
    elif predicao < base['Valor_Gasto'].mean():
        st.markdown('<p style="color: red;">O valor previsto está abaixo da média histórica de gastos.</p>', unsafe_allow_html=True)
    else:
        st.markdown('<p style="color: orange;">O valor previsto está próximo da média histórica de gastos.</p>', unsafe_allow_html=True)
