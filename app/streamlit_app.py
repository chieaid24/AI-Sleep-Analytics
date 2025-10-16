import streamlit as st
import pandas as pd
import boto3
from io import StringIO
st.set_page_config(
    page_title="Sleep Dashboard",
    page_icon="🌝",
    initial_sidebar_state="expanded",
)

st.title("🌛 Sleep Quality Forecast Dashboard")
s3 = boto3.client("s3")
bucket = "sleep-quality-forecast-bucket"

# drop down
metric = st.selectbox(
    "Choose a metric:",
    ["SLEEP_SCORE", "USAGE_HOURS", "AHI", "LEAK_95_PERCENTILE", "MASK_SESSION_COUNT"]
)

# get CSV info from the bucket
forecast_key = f"forecasts/{metric}_forecast.csv"

try:
    obj = s3.get_object(Bucket=bucket, Key=forecast_key)
    forecast_df = pd.read_csv(obj['Body'])

    st.subheader(f"7-day Forecast for {metric}")
    st.dataframe(forecast_df)

    # Plot forecast line
    st.line_chart(forecast_df.set_index("Date")["Predicted Value"])

except s3.exceptions.NoSuchKey:
    st.error(f"No forecast found for {metric}. Run the model_prediction notebook to generate it first.")
except Exception as e:
    st.error(f"Error loading forecast: {e}")
