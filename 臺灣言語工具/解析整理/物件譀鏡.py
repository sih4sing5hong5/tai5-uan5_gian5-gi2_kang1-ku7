# -*- coding: utf-8 -*-
"""
著作權所有 (C) 民國102年 意傳文化科技
開發者：薛丞宏
網址：http://意傳.台灣
語料來源：請看各資料庫內說明

本程式乃自由軟體，您必須遵照SocialCalc設計的通用公共授權（Common Public Attribution License, CPAL)來修改和重新發佈這一程式，詳情請參閱條文。授權大略如下，若有歧異，以授權原文為主：
	１．得使用、修改、複製並發佈此程式碼，且必須以通用公共授權發行；
	２．任何以程式碼衍生的執行檔或網路服務，必須公開該程式碼；
	３．將此程式的原始碼當函式庫引用入商業軟體，且不需公開非關此函式庫的任何程式碼

此開放原始碼、共享軟體或說明文件之使用或散佈不負擔保責任，並拒絕負擔因使用上述軟體或說明文件所致任何及一切賠償責任或損害。

臺灣言語工具緣起於本土文化推廣與傳承，非常歡迎各界用於商業軟體，但希望在使用之餘，能夠提供建議、錯誤回報或修補，回饋給這塊土地。

感謝您的使用與推廣～～勞力！承蒙！
"""
from 臺灣言語工具.基本元素.字 import 字
from 臺灣言語工具.基本元素.詞 import 詞
from 臺灣言語工具.基本元素.組 import 組
from 臺灣言語工具.基本元素.集 import 集
from 臺灣言語工具.基本元素.句 import 句
from 臺灣言語工具.基本元素.章 import 章
from 臺灣言語工具.解析整理.解析錯誤 import 解析錯誤
from 臺灣言語工具.基本元素.公用變數 import 分字符號
from 臺灣言語工具.基本元素.公用變數 import 分詞符號
from 臺灣言語工具.基本元素.公用變數 import 無音
from 臺灣言語工具.解析整理.程式掠漏 import 程式掠漏
from 臺灣言語工具.基本元素.公用變數 import 分型音符號

class 物件譀鏡:
	_掠漏 = 程式掠漏()
	def 看型(self, 物件, 物件分字符號='', 物件分詞符號=''):
		if isinstance(物件, 字):
			return self.看字物件型(物件, 物件分字符號, 物件分詞符號)
		if isinstance(物件, 詞):
			return self.看詞物件型(物件, 物件分字符號, 物件分詞符號)
		if isinstance(物件, 組):
			return self.看組物件型(物件, 物件分字符號, 物件分詞符號)
		if isinstance(物件, 集):
			return self.看集物件型(物件, 物件分字符號, 物件分詞符號)
		if isinstance(物件, 句):
			return self.看句物件型(物件, 物件分字符號, 物件分詞符號)
		if isinstance(物件, 章):
			return self.看章物件型(物件, 物件分字符號, 物件分詞符號)
		self._掠漏.毋是字詞組集句章的毋著(物件)

	def 看音(self, 物件, 物件分字符號=分字符號, 物件分詞符號=分詞符號):
		if isinstance(物件, 字):
			return self.看字物件音(物件, 物件分字符號, 物件分詞符號)
		if isinstance(物件, 詞):
			return self.看詞物件音(物件, 物件分字符號, 物件分詞符號)
		if isinstance(物件, 組):
			return self.看組物件音(物件, 物件分字符號, 物件分詞符號)
		if isinstance(物件, 集):
			return self.看集物件音(物件, 物件分字符號, 物件分詞符號)
		if isinstance(物件, 句):
			return self.看句物件音(物件, 物件分字符號, 物件分詞符號)
		if isinstance(物件, 章):
			return self.看章物件音(物件, 物件分字符號, 物件分詞符號)
		self._掠漏.毋是字詞組集句章的毋著(物件)

	def 看斷詞(self, 物件, 物件分型音符號=分型音符號, 物件分字符號=分字符號, 物件分詞符號=分詞符號):
		if isinstance(物件, 字):
			return self.看字物件斷詞(物件, 物件分型音符號, 物件分字符號, 物件分詞符號)
		if isinstance(物件, 詞):
			return self.看詞物件斷詞(物件, 物件分型音符號, 物件分字符號, 物件分詞符號)
		if isinstance(物件, 組):
			return self.看組物件斷詞(物件, 物件分型音符號, 物件分字符號, 物件分詞符號)
		if isinstance(物件, 集):
			return self.看集物件斷詞(物件, 物件分型音符號, 物件分字符號, 物件分詞符號)
		if isinstance(物件, 句):
			return self.看句物件斷詞(物件, 物件分型音符號, 物件分字符號, 物件分詞符號)
		if isinstance(物件, 章):
			return self.看章物件斷詞(物件, 物件分型音符號, 物件分字符號, 物件分詞符號)
		self._掠漏.毋是字詞組集句章的毋著(物件)

	def 看字物件型(self, 字物件, 物件分字符號='', 物件分詞符號=''):
		self._掠漏.毋是字物件就毋著(字物件)
		return 字物件.型

	def 看詞物件型(self, 詞物件, 物件分字符號='', 物件分詞符號=''):
		self._掠漏.毋是詞物件就毋著(詞物件)
		字的型 = []
		for 一字 in 詞物件.內底字:
			字的型.append(self.看字物件型(一字, 物件分字符號, 物件分詞符號))
		return 物件分字符號.join(字的型)

	def 看組物件型(self, 組物件, 物件分字符號='', 物件分詞符號=''):
		self._掠漏.毋是組物件就毋著(組物件)
		詞的型 = []
		for 一詞 in 組物件.內底詞:
			詞的型.append(self.看詞物件型(一詞, 物件分字符號, 物件分詞符號))
		return 物件分詞符號.join(詞的型)

	def 看集物件型(self, 集物件, 物件分字符號='', 物件分詞符號=''):
		self._掠漏.毋是集物件就毋著(集物件)
		if len(集物件.內底組) == 0:
			raise 解析錯誤('內底組是空的！！')
		if len(集物件.內底組) > 1:
			raise 解析錯誤('內底組毋焦一个！！{0}'.format(str(集物件)))
		return self.看組物件型(集物件.內底組[0], 物件分字符號, 物件分詞符號)

	def 看句物件型(self, 句物件, 物件分字符號='', 物件分詞符號=''):
		self._掠漏.毋是句物件就毋著(句物件)
		集的型 = []
		for 一集 in 句物件.內底集:
			集的型.append(self.看集物件型(一集, 物件分字符號, 物件分詞符號))
		return 物件分詞符號.join(集的型)

	def 看章物件型(self, 章物件, 物件分字符號='', 物件分詞符號=''):
		self._掠漏.毋是章物件就毋著(章物件)
		句的型 = []
		for 一句 in 章物件.內底句:
			句的型.append(self.看句物件型(一句, 物件分字符號, 物件分詞符號))
		return 物件分詞符號.join(句的型)

	def 看字物件音(self, 字物件, 物件分字符號=分字符號, 物件分詞符號=分詞符號):
		self._掠漏.毋是字物件就毋著(字物件)
		return 字物件.音

	def 看詞物件音(self, 詞物件, 物件分字符號=分字符號, 物件分詞符號=分詞符號):
		self._掠漏.毋是詞物件就毋著(詞物件)
		字的音 = self._提著詞物件的字物件音陣列(詞物件, 物件分字符號, 物件分詞符號)
		攏有音 = []
		for 音標 in 字的音:
			if 音標 != 無音:
				攏有音.append(音標)
		return 物件分字符號.join(攏有音)

	def _提著詞物件的字物件音陣列(self, 詞物件, 物件分字符號, 物件分詞符號):
		字的音 = []
		for 一字 in 詞物件.內底字:
			音標 = self.看字物件音(一字, 物件分字符號, 物件分詞符號)
			字的音.append(音標)
		return 字的音
	def 看組物件音(self, 組物件, 物件分字符號=分字符號, 物件分詞符號=分詞符號):
		self._掠漏.毋是組物件就毋著(組物件)
		詞的音 = []
		for 一詞 in 組物件.內底詞:
			音標 = self.看詞物件音(一詞, 物件分字符號, 物件分詞符號)
			if 音標 != 無音:
				詞的音.append(音標)
		return 物件分詞符號.join(詞的音)

	def 看集物件音(self, 集物件, 物件分字符號=分字符號, 物件分詞符號=分詞符號):
		self._掠漏.毋是集物件就毋著(集物件)
		if len(集物件.內底組) == 0:
			raise 解析錯誤('內底組是空的！！')
		if len(集物件.內底組) > 1:
			raise 解析錯誤('內底組毋焦一个！！{0}'.format(str(集物件)))
		return self.看組物件音(集物件.內底組[0], 物件分字符號, 物件分詞符號)

	def 看句物件音(self, 句物件, 物件分字符號=分字符號, 物件分詞符號=分詞符號):
		self._掠漏.毋是句物件就毋著(句物件)
		集的音 = []
		for 一集 in 句物件.內底集:
			音標 = self.看集物件音(一集, 物件分字符號, 物件分詞符號)
			if 音標 != 無音:
				集的音.append(音標)
		return 物件分詞符號.join(集的音)

	def 看章物件音(self, 章物件, 物件分字符號=分字符號, 物件分詞符號=分詞符號):
		self._掠漏.毋是章物件就毋著(章物件)
		句的音 = []
		for 一句 in 章物件.內底句:
			音標 = self.看句物件音(一句, 物件分字符號, 物件分詞符號)
			if 音標 != 無音:
				句的音.append(音標)
		return 物件分詞符號.join(句的音)


	def 看字物件斷詞(self, 字物件, 物件分型音符號=分型音符號, 物件分字符號=分字符號, 物件分詞符號=分詞符號):
		self._掠漏.毋是字物件就毋著(字物件)
		if 字物件.音 == 無音:
			return self.看字物件型(字物件, 物件分字符號, 物件分詞符號)
		return self.看字物件型(字物件, 物件分字符號, 物件分詞符號) + 物件分型音符號\
			+ self.看字物件音(字物件, 物件分字符號, 物件分詞符號)

	def 看詞物件斷詞(self, 詞物件, 物件分型音符號=分型音符號, 物件分字符號=分字符號, 物件分詞符號=分詞符號):
		self._掠漏.毋是詞物件就毋著(詞物件)
		字的音 = self._提著詞物件的字物件音陣列(詞物件, 物件分字符號, 物件分詞符號)
		無音數量 = 0
		for 音 in 字的音:
			if 音 == 無音:
				無音數量 += 1
		if 無音數量 == len(字的音):
			return self.看詞物件型(詞物件, 物件分字符號, 物件分詞符號)
		if 無音數量 == 0:
			return self.看詞物件型(詞物件, 物件分字符號, 物件分詞符號) + 物件分型音符號\
				+ self.看詞物件音(詞物件, 物件分字符號, 物件分詞符號)
		raise 解析錯誤('詞內底有的字有音，有的字無音')

	def 看組物件斷詞(self, 組物件, 物件分型音符號=分型音符號, 物件分字符號=分字符號, 物件分詞符號=分詞符號):
		self._掠漏.毋是組物件就毋著(組物件)
		詞的音 = []
		for 一詞 in 組物件.內底詞:
			音標 = self.看詞物件斷詞(一詞, 物件分型音符號, 物件分字符號, 物件分詞符號)
			if 音標 != '':
				詞的音.append(音標)
		return 物件分詞符號.join(詞的音)

	def 看集物件斷詞(self, 集物件, 物件分型音符號=分型音符號, 物件分字符號=分字符號, 物件分詞符號=分詞符號):
		self._掠漏.毋是集物件就毋著(集物件)
		if len(集物件.內底組) == 0:
			raise 解析錯誤('內底組是空的！！')
		if len(集物件.內底組) > 1:
			raise 解析錯誤('內底組毋焦一个！！{0}'.format(str(集物件)))
		return self.看組物件斷詞(集物件.內底組[0], 物件分型音符號, 物件分字符號, 物件分詞符號)

	def 看句物件斷詞(self, 句物件, 物件分型音符號=分型音符號, 物件分字符號=分字符號, 物件分詞符號=分詞符號):
		self._掠漏.毋是句物件就毋著(句物件)
		集的音 = []
		for 一集 in 句物件.內底集:
			音標 = self.看集物件斷詞(一集, 物件分型音符號, 物件分字符號, 物件分詞符號)
			if 音標 != 無音:
				集的音.append(音標)
		return 物件分詞符號.join(集的音)

	def 看章物件斷詞(self, 章物件, 物件分型音符號=分型音符號, 物件分字符號=分字符號, 物件分詞符號=分詞符號):
		self._掠漏.毋是章物件就毋著(章物件)
		句的音 = []
		for 一句 in 章物件.內底句:
			音標 = self.看句物件斷詞(一句, 物件分型音符號, 物件分字符號, 物件分詞符號)
			if 音標 != 無音:
				句的音.append(音標)
		return 物件分詞符號.join(句的音)
