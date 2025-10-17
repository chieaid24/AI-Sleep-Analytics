<h1 align="center"> 🌝 Sleep Regression & Forecasting with Machine Learning</h1>

> As someone with [sleep apnea](https://www.nhlbi.nih.gov/health/sleep-apnea), I tracked and analyzed my CPAP data for 2 years, and here are my findings.

## 🧠 Skills Used

| Category | Tools / Frameworks |
|-----------|--------------------|
| **Data Processing** | Python, Pandas, NumPy, Jupyter Notebooks |
| **AWS Cloud Services** | SageMaker AI, S3, Glue |
| **ML Models / Techniques** | Prophet, Scikit-learn, Random Forest Regression, Bayesian Optimization |


<h2>✨ Overview</h2>

Every night, my CPAP (continuous positive airway pressure) uploads data like `USAGE_HOURS`, `AHI`, and `LEAK`, as well as an overall `SLEEP_SCORE` for the night—a range from 0 to 100. 
- So I made a [regression model](#-regression-model) that will predict my `SLEEP_SCORE` for any given night
- And a [forecasting model](#-forecasting-model) that uses the historical data to predict what my sleep will be like in the future
- Leveraged **SageMaker Studio Jupyter Notebooks** for implementation, **S3** for data and model storage, and **Glue** for generating metadata
## 📈 Regression Model
### Purpose
- Find the relationship between `SLEEP_SCORE` and the other metrics, by visualizing how each metric affects the overarching `SLEEP_SCORE`.

### Model Comparison
- Trained and compared several machine learning models, including **Linear Regression**, **Random Forest**, **XGBoost**, and a **Neural Network Regressor** on the same data.
- Resulted in the **Scikit-Learn Random Forest** model performing the best.



<p align="center">
  <img src="https://github.com/user-attachments/assets/7bf312f6-7682-42fb-be24-29bcc618deb5" width="40%" alt="Model Performance Table" />
  <img src="https://github.com/user-attachments/assets/b043f807-43f0-4917-b921-d892d86256c5" width="45%" alt="Model Performance Chart"/>
</p>

---

### Model Tuning
- Picked this model, and fine-tuned its hyperparameters with **Bayesian Optimization**.
- Resulted in a improvement of **8.95%** in RMSE and **0.19%** in R². 

### Final Result
- The model is saved at `models/rf_bayesian_tuned_model.pkl`, and resulted in values of **0.99** R² and **0.28** RMSE. 
> Below are the listed features and their calculated weights on determining `SLEEP_SCORE`
<p align="center">
  <img alt="image" src="https://github.com/user-attachments/assets/7f4e8b16-7bd3-4b88-9385-c8f141aac795" width="90%"/>
</p>

---

## 💫 Forecasting Model
### Purpose
- Use time series modeling to extrapolate `SLEEP_SCORE`, `AHI`, `MASK_SESSION`, `USAGE_HOURS`, and `LEAK` metrics 7 days into the future.

### Model Training
- Used Meta's Prophet model to analyze each metric in the dataset, saving the last week for testing predictions
- Achieved RMSE's of **0.83** `SLEEP_SCORE` points, **0.23** `AHI` events, **0.74** `MASK_SESSION` events, **0.52** `USAGE_HOURS` hours, and **1.9** `LEAK` L/h.
- Analyzed weekly seasonality trends, like my sleep score consistently being worse on Friday (see below)
<p align="center">
  <img width="90%" alt="image" src="https://github.com/user-attachments/assets/235e1987-7d2e-41cb-b42c-d0fb861c12da" />
</p>

- Example trend graph (this tracks the amount of air leaking from the mask)
<p align="center">
  <img width="90%" alt="image" src="https://github.com/user-attachments/assets/96c3a254-15a2-4a2e-b954-7269b777d88e" />
</p>

### Model Predictions
- Loops through each of the **Prophet** models saved in my S3 bucket, and predicts the values for 7 days after the training data stops
- Displayed tabularly and graphically

https://github.com/user-attachments/assets/5ece1f5e-44cf-4d59-be75-7831ced4cc21

