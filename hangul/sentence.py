from . import Hangul

class HangulSentence:
    def __init__(self, word: str, savechosung: bool = False):
        self.word = word
        self.ischosungsaved = savechosung
        self.chosung = [] if savechosung else None
        self.wordchars = []

        for char in word:
            try:
                hangul_char = Hangul(char)
                self.wordchars.append(hangul_char)
                if savechosung:
                    self.chosung.append(hangul_char.chosung)
            except Exception:
                self.wordchars.append(char)

    def match(self, text: str) -> bool:
        return text in self.word

    def perfectmatch(self, text: str) -> bool:
        return text == self.word


    def perfectchosungmatch(self, chosung: str) -> bool:
        """
        입력된 초성 문자열이 주어진 문장 초성과 완전히 일치하는지 확인.
        """
        return self.chosung == list(chosung)

    def chosungmatch(self, chosung: str) -> bool:
        """
        입력된 초성 문자열이 주어진 문장 초성과 완전히 일치하는지 확인.
        """
        return ''.join(list(chosung)) in ''.join(self.chosung)




    def returnhangul(self):
        return [char.dic() for char in self.wordchars]

    def __repr__(self) -> str:
        return "".join([str(char) for char in self.wordchars])

    def __str__(self):
        return "".join([str(char) for char in self.wordchars])

    def add(self, sentence:str):

        for char in sentence:
            try:
                self.wordchars.append(Hangul(char))
            except:
                self.wordchars.append(char)

    def addjosa(self, josa:str):
        """
        조사를 추가해줍니다.
        아래는 추가할수있는 조사입니다.

        *보조사*
        - -이
        - -을
        - -은

        *접속조사*
        - -와

        서술격 조사
        - -다

        :param josa: 조사입니다 **-이, -을** 등을 사용할수 있습니다.

        :return:
        """
        hasjongsunginkor = ["r", "t", "p", "g", "l", "c", "b", "n", "m", "R", "L", "N", "M"]

        if josa in ["-이", "-와", "-을", "-은", "-다"]:
            try:
                # 마지막 문자 가져오기
                last_char = self.wordchars[-1]

                # 문자열 변환 (Hangul 객체가 아닐 경우 대비)
                last_char_str = str(last_char) if isinstance(last_char, Hangul) else last_char

                if not isinstance(last_char, Hangul) and last_char_str in hasjongsunginkor:
                    if josa == "-이":
                        self.wordchars.append(Hangul("이"))
                    elif josa == "-와":
                        self.wordchars.append(Hangul("과"))
                    elif josa == "-을":
                        self.wordchars.append(Hangul("을"))
                    elif josa == "-은":
                        self.wordchars.append(Hangul("은"))
                    elif josa == "-다":
                        self.wordchars.append(Hangul("이"))
                        self.wordchars.append(Hangul("다"))
                elif not isinstance(last_char, Hangul) and last_char_str not in hasjongsunginkor:
                    if josa == "-이":
                        self.wordchars.append(Hangul("가"))
                    elif josa == "-와":
                        self.wordchars.append(Hangul("와"))
                    elif josa == "-을":
                        self.wordchars.append(Hangul("를"))
                    elif josa == "-은":
                        self.wordchars.append(Hangul("는"))
                    elif josa == "-다":
                        self.wordchars.append(Hangul("다"))
                elif isinstance(last_char, Hangul) and last_char.jongsung == "":
                    if josa == "-이":
                        self.wordchars.append(Hangul("가"))
                    elif josa == "-와":
                        self.wordchars.append(Hangul("와"))
                    elif josa == "-을":
                        self.wordchars.append(Hangul("를"))
                    elif josa == "-은":
                        self.wordchars.append(Hangul("는"))
                    elif josa == "-다":
                        self.wordchars.append(Hangul("다"))
                else:
                    if josa == "-이":
                        self.wordchars.append(Hangul("이"))
                    elif josa == "-와":
                        self.wordchars.append(Hangul("과"))
                    elif josa == "-을":
                        self.wordchars.append(Hangul("을"))
                    elif josa == "-은":
                        self.wordchars.append(Hangul("은"))
                    elif josa == "-다":
                        self.wordchars.append(Hangul("이"))
                        self.wordchars.append(Hangul("다"))
            except Exception as e:
                # 디버깅을 위해 예외 메시지 추가
                print(f"Error processing josa '{josa}' with last_char '{last_char}': {e}")
                raise LastCharactorError from e
        else:
            raise UndefinedJosa(josa)

        self.wordchars.append(" ")

        return "".join([str(char) for char in self.wordchars])



class LastCharactorError(Exception):
    """
    마지막 글자가 완벽한 한국어가 아니거나 한국어가 아닙니다.
    """
    def __init__(self):
        super().__init__(f"The last charactor is not perfect Korean or it is not Korean")

class UndefinedJosa(Exception):
    """
    정의되지않은 조사입니다
    """
    def __init__(self, josa):
        super().__init__(f"{josa} is undefined Josa")

"""
나영이 보고싶다
"""