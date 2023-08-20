from pipeline.config import Config
import os
import pandas as pd
from typing import List

class DataFramePipeline(Config):
    def __init__(self, config):
        assert isinstance(config, Config)
        self.config = config
        self.files = []
        self.dataframes = []
        self.schema = {
            'title': 'string',
            'artist': 'string',
            'album': 'string',
            'year': 'int64',
            'duration(minutes)': 'float64'
        }
        self.output_schema = {
            'artist': 'string',
            'title': 'int64',
            'album': 'string',
            'duration(minutes)': 'float64'
        }

    def lower_case_columns(self, dataframe: pd.DataFrame) -> pd.DataFrame:
        """Converts all columns to lower case
        """
        dataframe.columns = dataframe.columns.str.lower()
        return dataframe
    
    def validate_input_schema(self, schema: dict, dataframe: pd.DataFrame) -> bool:
        """Validates the input schema against the dataframe
        """
        for column in dataframe.columns:
            assert column in schema.keys(), 'Schema is not valid'
    
        print('Schema is valid')

    def validate_output_schema(self, schema: dict, dataframe: pd.DataFrame) -> bool:
        """Validates the output schema against the dataframe
        """
        print('Validating output schema...')
        for column in dataframe.columns:
            assert column in schema.keys(), 'Schema is not valid'
        print('Schema is valid')


    def print_config(self) -> None:
        """Prints the config file
        """
        print(self.config)

    def read_files(self, path, file_type='csv') -> List[str]:
        """Reads all files in a directory
        """
        for file in os.listdir(path):
            if file.endswith(file_type):
                self.files.append(file)
        
        print(f'Found {len(self.files)} files')
        return self.files

    def print_files(self) -> None:
        """Prints all files found in the directory
        """
        print(self.files)

    def print_dataframe(self, dataframe: pd.DataFrame) -> None:
        print(dataframe)
    
    def read_dataframes(self, path: str = os.getcwd()) -> List[pd.DataFrame]:
        """Reads all dataframes in a directory"""

        print('Reading dataframes...')

        if len(self.files) == 0:
            self.read_files(self.config.source)
        
        
        for file in self.files:
            dataframe = pd.read_csv(f'{path}/{file}')
            dataframe = self.lower_case_columns(dataframe)
            self.validate_input_schema(self.schema, dataframe)
            self.dataframes.append(dataframe)

        print(f'Found {len(self.dataframes)} dataframes')
        return self.dataframes
    
    def print_dataframes(self) -> None:
        """Prints all dataframes found in the directory"""
        for dataframe in self.dataframes:
            print(dataframe.head()) 

        print(f'Found {len(self.dataframes)} dataframes')   

    def concatentate_dataframes(self) -> pd.DataFrame:
        """Concatenates all dataframes into one dataframe"""
        
        print('Concatenating dataframes...')
        self.concat_dataframe = pd.concat(self.dataframes)
        print(f'Concatenated dataframes, {len(self.concat_dataframe)} rows')
        return self.concat_dataframe
    
    def remove_duplicates(self) -> pd.DataFrame:
        """Removes duplicates from the dataframe"""
        print('Removing duplicates...')
        self.concat_dataframe.drop_duplicates(inplace=True)
        print(f'Removed duplicates, {len(self.concat_dataframe)} rows')
        return self.concat_dataframe
    

    def aggegrate_count(self) -> pd.DataFrame:
        """Get the total number of song by each artist"""
        print('Aggegrating count...')
        self.artist_count_df = self.concat_dataframe.groupby('artist').count()
        print(f'Aggegrated count, {len(self.artist_count_df)} rows')
        return self.artist_count_df
    


        
        


    def run(self):
        # Reading the file multiple times to create duplicates.
        self.read_files(path=self.config.source)
        self.read_files(path=self.config.source)
        self.read_files(path=self.config.source)

        self.print_files()
        self.read_dataframes(path=self.config.source)
        self.print_dataframes()

        # Concatenate all dataframes
        self.concatentate_dataframes()

        # Remove Duplicates
        self.remove_duplicates()

        #Aggegrate count of each column
        self.aggegrate_count()
        self.print_dataframe(self.artist_count_df)