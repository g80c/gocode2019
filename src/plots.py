import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


if __name__ == '__main__':
    df = pd.read_csv('../../data_misc/data/grad_degrees.csv')
    df2 = df.filter(['year', 'ageDesc'], axis=1).dropna()
    df2 = df2[df2['ageDesc'] != 'Unknown']
    # df2 = df2[df2['ageDesc'] == '21-24']
    # df2 = df2[df2['ageDesc'] == '17-20']
    # df2 = df2[df2['ageDesc'] == 'Under 17']

    # degree_data = pd.DataFrame({
    #             'Bachelor':[4087, 4220, 4587, 4636, 4830, 5459, 5901, 6403, 6698],
    #             'Associate':[1886, 1983, 2112, 1853, 2176, 2899, 3092, 3339, 3426],
    #             'Master':[1573, 1687, 1802, 1752, 1879, 2286, 2442, 2639, 2807],
    #             'Certificate': [1320, 1654, 1936, 1842, 2314, 3012, 3467, 4597, 5177] },
    #             index=range(1, 10))
    #
    # inst_data = pd.DataFrame({
    #             'University':[5719, 5948, 6489, 6540, 6904, 7802, 8357, 9008, 9422],
    #             'Community College':[2524, 2873, 3238, 2911, 3481, 4720, 5144, 5788, 6371],
    #             'State College':[1026, 1165, 1226, 1195, 1414, 1774, 2087, 2912, 3030], },
    #             index=range(1, 10))
    #
    # # plt.plot(inst_data['University'], inst_data['Community College'], inst_data['State College'],
    # #     labels=['University','Community College','State College'])
    # plt.plot(range(2001,2018,2), inst_data['University'])
    # plt.plot(range(2001,2018,2), inst_data['Community College'])
    # plt.plot(range(2001,2018,2), inst_data['State College'])
    # plt.legend(loc='upper left')
    # plt.xlabel('Year')
    # plt.ylabel('Number of Awardees')
    # plt.title('Number of Awardees from Institutions')
    # plt.show()
