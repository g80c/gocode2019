import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def college_type(x):
    if isinstance(x, str) and 'community' in x.lower().split():
        return 'community college'
    elif isinstance(x, str) and 'university' in x.lower().split():
        return 'university'
    elif isinstance(x, float):
        return x
    else:
        return 'state college'


if __name__ == '__main__':
    df = pd.read_csv('../../data_misc/data/grad_degrees.csv')
    df['type'] = df['institutionName'].apply(college_type)
    df2 = df.filter(['year', 'type'], axis=1).dropna()

    # Plotting Stacked chart for Institution Type

    # yr_2001 = df2[df2['year'] == 2001]
    # counts_2001 = yr_2001['type'].value_counts(dropna=True, sort=True)

    # yr_2003 = df2[df2['year'] == 2003]
    # counts_2003 = yr_2003['type'].value_counts(dropna=True, sort=True)

    # yr_2005 = df2[df2['year'] == 2005]
    # counts_2005 = yr_2005['type'].value_counts(dropna=True, sort=True)

    # yr_2007 = df2[df2['year'] == 2007]
    # counts_2007 = yr_2007['type'].value_counts(dropna=True, sort=True)

    # yr_2009 = df2[df2['year'] == 2009]
    # counts_2009 = yr_2009['type'].value_counts(dropna=True, sort=True)

    # yr_2012 = df2[df2['year'] == 2012]
    # counts_2012 = yr_2012['type'].value_counts(dropna=True, sort=True)

    # yr_2013 = df2[df2['year'] == 2013]
    # counts_2013 = yr_2013['type'].value_counts(dropna=True, sort=True)

    # yr_2015 = df2[df2['year'] == 2015]
    # counts_2015 = yr_2015['type'].value_counts(dropna=True, sort=True)

    # yr_2017 = df2[df2['year'] == 2017]
    # counts_2017 = yr_2017['type'].value_counts(dropna=True, sort=True)

    # data = pd.DataFrame({
    #             'University':[5719, 5948, 6489, 6540, 6904, 7802, 8357, 9008, 9422],
    #             'Community College':[2524, 2873, 3238, 2911, 3481, 4720, 5144, 5788, 6371],
    #             'State College':[1026, 1165, 1226, 1195, 1414, 1774, 2087, 2912, 3030], },
    #             index=range(1, 10))
    #
    # data_perc = data.divide(data.sum(axis=1), axis=0)
    #
    # plt.stackplot(range(2001,2018, 2),  data_perc["University"],  data_perc["Community College"],
    #             data_perc["State College"], labels=['University','Community College','State College'])
    # plt.legend(loc='lower left')
    # plt.margins(0,0)
    # plt.xlabel('Year')
    # plt.ylabel('Percentage')
    # plt.tick_params(axis='y', which='both', labelleft='on', labelright='on')
    # plt.title('Awardees by Institution Type')
    # plt.savefig('../images/stacked_perc_charts/intst_type')
    # plt.show()




    # Plotting stacked chart for degree level
    # only looking at the main degrees (Bachelors, Masters, Associates, Certificate)
    df3 = df.filter(['year', 'degreeLevel'], axis=1).dropna()
    df3 = df3[df3['degreeLevel'] != 'OtherGraduate']
    df3 = df3[df3['degreeLevel'] != 'Specialist']
    df3 = df3[df3['degreeLevel'] != 'Professional']
    df3 = df3[df3['degreeLevel'] != 'Doctoral']

    # yr_2001 = df3[df3['year'] == 2001]
    # counts_2001 = yr_2001['degreeLevel'].value_counts(dropna=True, sort=True)

    # yr_2003 = df3[df3['year'] == 2003]
    # counts_2003 = yr_2003['degreeLevel'].value_counts(dropna=True, sort=True)

    # yr_2005 = df3[df3['year'] == 2005]
    # counts_2005 = yr_2005['degreeLevel'].value_counts(dropna=True, sort=True)

    # yr_2007 = df3[df3['year'] == 2007]
    # counts_2007 = yr_2007['degreeLevel'].value_counts(dropna=True, sort=True)

    # yr_2009 = df3[df3['year'] == 2009]
    # counts_2009 = yr_2009['degreeLevel'].value_counts(dropna=True, sort=True)

    # yr_2012 = df3[df3['year'] == 2012]
    # counts_2012 = yr_2012['degreeLevel'].value_counts(dropna=True, sort=True)

    # yr_2013 = df3[df3['year'] == 2013]
    # counts_2013 = yr_2013['degreeLevel'].value_counts(dropna=True, sort=True)

    # yr_2015 = df3[df3['year'] == 2015]
    # counts_2015 = yr_2015['degreeLevel'].value_counts(dropna=True, sort=True)

    # yr_2017 = df3[df3['year'] == 2017]
    # counts_2017 = yr_2017['degreeLevel'].value_counts(dropna=True, sort=True)

    data = pd.DataFrame({
                'Bachelor':[4087, 4220, 4587, 4636, 4830, 5459, 5901, 6403, 6698],
                'Associate':[1886, 1983, 2112, 1853, 2176, 2899, 3092, 3339, 3426],
                'Master':[1573, 1687, 1802, 1752, 1879, 2286, 2442, 2639, 2807],
                'Certificate': [1320, 1654, 1936, 1842, 2314, 3012, 3467, 4597, 5177] },
                index=range(1, 10))

    data_perc = data.divide(data.sum(axis=1), axis=0)

    plt.stackplot(range(2001,2018, 2),  data_perc["Bachelor"],  data_perc["Associate"],
                data_perc["Master"], data_perc["Certificate"], labels=['Bachelor',
                'Associate','Master', 'Certificate'])

    plt.legend(loc='lower left')
    plt.margins(0,0)
    plt.xlabel('Year')
    plt.ylabel('Percentage')
    plt.tick_params(axis='y', which='both', labelleft='on', labelright='on')
    plt.title('Awardees by Institution Degree Type')
    plt.savefig('../images/stacked_perc_charts/degree_type')
    # plt.show()
