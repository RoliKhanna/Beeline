
import pandas as pd
from datetime import datetime
from util import RAW_DATA, PROCESS_LEVEL1

pd.options.display.expand_frame_repr = False

# raw_data = pd.read_csv(RAW_DATA)
# print(raw_data.head())

def parsedate(x):
    return datetime.strptime(x, '%Y %m %d %H')

raw_data = pd.read_csv(RAW_DATA, parse_dates=[['year', 'month', 'day', 'hour']], index_col=0, date_parser=parsedate)
raw_data.drop('No', axis=1, inplace=True)
raw_data.columns = ['pollution', 'dew', 'temp', 'press', 'wnd_dir', 'wnd_spd', 'snow', 'rain']
raw_data.index.name = 'date'

raw_data['pollution'].fillna(0, inplace=True)
raw_data = raw_data[24:]
# print(raw_data.head())
raw_data.to_csv(PROCESS_LEVEL1)
