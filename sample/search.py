"""
맞는글자 검색
초성 혹은 글자를 입력하시오
"""

import hangul.sentence as hs

data = [
    "사과", "바나나", "포도", "수박", "복숭아",
    "딸기", "참외", "오렌지", "자두", "망고",
    "감", "배", "무화과", "코코넛", "체리",
    "레몬", "라임", "파인애플", "블루베리",
    "라즈베리", "크랜베리", "구아바", "아보카도", "키위",
    "대추", "석류", "용과", "두리안", "피타야",
    "호박", "고구마", "감자", "양파", "마늘",
    "당근", "시금치", "배추", "상추", "미나리",
    "브로콜리", "파프리카", "토마토", "오이", "애호박",
    "무", "파", "고추", "피망", "콩나물",
    "녹두", "강낭콩", "팥", "밤", "도토리",
    "호두", "땅콩", "아몬드", "잣", "참깨",
    "들깨", "쌀", "보리", "밀", "옥수수",
    "귤", "자몽", "복분자", "살구", "야자",
    "푸른자몽", "아세로라", "카카오", "코코아", "패션프루트",
    "잎새버섯", "표고버섯", "새송이버섯", "양송이버섯", "능이버섯"
]

match = []

while True:
    match = []
    x = input()

    for i in data:
        hgs = hs.HangulSentence(i, True)
        if hgs.chosungmatch(x):
            match.append(i)
        elif hgs.match(x):
            match.append(i)

    if len(match) == 0:
        print("결과가 없습니다.\n")
    else:
        print(f"{len(match)}개의 결과가 있습니다.")
        print(", ".join(match), end="\n\n")




