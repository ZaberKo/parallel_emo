import pandas as pd
import numpy as np


class PopPool(object):
    def __init__(self, dtype=np.float64):
        self.pool = pd.Series([], dtype=dtype)

    def init_pool(self, pops):
        for pop in pops:
            self.pool.append(pd.Series(pop))


    def update_pool(self, pop:pd.Series):
        self.pool.append(pop)
        amount=pop.size
        new_pop=self.pool.sample(amount)
        self.pool.drop(new_pop.index,inplace=True)
        return new_pop.tolist()

