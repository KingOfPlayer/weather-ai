import json
import matplotlib.pyplot as plt
import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose

def fillData():
    global data
    data['totalPrecipitation'] = data['totalPrecipitation'].interpolate()
    data['pressure'] = data['pressure'].interpolate()
    data['windDir'] = data['windDir'].interpolate()

def saveSeasonalPlot(array, feature_name):
    result = seasonal_decompose(array,model='additive')
    result.plot()
    plt.subplot(4, 1, 1)
    plt.title(f"{feature_name}")
    plt.savefig(f"{feature_name}.png")

# def saveSeasonalDataSet(array, feature_name): # (Not Work)
#     loaddataset = open(f'{Data_file}_{feature_name}.json', 'w+')
#     result = seasonal_decompose(array,model='additive')
#     loaddataset.truncate(0)
#     loaddataset.write(result.to_json())
#     loaddataset.close()

def saveDataset(array,name):
    loaddataset = open(f"{Data_file}_{name}.json", 'w+')
    loaddataset.truncate(0)
    loaddataset.write(array.to_json())
    loaddataset.close()

    print("Saved")
    
Data_file = "LTBQ0"

data = pd.read_json(path_or_buf=f"{Data_file}.json",date_unit="s")
data.columns=['date','temp','dewPoint','totalPrecipitation','condition','windSpeed','pressure','humidity','windDir']
data['date'] = pd.to_datetime(data['date'],format="%Y-%m-%dT%H:%M:%S")
data = data.set_index('date')

fillData()

saveDataset(data,"filled")

offset_length = 24*30
offset = 10000

# Seasonal data save (Not Work)
# saveSeasonalDataSet(data['temp'],"Sıcaklık")
# saveSeasonalDataSet(data['dewPoint'],"Çiğ Noktası")
# saveSeasonalDataSet(data['totalPrecipitation'],"Toplam Yağış")
# saveSeasonalDataSet(data['windSpeed'],"Rüzgar Hızı")
# saveSeasonalDataSet(data['pressure'],"Basınç")
# saveSeasonalDataSet(data['humidity'],"Bağıl Nem")

# Seasonal data plot save
saveSeasonalPlot(data['temp'].iloc[offset:offset+offset_length],"Sıcaklık")
saveSeasonalPlot(data['dewPoint'].iloc[offset:offset+offset_length],"Çiğ Noktası")
saveSeasonalPlot(data['totalPrecipitation'].iloc[offset:offset+offset_length],"Toplam Yağış")
saveSeasonalPlot(data['windSpeed'].iloc[offset:offset+offset_length],"Rüzgar Hızı")
saveSeasonalPlot(data['pressure'].iloc[offset:offset+offset_length],"Basınç")
saveSeasonalPlot(data['humidity'].iloc[offset:offset+offset_length],"Bağıl Nem")