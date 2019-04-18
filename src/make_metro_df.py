import numpy as np
import pandas as pd

def metro_area(row):
    if row['institutionName'] == 'Aims Community College':
        return 'Greeley'
    elif row['institutionName'] == 'University of Colorado Colorado Springs':
        return 'Colorado Springs'
    elif row['institutionName'] == 'University of Colorado Boulder':
        return 'Boulder'
    elif row['institutionName'] == 'Arapahoe Community College':
        return 'Denver'
    elif row['institutionName'] == 'Pikes Peak Community College':
        return 'Colorado Springs'
    elif row['institutionName'] == 'Community College of Denver':
        return 'Denver'
    elif row['institutionName'] == 'Colorado School of Mines':
        return 'Denver'
    elif row['institutionName'] == 'Colorado State University':
        return 'Fort Collins'
    elif row['institutionName'] == 'Colorado Mountain College':
        return 'Western Slope'
    elif row['institutionName'] == 'CSU-Global Campus':
        return 'Fort Collins'
    elif row['institutionName'] == 'Otero Junior College':
        return 'Pueblo'
    elif row['institutionName'] == 'University of Colorado Denver':
        return 'Denver'
    elif row['institutionName'] == 'Community College of Aurora':
        return 'Denver'
    elif row['institutionName'] == 'Front Range Community College':
        return 'Boulder'
    elif row['institutionName'] == 'Red Rocks Community College':
        return 'Denver'
    elif row['institutionName'] == 'Lamar Community College':
        return 'Pueblo'
    elif row['institutionName'] == 'Morgan Community College':
        return 'Greeley'
    elif row['institutionName'] == 'Northeastern Junior College':
        return 'Greeley'
    elif row['institutionName'] == 'Pueblo Community College':
        return 'Pueblo'
    elif row['institutionName'] == 'Trinidad State Junior College':
        return 'Pueblo'
    elif row['institutionName'] == 'Adams State University':
        return 'Pueblo'
    elif row['institutionName'] == 'Colorado Mesa University':
        return 'Western Slope'
    elif row['institutionName'] == 'Colorado State University - Pueblo':
        return 'Pueblo'
    elif row['institutionName'] == 'Fort Lewis College':
        return 'Western Slope'
    elif row['institutionName'] == 'Metropolitan State University of Denver':
        return 'Denver'
    elif row['institutionName'] == 'University of Northern Colorado':
        return 'Greeley'
    elif row['institutionName'] == 'Western State Colorado University':
        return 'Western Slope'
    elif row['institutionName'] == 'Colorado Northwestern Community College':
        return 'Western Slope'
    else:
        return 'Other'

def college_type(x):
    if isinstance(x, str) and 'community' in x.lower().split():
        return 'community college'
    elif isinstance(x, str) and 'university' in x.lower().split():
        return 'university'
    elif isinstance(x, float):
        return x
    else:
        return 'state college'

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

if __name__ == '__main__':
    inst_df = pd.read_csv('../../data_misc/data/grad_degrees.csv')
    inst_df['type'] = inst_df['institutionName'].apply(college_type)
    inst_df['programBucket'] = inst_df.apply(lambda row: label_program(row), axis=1)
    inst_df = inst_df.filter(['year', 'institutionName', 'type', 'degreeLevel', 'programBucket'], axis=1).dropna()
    inst_df['metro_area'] = inst_df.apply(lambda row: metro_area(row), axis=1)

    inst_df.to_csv('../../data_misc/data/metro_df.csv')



    # metro_df = pd.read_csv('../../data_misc/data/college_location_metro.csv')
