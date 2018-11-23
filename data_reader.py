import numpy as np

class DataReader(object):
    def __init__(self):
        pass

    def get_iris_data(self):
        data = []
        label_map = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
        inverse_label_map = self._build_inverse_map(label_map)

        with open('./data/iris/iris.data', 'r', encoding='utf-8') as f:
            lines=f.readlines()
            for line in lines:
                line = line.strip('\n')
                if line == '':
                    continue

                parts = line.split(',')

                x = [parts[i] for i in range(4)]
                label = inverse_label_map[parts[4]]
                data.append((x, label))

        np.random.shuffle(data)
        return data

    def _build_inverse_map(self, label_map):
        inverse_label_map = {}
        for i, label in enumerate(label_map):
            inverse_label_map[label] = i
        return inverse_label_map

