import pandas as pd
import numpy as np

np.set_printoptions(threshold=np.inf,linewidth=np.inf)

xlsx = pd.read_csv('C:/Users/mdc_int_94/Desktop/11.csv')
#print(xlsx.info())
#

df = pd.DataFrame(xlsx)
columns = df.columns
#print(columns)
#print(len(df.columns))
columns_count = int((len(columns)-7)/13)
#print(columns_count)
#print(df.loc[0])
#print(df.iloc[:,0:2]) #행과 열로 출력

df_main_body = df.iloc[:,0:20].copy()
year = df_main_body['Unnamed: 7'][0]  # 행당 년도 추출
print(df_main_body)
for i in df_main_body: #데이터 컬럼명 변경
    #print(dataframe[i][1])
    df_main_body.rename(columns={i:df_main_body[i][1]},inplace=True)
    #print(i,dataframe[i][1])

df_main_body.insert(2,'년',year+'년',True) #년도 관련 열 생성
df_main_body = df_main_body.drop(index=[0,1],axis=0) # 데이터프레임 행 삭제
df_main_body = df_main_body.reset_index(drop=True) #인덱스 초기화
print(df_main_body)

#print(df.iloc[:,7:20])

for i in range(1,columns_count):
    df_input = df.iloc[:, 0:7].copy()
    a = df.iloc[:,7+(i*13):20+i*13]
    #print(a)
    #b = df_main_body
    #print(b)
    #print(len(b))
    #print(len(a['Unnamed: 20'].tolist()))
    #df_main_body['sss'] = a['Unnamed: 20'].tolist()
    year = a.iloc[0,0]
    print(year)
    print(df_input)
    for k in a:
        #print(a[i].tolist())
        #print(type(i),i)
        df_input[k] = a[k].tolist()

    for j in df_input:  # 데이터 컬럼명 변경
        df_input.rename(columns={j: df_input[j][1]}, inplace=True)
    df_input.insert(2, '년', year+'년', True)  # 년도 관련 열 생성
    df_input = df_input.drop(index=[0, 1], axis=0)  # 데이터프레임 행 삭제
    df_input = df_input.reset_index(drop=True)  # 인덱스 초기화

    df_main_body = pd.concat([df_main_body,df_input])
    df_main_body = df_main_body.reset_index(drop=True)  # 인덱스 초기화

    print(df_main_body)

df_main_body.to_csv('C:/Users/mdc_int_94/Desktop/file.csv',encoding='utf-8-sig')

print(df_main_body['주변분기점'])

'''
dataframe = pd.DataFrame(xlsx)
print(dataframe)
year = dataframe['Unnamed: 7'][0] #행당 년도 추출
print(year)
for i in dataframe: #데이터 컬럼명 변경
    #print(dataframe[i][1])
    dataframe.rename(columns={i:dataframe[i][1]},inplace=True)
    #print(i,dataframe[i][1])

dataframe.insert(2,'년',year,True) #년도 관련 열 생성
dataframe = dataframe.drop(index=[0,1],axis=0) # 데이터프레임 행 삭제

dataframe = dataframe.reset_index(drop=True) #인덱스 초기화

print(dataframe)
'''


