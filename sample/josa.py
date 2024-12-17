"""
조사 테스트
입력에 명사를 넣으시오.
"""


import hangul.sentence as hs

josa = ["-이", "-와", "-을", "-은", "-다"]

while True:
    x = input()
    for i in josa:
        hsh = hs.HangulSentence(x)
        hsh.addjosa(i)
        print(hsh)