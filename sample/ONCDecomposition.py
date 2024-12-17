"""
초성 중성 종성 분할
분해할 한글을 넣으시오
"""

import hangul.char as hc

while True:
    x = input()
    h = hc.Hangul(x)
    print(f"초성:{h.chosung}")
    print(f"중성:{h.jungsung}")
    print(f"종성:{h.jongsung}")
