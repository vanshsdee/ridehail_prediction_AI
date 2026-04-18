"""Base class for spatiotemporal models."""
import torch.nn as nn

class SpatioTemporalModel(nn.Module):
    def forward(self, x, **kwargs):
        raise NotImplementedError
