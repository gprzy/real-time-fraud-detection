import time
import pandas as pd


data_base_path = '../../../data/'
raw_data_path = 'raw/'
processed_data_path = 'processed/'
file_name = 'creditcard'


if __name__ == '__main__':
    df = pd.read_csv(
        f'{data_base_path}{raw_data_path}{file_name}.csv'
    )

    print(df.shape)

    df.columns = [col.lower() for col in df.columns]
    
    df.to_parquet(
        f'{data_base_path}{processed_data_path}{file_name}.parquet',
        index=False
    )
