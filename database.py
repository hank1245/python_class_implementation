class Database:
    def __init__(self):
        self.customers = {}

    def registNewCustomer(self, id, name):
        if id in self.customers:
            return -1
        self.customers[id] = name
        tmp = dict({id: name})
        return tmp

    def getCustomerNumber(self):
        return len(self.customers)

    def getCustomerNameByID(self, id):
        if id in self.customers:
            return {id: self.customers[id]}
        return -1

    def getCustomerIDByName(self, name):
        tmp = {}
        keys = self.customers.keys()
        values = self.customers.values()
        if name not in values:
            return -1
        for key in keys:
            if self.customers[key] == name:
                tmp[key] = name
        return tmp

    def getAllCustomer(self):
        return self.customers

    def removeCustomerByID(self, id):
        if id not in self.customers:
            return -1
        self.customers.pop(id)
        return self.customers

    # self.customers 딕셔너리를 순회하면서 동시에 요소를 삭제하면 반복 중에 딕셔너리 크기가 변경되므로 RuntimeError가 발생합니다.
    # for key, value in self.customers:  딕셔너리를 직접 순회하면 키만 반환하게 됩니다. 키와 값 모두를 얻으려면 for key, value in self.customers.items():와 같이 .items()를 사용해야 합니다.
    def removeCustomerByName(self, name):
        keys = []
        count = 0
        for key, value in self.customers.items():
            if value == name:
                keys.append(key)
                count += 1
        if count != 0:
            for element in keys:
                self.customers.pop(element)
            return self.customers
        else:
            return -1

        return self.customers

    def getAllCustomerNameSorted(self):
        names = self.customers.values()
        # set을 먼저 하고 리스트로 바꾸고 sort해야함 순서 바뀔수잇다 set에서
        sortedNames = sorted(list(set(names)))
        return sortedNames

    def getAllCustomerIDSorted(self):
        ids = self.customers.keys()
        sortedIds = sorted(ids)
        return sortedIds

    def getDuplicatedCustomerNames(self):
        names = []
        duplicated = []
        for key, value in self.customers.items():
            if value not in names:
                names.append(value)
            else:
                duplicated.append(value)
        tmp = {}
        for key, value in self.customers.items():
            if value in duplicated:
                tmp[key] = value
        return tmp


# Scoring
score = 0

# problem 1
try:
    myDB = Database()

    solution = [True, True, True]
    answer = []

    res = myDB.registNewCustomer("0001", "Apple")
    if res == {"0001": "Apple"}:
        answer.append(True)

    res = myDB.registNewCustomer("0002", "Tomato")
    if res == {"0002": "Tomato"}:
        answer.append(True)

    res = myDB.registNewCustomer("0001", "Apple")
    if res == -1:
        answer.append(True)

    if answer == solution:
        score += 6
        print("[1] SUCCESS")
    else:
        print("[1] FAIL")
except:
    print("[1] FAIL")

# problem 2
try:
    solution = 3
    answer = 0

    myDB = Database()

    myDB.registNewCustomer("0001", "Apple")
    myDB.registNewCustomer("0002", "Tomato")
    myDB.registNewCustomer("0009", "Peach")

    answer = myDB.getCustomerNumber()
    # print(answer)

    if answer == solution:
        score += 6
        print("[2] SUCCESS")
    else:
        print("[2] FAIL")
except:
    print("[2] FAIL")

# problem 3
try:
    solution = {"0002": "Tomato"}
    answer = 0

    myDB = Database()

    myDB.registNewCustomer("0001", "Apple")
    myDB.registNewCustomer("0002", "Tomato")
    myDB.registNewCustomer("0009", "Peach")

    answer = myDB.getCustomerNameByID("0002")
    # print(answer)

    if answer == solution:
        answer = myDB.getCustomerNameByID("0010")
        if answer == -1:
            score += 6
            print("[3] SUCCESS")
        else:
            print("[3] FAIL")
    else:
        print("[3] FAIL")
except:
    print("[3] FAIL")


# problem 4
try:
    solution = {"0002": "Tomato", "0004": "Tomato"}
    answer = 0

    myDB = Database()

    myDB.registNewCustomer("0001", "Apple")
    myDB.registNewCustomer("0002", "Tomato")
    myDB.registNewCustomer("0004", "Tomato")
    myDB.registNewCustomer("0009", "Peach")

    answer = myDB.getCustomerIDByName("Tomato")
    # print(answer)

    if answer == solution:
        if myDB.getCustomerIDByName("XXX") == -1:
            score += 6
            print("[4] SUCCESS")
        else:
            print("[4] FAIL")
    else:
        print("[4] FAIL")
except:
    print("[4] FAIL")

# problem 5
try:
    solution = {"0001": "Apple", "0002": "Tomato", "0004": "Tomato", "0009": "Peach"}
    answer = 0

    myDB = Database()

    myDB.registNewCustomer("0001", "Apple")
    myDB.registNewCustomer("0002", "Tomato")
    myDB.registNewCustomer("0004", "Tomato")
    myDB.registNewCustomer("0009", "Peach")

    answer = myDB.getAllCustomer()
    # print(answer)

    if answer == solution:
        score += 6
        print("[5] SUCCESS")
    else:
        print("[5] FAIL")
except:
    print("[5] FAIL")

# problem 6
try:
    solution = {"0001": "Apple", "0002": "Tomato", "0004": "Tomato"}
    answer = 0

    myDB = Database()

    myDB.registNewCustomer("0001", "Apple")
    myDB.registNewCustomer("0002", "Tomato")
    myDB.registNewCustomer("0004", "Tomato")
    myDB.registNewCustomer("0009", "Peach")

    answer = myDB.removeCustomerByID("0009")
    # print(answer)

    if answer == solution:
        if myDB.removeCustomerByID("0009") == -1:
            score += 6
            print("[6] SUCCESS")
        else:
            print("[6] FAIL")
    else:
        print("[6] FAIL")
except:
    print("[6] FAIL")

# problem 7
try:
    solution = {"0001": "Apple", "0009": "Peach"}
    answer = 0

    myDB = Database()

    myDB.registNewCustomer("0001", "Apple")
    myDB.registNewCustomer("0002", "Tomato")
    myDB.registNewCustomer("0004", "Tomato")
    myDB.registNewCustomer("0009", "Peach")
    answer = myDB.removeCustomerByName("Tomato")
    print(answer)
    if answer == solution:
        if myDB.removeCustomerByName("Tomato") == -1:
            score += 6
            print("[7] SUCCESS")
        else:
            print("[7] FAIL")
    else:
        print("[7] FAIL")
except:
    print("[7] FAIL")

# problem 8
try:
    solution = ["Apple", "Peach", "Tomato"]
    answer = 0

    myDB = Database()

    myDB.registNewCustomer("0001", "Apple")
    myDB.registNewCustomer("0002", "Tomato")
    myDB.registNewCustomer("0004", "Tomato")
    myDB.registNewCustomer("0009", "Peach")

    answer = myDB.getAllCustomerNameSorted()
    # print(answer)

    if answer == solution:
        score += 6
        print("[8] SUCCESS")
    else:
        print("[8] FAIL")
except:
    print("[8] FAIL")

# problem 9
try:
    solution = ["0001", "0002", "0004", "0009"]
    answer = 0

    myDB = Database()

    myDB.registNewCustomer("0001", "Apple")
    myDB.registNewCustomer("0009", "Peach")
    myDB.registNewCustomer("0004", "Tomato")
    myDB.registNewCustomer("0002", "Tomato")

    answer = myDB.getAllCustomerIDSorted()
    # print(answer)

    if answer == solution:
        score += 6
        print("[9] SUCCESS")
    else:
        print("[9] FAIL")
except:
    print("[9] FAIL")

    # name이 dict에 있다면 그걸 삭제 for 문돌면서 value가 name이면 del
    # dict는 인덱스 접근 불가능하다 for문 돌릴때는 키값으로 돌린다
    # del d[key]로 삭제 가능하다

# problem 10
try:
    solution = {"0002": "Tomato", "0004": "Tomato", "0009": "Peach", "0008": "Peach"}
    answer = 0

    myDB = Database()

    myDB.registNewCustomer("0001", "Apple")
    myDB.registNewCustomer("0002", "Tomato")
    myDB.registNewCustomer("0004", "Tomato")
    myDB.registNewCustomer("0009", "Peach")
    myDB.registNewCustomer("0008", "Peach")

    answer = myDB.getDuplicatedCustomerNames()
    #  print(answer)

    if answer == solution:
        score += 6
        print("[0] SUCCESS")
    else:
        print("[0] FAIL")
except:
    print("[0] FAIL")

print("\nTOTAL SCORE -->> ", score, "\n")
