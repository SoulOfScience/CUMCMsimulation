import pandas as pd
import csv
import xlwt

# convert weather phenomenon to digits
def weather(string):
    if string == '晴':
        return 0
    elif string=='阴':
        return 1
    elif string=='多云':
        return 1
    elif string=='小雨':
        return 2
    elif string=='阵雨':
        return 2
    elif string=='中雨':
        return 3
    elif string== '雷阵雨':
        return 4
    elif string== '雨夹雪':
        return 5
    elif string== '暴雨':
        return 6
    elif string== '中雪':
        return 8
    elif string== '大雪':
        return 9
    elif string== '小到中雪':
        return 7
    elif string== '中到大雪':
        return 8
    elif string== '大到暴雪':
        return 10
    elif string== '扬沙':
        return 2
    elif string== '雾':
        return 2
    elif string== '沙尘暴':
        return 2
    elif string== '零散阵雨':
        return 3
    elif string== '零散雷雨':
        return 4
    elif string== '浮沙':
        return 1
    elif string== '冻雨':
        return 5
    elif string== '小雨-中雨':
        return 4
    elif string== '中雨-大雨':
        return 5
    elif string== '小到中雨':
        return 4
    elif string== '中到大雨':
        return 5
    elif string== '大到暴雨':
        return 6
    elif string== '暴雨到大暴雨':
        return 7
    elif string== '大暴雨到特大暴雨':
        return 8
    elif string== '薄雾':
        return 0
    elif string== '局部多云':
        return 1
    elif string== '少云':
        return 0
    elif string== '刮风':
        return 1
    elif string == '雷阵雨':
        return 5
    elif string == '雷阵雨伴有冰雹':
        return 8
    elif string == '中度霾':
        return 2
    elif string == '重度霾':
        return 3
    elif string == '晴间多云':
        return 0
    else:
        return -1

file_path = r'D:\ACodeBox\python\数学建模国赛模拟\weather.xlsx'
data = pd.read_excel(file_path)
data[u'weatherphenomenon'] = data[u'weatherphenomenon'].astype(str)
result = []
book = xlwt.Workbook()
sheet1 = book.add_sheet(u'weatherphenomenon',cell_overwrite_ok=True)
i = 0

for da in data[u'weatherphenomenon']:
    first = da.split('/')[0].split(' ')[0]
    second = da.split('/')[1]
    result = weather(first)+weather(second)
    sheet1.write(i,1,result)
    i+=1
    #print(weather(first)+weather(second))

book.save(r'D:\ACodeBox\python\数学建模国赛模拟\weatherphenomenon.xls')
print("Success")