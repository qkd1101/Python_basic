class sub : 
    def __init__(self, kor,eng,mat) :
        self.__kor = kor
        self.__eng = eng
        self.__mat = mat

    @property
    def kor(self) :
        return self.__kor
    
    @property
    def eng(self) :
        return self.__eng

    @property
    def mat(self) :
        return self.__mat

    def total_score(self) :
        return self.__kor + self.__eng + self.__mat

input_str = list(map(int,input().split()))
socre = sub(input_str[0],input_str[1],input_str[2])
print(socre.total_score())
