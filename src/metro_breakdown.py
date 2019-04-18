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

def label_degree(row):
    '''
    use this helper function to label smaller degrees as 'other'
    '''
    if row['perc'] > 1.0:
        return row['unique_values']
    else:
        return 'Other'

def pie_chart_inst_name_by_year(year, metro_area, title, save_as):
    '''
    create a pie chart of the awardees of universities in Colorado as percentages
    by year
    '''
    temp_df = df[df['year']==year]
    temp_df = temp_df[temp_df['metro_area']==metro_area]
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
    plt.savefig('../images/wslope/' + save_as)
    # plt.show()

def pie_chart_degree_level_by_year(year, metro_area, title, save_as):
    '''
    create a pie chart of the degrees of students in Colorado as percentages
    by year
    '''
    temp_df = df[df['year']==year]
    temp_df = temp_df[temp_df['metro_area']==metro_area]
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
    plt.savefig('../images/wslope/' + save_as)
    # plt.show()

def pie_chart_program_by_year(year, metro_area, title, save_as):
    '''
    create a pie chart of the programs of students in Colorado as percentages
    by year
    '''
    temp_df = df[df['year'] == year]
    temp_df = temp_df[temp_df['metro_area']==metro_area]
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
    plt.savefig('../images/wslope/' + save_as)
    # plt.show()



if __name__ == '__main__':
    df = pd.read_csv('../../data_misc/data/metro_df.csv')

    # Program Breakdown by Metros
    # pie_chart_program_by_year(2017, 'Boulder', '2017 Boulder Breakdown', 'boulder2017_prog')
    # pie_chart_program_by_year(2009, 'Boulder', '2009 Boulder Breakdown', 'boulder2009_prog')
    # pie_chart_program_by_year(2001, 'Boulder', '2001 Boulder Breakdown', 'boulder2001_prog')

    # pie_chart_program_by_year(2017, 'Colorado Springs', '2017 Colorado Springs Breakdown', 'csprings2017_prog')
    # pie_chart_program_by_year(2009, 'Colorado Springs', '2009 Colorado Springs Breakdown', 'csprings2009_prog')
    # pie_chart_program_by_year(2001, 'Colorado Springs', '2001 Colorado Springs Breakdown', 'csprings2001_prog')

    # pie_chart_program_by_year(2017, 'Denver', '2017 Denver Breakdown', 'denver2017_prog')
    # pie_chart_program_by_year(2009, 'Denver', '2009 Denver Breakdown', 'denver2009_prog')
    # pie_chart_program_by_year(2001, 'Denver', '2001 Denver Breakdown', 'denver2001_prog')

    # pie_chart_program_by_year(2017, 'Fort Collins', '2017 Fort Collins Breakdown', 'ftcollins2017_prog')
    # pie_chart_program_by_year(2009, 'Fort Collins', '2009 Fort Collins Breakdown', 'ftcollins2009_prog')
    # pie_chart_program_by_year(2001, 'Fort Collins', '2001 Fort Collins Breakdown', 'ftcollins2001_prog')

    # pie_chart_program_by_year(2017, 'Greeley', '2017 Greeley Breakdown', 'greeley2017_prog')
    # pie_chart_program_by_year(2009, 'Greeley', '2009 Greeley Breakdown', 'greeley2009_prog')
    # pie_chart_program_by_year(2001, 'Greeley', '2001 Greeley Breakdown', 'greeley2001_prog')

    # pie_chart_program_by_year(2017, 'Pueblo', '2017 Pueblo Breakdown', 'pueblo2017_prog')
    # pie_chart_program_by_year(2009, 'Pueblo', '2009 Pueblo Breakdown', 'pueblo2009_prog')
    # pie_chart_program_by_year(2001, 'Pueblo', '2001 Pueblo Breakdown', 'pueblo2001_prog')

    # pie_chart_program_by_year(2017, 'Western Slope', '2017 Western Slope Breakdown', 'wslope2017_prog')
    # pie_chart_program_by_year(2009, 'Western Slope', '2009 Western Slope Breakdown', 'wslope2009_prog')
    # pie_chart_program_by_year(2001, 'Western Slope', '2001 Western Slope Breakdown', 'wslope2001_prog')

    # Degree Breakdown by Metros
    # pie_chart_degree_level_by_year(2017, 'Boulder', '2017 Boulder Breakdown', 'boulder2017_degree')
    # pie_chart_degree_level_by_year(2009, 'Boulder', '2009 Boulder Breakdown', 'boulder2009_degree')
    # pie_chart_degree_level_by_year(2001, 'Boulder', '2001 Boulder Breakdown', 'boulder2001_degree')

    # pie_chart_degree_level_by_year(2017, 'Colorado Springs', '2017 Colorado Springs Breakdown', 'csprings2017_degree')
    # pie_chart_degree_level_by_year(2009, 'Colorado Springs', '2009 Colorado Springs Breakdown', 'csprings2009_degree')
    # pie_chart_degree_level_by_year(2001, 'Colorado Springs', '2001 Colorado Springs Breakdown', 'csprings2001_degree')

    # pie_chart_degree_level_by_year(2017, 'Denver', '2017 Denver Breakdown', 'denver2017_degree')
    # pie_chart_degree_level_by_year(2009, 'Denver', '2009 Denver Breakdown', 'denver2009_degree')
    # pie_chart_degree_level_by_year(2001, 'Denver', '2001 Denver Breakdown', 'denver2001_degree')

    # pie_chart_degree_level_by_year(2017, 'Fort Collins', '2017 Fort Collins Breakdown', 'ftcollins2017_degree')
    # pie_chart_degree_level_by_year(2009, 'Fort Collins', '2009 Fort Collins Breakdown', 'ftcollins2009_degree')
    # pie_chart_degree_level_by_year(2001, 'Fort Collins', '2001 Fort Collins Breakdown', 'ftcollins2001_degree')

    # pie_chart_degree_level_by_year(2017, 'Greeley', '2017 Greeley Breakdown', 'greeley2017_degree')
    # pie_chart_degree_level_by_year(2009, 'Greeley', '2009 Greeley Breakdown', 'greeley2009_degree')
    # pie_chart_degree_level_by_year(2001, 'Greeley', '2001 Greeley Breakdown', 'greeley2001_degree')

    # pie_chart_degree_level_by_year(2017, 'Pueblo', '2017 Pueblo Breakdown', 'pueblo2017_degree')
    # pie_chart_degree_level_by_year(2009, 'Pueblo', '2009 Pueblo Breakdown', 'pueblo2009_degree')
    # pie_chart_degree_level_by_year(2001, 'Pueblo', '2001 Pueblo Breakdown', 'pueblo2001_degree')

    # pie_chart_degree_level_by_year(2017, 'Western Slope', '2017 Western Slope Breakdown', 'wslope2017_degree')
    # pie_chart_degree_level_by_year(2009, 'Western Slope', '2009 Western Slope Breakdown', 'wslope2009_degree')
    # pie_chart_degree_level_by_year(2001, 'Western Slope', '2001 Western Slope Breakdown', 'wslope2001_degree')

    # Institution Breakdown by Metros
    # pie_chart_inst_name_by_year(2017, 'Boulder', '2017 Boulder Breakdown', 'boulder2017_instit')
    # pie_chart_inst_name_by_year(2009, 'Boulder', '2009 Boulder Breakdown', 'boulder2009_instit')
    # pie_chart_inst_name_by_year(2001, 'Boulder', '2001 Boulder Breakdown', 'boulder2001_instit')

    # pie_chart_inst_name_by_year(2017, 'Colorado Springs', '2017 Colorado Springs Breakdown', 'csprings2017_instit')
    # pie_chart_inst_name_by_year(2009, 'Colorado Springs', '2009 Colorado Springs Breakdown', 'csprings2009_instit')
    # pie_chart_inst_name_by_year(2001, 'Colorado Springs', '2001 Colorado Springs Breakdown', 'csprings2001_instit')

    # pie_chart_inst_name_by_year(2017, 'Denver', '2017 Denver Breakdown', 'denver2017_instit')
    # pie_chart_inst_name_by_year(2009, 'Denver', '2009 Denver Breakdown', 'denver2009_instit')
    # pie_chart_inst_name_by_year(2001, 'Denver', '2001 Denver Breakdown', 'denver2001_instit')

    # pie_chart_inst_name_by_year(2017, 'Fort Collins', '2017 Fort Collins Breakdown', 'ftcollins2017_instit')
    # pie_chart_inst_name_by_year(2009, 'Fort Collins', '2009 Fort Collins Breakdown', 'ftcollins2009_instit')
    # pie_chart_inst_name_by_year(2001, 'Fort Collins', '2001 Fort Collins Breakdown', 'ftcollins2001_instit')

    # pie_chart_inst_name_by_year(2017, 'Greeley', '2017 Greeley Breakdown', 'greeley2017_instit')
    # pie_chart_inst_name_by_year(2009, 'Greeley', '2009 Greeley Breakdown', 'greeley2009_instit')
    # pie_chart_inst_name_by_year(2001, 'Greeley', '2001 Greeley Breakdown', 'greeley2001_instit')

    # pie_chart_inst_name_by_year(2017, 'Pueblo', '2017 Pueblo Breakdown', 'pueblo2017_instit')
    # pie_chart_inst_name_by_year(2009, 'Pueblo', '2009 Pueblo Breakdown', 'pueblo2009_instit')
    # pie_chart_inst_name_by_year(2001, 'Pueblo', '2001 Pueblo Breakdown', 'pueblo2001_instit')

    # pie_chart_inst_name_by_year(2017, 'Western Slope', '2017 Western Slope Breakdown', 'wslope2017_instit')
    # pie_chart_inst_name_by_year(2009, 'Western Slope', '2009 Western Slope Breakdown', 'wslope2009_instit')
    # pie_chart_inst_name_by_year(2001, 'Western Slope', '2001 Western Slope Breakdown', 'wslope2001_instit')
