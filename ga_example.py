import random
import time


class GA(object):
    def __init__(self, dataset):
        self.dataset = dataset
        self.pop = [i for i in 'Just Test']
        self.iter = 0

    def init_run(self):
        time.sleep(random.randint(3, 7))

    def run(self):
        for i in range(5):
            time.sleep(1)
            self.iter += 1
