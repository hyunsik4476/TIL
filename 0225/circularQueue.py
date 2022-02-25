def enQueue(item):
    global rear
    if isFull() : print('queue_full')
    else:
        rear = (rear+1) % len(cQ)
        cQ[rear] = item

def deQueue():
    if isEmpty() : print('queue_empty')
    else:
        front = (front+1) % len(cQ)
        return cQ[front]

def isEmpty():
    return front == rear

def isFull():
    return (rear+1) % len(cQ) == front

cQ = [0]*10
front = rear = 0