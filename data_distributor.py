import pandas as pd
import numpy as np

from data_reader import DataReader


class DataDistributor(object):
    def __init__(self, worker_num, dataset=[]):
        self.worker_num=worker_num
        self.dataset=pd.Series(dataset)
        self.data_size=len(dataset)

    def set_dataset(self,dataset:list):
        self.dataset=pd.Series(dataset)
        self.data_size = len(dataset)

    def partition(self,amount=None):
        partitioned_data = []
        if amount is None:
            amount=self.data_size//self.worker_num
            cnt=self.data_size

            for i in range(self.worker_num):
                if(cnt<amount):
                    data=self.dataset[i*amount:]
                    data.append(self.dataset.sample(amount-cnt))
                    partitioned_data.append(data)
                else:
                    partitioned_data.append(self.dataset[i*amount:(i+1)*amount])
                    cnt-=amount
        else:
            if amount>self.data_size:
                amount=self.data_size
            for i in range(self.worker_num):
                partitioned_data.append(self.dataset.sample(amount).to)

        return partitioned_data


if __name__ == '__main__':
    reader = DataReader()
    data=reader.get_iris_data()
    d=DataDistributor(12,data)
    t=d.partition(50)
    print()





