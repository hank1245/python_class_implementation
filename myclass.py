class MyClass:
    count = 0

    def __init__(self, id):
        self.id = id
        MyClass.count += 1
        self.wordDict = {}

    def getId(self):
        return self.id

    def setId(self, id):
        if type(id) == int or type(id) == float:
            self.id = "XXXX"
        else:
            self.id = id

    def getNumberOfObject(self):
        return MyClass.count

    def storeWordlistAsDictionary(self, wordlist):
        sortedList = sorted(wordlist)
        # 횟수를 세어서 저장한다
        # for문으로 wordlist돌면서 dict에 저장하고 또 나오면 +1값 저장
        for word in sortedList:
            words = self.wordDict.keys()
            if word not in words:
                self.wordDict[word] = 1
            else:
                self.wordDict[word] += 1
        return self.wordDict

    def getWordCount(self, word):
        for key, value in self.wordDict.items():
            if key == word:
                return (key, value)
            else:
                return False

    def getWordList(self):
        wordlist = self.wordDict.keys()
        if len(wordlist) != 0:
            return sorted(wordlist)
        else:
            return False


class MyDerivedClass(MyClass):
    # 상속할때 super하고 별거없으면 init 안해도 되는건지? super도 의미없는건지?
    def __init__(self, id):
        super().__init__(id)
        if not id:
            self.id = "****"

    def __str__(self):
        result = "<"
        for key in self.wordDict.keys():
            result += str(key) + ","
        if len(result) > 1:
            result = result[: len(result) - 1]
        result += ">"
        return result

    def __gt__(self, obj):
        keyNumber = len(self.wordDict.keys())
        if keyNumber > len(obj.keys()):
            return True
        else:
            return False

    # __gt__ __add__등이 파이선에서의 연산자 오버로딩하는 방법이다
    def __add__(self, obj):
        tmp = {}
        for key, value in self.wordDict.items():
            tmp[key] = value
        keys = tmp.keys()
        for key, value in obj.items():
            if key in keys:
                tmp[key] += value
            else:
                tmp[key] = value
        newObj = MyDerivedClass(self.id)
        newObj.wordDict = tmp
        return newObj


me = MyClass("hank")
me.setId(123.342)
print(me.getId())
print(me.storeWordlistAsDictionary(["a", "a", "b", "c", "d", "d"]))
print(me.getWordCount("a"))
derived = MyDerivedClass("kim")
derived.storeWordlistAsDictionary(["a", "a", "b", "c", "d", "d"])
print(derived)
