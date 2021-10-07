import pandas as pd

# 상시교통량 홈페이지에서 받아온 엑셀 파일을 읽어 옵니다.
xlsx = pd.read_csv('C:/Users/mdc_int_94/Desktop/교통량.csv')
df = pd.DataFrame(xlsx)

# 컬럼의 종류를 확인합니다.
columns = df.columns

# 검색할 지점 번호
number = '3727-00'
# content :구분의 컬럼수 ex) 지점번호,호선명,월,일,방향,행정구역,주변분기점 으로 총 7개의 컬럼은 동일합니다.
content = 6
# feature : 해당 년도의 값 ex)1종,2종,3,종,...12종,전차종합계로 총 13개의 차종별 수치 데이터입니다.
feature = 13

# 선택 년도의 수를 count 해줍니다.
year_count = int((len(columns) - content) / feature)

# 구분 데이터 컬럼만 추출합니다.
df_main_body = df.iloc[:, 0:content + feature].copy()

# 초기 해당년도를 추출합니다.
year = df_main_body['Unnamed: ' + str(content)][0]  # 행당 년도 추출

# 데이터 컬럼명 변경
for i in df_main_body:
    df_main_body.rename(columns={i: df_main_body[i][1]}, inplace=True)

# 년도 관련 컬럼 생성
df_main_body.insert(2, '년', year + '년', True)

# 불필요한 row data를 삭제합니다.
df_main_body = df_main_body.drop(index=[0, 1], axis=0)

# 인덱스 초기화
df_main_body = df_main_body.reset_index(drop=True)

# 총 년수만큼 반복문을 돌립니다.
for i in range(1, year_count):

    # 공통 컬럼인 구분 컬럼 추출(지점번호, 호선명... 주변분기점까지 추출합니다.)
    df_input = df.iloc[:, 0:content].copy()

    # 년도에 해당 데이터 추출
    a = df.iloc[:, content + (i * feature):content + feature + (i * feature)]
    year = a.iloc[0, 0]

    # 추출한 a(1종,2종...전차종합계까지) 의 컬럼을 추가합니다.
    for k in a:
        df_input[k] = a[k].tolist()

    # 데이터 컬럼명 변경
    for j in df_input:
        df_input.rename(columns={j: df_input[j][1]}, inplace=True)

    # 년도 관련 열 생성
    df_input.insert(2, '년', year + '년', True)
    # 데이터프레임 행 삭제
    df_input = df_input.drop(index=[0, 1], axis=0)
    # 인덱스 초기화
    df_input = df_input.reset_index(drop=True)

    # 메인 data에 input data를 추가합니다.
    df_main_body = pd.concat([df_main_body, df_input])
    # 인덱스 초기화
    df_main_body = df_main_body.reset_index(drop=True)

# 가공한 데이터를 csv 파일로 저장합니다.
df_main_body.to_csv('C:/Users/mdc_int_94/Desktop/original.csv', encoding='utf-8-sig', date_format=None)

dict = {}
for i in df_main_body['지점번호']:
    dict[i[1:]] = 0
print(dict)
print(len(dict))

add_list = []
for i in range(len(df_main_body)):
    if df_main_body['지점번호'][i][1:] == number:
        add_list.append(df_main_body.iloc[i].tolist())

col = df_main_body.columns
extract_data = pd.DataFrame(add_list,columns = col)
extract_data.to_csv('C:/Users/mdc_int_94/Desktop/extract_data.csv',encoding='utf-8-sig',date_format= None)