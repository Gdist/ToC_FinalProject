import os
import numpy as np
import pandas as pd
import geopandas as gpd
import mapclassify as mc
import matplotlib.pyplot as plt
from palettable.cmocean.diverging import * # Color Map

#plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['font.sans-serif'] = ['Noto Sans TC'] 
plt.rcParams['axes.unicode_minus'] = False

import vote

if not os.path.isdir('./output/map'):
	os.mkdir('./output/map')
twShp = gpd.read_file('./data/map/TOWN_MOI_1100415.shp', encoding='utf-8')

def readData():
	# 載入
	data = {}
	for themeId in range(17, 21):
		if os.path.exists('./data/data{}.csv'.format(themeId)):
			data[themeId] = pd.read_csv(f'./data/data{themeId}.csv')
		else:
			vote.getStats(themeId=themeId, saveJSON=True, saveCSV=True)
			data[themeId] = pd.read_csv(f'./data/data{themeId}.csv')
	# 處理
	data['All'] = data[17].copy()
	needs = ['agree_ticket','vote_ticket']
	for themeId in range(18, 21):
		for need in needs:
			data['All'].loc[:, need] += data[themeId].loc[:, need]
	return data

data = readData()

def plotTaiwan(themeId="All"):
	if themeId not in range(17, 21):
		themeId = 'All'
	# 取鄉鎮市區
	data_agree_rate = data[themeId][(data[themeId]['村里']=='合計') & (data[themeId]['鄉鎮市區'] !='合計')]
	# 合併，去除鄉鎮市區名稱相同
	TW_agree_rate = twShp.merge(data_agree_rate, how="inner", left_on=('TOWNNAME'), right_on=('鄉鎮市區'))
	TW_agree_rate = TW_agree_rate[(TW_agree_rate['COUNTYNAME']==TW_agree_rate['縣市'])]
	# 計算同意率
	TW_agree_rate = TW_agree_rate.assign(agree_rate="")
	TW_agree_rate.loc[:, 'agree_rate'] = 100 * round(TW_agree_rate['agree_ticket'] / TW_agree_rate['vote_ticket'], 4)
	#data_agree_rate['agree_rate'] = 100 * round(data_agree_rate['agree_ticket'] / data_agree_rate['vote_ticket'], 4)
	# 試算分群
	#bp = mc.UserDefined(TW_agree_rate['agree_rate'], bins=np.arange(25, 80, 5))
	# Plot
	TW_agree_rate.plot(figsize=(8, 12), column='agree_rate', cmap=Delta_12_r.mpl_colormap,
					legend=True,
					legend_kwds={'loc': 'lower right', 'title': '同意率',},
					scheme='UserDefined',
					classification_kwds={'bins': np.arange(25, 80, 5)},
				)
	plt.xlim((119.2, 122.5))
	plt.ylim((21.5, 25.5))
	title = f"全國第{themeId}案同意率分層設色圖" if isinstance(themeId, int) else "全國四案同意率分層設色圖"
	plt.title(title , fontsize=24) 
	plt.axis('off')
	plt.savefig(f'./output/map/Taiwan_{themeId}.png')
	#plt.show()

def plotCity(themeId="All", cityName="臺南市"):
	if themeId not in range(17, 21):
		themeId = 'All'
	if cityName == 'Taiwan':
		plotTaiwan(themeId=themeId)
		return
	cityShp = twShp[twShp['COUNTYNAME']==cityName]
	# 取該縣市鄉鎮市區
	data_agree_rate = data[themeId][(data[themeId]['縣市']==cityName) & (data[themeId]['村里']=='合計') & (data[themeId]['鄉鎮市區']!='合計')]
	city_agree_rate = cityShp.merge(data_agree_rate, left_on=('TOWNNAME'), right_on=('鄉鎮市區'))
	city_agree_rate = city_agree_rate[(city_agree_rate['COUNTYNAME']==city_agree_rate['縣市'])]
	# 計算同意率
	city_agree_rate = city_agree_rate.assign(agree_rate="")
	city_agree_rate.loc[:, 'agree_rate'] = 100 * round(city_agree_rate['agree_ticket'] / city_agree_rate['vote_ticket'], 4)
	# 試算分群，不可能對縣市分別調適，直接調用mapclassify的NaturalBreaks(K-Means)/Quantiles
	#bp = mc.NaturalBreaks(city_agree_rate['agree_rate'], k=11)
	# Plot
	city_agree_rate.plot(figsize=(12, 12), column='agree_rate', cmap=Delta_11_r.mpl_colormap,
					legend=True,
					legend_kwds={'loc': 'lower right', 'title': '同意率',},
					scheme='NaturalBreaks', k=11,
				)
	title = f"{cityName}第{themeId}案同意率分層設色圖" if isinstance(themeId, int) else f"{cityName}四案同意率分層設色圖"
	plt.title(title , fontsize=24)
	if cityName == "高雄市":
		plt.xlim((120, 121.2))
		plt.ylim((22.3, 23.6))
	plt.axis('off')
	plt.savefig(f'./output/map/{cityName}_{themeId}.png')

if __name__ == '__main__':
	#plotTaiwan(themeId='All')
	#plotCity(themeId='All', cityName="高雄市")
	plotCity(themeId='All', cityName="澎湖縣")
	


