import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def label_uni(row):
    '''
    use this helper function to label smaller universities as 'other'
    '''
    if row['perc'] > 3.0:
        return row['unique_values']
    else:
        return 'Other'

def label_uni_start(row):
    '''
    use this helper function to label smaller universities as 'other' for the
    perc change df
    '''
    if row['start_perc'] > 2.5:
        return row['unique_values']
    else:
        return 'Other'

def label_uni_end(row):
    '''
    use this helper function to label smaller universities as 'other' for the
    perc change df
    '''
    if row['end_perc'] > 3.0:
        return row['unique_values']
    else:
        return 'Other'

def label_degree(row):
    '''
    use this helper function to label smaller degrees as 'other'
    '''
    if row['perc'] > 1.0:
        return row['unique_values']
    else:
        return 'Other'

def label_program(row):
    '''
    use this helper function to bucket the many degree programs into about 9
    individual buckets rather than 31
    '''
    if row['cip2'] == 10 or row['cip2'] == 11:
        return 'Computer Science'
    elif row['cip2'] == 12 or row['cip2'] == 16 or row['cip2'] == 23 or \
    row['cip2'] == 24 or row['cip2'] == 50 or row['cip2'] == 54:
        return 'Arts/History'
    elif row['cip2'] == 13 or row['cip2'] == 25 or row['cip2'] == 30 or \
    row['cip2'] == 38 or row['cip2'] == 42 or row['cip2'] == 44 or row['cip2'] == 45:
        return 'Social Science'
    elif row['cip2'] == 14 or row['cip2'] == 15 or row['cip2'] == 27 or row['cip2'] == 49:
        return 'Math/Engineering'
    elif row['cip2'] == 19 or row['cip2'] == 51 or row['cip2'] == 31:
        return 'Physical/Medical/Wellness'
    elif row['cip2'] == 43 or row['cip2'] == 22:
        return 'Law'
    elif row['cip2'] == 26 or row['cip2'] == 40 or row['cip2'] == 41:
        return 'General Sciences'
    elif row['cip2'] == 46 or row['cip2'] == 47 or row['cip2'] == 48:
        return 'Labor'
    elif row['cip2'] == 52:
        return 'Business'
    else:
        return 'Other'

def pie_chart_inst_name_by_year(year, title, save_as):
    '''
    create a pie chart of the attendees of universities in Colorado as percentages
    by year
    '''
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

# def percent_increase_inst

def pie_chart_degree_level_by_year(year, title, save_as):
    '''
    create a pie chart of the degrees of students in Colorado as percentages
    by year
    '''
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

def pie_chart_program_by_year(year, title, save_as):
    '''
    create a pie chart of the programs of students in Colorado as percentages
    by year
    '''
    temp_df = df2[df2['year'] == year]
    value_counts = temp_df['programBucket'].value_counts(dropna=True, sort=True)
    temp_df = value_counts.rename_axis('unique_values').reset_index(name='counts')
    temp_df['perc'] = (temp_df['counts']/temp_df['counts'].sum())*100
    labels = temp_df['unique_values'].tolist()
    counts = temp_df['perc'].tolist()
    colors = ['#fb7d07', '#0203e2', '#d0c101', '#738595', '#e03fd8', '#645403',
    '#8e82fe', '#e50000', '#019529']
    fig1, ax1 = plt.subplots()
    ax1.pie(counts, labels=labels, colors=colors, autopct='%1.1f%%')
    ax1.axis('equal')
    ax1.set_title(title)
    plt.savefig('../images/program_piecharts/' + save_as)

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
    df2 = df.filter(items=['year', 'cip2', 'programName']).dropna(subset = ['programName'])
    df2['programBucket'] = df2.apply(lambda row: label_program(row), axis=1)
    df['type'] = df['institutionName'].apply(college_type)
    # create pie charts of institutuion breakdowns
    # pie_chart_inst_name_by_year(2001, '2001 Breakdown of Institutions', '2001')
    # pie_chart_inst_name_by_year(2005, '2005 Breakdown of Institutions', '2005')
    # pie_chart_inst_name_by_year(2009, '2009 Breakdown of Institutions', '2009')
    # pie_chart_inst_name_by_year(2013, '2013 Breakdown of Institutions', '2013')
    # pie_chart_inst_name_by_year(2017, '2017 Breakdown of Institutions', '2017')

    # create pie charts of degree level breakdowns
    # pie_chart_degree_level_by_year(2001, '2001 Breakdown of Degrees', '2001')
    # pie_chart_degree_level_by_year(2009, '2009 Breakdown of Degrees', '2009')
    # pie_chart_degree_level_by_year(2017, '2017 Breakdown of Degrees', '2017')

    # create pie charts of program level breakdowns
    # pie_chart_program_by_year(2001, '2001 Breakdown of Programs', '2001')
    # pie_chart_program_by_year(2005, '2005 Breakdown of Programs', '2005')
    # pie_chart_program_by_year(2009, '2009 Breakdown of Programs', '2009')
    # pie_chart_program_by_year(2013, '2013 Breakdown of Programs', '2013')
    # pie_chart_program_by_year(2017, '2017 Breakdown of Programs', '2017')

    # start_df = df[df['year']==2001]
    # value_counts = start_df['institutionName'].value_counts(dropna=True, sort=True)
    # start_df = value_counts.rename_axis('unique_values').reset_index(name='counts')
    # start_df['start_perc'] = (start_df['counts']/start_df['counts'].sum())*100
    # start_df['insts'] = start_df.apply(lambda row: label_uni_start(row), axis=1)
    # start_df = start_df.groupby('insts')['start_perc'].sum().reset_index()
    #
    # end_df = df[df['year']==2017]
    # value_counts = end_df['institutionName'].value_counts(dropna=True, sort=True)
    # end_df = value_counts.rename_axis('unique_values').reset_index(name='counts')
    # end_df['end_perc'] = (end_df['counts']/end_df['counts'].sum())*100
    # end_df['insts'] = end_df.apply(lambda row: label_uni_end(row), axis=1)
    # end_df = end_df.groupby('insts')['end_perc'].sum().reset_index()
    #
    # perc_change_df = start_df.merge(end_df, left_on='insts', right_on='insts', how='outer')
    # perc_change_df = perc_change_df.dropna(subset = ['start_perc', 'end_perc'])
    # perc_change_df['%change'] = ((perc_change_df['end_perc'] - perc_change_df['start_perc']) / perc_change_df['start_perc'])*100
    # perc_change_df = perc_change_df.sort_values(by=['%change'])
    # perc_change_df['positive'] = perc_change_df['%change'] > 0
    #
    # labels = perc_change_df['insts'].tolist()
    # labels2 = ['CU-Boulder', 'UNC', 'CSU', 'DU', 'MSU-Denver', 'CU-Colorado Springs',
    # 'Other', 'Front Range CC', 'Pueblo CC', 'Pikes Peak CC', 'Red Rocks CC']
    # values = perc_change_df['%change'].tolist()
    # fig, ax = plt.subplots()
    # index = np.arange(len(labels2))
    # bar_width = 0.35
    # plt.bar(index, values, bar_width, color=perc_change_df['positive'].map({True: 'b', False: 'r'}))
    # plt.xticks(index + bar_width/2, labels2, rotation=85)
    # plt.tight_layout()
    # plt.axhline(y=0, color='black')
    # plt.title('% Change from 2001-2017 of % of Student Awardees')
    # plt.xlabel('* awardee - student earning a certificate, degree, or formal award. 100% of awardees contains all of Colorado')
    # plt.show()
