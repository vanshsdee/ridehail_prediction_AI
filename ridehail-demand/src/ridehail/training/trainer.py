"""Trainer skeleton — fill in once a model + dataset are ready."""
class Trainer:
    def __init__(self, model, optimizer, loss_fn, device):
        self.model, self.optimizer, self.loss_fn, self.device = model, optimizer, loss_fn, device
    def fit(self, train_loader, val_loader, epochs: int):
        raise NotImplementedError
