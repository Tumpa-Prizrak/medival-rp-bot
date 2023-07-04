import json
from dataclasses import dataclass
from typing import List

@dataclass
class Config:
    token: str
    prefix: str
    channel_id: int
    owners: List[str]

def load_config():
    """Load config from config.json file."""
    with open('config.json') as f:
        config = json.load(f)
    return Config(**config)
