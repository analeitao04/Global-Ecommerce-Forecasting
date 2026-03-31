# Global E-commerce: Demand Forecasting & Analytics

## About the Project
This is an end-to-end **Data Science applied to Retail (B2B/B2C)** project. The goal was to analyze over 100,000 transactions from a global e-commerce platform, extract business insights through RFM (Recency, Frequency, Monetary) Analysis, and build a predictive **Demand Forecasting** model.

## Key Findings (Business Insights)
* **Macroeconomic Impact:** It was proven that indicators such as Inflation and GDP have an almost zero correlation with the purchasing volume at the time of checkout. Unit price is the primary driver.
* **Churn Prevention:** We identified a VIP Client (Top 5 in revenue) at severe risk of *churn* (no purchases for 268 days), enabling immediate win-back actions.
* **Logistics Optimization:** The developed predictive model has an error margin (MAE) of only ~8 units, allowing warehouse teams to prevent stockouts and avoid excess inventory.

## Technologies Used
* **Language:** Python
* **Analysis and Cleaning:** Pandas, NumPy
* **Visualization:** Matplotlib, Seaborn
* **Machine Learning:** Scikit-Learn (Random Forest Regressor)
* **Deployment (Dashboard):** Streamlit

## How to run the project locally
1. Clone this repository.
2. Install the dependencies: `pip install -r requirements.txt`
3. To view the data analysis, open `ecommerce.ipynb`.
4. To simulate the Artificial Intelligence on the Dashboard, run in the terminal: `streamlit run app.py`
