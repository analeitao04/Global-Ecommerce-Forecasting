# Global E-commerce: Demand Forecasting & Analytics

## Sobre o Projeto
Este é um projeto ponta-a-ponta de **Data Science aplicado ao Retalho (B2B/B2C)**. O objetivo foi analisar mais de 100 mil transações de um e-commerce global, extrair insights de negócio através de Análise RFM (Recency, Frequency, Monetary) e criar um modelo preditivo de **Demand Forecasting**.

## rincipais Descobertas (Business Insights)
* **O Impacto da Macroeconomia:** Provou-se que indicadores como Inflação e PIB têm uma correlação quase nula com o volume de compra no momento do checkout. O preço unitário é o grande impulsionador.
* **Prevenção de Churn:** Identificámos um Cliente VIP (Top 5 de faturação) em risco severo de *churn* (sem compras há 268 dias), permitindo ações imediatas de reconquista.
* **Otimização de Logística:** O modelo preditivo desenvolvido tem uma margem de erro (MAE) de apenas ~8 unidades, permitindo às equipas de armazém evitar ruturas de stock e excesso de inventário.

## Tecnologias Utilizadas
* **Linguagem:** Python
* **Análise e Limpeza:** Pandas, NumPy
* **Visualização:** Matplotlib, Seaborn
* **Machine Learning:** Scikit-Learn (Random Forest Regressor)
* **Deployment (Dashboard):** Streamlit

## Como correr o projeto localmente
1. Clone este repositório.
2. Instale as dependências: `pip install -r requirements.txt`
3. Para ver a análise de dados, abra o `ecommerce.ipynb`.
4. Para simular a Inteligência Artificial na Dashboard, corra no terminal: `streamlit run app.py`


