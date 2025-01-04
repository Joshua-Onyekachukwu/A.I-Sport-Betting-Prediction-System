# utils/logger.py
import logging
import yaml
import os

def setup_logger():
    with open("config/logging_config.yaml", "r") as f:
        config = yaml.safe_load(f)
    logging.config.dictConfig(config)

def get_logger(name):
    return logging.getLogger(name)