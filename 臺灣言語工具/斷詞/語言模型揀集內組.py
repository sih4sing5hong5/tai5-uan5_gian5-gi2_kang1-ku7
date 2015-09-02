# -*- coding: utf-8 -*-
from 臺灣言語工具.基本元素.字 import 字
from 臺灣言語工具.基本元素.詞 import 詞
from 臺灣言語工具.基本元素.組 import 組
from 臺灣言語工具.基本元素.集 import 集
from 臺灣言語工具.基本元素.句 import 句
from 臺灣言語工具.基本元素.章 import 章
from 臺灣言語工具.解析整理.解析錯誤 import 解析錯誤
from 臺灣言語工具.解析整理.詞物件網仔 import 詞物件網仔
from 臺灣言語工具.解析整理.程式掠漏 import 程式掠漏
from 臺灣言語工具.解析整理.物件譀鏡 import 物件譀鏡
from 臺灣言語工具.基本元素.公用變數 import 分詞符號


class 語言模型揀集內組:
    _掠漏 = 程式掠漏()
    _網仔 = 詞物件網仔()
    _譀鏡 = 物件譀鏡()

    def 揀(self, 語言模型, 物件):
        if isinstance(物件, 字) or isinstance(物件, 詞) or isinstance(物件, 組):
            return self._揀字詞組物件音(語言模型, 物件)
        if isinstance(物件, 集):
            句物件 = 句()
            句物件.內底集.append(物件)
            標好句物件, 上好分數, 詞數 = self._揀句物件音(語言模型, 句物件)
            return (標好句物件.內底集[0], 上好分數, 詞數)
        if isinstance(物件, 句):
            return self._揀句物件音(語言模型, 物件)
        if isinstance(物件, 章):
            return self._揀章物件音(語言模型, 物件)
        self._掠漏.毋是字詞組集句章的毋著(物件)

    def _揀字詞組物件音(self, 語言模型, 物件):
        評分結果 = list(語言模型.評分(物件))
        return (物件, sum(評分結果), len(評分結果) + 1)

    def _揀章物件音(self, 語言模型, 章物件):
        標好章物件 = 章()
        總分 = 0
        總詞數 = 0
        for 句物件 in 章物件.內底句:
            標好句物件, 分數, 詞數 = self._揀句物件音(語言模型, 句物件)
            標好章物件.內底句.append(標好句物件)
            總分 += 分數
            總詞數 += 詞數
        return (標好章物件, 總分, 總詞數)

    def _揀句物件音(self, 語言模型, 句物件):
        開始組 = 組([語言模型.開始()])
        全部分數佮來源 = [{(開始組,): (0, 0, None)}]
        if len(句物件.內底集) == 0:
            分數, 詞數, 來源 = 全部分數佮來源[-1][(開始組,)]
            算的分數, 算的詞數 = self._算上尾組物件分數(語言模型, (開始組, 組()), True)
            這馬詞數 = 詞數 + 算的詞數
            這馬分數 = 分數 + 算的分數
            return (句物件, 這馬分數, 這馬詞數 + 1)
        for 這馬集物件 in 句物件.內底集:
            頂一个狀態 = 全部分數佮來源[-1].items()
            愛揣的組合 = sorted(頂一个狀態, key=str)
            這格分數佮來源 = {}
            for 組合, 分數佮來源 in 愛揣的組合:
                分數, 詞數, 來源 = 分數佮來源
                if len(這馬集物件.內底組) == 0:
                    raise 解析錯誤('有空的集物件：{0}'.format(句物件))
                for 選擇組物件 in 這馬集物件.內底組:
                    if 語言模型.上濟詞數() == 1:
                        這馬組合 = (選擇組物件,)
                    else:
                        這馬組合 = (組合 + (選擇組物件,))[-語言模型.上濟詞數():]
                    算的分數, 算的詞數 = self._算上尾組物件分數(語言模型, 這馬組合,
                                                len(全部分數佮來源) == len(句物件.內底集))
                    這馬詞數 = 詞數 + 算的詞數
                    這馬分數 = 分數 + 算的分數
                    if 這馬組合 not in 這格分數佮來源:
                        這格分數佮來源[這馬組合] = (這馬分數, 這馬詞數, 組合)
                    elif 這馬分數 > 這格分數佮來源[這馬組合][0]:
                        這格分數佮來源[這馬組合] = (這馬分數, 這馬詞數, 組合)
            全部分數佮來源.append(這格分數佮來源)
        結果集陣列 = []
        這馬組合 = None
        上好分數 = None
        結果詞數 = None
# 		print('全部分數佮來源[-1]',全部分數佮來源[-1])
        for 組合, 分數佮來源 in 全部分數佮來源[-1].items():
            分數, 詞數, 來源 = 分數佮來源
            if 這馬組合 is None or 分數 > 上好分數:
                這馬組合 = 組合
                上好分數 = 分數
                結果詞數 = 詞數
        for 這格分數佮來源 in 全部分數佮來源[:0:-1]:
            集物件 = 集()
            # 物件內底毋是空的
# 			if 這馬組合!=None:
            集物件.內底組.append(這馬組合[-1])
            結果集陣列.append(集物件)
            分數, 詞數, 來源 = 這格分數佮來源[這馬組合]
# 			print(結果集陣列[-1],分數,詞數)
            這馬組合 = 來源
        句物件 = 句()
        句物件.內底集 = 結果集陣列[::-1]
        return (句物件, 上好分數, 結果詞數 + 1)

    def _揀懸分出來(self, 組合和分數佮來源):
        組合, 分數佮來源 = 組合和分數佮來源
        分數, 詞數 = 分數佮來源[:2]
        字串 = []
        for 一个詞 in 組合:
            字串.append(self._譀鏡.看分詞(一个詞))
        return (-分數, 詞數, 分詞符號.join(字串))

    def _算上尾組物件分數(self, 語言模型, 組陣列, 是毋是上尾一个):
        '會當對陣列接起來最佳化'
# 		print('_算上尾組物件分數(self', 語言模型, 組陣列, 是毋是上尾一个)
        頭前詞陣列 = []
        for 組物件 in 組陣列[-2::-1]:
            頭前詞陣列 = 組物件.內底詞 + 頭前詞陣列
            if len(頭前詞陣列) >= 語言模型.上濟詞數():
                頭前詞陣列 = 頭前詞陣列[-語言模型.上濟詞數():]
                break
        評分詞陣列 = 頭前詞陣列 + 組陣列[-1].內底詞
        if 是毋是上尾一个:
            評分詞陣列.append(語言模型.結束())
        評分結果 = 語言模型.評詞陣列分(
            評分詞陣列,
            len(頭前詞陣列)
        )
        分數 = sum(評分結果)
# 		print('評分詞陣列',評分詞陣列,評分結果)
        return 分數, len(評分詞陣列) - len(頭前詞陣列)
