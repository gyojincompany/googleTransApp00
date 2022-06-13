import pprint

import googletrans

trans = googletrans.Translator()
str1 = "나는 한국인 입니다"
str2 = "I love Korea"

pprint.pprint(googletrans.LANGUAGES) # 번역 언어 ticker 불러오기

result1 = trans.translate(str1, dest='en')
result2 = trans.translate(str2, dest='ko')
result3 = trans.translate(str2, dest='ja')

print(f"번역 결과1 : {result1.text}")
print(f"번역 결과2 : {result2.text}")
print(f"번역 결과3 : {result3.text}")
