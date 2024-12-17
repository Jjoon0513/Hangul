class Hangul:
    def __init__(self, koreanchar: str):
        if len(koreanchar) != 1:
            raise IsNotCharOfHangul

        decomposed = hangul_decompose(koreanchar)
        if decomposed is None:
            raise IsNotHangul(koreanchar)

        self.__koreanchar = koreanchar
        self.chosung = decomposed[0]
        self.jungsung = decomposed[1]
        self.jongsung = decomposed[2]

    def ischosung(self, chosung: str):
        return self.chosung == chosung

    def dic(self):
        return self.chosung, self.jungsung, self.jongsung

    def __str__(self):
        return  self.__koreanchar

    def __repr__(self):
        return self.__koreanchar


def hangul_decompose(char):
    """
    한글 한 문자를 초성, 중성, 종성으로 분리합니다.
    """
    # 한글 유니코드 범위
    start = 0xAC00  # '가'
    end = 0xD7A3  # '힣'
    chosung = [
        "ㄱ", "ㄲ", "ㄴ", "ㄷ", "ㄸ", "ㄹ", "ㅁ", "ㅂ", "ㅃ",
        "ㅅ", "ㅆ", "ㅇ", "ㅈ", "ㅉ", "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅎ"
    ]
    jungsung = [
        "ㅏ", "ㅐ", "ㅑ", "ㅒ", "ㅓ", "ㅔ", "ㅕ", "ㅖ",
        "ㅗ", "ㅘ", "ㅙ", "ㅚ", "ㅛ", "ㅜ", "ㅝ", "ㅞ",
        "ㅟ", "ㅠ", "ㅡ", "ㅢ", "ㅣ"
    ]
    jongsung = [
        "", "ㄱ", "ㄲ", "ㄳ", "ㄴ", "ㄵ", "ㄶ", "ㄷ",
        "ㄹ", "ㄺ", "ㄻ", "ㄼ", "ㄽ", "ㄾ", "ㄿ", "ㅀ",
        "ㅁ", "ㅂ", "ㅄ", "ㅅ", "ㅆ", "ㅇ", "ㅈ", "ㅊ",
        "ㅋ", "ㅌ", "ㅍ", "ㅎ"
    ]
    try:
        code = ord(char)
    except:
        raise IsNotHangul(char)
    if not (start <= code <= end):
        return None

    code -= start
    cho_idx = code // 588
    jung_idx = (code % 588) // 28
    jong_idx = code % 28

    return chosung[cho_idx], jungsung[jung_idx], jongsung[jong_idx]


class IsNotHangul(Exception):
    """
    완성된 한글(1자)가 아닐때 또는 한글이 아닐때 이 메시지가 표시됩니다
    """
    def __init__(self, char):
        super().__init__(f"{char} is not a complete 1 character or it is not Hangul")


class IsNotCharOfHangul(Exception):
    def __init__(self):
        super().__init__(f"The Hangul class only supports 1 character. For Hangul classes that are longer than 1 character, use HangulSentence.")