# ridehail_prediction_AI
this is AI model for prediction of RIDE HAILING DEMAND PREDICTION SYSTEM.

Repository Structure
spatiotemporal-ride-demand/
│
├── data/
│   ├── raw/                  # Downloaded NYC TLC parquet files
│   ├── processed/            # Cleaned and feature-engineered datasets
│   └── graphs/               # Zone adjacency matrix and GeoJSON
│
├── notebooks/
│   ├── 01_eda.ipynb          # Exploratory data analysis
│   ├── 02_feature_engineering.ipynb
│   └── 03_model_comparison.ipynb
│
├── src/
│   ├── data/
│   │   ├── download.py       # Data download scripts
│   │   ├── preprocess.py     # Cleaning and aggregation
│   │   └── graph.py          # Zone graph construction
│   ├── models/
│   │   ├── convlstm.py       # ConvLSTM implementation
│   │   ├── gcn_lstm.py       # GCN + LSTM implementation
│   │   ├── st_transformer.py # Spatiotemporal Transformer
│   │   └── tgn.py            # Temporal Graph Network
│   ├── training/
│   │   ├── train.py          # Training loop
│   │   ├── evaluate.py       # Metrics: MAE, RMSE, MAPE
│   │   └── hpo.py            # Optuna hyperparameter optimisation
│   └── serving/
│       └── api.py            # FastAPI prediction endpoint
│
├── dashboard/
│   └── app.py                # Streamlit demand forecasting dashboard
│
├── tests/
│   ├── test_data.py
│   ├── test_models.py
│   └── test_api.py
│
├── docs/
│   ├── architecture.md       # System design overview
│   ├── literature.md         # Paper summaries
│   ├── experiments.md        # Model comparison log
│   └── data.md               # Dataset and preprocessing notes
│
├── .github/
│   └── workflows/
│       └── ci.yml            # GitHub Actions CI pipeline
│
├── Dockerfile
├── requirements.txt
├── CHANGELOG.md
└── README.md
