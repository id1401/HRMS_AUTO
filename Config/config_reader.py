import configparser
import os

class ConfigReader:
    def __init__(self, env='Testing'):
        self.env = env.upper()
        self.config = configparser.ConfigParser()
        config_path = os.path.join(os.path.dirname(__file__), 'config.ini')
        self.config.read(config_path)

        if self.env not in self.config:
            raise ValueError(f"❌ Environment {self.env} not found in config.ini")

    def get(self, key):
        return self.config[self.env][key]
