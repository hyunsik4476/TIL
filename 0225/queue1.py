def enQueue(item):
    global rear
    if isFull() : print('queue_full')
    else:
        rear += 1
        Q[rear] = item


def deQueue():
    if isEmpty() : print('queue_empty')
    else:
        front += 1
        return Q[front]


def isEmpty():
    return front == rear


def isFull():
    return rear == len(Q) - 1


def Qpeek():
    if isEmpty() : print('queue_empty')
    else: return Q[front+1]


Q = [0]*N
front = rear = -1