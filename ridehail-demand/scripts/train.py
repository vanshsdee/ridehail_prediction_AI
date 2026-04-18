"""Entry point: python scripts/train.py model=tgnn data=nyc_taxi"""
import hydra
from omegaconf import DictConfig, OmegaConf

from ridehail.utils.seed import set_seed
from ridehail.utils.device import get_device


@hydra.main(version_base=None, config_path="../configs", config_name="config")
def main(cfg: DictConfig) -> None:
    print(OmegaConf.to_yaml(cfg))
    set_seed(cfg.seed)
    device = get_device(cfg.device)
    print(f"Using device: {device}")
    # TODO: build dataset, model, trainer


if __name__ == "__main__":
    main()
