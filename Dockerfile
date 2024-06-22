FROM python:3.12

WORKDIR /src

COPY app.py .
COPY base_marketing_realistic.csv .

RUN pip install pandas streamlit scikit-learn

EXPOSE 8501

ENTRYPOINT ["python", "-m", "streamlit", "run", "--server.port", "8501", "--server.address", "0.0.0.0", "app.py"]



