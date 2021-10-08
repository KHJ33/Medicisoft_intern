import pandas as pd
import re

# from konlpy.tag import Twitter
# from pyjosa.josa import Josa

df = pd.read_csv('lon_srvc_ptnt.csv')
total_list = []

for i in range(len(df)):
    list = df.iloc[i, :].values
    tmp = ''

    for k in list:
        k = k.replace(',', '')
        # print(k)
        tmp += k + ' '

    # print(tmp)
    tmp = re.sub('(에게서)?(만치)?(만큼)?(처럼)?(같이)?(부터)?(한테)?(에게)?(께서)?(되는)?(하는)?([고과도랑써로께서가된와형에의이은를것상는을])?\s', ' ', tmp)
    input_list = tmp.split()
    # print(input_list)

    dict = {}

    for k in input_list:
        # k = k.replace('이', "").replace('의', "").replace('은', "").replace('을', "").replace('것', "").replace('상', "").replace('자', "").replace('각', "").replace('하는', "").replace('와', "").replace('된', "").replace('는', "").replace('시키', "")
        if k in dict:
            dict[k] += 1
        else:
            dict[k] = 1

    keyList = dict.keys()

    tmp = '#'
    for k in keyList:
        if dict[k] >= 2:
            if len(tmp) == 1:
                tmp += k
            else:
                tmp += ' #' + k
    # print(tmp)
    total_list.append(tmp)

# print(total_list)

df['biz_srvc_tag'] = total_list
# df