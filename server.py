class Server:
    def __init__(self):
        self.orders = []

    def makeOrder(self, orderNumber, li):
        orderExist = False
        newOrder = [orderNumber, li]
        # 파이썬에서 주의해야할점.. 반복문 안의 변수가 이미 존재한다면 override가 안됨..
        for order in self.orders:
            if order[0] == orderNumber:
                orderExist = True
        if orderExist:
            return -1
        self.orders.append(newOrder)
        return newOrder

    def getWaitingTime(self, orderNumber, timePerOne):
        # 주문번호가 있는지 확인
        # 주문번호가 있는 경우 해당 주문번호의 index를 가져오고 그 index까지의 order안의 list의 갯수만큼을 timerPerOne곱해서 리턴
        # 주문번호가 없는 경우 return -1
        orderExist = False
        index = 0
        count = 0
        for i in range(len(self.orders)):
            if self.orders[i][0] == orderNumber:
                orderExist = True
                index = i
        if not orderExist:
            return -1
        newOrders = self.orders[: index + 1]
        for order in newOrders:
            count += len(order[1])
        return count * timePerOne

    def serveOrder(self):
        removed = self.orders[0]
        # remove는 특정 값을 삭제하는거고 몇번째 원소를 없애는게 아님
        del self.orders[0]
        return removed[0], removed[1]

    def getOrderNumber(self):
        return len(self.orders)

    def cancelOrder(self, orderNumber):
        orderExist = False
        index = -1
        count = 0
        for order in self.orders:
            if order[0] == orderNumber:
                orderExist = True
                index = count
            count += 1
        if not orderExist:
            return -1, -1
        cancelledNumber = self.orders[index][0]
        cancelledList = self.orders[index][1]
        return cancelledNumber, cancelledList

    def makeOrderVIP(self, orderNumber, orderList):
        orderExist = False
        for order in self.orders:
            if order[0] == orderNumber:
                orderExist = True
        if not orderExist:
            self.orders.insert(0, [orderNumber, orderList])
            tmp = []
            for order in self.orders:
                tmp.append(order[0])
            return tmp
        return -1

    def giveService(self, orderNumber, product):
        orderExist = False
        index = -1
        count = 0
        for order in self.orders:
            if order[0] == orderNumber:
                orderExist = True
                index = count
            count += 1
        if orderExist:
            self.orders[index][1].append(product)
            selected = self.orders[index]
            return selected[0], selected[1]

        else:
            return -1, -1

    def getOrderItems(self):
        count = 0
        for order in self.orders:
            for _ in order[1]:
                count += 1
        return count


# Scoring
score = 0

# 1
try:
    solution = ["0001", ["pizza", "pie"]]
    answer = []

    s = Server()
    answer = s.makeOrder("0001", ["pizza", "pie"])
    if answer == solution:
        answer = s.makeOrder("0001", ["pizza", "pie"])
        if answer == -1:
            score += 8
            print("[1] SUCCESS")
        else:
            print("[1] FAIL.a")
    else:
        print("[1] FAIL.b")
except:
    print("[1] FAIL.e")

# 2
try:
    solution = 60
    answer = 0

    score_2 = 0

    s = Server()
    s.makeOrder("0001", ["pizza", "pie"])
    s.makeOrder("0002", ["pizza", "pie", "pasta"])
    s.makeOrder("0003", ["pizza"])

    try:
        answer = s.getWaitingTime("0003", 10)
        if answer == solution:
            answer = s.getWaitingTime("0004", 10)
            if answer == -1:
                score += 8
                score_2 += 8
                print("[2] SUCCESS")
            else:
                print("[2] FAIL.a")
        else:
            print("[2] FAIL.b")
    except:
        print("[2] int error")
    try:
        if score_2 != 8:
            answer = s.getWaitingTime("0003", "10")
            if answer == solution:
                answer = s.getWaitingTime("0004", "10")
                if answer == -1:
                    score += 8
                    score_2 += 8
                    print("[2s] SUCCESS")
                else:
                    print("[2s] FAIL.a")
            else:
                print("[2s] FAIL.b")
    except:
        print("[2s] string error")

    if score_2 == 16:
        score -= 8

except:
    print("[2] FAIL.e")
# 3
try:
    solution1 = ["0001", ["pizza", "pie"]]
    solution2 = ["0002", ["pizza", "pie", "pasta"]]
    answer = 0

    s = Server()
    s.makeOrder("0001", ["pizza", "pie"])
    s.makeOrder("0002", ["pizza", "pie", "pasta"])
    s.makeOrder("0003", ["pizza"])

    num, list = s.serveOrder()
    if num == solution1[0] and list == solution1[1]:
        num, list = s.serveOrder()
        if num == solution2[0] and list == solution2[1]:
            score += 8
            print("[3] SUCCESS")
        else:
            print("[3] FAIL.a")
    else:
        print("[3] FAIL.b")
except:
    print("[3] FAIL.e")
# 4
try:
    solution = [1, 2, 3]
    answer = []

    s = Server()
    s.makeOrder("0001", ["pizza", "pie"])
    answer.append(s.getOrderNumber())
    s.makeOrder("0002", ["pizza", "pie", "pasta"])
    answer.append(s.getOrderNumber())
    s.makeOrder("0003", ["pizza"])
    answer.append(s.getOrderNumber())

    if answer == solution:
        score += 4
        print("[4] SUCCESS")
    else:
        print("[4] FAIL.a")
except:
    print("[4] FAIL.e")

# 5
try:
    solution1 = ["0001", ["pizza", "pie"]]
    solution2 = ["0002", ["pizza", "pie", "pasta"]]
    answer = 0

    s = Server()
    s.makeOrder("0001", ["pizza", "pie"])
    s.makeOrder("0002", ["pizza", "pie", "pasta"])
    s.makeOrder("0003", ["pizza"])

    num, list = s.cancelOrder("0001")

    if num == solution1[0] and list == solution1[1]:
        num, list = s.cancelOrder("0002")
        if num == solution2[0] and list == solution2[1]:
            res1, res2 = s.cancelOrder("0009")
            if res1 == -1 and res2 == -1:
                score += 8
                print("[5] SUCCESS")
            else:
                print("[5] FAIL.a")
        else:
            print("[5] FAIL.b")
    else:
        print("[5] FAIL.c")
except:
    print("[5] FAIL.e")

try:
    solution = ["0004", "0001", "0002", "0003"]
    answer = 0

    s = Server()
    s.makeOrder("0001", ["pizza", "pie"])
    s.makeOrder("0002", ["pizza", "pie", "pasta"])
    s.makeOrder("0003", ["pizza"])

    answer = s.makeOrderVIP("0004", ["pizza"])

    if answer == solution:
        score += 8
        print("[6] SUCCESS")
    else:
        print("[6] FAIL.a")
except:
    print("[6] FAIL.e")

try:
    solution = ["0002", ["pizza", "pie", "pasta", "coke"]]
    answer = 0

    s = Server()
    s.makeOrder("0001", ["pizza", "pie"])
    s.makeOrder("0002", ["pizza", "pie", "pasta"])
    s.makeOrder("0003", ["pizza"])

    num, list = s.giveService("0002", "coke")

    if num == solution[0] and list == solution[1]:
        res = s.giveService("0004", "coke")
        if res1 == -1 and res2 == -1:
            score += 8
            print("[7] SUCCESS")
        else:
            print("[7] FAIL.a")
    else:
        print("[7] FAIL.b")
except:
    print("[7] FAIL.e")

try:
    solution = 6
    answer = 0

    s = Server()
    s.makeOrder("0001", ["pizza", "pie"])
    s.makeOrder("0002", ["pizza", "pie", "pasta"])
    s.makeOrder("0003", ["pizza"])

    answer = s.getOrderItems()

    if answer == solution:
        score += 8
        print("[8] SUCCESS")
    else:
        print("[8] FAIL.a")
except:
    print("[8] FAIL.e")


print("\nTOTAL SCORE -->> ", score, "\n")
