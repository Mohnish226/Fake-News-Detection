import glob 
import pandas as pd
import numpy as np
from tqdm import tqdm


def get_datasets(shuffle=False):
    df = pd.DataFrame()
    for file in tqdm(glob.glob('Datasets/*/*_*.csv')):
        df = df.append(pd.read_csv(file), ignore_index=True)
    if shuffle:
    	#df = df.sample(frac=1).reset_index(drop=True)
    	df = df.reindex(np.random.permutation(df.index)).reset_index(drop=True)
    return df