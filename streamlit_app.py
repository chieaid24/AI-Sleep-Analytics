{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "ab854370-6334-4985-86a2-954f023c4ae2",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-10-16T19:32:15.812606Z",
     "iopub.status.busy": "2025-10-16T19:32:15.812302Z",
     "iopub.status.idle": "2025-10-16T19:32:18.127367Z",
     "shell.execute_reply": "2025-10-16T19:32:18.126438Z",
     "shell.execute_reply.started": "2025-10-16T19:32:15.812583Z"
    }
   },
   "outputs": [],
   "source": [
    "!pip install streamlit --quiet"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4cab4867-a1cf-496a-aff0-0c49e5095404",
   "metadata": {
    "execution": {
     "iopub.status.busy": "2025-10-16T19:41:55.666896Z",
     "iopub.status.idle": "2025-10-16T19:41:55.667163Z",
     "shell.execute_reply": "2025-10-16T19:41:55.667058Z",
     "shell.execute_reply.started": "2025-10-16T19:41:55.667046Z"
    }
   },
   "outputs": [],
   "source": [
    "!streamlit --version"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "281448a7-0561-419d-9d5c-92cde5456e9e",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-10-16T19:32:08.509151Z",
     "iopub.status.busy": "2025-10-16T19:32:08.508853Z",
     "iopub.status.idle": "2025-10-16T19:32:08.668355Z",
     "shell.execute_reply": "2025-10-16T19:32:08.667546Z",
     "shell.execute_reply.started": "2025-10-16T19:32:08.509130Z"
    }
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-10-16 19:32:08.511 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-10-16 19:32:08.513 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-10-16 19:32:08.514 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-10-16 19:32:08.523 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-10-16 19:32:08.524 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-10-16 19:32:08.525 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-10-16 19:32:08.526 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-10-16 19:32:08.526 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-10-16 19:32:08.527 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-10-16 19:32:08.527 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-10-16 19:32:08.591 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-10-16 19:32:08.593 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-10-16 19:32:08.593 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-10-16 19:32:08.596 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-10-16 19:32:08.596 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-10-16 19:32:08.597 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-10-16 19:32:08.660 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-10-16 19:32:08.661 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-10-16 19:32:08.663 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "import pandas as pd\n",
    "import boto3\n",
    "from io import StringIO\n",
    "\n",
    "st.title(\"🧠 Sleep Quality Forecast Dashboard\")\n",
    "s3 = boto3.client(\"s3\")\n",
    "bucket = \"sleep-quality-forecast-bucket\"\n",
    "\n",
    "# drop down\n",
    "metric = st.selectbox(\n",
    "    \"Choose a metric:\",\n",
    "    [\"SLEEP_SCORE\", \"USAGE_HOURS\", \"AHI\", \"LEAK_95_PERCENTILE\", \"MASK_SESSION_COUNT\"]\n",
    ")\n",
    "\n",
    "# get CSV info from the bucket\n",
    "forecast_key = f\"forecasts/{metric}_forecast.csv\"\n",
    "\n",
    "try:\n",
    "    obj = s3.get_object(Bucket=bucket, Key=forecast_key)\n",
    "    forecast_df = pd.read_csv(obj['Body'])\n",
    "\n",
    "    st.subheader(f\"7 day Forecast for {metric}\")\n",
    "    st.dataframe(forecast_df)\n",
    "\n",
    "    # Plot forecast line\n",
    "    st.line_chart(forecast_df.set_index(\"ds\")[\"yhat\"])\n",
    "\n",
    "except s3.exceptions.NoSuchKey:\n",
    "    st.error(f\"No forecast found for {metric}. Run the model_prediction notebook to generate it first.\")\n",
    "except Exception as e:\n",
    "    st.error(f\"Error loading forecast: {e}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "07e1a025-7909-4bd1-ab37-40b92f49474b",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
