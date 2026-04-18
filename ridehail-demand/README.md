# Spatiotemporal Ride-Hailing Demand Prediction

Deep learning system that predicts ride-hailing demand across city zones and time, combining spatial structure (zones / graph of regions) with temporal patterns (hour, day-of-week, events).

## Stack

- **Python 3.11**, conda environment
- **PyTorch** + **PyTorch Geometric** (Graph Neural Networks)
- **Hydra** for configuration, **TensorBoard** for logging
- **GeoPandas** for zone geometries

## Setup

```bash
# 1. Create the environment
conda env create -f environment.yml
conda activate ridehail

# 2. Install the local package in editable mode
pip install -e .

# 3. Sanity check
pytest -q
```

If conda's PyG solve is slow, install `pytorch` first via conda, then `pyg` and its companions, then the rest with pip.

## Project layout

```
ridehail-demand/
├── configs/              # Hydra configs (data / model / training)
├── data/
│   ├── raw/              # Original downloads (gitignored)
│   ├── interim/          # Cleaned but not yet model-ready
│   └── processed/        # Tensors ready for training
├── notebooks/            # Exploration
├── src/ridehail/
│   ├── data/             # Datasets & loaders
│   ├── features/         # Spatial + temporal feature engineering
│   ├── models/           # ConvLSTM, T-GNN, ST-Transformer
│   ├── training/         # Trainer, schedulers, callbacks
│   ├── evaluation/       # Metrics: MAE, RMSE, MAPE
│   └── utils/            # Seed, device, IO
├── scripts/
│   ├── preprocess.py     # raw -> processed
│   └── train.py          # Hydra entry point
├── tests/
└── outputs/              # Checkpoints, logs, figures (gitignored)
```

## Roadmap

1. **Now** — environment + scaffold (this step)
2. Pick dataset (NYC TLC / Uber Movement / DiDi), implement `preprocess.py`
3. Build zone graph (adjacency by shared border or k-NN of centroids)
4. Baseline: Historical Average, ARIMA, ConvLSTM
5. Main models: T-GNN (GCN/GAT + GRU), Spatiotemporal Transformer
6. Optimization (D/HD): Bayesian HPO, multi-horizon, attention, ensembling

## Train

```bash
python scripts/train.py model=convlstm data=nyc_taxi
python scripts/train.py model=tgnn training.epochs=100
```
