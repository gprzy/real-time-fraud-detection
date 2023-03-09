import time
import pandas as pd


url = 'http://localhost:5001/download'
raw_data_path = '../../../data/raw/'
raw_data_file_name = 'creditcard.csv'


if __name__ == '__main__':
    start = time.time()

    print('PROCESS STARTED')

    print(f'\nGET data from {url}...')
    df = pd.read_csv(url)
    print('data shape =', df.shape)

    print(f'\nsaving raw data in "{raw_data_path + raw_data_file_name}"')
    df.to_csv(raw_data_path + raw_data_file_name, index=False)
    print('data saved with success!')

    print('\nPROCESS FINISHED!')
    print(f'elapsed time = {round(time.time() - start, 2)}s')
