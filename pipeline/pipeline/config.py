import yaml
import os
import argparse

class Config:
    def __init__(self, config_file):
        self.config_file = config_file
        self.base_config = None

    def load_yaml_config(self):
        # Loading config file
        with open(self.config_file) as f:
            base_config = yaml.safe_load(f)
        
        # Load all variablse as attributes to this Config class
        for key, value in base_config.items():
            setattr(self, key, value)

        # Save the config dict as an attribute
        self.base_config = base_config

        return self

    def load_env_config(self):
        assert self.base_config is not None, 'Must load yaml config first'
        # Check all envinronment variables are set
        for key, value in self.base_config.items():
            env = os.getenv(key.upper())
            if env is not None:
                setattr(self, key, env)
        
        return self
    
    def load_argparse_config(self):
        assert self.base_config is not None, 'Must load yaml config first'
        # Check argparse variables, if any are specified replace the key in the
        # config file with the argparse value

        parser = argparse.ArgumentParser()
        for key, value in self.base_config.items():
            parser.add_argument(f'--{key.lower()}')
        
        args = parser.parse_args()
        for key, value in self.base_config.items():
            arg = getattr(args, key)
            if arg is not None:
                setattr(self, key, arg)

        return self

    def load_config(self):
        self.load_yaml_config()
        self.load_env_config()
        self.load_argparse_config()

        return self


    def print_config(self):
        print(self.__dict__)