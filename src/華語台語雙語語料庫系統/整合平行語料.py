'''
Created on 2013/3/5

@author: Ihc
'''
from 教育部臺灣閩南語常用詞辭典.資料庫連線 import 資料庫連線
from 文章音標解析器 import 文章音標解析器
from 華語台語雙語語料庫系統.文章標點處理工具 import 文章標點處理工具
from 華語台語雙語語料庫系統.何澤政教會羅馬字音標 import 何澤政教會羅馬字音標

揣攏總資料 = 資料庫連線.prepare('SELECT "aid","year", ' +
	'"title","title_translation","content","TaiLuo","JiaoLuo" ' +
	'FROM "華語台語雙語語料庫系統"."article_frank" WHERE "整合遏袂"=false AND ("TaiLuo"!=\'\' OR "JiaoLuo"!=\'\') ' +
	'ORDER BY "aid" DESC LIMIT 10')

標點符號 = {' ', '-', ',', '。', '、', '，',
	'「', '「', '」', '(', ')', '；', '？', '『', '』', '【', '】', '！', '：', '"'}
# 臺羅解析器 = 文章音標解析器(教會羅馬字音標)
# 臺羅解析器.合法字元 = {'-', ' '}
教羅解析器 = 文章音標解析器(何澤政教會羅馬字音標)
教羅解析器.標點符號 = 標點符號
標點處理工具 = 文章標點處理工具()
標點處理工具.標點符號 = 標點符號
# 通用解析器 = 文章音標解析器(通用拼音音標)
# 通用解析器.合法字元 = {'-', ' '}
# 「 Toa7-tiau5-hang7 」
代換字串 = [('　', ' '), ('  ', ' '), ('  ', ' '), ('  ', ' ')]
for 文章編號, 西元年, 標題國語, 標題音標, 國語, 臺羅, 教羅 in 揣攏總資料():
	print(文章編號)
	if 臺羅 == '':
		內文音標 = 教羅
	else:
		內文音標 = 臺羅
	for 錯誤, 正確 in 代換字串:
		標題國語 = 標題國語.replace(錯誤, 正確)
		標題音標 = 標題音標.replace(錯誤, 正確)
		國語 = 國語.replace(錯誤, 正確)
		內文音標 = 內文音標.replace(錯誤, 正確)
	標題國語 = 標題國語.strip()
	標題音標 = 標題音標.strip()
	國語文章 = [標點處理工具.切開語句(標題國語)]
	音標文章 = [標點處理工具.切開語句(標題音標)]

	標題翻譯解析結果, 標題翻譯合法無 = 教羅解析器.解析語句佮顯示毋著字元(標題音標)
	for 處理一半的國語 in 國語.split('\r\n'):
		for 一逝國語 in 處理一半的國語.split('\r\n'):
			一个句語的詞 = 標點處理工具.切開語句(一逝國語.strip())
			國語文章.append(一个句語的詞)
# 			for 一个詞 in 一个句語的詞:
# 				國語文章.append(一个詞)
# 				print(一个詞, end = '')
# 			print(一个句語的詞)
	for 處理一半的內文音標 in 內文音標.split('\r\n'):
		for 一逝內文音標 in 處理一半的內文音標.split('\r\n'):
			一个句語的詞 = 標點處理工具.切開語句(一逝內文音標.strip())
			新語句 = []
			for 一个詞 in 一个句語的詞:
				內文翻譯解析結果, 內文翻譯合法無 = 教羅解析器.解析語句佮顯示毋著字元(一个詞, True)
				新語句.append(內文翻譯解析結果)
				if not 內文翻譯合法無:
					print('「'+一个詞+'」是英文諾？')
			音標文章.append(新語句)
# 				print(內文翻譯解析結果, end = '')
# 			print(一个句語的詞)
# 			print()
# 	print(len(國語文章))
# 	print(len(音標文章))
	長度 = (len(國語文章), len(音標文章))
	print('語句數量=' + str(長度))
	if min(長度) != max(長度):
# 		print(國語文章)
# 		print(音標文章)
		綜合文章 = []
		for i in range(min(長度)):
			綜合文章.append((國語文章[i], 音標文章[i]))
		print(綜合文章)
	else:
		for i in range(長度[0]):
			舊國語語句=國語文章[i]
			舊音標語句=音標文章[i]
			語句長度 = (len(舊國語語句), len(舊音標語句))
			if min(語句長度) != max(語句長度):
		# 		print(國語文章)
		# 		print(音標文章)
				綜合文章 = []
				for j in range(min(語句長度)):
					綜合文章.append((舊國語語句[j], 舊音標語句[j]))
				print(綜合文章)

