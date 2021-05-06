import numpy as np
import pandas as pd
import os

df = pd.read_csv(os.path.join(os.path.dirname(__file__),'betta.csv'), delimiter=',')
print('Number of datapoints: {}'.format(len(df)))

sleep_quality = list(df['sleep_quality'])
rested_morning = list(df['rested_morning'])
rested_overall = list(df['rested_overall'])

rho = np.corrcoef([sleep_quality, rested_morning, rested_overall])

print(rho)