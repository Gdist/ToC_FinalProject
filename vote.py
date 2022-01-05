import os, re
import requests, json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from palettable.colorbrewer.qualitative import * # Color Map

requests.packages.urllib3.disable_warnings()

if not os.path.isdir('./data'):
	os.mkdir('./data')
if not os.path.isdir('./output'):
	os.mkdir('./output')
if not os.path.isdir('./output/anyly'):
	os.mkdir('./output')
def getStats(themeId=17, saveJSON=False, saveCSV=True):
	data = {}
	themes = {
		17 : "79b8adc5242fb9232566f29a3114eddd",
		18 : "896b2dbb2f0c83084b9ca99d12b4a2d2",
		19 : "450483c187d6249faeca40711f00f45d",
		20 : "aad5b411b067a25611f7082f8fd6807c",
	}
	url = "https://referendums.2021.nat.gov.tw/static/referendums/data/profiles/N/{}/C/00_000_00_000_0000.json".format(themes[themeId])
	urlD = "https://referendums.2021.nat.gov.tw/static/referendums/data/profiles/N/{}/D/{}_{}_00_000_0000.json"
	urlL = "https://referendums.2021.nat.gov.tw/static/referendums/data/profiles/N/{}/L/{}_{}_00_000_0000.json"
	res = requests.get(url)
	resJson = json.loads(res.text)
	# Needed items
	needs = ['valid_ticket', 'agree_ticket', 'disagree_ticket', 'invalid_ticket', 'vote_ticket', 'votable_population', 'population', 'vote_to_votable', 'agree_to_votable']
	for city in resJson['00_000_00_000_0000']:
		data[city['area_name']] = {}
		resD = requests.get(urlD.format(themes[themeId], city['prv_code'], city['city_code']))
		resJsonD = json.loads(resD.text)
		resL = requests.get(urlL.format(themes[themeId], city['prv_code'], city['city_code']))
		resJsonL = json.loads(resL.text)
		for dept in resJsonD['{}_{}_00_000_0000'.format(city['prv_code'], city['city_code'])]:
			data[city['area_name']][dept['area_name']]={}
			for li in resJsonL['{}_{}_{}_{}_0000'.format(dept['prv_code'], dept['city_code'], dept['area_code'], dept['dept_code'])]:
				data[city['area_name']][dept['area_name']][li['area_name']] = {key: value for key, value in li.items() if key in needs}
			data[city['area_name']][dept['area_name']]['合計'] = {key: value for key, value in dept.items() if key in needs}
		data[city['area_name']]['合計'] = {}
		data[city['area_name']]['合計']['合計'] = {key: value for key, value in city.items() if key in needs}

	if saveJSON:
		with open('./data/data{}.json'.format(themeId), 'w', encoding='utf-8') as f:
			json.dump(data, f, ensure_ascii=False, indent=4)
	if saveCSV:
		with open('./data/data{}.csv'.format(themeId), 'w', encoding='utf-8') as f:
			f.write(f"縣市,鄉鎮市區,村里,valid_ticket,agree_ticket,disagree_ticket,invalid_ticket,vote_ticket,votable_population,population,vote_to_votable,agree_to_votable\n")
			for city in data:
				for dept in data[city]:
					for li in data[city][dept]:
						f.write(",".join([city, dept, li] + [str(value) for value in data[city][dept][li].values()])+"\n")
	return data

def readDataFromJson(saveJSON=True, saveCSV=False):
	data = {}
	if not os.path.isdir('./data'):
		os.mkdir('./data')
	if not os.path.isdir('./output'):
		os.mkdir('./output')
	for themeId in range(17, 21):
		if os.path.exists('./data/data{}.json'.format(themeId)):
			with open('./data/data{}.json'.format(themeId), encoding='utf-8') as f:
				data[themeId] = json.load(f)
		else:
			print(f"正在爬取第{themeId}案統計數據")
			data[themeId] = getStats(themeId=themeId, saveJSON=saveJSON, saveCSV=saveCSV)
	return data

def plot(count, title, saveName):
	plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
	plt.rcParams['axes.unicode_minus'] = False

	data = {
		"同意": [ round(votes['agree']/votes['valid'], 4) for votes in count.values()] ,
		"不同意": [ 1 - round(votes['agree']/votes['valid'], 4) for votes in count.values()]
	}

	df = pd.DataFrame(data, index=range(17,21))
	df.plot(kind='bar', stacked=True, colormap=Paired_3.mpl_colormap, figsize=(10, 6), rot=0)

	plt.legend(loc="lower left", ncol=2)
	plt.title(title, fontsize=20, fontweight="bold")
	plt.xlabel("第#案公投", fontsize=14, fontweight="bold")
	plt.ylabel("比例", fontsize=14, fontweight="bold")

	for n, x in enumerate([*df.index.values]):
		for (proportion, y_loc) in zip(df.loc[x], df.loc[x].cumsum()):
			plt.text(x=n-0.17,
				 y=(y_loc-proportion)+(proportion/2),
				 s=f'{np.round(proportion*100, 2)}%', 
				 color="black", fontsize=12, fontweight="bold")
	plt.savefig(f"./output/anyly/{saveName}.png")
	#plt.show()

def main(item="收入", byData='平均數', numData=100, ascending=False):
	# 處理資料輸入
	if item=="收入":
		df = pd.read_csv('./data/107_165-9.csv', sep=",", header=0, encoding='utf-8-sig')
		df = df[~df.村里.isin(["其他", "合計"])]
		df = df[(df['納稅單位']>=10)]
		df = df.rename(columns={'﻿縣市' : '縣市'}) # 含有\ufeff
	else: #年齡
		#byData = '平均數'
		#if False: pass
		if os.path.exists('./data/age.csv'):
			df = pd.read_csv('./data/age.csv', sep=",", header=0, encoding='utf-8-sig')
		else:
			df = pd.read_csv('./data/opendata11004M030.csv', sep=",", header=1, encoding='utf-8-sig')
			df = df.assign(縣市="", 鄉鎮市區="", 平均數=0, 中位數=0)
			df.loc[:,['30歲以下比例', '40歲以下比例', '70歲以上比例', '80歲以上比例']] = 0
			for index, row in df.iterrows():
				reRegion = re.search(r"(.+)(縣|市)(.+)(鄉|鎮|市|區)", row.loc()['區域別'])
				df.loc()[index, '縣市'] = reRegion.group(1)+reRegion.group(2)
				df.loc()[index, '鄉鎮市區'] = reRegion.group(3)+reRegion.group(4)
				avg_age = sum([ (row.iloc()[age*2+8] + row.iloc()[age*2+9]) * age for age in range(0, 101)]) / row.iloc()[5]
				below30 = sum([ (row.iloc()[age*2+8] + row.iloc()[age*2+9]) for age in range(18, 31)]) / row.iloc()[5]
				below40 = sum([ (row.iloc()[age*2+8] + row.iloc()[age*2+9]) for age in range(18, 41)]) / row.iloc()[5]
				above70 = sum([ (row.iloc()[age*2+8] + row.iloc()[age*2+9]) for age in range(70, 101)]) / row.iloc()[5]
				above80 = sum([ (row.iloc()[age*2+8] + row.iloc()[age*2+9]) for age in range(80, 101)]) / row.iloc()[5]
				# find Median
				medianPos, medianSum = row.iloc()[5] / 2 , 0
				for age in range(0, 101):
					medianSum += (row.iloc()[age*2+8] + row.iloc()[age*2+9])
					if medianSum > medianPos:
						median = age
						break
				df.loc()[index, '平均數'] = round(avg_age, 4)
				df.loc()[index, '中位數'] = median
				df.loc()[index, '30歲以下比例'] = round(100* below30, 2)
				df.loc()[index, '40歲以下比例'] = round(100* below40, 2)
				df.loc()[index, '70歲以上比例'] = round(100* above70, 2)
				df.loc()[index, '80歲以上比例'] = round(100* above80, 2)
			df.drop(df.columns[8:210], axis=1, inplace=True)
			df.to_csv('./data/age.csv', encoding='utf-8-sig', index=False)
	# 排序
	df = df.sort_values(by=[byData], ascending=ascending)
	df100 = df.iloc[0:numData, :]
	#print(df100)
	data = readDataFromJson()
	if item=="收入":
		stats = pd.DataFrame(columns=['縣市', '鄉鎮市區', '村里', '納稅單位', '綜合所得總額', '平均數', '中位數', 
			'第17案同意票數', '第17案有效票數', '第17案同意率',
			'第18案同意票數', '第18案有效票數', '第18案同意率',
			'第19案同意票數', '第19案有效票數', '第19案同意率',
			'第20案同意票數', '第20案有效票數', '第20案同意率'])
	else:
		stats = pd.DataFrame(columns=['縣市', '鄉鎮市區', '村里', '戶數', '人口數', '人口數-男', '人口數-女',
			'平均數', '中位數', '30歲以下比例', '40歲以下比例', '70歲以上比例', '80歲以上比例',
			'第17案同意票數', '第17案有效票數', '第17案同意率',
			'第18案同意票數', '第18案有效票數', '第18案同意率',
			'第19案同意票數', '第19案有效票數', '第19案同意率',
			'第20案同意票數', '第20案有效票數', '第20案同意率'])
	count = {}
	for themeId in range(17, 21):
		count[themeId] = {}
		count[themeId]['valid'], count[themeId]['agree'], count[themeId]['disagree'] = 0, 0, 0
	for index, row in df100.iterrows():
		if item=="收入":
			cur = row.iloc[[0,1,2,3,4,5,6]]
		else:
			cur = row.iloc[[8,9,3,4,5,6,7,10,11,12,13,14]]
		for themeId in range(17, 21):
			try:
				votes = data[themeId][row['縣市']][row['鄉鎮市區']][row['村里']]
			except:
				for li in data[themeId][row['縣市']][row['鄉鎮市區']]:
					if row['村里'] in li:
						votes = data[themeId][row['縣市']][row['鄉鎮市區']][li]
			agree_rate = round(votes['agree_ticket'] / votes['valid_ticket'], 4)
			count[themeId]['valid'] += votes['valid_ticket']
			count[themeId]['agree'] += votes['agree_ticket']
			count[themeId]['disagree'] += votes['disagree_ticket']
			cur = cur.append(
				pd.Series([votes['agree_ticket'], votes['valid_ticket'], agree_rate],
					index=['第{}案同意票數'.format(themeId), '第{}案有效票數'.format(themeId), '第{}案同意率'.format(themeId)]))
		stats = stats.append(cur, ignore_index=True)

	'''stats['縣市'] = stats['縣市'] # Duplicate, unknown error -> \ufeff in first col title
	stats.drop(stats.columns[[19]], axis=1, inplace=True)'''

	total = pd.Series([stats['第17案同意票數'].sum(), stats['第17案有效票數'].sum(), round(stats['第17案同意票數'].sum() / stats['第17案有效票數'].sum(), 4), 
						stats['第18案同意票數'].sum(), stats['第18案有效票數'].sum(), round(stats['第18案同意票數'].sum() / stats['第18案有效票數'].sum(), 4), 
						stats['第19案同意票數'].sum(), stats['第19案有效票數'].sum(), round(stats['第19案同意票數'].sum() / stats['第19案有效票數'].sum(), 4), 
						stats['第20案同意票數'].sum(), stats['第20案有效票數'].sum(), round(stats['第20案同意票數'].sum() / stats['第20案有效票數'].sum(), 4)],
					index=['第17案同意票數', '第17案有效票數', '第17案同意率',
							'第18案同意票數', '第18案有效票數', '第18案同意率',
							'第19案同意票數', '第19案有效票數', '第19案同意率',
							'第20案同意票數', '第20案有效票數', '第20案同意率',])
	stats = stats.append(total, ignore_index=True)
	#print(stats)

	order = "最高" if not ascending else "最低"
	saveName = f"{item}{byData}{order}{numData}"
	stats.to_csv(f"./output/anyly/{saveName}.csv", index=False, encoding='utf-8-sig')

	plot(count, title=f"{saveName}村里", saveName=saveName)

if __name__ == '__main__':
	data = readDataFromJson(saveJSON=True, saveCSV=True)
	main(item="年齡" ,byData='中位數', numData=200, ascending=False)
