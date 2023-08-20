from pipeline.pipeline import DataFramePipeline
from pipeline.config import Config


def main():


    config = Config('config.yaml')
    config.load_config()
    config.print_config()

    songs_pipeline = DataFramePipeline(config)
    songs_pipeline.run()

if __name__ == '__main__':
    main()