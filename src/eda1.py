import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def label_uni(row):
    if row['perc'] > 5.0:
        return row['unique_values']
    else:
        return 'Other'

def label_degree(row):
    if row['perc'] > 1.0:
        return row['unique_values']
    else:
        return 'Other'

def pie_chart_inst_name_by_year(year, title, save_as):
    temp_df = df[df['year']==year]
    value_counts = temp_df['institutionName'].value_counts(dropna=True, sort=True)
    temp_df = value_counts.rename_axis('unique_values').reset_index(name='counts')
    temp_df['perc'] = (temp_df['counts']/temp_df['counts'].sum())*100
    temp_df['insts'] = temp_df.apply(lambda row: label_uni(row), axis=1)
    temp_df = temp_df.groupby('insts')['perc'].sum().reset_index()
    labels = temp_df['insts'].tolist()
    counts = temp_df['perc'].tolist()
    fig1, ax1 = plt.subplots()
    ax1.pie(counts, labels=labels, autopct='%1.1f%%')
    ax1.axis('equal')
    ax1.set_title(title)
    plt.savefig('../images/institution_piecharts/' + save_as)
    # print (temp_df)

def pie_chart_degree_level_by_year(year, title, save_as):
    temp_df = df[df['year']==year]
    value_counts = temp_df['degreeLevel'].value_counts(dropna=True, sort=True)
    temp_df = value_counts.rename_axis('unique_values').reset_index(name='counts')
    temp_df['perc'] = (temp_df['counts']/temp_df['counts'].sum())*100
    temp_df['degree'] = temp_df.apply(lambda row: label_degree(row), axis=1)
    temp_df = temp_df.groupby('degree')['perc'].sum().reset_index()
    labels = temp_df['degree'].tolist()
    counts = temp_df['perc'].tolist()
    fig1, ax1 = plt.subplots()
    ax1.pie(counts, labels=labels, autopct='%1.1f%%')
    ax1.axis('equal')
    ax1.set_title(title)
    plt.savefig('../images/degree_piecharts/' + save_as)



if __name__ == '__main__':
    df = pd.read_csv('../../data_misc/data/grad_degrees.csv')

    # create pie charts of institutuion breakdowns
    # pie_chart_inst_name_by_year(2001, '2001 Breakdown of Institutions', '2001')
    # pie_chart_inst_name_by_year(2005, '2005 Breakdown of Institutions', '2005')
    # pie_chart_inst_name_by_year(2009, '2009 Breakdown of Institutions', '2009')
    # pie_chart_inst_name_by_year(2013, '2013 Breakdown of Institutions', '2013')
    # pie_chart_inst_name_by_year(2017, '2017 Breakdown of Institutions', '2017')

    # create pie charts of degree level breakdowns
    pie_chart_degree_level_by_year(2001, '2001 Breakdown of Degrees', '2001')
    pie_chart_degree_level_by_year(2009, '2009 Breakdown of Degrees', '2009')
    pie_chart_degree_level_by_year(2017, '2017 Breakdown of Degrees', '2017')
