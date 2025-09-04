import json

class Config:
    """Manages framework configuration settings."""
    def __init__(self, config_path=None):
        self.settings = {
            'simulation_name': 'default_sim',
            'max_steps': 100,
            'log_level': 'INFO'
        }
        if config_path:
            self.load_from_file(config_path)

    def load_from_file(self, path):
        """Loads configuration from a JSON file."""
        try:
            with open(path, 'r') as f:
                self.settings.update(json.load(f))
        except FileNotFoundError:
            print(f"Warning: Config file not found at {path}")

    def get(self, key):
        """Gets a configuration value."""
        return self.settings.get(key)

