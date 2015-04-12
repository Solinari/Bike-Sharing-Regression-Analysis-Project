import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('train.csv')

def Show_BoxPlot(DataFrame):
    '''show sample boxplots'''

    groupby =['season','holiday','weather','temp','atemp',
              'humidity','windspeed','casual','registered', 'count']

    for i in range(len(groupby)):

        DataFrame.boxplot(column=['season','holiday','weather','temp','atemp',
                                  'humidity','windspeed','casual','registered',
                                  'count'],
                          by=groupby[i],
                          notch=True,
                          showmeans=True)
        plt.show()

#run it
Show_BoxPlot(df)
