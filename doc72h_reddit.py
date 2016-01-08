#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime

'''
「横浜 オールナイトでとんかつを」

横浜にある24時間営業のとんかつ屋が舞台。 # これは写真の説明なのでいらない
日本有数の歓楽街の一角にある。             # これも
早朝や深夜、肉をほおばりにくる人々。      # これも
横浜の歓楽街にある24時間営業のとんかつ屋が舞台。早朝から深夜まで、さまざまな人が肉をほおばりにやってくる。精をつけてネオン街に向かうという男性。飲みの締めにきたキャバクラ嬢。徹夜仕事を終え、明け方ひと息つく男性の姿もある。マンションの高騰や大企業の利益増加など派手なニュースも飛び交った2015年。人々はどんな年の瀬を迎えているのか。不夜城のとんかつ屋で3日間、悲喜こもごもの人間模様を見つめた。

【語り】市川実日子
'''

'''
NHK - ドキュメント72時間「横浜 オールナイトでとんかつを」1月8日(金曜) 22:55 #72時間

> 横浜の歓楽街にある24時間営業のとんかつ屋が舞台。早朝から深夜まで、さまざまな人が肉をほおばりにやってくる。精をつけてネオン街に向かうという男性。飲みの締めにきたキャバクラ嬢。徹夜仕事を終え、明け方ひと息つく男性の姿もある。マンションの高騰や大企業の利益増加など派手なニュースも飛び交った2015年。人々はどんな年の瀬を迎えているのか。不夜城のとんかつ屋で3日間、悲喜こもごもの人間模様を見つめた。
>
> 【語り】市川実日子

http://www4.nhk.or.jp/72hours/
'''

data = []
print '「から】語り〜〜〜〜までコピペしたあと改行して done: '
while True:
    line = raw_input()
    if line == 'done':
        break
    data.append(line)

description = ''
for line in data:
    if line.startswith('「') and line.endswith('」'):
        title = line
    elif line.startswith('【語り】'):
        narrator = line
    else:
        if len(description) < len(line):
            description = line


today = datetime.date.today()
month = today.month
day = today.day
url = 'http://www4.nhk.or.jp/72hours/'

title_output = 'NHK - ドキュメント72時間{0}{1}月{2}日(金曜) 22:55 #72時間'.format(title, month, day)

print '-' * 64
print title_output
print '-' * 64
print '>', description
print '>'
print '>', narrator, '\n'
print url
print '-' * 64
