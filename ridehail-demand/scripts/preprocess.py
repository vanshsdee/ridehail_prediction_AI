"""Convert raw trip records → zone × time demand tensors in data/processed/."""
import argparse
def main():
    p = argparse.ArgumentParser()
    p.add_argument("--config", default="configs/data/nyc_taxi.yaml")
    args = p.parse_args()
    print(f"[stub] preprocess using {args.config}")
if __name__ == "__main__":
    main()
