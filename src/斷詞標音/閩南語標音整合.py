
from 字詞組集句章.解析整理工具.拆文分析器 import 拆文分析器
from 字詞組集句章.解析整理工具.文章初胚工具 import 文章初胚工具
from 字詞組集句章.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音
from 斷詞標音.型音辭典 import 型音辭典
from 斷詞標音.動態規劃斷詞標音 import 動態規劃斷詞標音
from 斷詞標音.辭典條目 import 辭典條目

class 閩南語標音整合:
	腔口 = '漢語族閩方言閩南語偏漳優勢音'
	文讀層 = '文讀層'
	白話層 = '白話層'
	全部 = '全部'
	條目 = 辭典條目()
	初胚工具 = 文章初胚工具()
	分析器 = 拆文分析器()
	辭典 = None
	斷詞標音 = 動態規劃斷詞標音()
	def __init__(self, 腔口, 辭典):
		self.腔口 = 腔口
		self.文讀字 = set()
		[self.文讀字.add(字詞[0]) for 字詞 in self.條目.揣言語層的字詞(self.腔口, '文讀層')]
		self.白話字 = set()
		[self.白話字.add(字詞[0]) for 字詞 in self.條目.揣言語層的字詞(self.腔口, '白話層')]
		self.辭典 = 辭典(4)
		音標工具 = 臺灣閩南語羅馬字拼音
		for 流水號, 型體, 音標 in self.條目.揣腔口資料(腔口):
			處理過的音標 = self.初胚工具.建立物件語句前處理減號(音標工具, 音標)
			# 愛加詞組無
			組物件 = self.分析器.產生對齊組(型體, 處理過的音標)
			for 詞物件 in 組物件.內底詞:
				詞物件.屬性 = {}
				if 流水號 in self.文讀字:
					if self.文讀層 not in 詞物件.屬性:
						詞物件.屬性[self.文讀層] = 0
					詞物件.屬性[self.文讀層] += 1
				elif 流水號 in self.白話字:
					if self.白話層 not in 詞物件.屬性:
						詞物件.屬性[self.白話層] = 0
					詞物件.屬性[self.白話層] += 1
				self.辭典.加詞(詞物件)
				
	def 產生標音結果(self, 語句, 語言層):
		章物件 = self.分析器.建立章物件(語句)
		return self.斷詞標音.斷詞標音(self.辭典, 章物件)

if __name__ == '__main__':
	標音 = 閩南語標音整合('漢語族閩方言閩南語偏漳腔', 型音辭典)
	音 = 標音.產生標音結果('台語字', 標音.文讀層)
	print(音)
	音 = 標音.產生標音結果('台語字', 標音.白話層)
	print(音)
	音 = 標音.產生標音結果('台語字', 標音.全部)
	print(音)
	音 = 標音.產生標音結果('白日依山盡', 標音.文讀層)
	print(音)
	音 = 標音.產生標音結果('點仔膠', 標音.文讀層)
	print(音)
	音 = 標音.產生標音結果('好好鱟刣甲屎那流。', 標音.文讀層)
	print(音)
	音 = 標音.產生標音結果('好好鱟刣甲屎那流,', 標音.文讀層)
	print(音)
	音 = 標音.產生標音結果('好好鱟,刣甲屎那流', 標音.白話層)
	print(音)

