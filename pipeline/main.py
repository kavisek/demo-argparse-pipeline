from pipeline.pipeline import Pipeline
from pipeline.config import Config


def main():
    config = Config('config.yaml')
    config.load_config()
    config.print_config()
    # print(config.config['env']
    # songs_pipeline = Pipeline(config)
    # songs_pipeline.run()

if __name__ == '__main__':
    main()