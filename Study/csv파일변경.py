import pandas as pd
from sklearn.preprocessing import LabelEncoder

#csv 파일 읽기
df = pd.read_csv('raw_2_1.csv')

#컬럼명 user_id 데이터를 list로 변경
str_id = df['user_id'].tolist()

#라벨인코딩
encoder = LabelEncoder()
encoder.fit(str_id)
labels = encoder.transform(str_id)

#라벨인코딩 데이터 사입
df['user_id'] = labels
print(labels)
print(len(labels))

#tmp list로 만들어서 사입하는것이 빠르다
tmp = []
for i in df['user_id'].values:
    tmp.append('user_' + str(i))
df['user_id'] = tmp
print(df['user_id'])


#컬럼명 변경
df = df.rename(columns={'user_id': 'std_user_id'})

input_ = []

#df DataFrame의 컬럼명
col = df.columns
for i in range(0, 355000):
    a = []
    a.append('user_' + str(i))
    a.append(df['jbcl_nm'][int(i % len(df))])
    a.append(df['use_intt_id'][int(i % len(df))])

    input_.append(a)

#df_input DataFrame 생성
df_input = pd.DataFrame(input_, columns=col)
#pandas의 concat을 통해 DataFrame 합치기
df = pd.concat([df, df_input])
#DataFrame 중복제거
df = df.drop_duplicates()
#DataFrame의 sample을 통해 셈플 섞기, index 초기화 진행
df = df.sample(frac=1).reset_index(drop=True)
# df = df.reset_index(drop=True)


df.to_csv('zzz.csv', index=False, encoding='utf-8-sig')