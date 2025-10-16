<h1 align="center"> 🌝 Sleep Regression & Forecasting with Machine Learning</h1>

> As someone with [sleep apnea](https://www.nhlbi.nih.gov/health/sleep-apnea), I tracked and analyzed my CPAP data for 2 years and here are my findings.

## Skills Used

| Category | Tools / Frameworks |
|-----------|--------------------|
| **Data Processing** | Python, Pandas, NumPy, Jupyter Notebooks |
| **AWS Cloud Services** | SageMaker AI, S3, Glue |
| **ML Models / Techniques** | Prophet, Random Forest Regression, Bayesian Optimization |

---

<h2>Overview</h2>

Every night, my CPAP (continuous positive airway pressure) uploads data like `USAGE_HOURS`, `AHI`, and `LEAK`, as well as an overall `SLEEP_SCORE` for the night—a range from 0 to 100. 
- So I made a [regression model](#regression-model) that will predict my `SLEEP_SCORE` for any given night
- And a [forecasting model](#forecasting-model) that uses the historical data to predict what my sleep will be like in the future

## Regression Model
### Purpose
Finding the relationship between `SLEEP_SCORE` and the other variables, by visualizing how each variable affects the overarching `SLEEP_SCORE` 

### Model Comparison
Trained and compared several machine learning models, including **Linear Regression**, **Random Forest**, **XGBoost**, and a **Neural Network Regressor** on the same data.

Resulted in the **Scikit-Learn Random Forest** model performing the best

<p align="center">
  <img src="https://github.com/user-attachments/assets/7bf312f6-7682-42fb-be24-29bcc618deb5" width="40%" alt="Model Performance Table" />
  <img src="https://github.com/user-attachments/assets/b043f807-43f0-4917-b921-d892d86256c5" width="45%" alt="Model Performance Chart"/>
</p>

### Model Tuning
Picked this model, and fine-tuned its hyperparameters with **Bayesian Optimization**

Resulted in a 8.95% decrease in RMSE and a 0.19% R^2 improvement. 


