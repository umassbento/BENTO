import argparse
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument('--verbose', action='store_true')
parser.add_argument('--upload', type=unicode)
parser.add_argument('--run', type=unicode)
parser.add_argument('--data', type=unicode)

opt = parser.parse_args()
