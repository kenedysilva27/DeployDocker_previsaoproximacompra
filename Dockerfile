# Use a imagem Python 3.12 como base
FROM python:3.12

# Define o diretório de trabalho como /src dentro do contêiner
WORKDIR /src

# Copia apenas os arquivos necessários para /app dentro do contêiner
COPY app.py .
COPY base_marketing_realistic.csv .
# Instala as dependências necessárias
RUN pip install pandas streamlit scikit-learn

# Expõe a porta 8501 para o Streamlit
EXPOSE 8501

# Comando para executar o aplicativo quando o contêiner for iniciado
ENTRYPOINT ["python", "-m", "streamlit", "run", "--server.port", "8501", "--server.address", "0.0.0.0", "app.py"]



