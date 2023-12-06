class Server:
    def __init__(self):
        self.orders = []

    def makeOrder(self, orderNumber, li):
        orderExist = False
        order = [orderNumber, li]
        for order in self.orders:
            print(orderNumber, order[0])
            if order[0] == orderNumber:
                orderExist = True
        if orderExist:
            return -1
        else:
            self.orders.append(order)
            return order

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
        else:
            newOrders = self.orders[: index + 1]
            for order in newOrders:
                count += len(order[1])
            return count * timePerOne


# orderNum = "234"
# orderlist = ["kimchi", "ironman", "rock"]
# server = Server()
# server.makeOrder(orderNum, orderlist)
# server.makeOrder("1", ["a", "s", "d"])
# print(server.orders)
# print(server.getWaitingTime("1", 3))

score = 0

try:
    solution = ["0001", ["pizza", "pie"]]
    answer = []

    s = Server()
    answer = s.makeOrder("0001", ["pizza", "pie"])
    if answer == solution:
        answer = s.makeOrder("0001", ["pizza", "pie"])
        print(answer)
        if answer == -1:
            score += 8
            print("[1] SUCCESS")
        else:
            print("[1] FAIL.a")
    else:
        print("[1] FAIL.b")
except:
    print("[1] FAIL.e")

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
