"""Spatiotemporal dataset stub.

Expected shape after preprocessing:
  X: (num_samples, history_steps, num_zones, num_features)
  y: (num_samples, horizon_steps, num_zones)
"""
from torch.utils.data import Dataset

class DemandDataset(Dataset):
    def __init__(self, X, y):
        self.X, self.y = X, y
    def __len__(self): return len(self.X)
    def __getitem__(self, i): return self.X[i], self.y[i]
