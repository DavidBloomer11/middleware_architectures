import pickle
import time

class Queue:

    def __init__(self,file_name=None):
        self.file_name = file_name
        if file_name == None:
            self.items = []
        else:
            try:
                with open(file_name, 'rb') as f:
                    self.items = pickle.load(f)
            except:
                self.items = []
                with open(file_name, 'wb') as f:
                    pickle.dump(self.items, f)

    def is_empty(self):
        return not self.items

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def save(self, file_name=None):
        if file_name == None:
            with open(self.file_name, 'wb') as f:
                pickle.dump(self.items, f)
        else:
            with open(file_name, 'wb') as f:
                pickle.dump(self.items, f)

    def load(self, file_name):
        with open(file_name, 'rb') as f:
            self.items = pickle.load(f)


def order_processor():
    # First we initialize the queue
    trip_queue = Queue('trip_queue.pkl')
    booking_queue = Queue('booking_queue.pkl')

    x = 10

    while True:
        #Every 10 seconds process the orders to the queue
        time.sleep(x)
        order_queue = Queue('order_queue.pkl')
        
        # Empty order queue and put into other booking and trip queue
        length = len(order_queue.items)
        for i in range(length):
            item = order_queue.dequeue()
            if item['type'] == 'booking':
                booking_queue.enqueue(item)
            else:
                trip_queue.enqueue(item)

        # Save the queues
        trip_queue.save()
        booking_queue.save()
        order_queue.save()

        print(f'Order queue processed after {x} seconds')

        

