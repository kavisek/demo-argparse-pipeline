from pipeline.config import Config

class Pipeline(Config):
    def __init__(self, config):
        assert isinstance(config, Config)
        self.config = config

        
    def print_config(self):
        print(self.config)

    
    def run(self):
        print('Running pipeline...')
