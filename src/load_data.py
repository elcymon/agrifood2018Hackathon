import pandas as pd
import os.path
import numpy as np
import cv2


class BeetRootData:
    size = None
    data = []
    img_dim = None
    start_idx = None
    end_idx = None
    labels = None

    def __init__(self, path='./../data/', name_stem='beet', dataset='Train', format='.jpg'):
        self.labels = pd.read_csv(path + dataset + '/' + dataset + '_labels.csv')

        if dataset[0] == 'T':
            low = 0
            high = 50
        else:
            low = 50
            high = 100

        for i in range(low, high):
            file_name = name_stem + str(i) + format
            img_file = path + dataset + '/' + file_name
            if os.path.isfile(img_file):
                # set/reset params
                self.data += [cv2.imread(img_file)]
            else:
                raise ValueError("There is no image " + img_file)

        self.size = len(self.data)
        self.img_dim = self.data[-1].shape

    def get_data(self):
        return self.data

    def get_size(self):
        return self.size

    # function returning the beetroot image 'beetN.jpg' where N is 'beetroot_num'
    def get_img(self, beetroot_num):
        return self.data[beetroot_num]

    # function returning the labelled (x,y) position of beetroot 'beetN.jpg' where N is 'beetroot_num'
    def get_pos(self, beetroot_num):
        return np.array([self.labels.x[beetroot_num], self.labels.y[beetroot_num]])

    # function returning 1 if 'beetN.jpg' is good or 0 if it is bad. - N is 'beetroot_num'
    def is_good(self, beetroot_num):
        return self.labels.is_good[beetroot_num]

