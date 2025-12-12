# Cinema Audience Forecasting
## End-to-End Time Series Forecasting from Ticket Images

This project aims to build a complete machine learning pipeline that forecasts cinema audience numbers using ticket images as the primary data source. Both online ticket screenshots and physical ticket photos are processed using OCR to extract structured information that feeds into a time series forecasting system.

The workflow spans Computer Vision → Data Engineering → Feature Engineering → ML/DL Models → Forecasting → Insights.

## Problem Statement

Cinema owners need to accurately forecast the audience count for upcoming shows to optimize:

- Staff scheduling
- Screen allocation
- Inventory and concessions
- Revenue planning
- Marketing efforts

However, the available data is unstructured:

- Online ticket booking screenshots
- Images of physical tickets bought at the cinema

Your goal is to transform these raw images into a clean forecasting dataset and then build models to predict upcoming audience demand.

## Project Objectives

### 1. OCR and Text Extraction
Extract raw text from ticket images using image preprocessing and OCR techniques.

### 2. Parsing and Structuring
Convert noisy OCR output into structured fields such as:

- Movie name
- Show date
- Show time
- Screen number
- Seat number
- Ticket price
- Ticket quantity

### 3. Data Cleaning and Preprocessing

Implement a robust preprocessing workflow that:

- Handles missing values
- Detects and corrects outliers
- Removes duplicates
- Normalizes numeric features
- Performs time-aware train/validation/test split

### 4. Exploratory Data Analysis (EDA)

Generate both low-level and high-level visualizations:

- Daily booking trends
- Monthly patterns
- Seasonality decomposition
- Heatmaps
- Festival or holiday-based analysis

### 5. Feature Engineering

Create meaningful features for forecasting:

- Temporal features (weekday, month, week number)
- Lag features (lag_1, lag_7, lag_30)
- Rolling window features (mean, standard deviation)
- Holiday or festival indicators

### 6. Model Development (Minimum Three Models)

Implement at least three forecasting models:

- ARIMA or Auto-ARIMA
- XGBoost
- LSTM or GRU

### 7. Hyperparameter Tuning

Optimize model performance using Optuna or other tuning frameworks.

### 8. Model Evaluation

Evaluate models using metrics:

- RMSE
- MAE
- MAPE
- R²

### 9. Final Forecast and Insights

Produce final predictions and summarize insights using visualizations and reports.

## Repository Structure

```
src/
├── ocr.py
├── parser.py
├── preprocess.py
├── features.py
├── visualize.py
├── data_loader.py
├── evaluate.py
│
├── models/
│   ├── arima_model.py
│   ├── xgb_model.py
│   └── lstm_model.py
│
└── pipeline/
    ├── pipeline.py
    └── stages/
```

Data directories:

```
data/
├── raw/
├── interim/
└── processed/
```

Additional directories:

```
plots/
reports/
models/
artifacts/
logs/
```

## Dataset Included

A minimal dataset is provided:

- data/raw/ → sample ticket images
- data/interim/ → sample OCR text output
- data/processed/ → structured dataset

You may extend or augment this dataset as needed.

## End-to-End Workflow Overview

```
Ticket Images
     ↓
OCR Extraction
     ↓
Parsed Fields
     ↓
Cleaned Data
     ↓
Feature Engineering
     ↓
Train/Validation/Test Split
     ↓
Model Training
     ↓
Hyperparameter Optimization
     ↓
Evaluation
     ↓
Final Forecast and Insights
```

