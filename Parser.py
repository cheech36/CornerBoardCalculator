from Tkconstants import *
import pandas as pd
import os


class Backend_Manager():
    def __init__(self, file, path):
        self.data_path = os.path.join(path, file)
        data_path = os.path.join(path, file)
        self.gauge_table = pd.read_csv(data_path)
        print(self.gauge_table.head())

    def parse(self, item, Text_Fields):



            print('Parsing Item {0}'.format(item))
            cb = CornerBoard_Item()
            Text_Fields[0].insert(END, "Glue Value")






class CornerBoard_Item():
    def __init__(self):
        print('Creating CornerBoard Item')



def LookupTable():
    def __init__(self):
        pass




