# GoCode Info:

Loom Video Link: [Put Link Here]

# Introduction

Where would you start a business?  Why would you chose that location?  Would it be worth moving or hiring from other regions to increase your chances of success?  In this analysis we will explore factors that should help guide you to choosing the best place to start your business or where to hire from.

# Methodology

## Selecting Datasets

The first step in our process was deciding what data sets to use to tackle our question. We began by each taking a look though the data sets provided by the State.  We settled on using "" as our baseline data set.  With this data set we then began to explore what other data would be needed to accomplish our mission.  We settled on using a few datasets focused on how students financing their education, degrees awarded by institutions, business formations, and GDP of the state.

## Cleaning and preparing Data

Cleaning data is always a large undertaking.  Datasets can be littered with Null values, strange combinations of data types, and totally incorrect entries.  Our team spent a fair amount of time looking into what the data sets were meant to hold within their structure and what the columns were supposed to mean, some names can be cryptic.

Another important task was to decide on what values to merge datasets. This meant looking for values in the datasets that had similar if not identical values.  Many of our data sets need out help to add the key that we would join them on. We settled on using each metro area as one of our keys.

## Exploratory Data Analysis (EDA)

Breaking the team up and having members look into different agreed upon datasets helped expedite our process.  We all then dove into the data to find what structures could be found below the surface. We then decided to look at each data set from a State and a metro area perceptive. EDA took up a substantial portion of our time.

## Modeling

For the first round we did some more simplistic modeling on the GDP of the metro areas.  

# Analysis

## Financial simple analysis:

### State

Colorado as a whole is giving out more aid.  We have seen a large up tick in State aid especially from 2014-2015. This seems to trend with the GDP increases over time.  Students have been getting less Federal loans and more scholarships.  Federal loans have been on the decline since 2012 but still make up about 50% of all loans.

### Metro Areas

Boulder - Seen a large increase in the number of scholarships awarded. Boulder gave out about 30 million in total scholarships in 2016.  This is the highest among the schools.

Colorado Springs -  Been fairly consistent in the number of scholarships.  Federal aid in this metro area has been fairly stable as well.

Denver - Denver has seen the largest growth in federal loans along with state aid.  Denver has had a large growth in scholarships but is still way below that of boulder. Over 70% of funds are coming from the federal government loans.

Fort Collins - Fort Collins has had slow growth on in the total number of federal loans.  The number of scholarships has nearly tripled. Fort Collins has not had significant growth in state aid.

Greeley - Greeley has missed growth in giving out scholarships. There has also been no significant increase in State aid.  The amount of federal loans doubled in between 2004 and 2016.

Pueblo - Pueblo has gone through a few cycles in terms of amount of scholarships awarded. Pueblo has also trended up and back down in both federal loans and state aid.   

Western Slope - Seen double the amount in state aid from 2004 - 2016.  Unfortunately there are minimal scholarships given out to schools on the western slopes. Federal loans to theses school have also more than doubled.


## Degree simple analysis:

### State

Overall students are opting to get more certificates. We see a larger percentage of students opting for a certificate over the traditional 2-4 year degree.  We have also seen labor programs have been making a substantial come back over the last 10 years.

### Metro

Boulder - Boulder has students in either a community college or University.  More students have chosen to go to a community college over the University. Boulder has the largest percentage of masters and doctoral degrees awarded.  The education has the highest percentage of  students graduating with math/engineering and business degrees.


Colorado Springs - Colorado Springs has students in either a community college or University.  More students have chosen to go to a community college over the University, over 50%.  Roughly 60% of students have opted to get certificates and associate awards over the traditional bachelors degree.

Denver - Denver has students in either a community college, University, or state school.  Student distributions have been fairly consistent.  Students in this region have the 2nd highest masters degree rate. There has also been a upswing in doctoral degrees. A large percentage of the degrees are math and science focused. Labor degrees have almost doubled from 2001 to 2017

Fort Collins - Fort Collins has the largest rate of bachelor and masters students graduating.  They have seen a decrease in the rate of students getting doctoral degrees. Fort Collins has a fairly even distribution of all the degree groups.    

Greeley - Greeley has a large focus on social science, art/history, and physical/medical/wellness.  they have seen a down trend in masters students and a large increase in certificate graduates. The percentage of certificates awarded has over taken the number of bachelor degrees awarded. This could be from the large population of nurses/teachers graduating get both a degree and certificate.

Pueblo - Has seen a very large increase in the percentage of certificate graduates. Bachelors and masters degrees make up less than 40% of their graduating population. There is a large focus in physical/medical/wellness and arts/history, roughly 30% of students. Labor degrees have also increased dramatically.

Western Slope - Over 30% of students are opting for a certificate program.  These programs focus on the arts/history and social sciences. This is the only metro area that saw a downturn in the number of labor based degrees.
Collapse

## Business Formation simple analysis:

### State

The total number of businesses formed in the state of Colorado from 2001-2017 was 1,147,849. Out of the total number of businesses formed, 36.1% were still in good standing when the dataset was used in 2019. This means that approximately 64% of businesses are no longer in good standing and may be considered failed in most cases. Most companies formed were Limited Liability Companies with 76.7% of the overall share. Corporations were the second most popular at 18.8%.

When looking at the number of businesses formed per year, we looked at the raw count and then controlled for population growth by looking at how many companies were formed per 1000 residents. The raw numbers show approximately 30,000 businesses being formed in 2001, and almost 100,000 new businesses in 2017. This is over 3x the amount of companies being created in 2017 versus 2001. When controlled for population we saw approximately seven (7) companies per 1000 residents being formed in 2001 and almost eighteen (18) companies for every 1000 residents in 2017. This shows that people are creating more new companies in the latter years versus any other time before.

Looking at the population trends for the state we see a linear growth pattern. The population of the state is growing steadily from 2001 to 2017.

State GDP was looked at using GDP in current dollars, which showed an upward trend, but based on the population growth we expected this. So we then controlled for population growth by looking at the state real per capita GDP chained to 2012 dollars. When we look at the per capita GDP, we see less growth, but still a slight upward trend from 2001 to 2017, meaning that economic output is increasing per person.

### Metro

Boulder - The total number of businesses formed in the Boulder Metro Area from 2001-2017 was 87,542. This is approximately 8% of the total companies in our study. Out of the Boulder companies formed, the highest category of status is Good Standing with 38.8% of the share and Delinquent is a close second at 38.5% of the share. When looking at the types of companies formed during this time period, Limited Liability Companies are by far the preferred type with 79.6% of the companies. Corporations are second with 16.2% of the companies. The number of companies have gone up substantially since 2001. In 2001 there were approximately 2,800 companies formed and in 2017 this number grew to approximately 7,500. Then we looked at real per capita GDP for Boulder and saw an upward trend since a low in 2002.

Results: When comparing Boulder to the State, Boulder has a higher percentage of businesses in Good Standing, a higher percentage of Limited Liability Companies and a Lower percentage of Corporations. Boulder has a strong upward trend in the number of companies being formed per year. And Boulder has a higher real per capita GDP than the state average. This makes us believe that Boulder would be a good place to start a company due to its strong economy, increase in business formations, and percentage of companies in Good Standing. However, you may need to pay more than average for talent in this area.

Colorado Springs - The total number of businesses formed in the Colorado Springs Metro Area from 2001-2017 was 110,486. This is approximately 10% of the total companies in our study. Out of the Colorado Springs companies formed, the highest category of status is Delinquent with 44.1% of the share and Good Standing is second at 35.0% of the share. When looking at the types of companies formed during this time period, Limited Liability Companies are the preferred type with 73.2% of the companies. Corporations are second with 22.0% of the companies. The number of companies formed per year has gone up substantially since 2001. In 2001 there were approximately 2,800 companies formed and in 2017 this number grew to approximately 10,000. Then we looked at real per capita GDP for Colorado Springs and found a peak high in 2005 at 42,500 and then a decline to approximately 39,000 in 2014. Since 2014, Colorado Springs has seen real per capita GDP on the rise, with 2017 at almost 40,000.

Results: When comparing Colorado Springs to the State, it has a higher percentage of businesses in a Delinquent state, and a lower percentage of companies in Good Standing. It has a lower percentage of Limited Liability Companies and a higher percentage of Corporations. Colorado Springs has a strong upward trend in the number of companies being formed per year. However, Colorado Springs has a lower real per capita GDP than the state average, but it is trending upward since 2014. This makes us believe that Colorado Springs strengths include a strengthening economy and high number of new business formation. If considering a company there you may be able to pay less for labor since real per capita GDP is below the state average.

Denver - The total number of businesses formed in the Denver Metro Area from 2001-2017 was 615,787. This is approximately 54% of the total companies in our study. Out of the Denver companies formed, the highest category of status is Delinquent with 45.2% of the share and Good Standing is second at 33.8% of the share. When looking at the types of companies formed during this time period, Limited Liability Companies are the preferred type with 76.9% of the companies. Corporations are second with 19.2% of the companies. The number of companies formed per year has gone up substantially since 2001. In 2001 there were approximately 18,000 companies formed and in 2017 this number grew to over 50,000. Then we looked at real per capita GDP for Denver and found a local low in 2011 at 59,000 and then strong growth to over 64,000 in 2017.

Results: When comparing Denver to the State, it has a higher percentage of businesses in a Delinquent state, and a lower percentage of companies in Good Standing. It has a higher percentage of Limited Liability Companies and a higher percentage of Corporations. Denver has a strong upward trend in the number of companies being formed. Denver also has a higher real per capita GDP than the state average, and is showing a strong upward trend since 2013. This makes us believe that Denver strengths include a strong economy and high number of new business formation.


# Breakdown of Financial Entity Data

There are 29 unique institutions described in the dataset. For any given year, if the awardees associated with the institution was greater than 5% of total awardees for the year, the institution is represented. For all institutions which make up less than or equal to 5% of total awardees, that institution is grouped into 'Other'.

![2001](images/plots/yearly/pie_sum_2004.png)  | ![2009](images/plots/yearly/pie_sum_2009.png)  | ![2017](images/plots/yearly/pie_sum_2006.png)
------------- | -------------  | -------------

From 2004 to 2016 we can see still about half of students were using federal loans to pay for college. State aid paid to university stayed consistent percentage wise, hovering around 8-9%.

The data set does not look to include private loans or paying for school out of pocket.  This information could be useful for future analysis into indebtedness of students.

Looking at total federal loans and State aid we can see there is a large increase from 2004 to 2016.

![](images/plots/state_aid_sum_inst.png)

![](images/plots/federal_loans_sum_inst.png)

State aid was stagnant after the recession of 2009 while federal loans continued to climb.  State aid doubled from 2004 to 2016 giving students about 160 million is aid.  Federal loans nearly doubled as well indebting students by about 800 million dollars in 2016.

Scholarship levels have shown continual growth from 2004 - 2016.  
![](images/plots/scholar_sum_inst.png)


what we are seeing is students have incurred more debt but they have also gained more aid from the State and more scholarships are being given out.


## Breakdown by Metro Areas

To further break down the analysis into more granular segments, we did similar analysis on seven different 'metro' areas we defined. They are:

* Boulder
* Colorado Springs
* Denver
* Fort Collins
* Greeley
* Pueblo
* Grand Junction / Western Slope

![](images/plots/state_aid_sum_region.png) |![](images/plots/federal_loans_sum_region.png) |![](images/plots/scholar_sum_region.png)
------------- | -------------  | -------------
### Boulder

#### Breakdown by Aid Type

![2004](images/plots/region_year/pie_sum_0.png)  | ![2009](images/plots/region_year/pie_sum_5.png)  | ![2016](images/plots/region_year/pie_sum_12.png)
------------- | -------------  | -------------


#### Average Breakdown by Aid Type 2004-2016

![](images/plots/region/pie_sum_0.png)



### Colorado Springs

#### Breakdown by Aid Type

![2004](images/plots/region_year/pie_sum_13.png)  | ![2009](images/plots/region_year/pie_sum_18.png)  | ![2016](images/plots/region_year/pie_sum_25.png)
------------- | -------------  | -------------

#### Average Breakdown by Aid Type 2004-2016

![](images/plots/region/pie_sum_1.png)  

### Denver

#### Breakdown by Aid Type

![2004](images/plots/region_year/pie_sum_26.png)  | ![2009](images/plots/region_year/pie_sum_31.png)  | ![2016](images/plots/region_year/pie_sum_38.png)
------------- | -------------  | -------------

#### Average Breakdown by Aid Type 2004-2016

![2001](images/plots/region/pie_sum_2.png)

### Fort Collins

#### Breakdown by Aid Type

![2004](images/plots/region_year/pie_sum_39.png)  | ![2009](images/plots/region_year/pie_sum_44.png)  | ![2016](images/plots/region_year/pie_sum_51.png)
------------- | -------------  | -------------

#### Breakdown by Aid Type 2004-2016

![2001](images/plots/region/pie_sum_3.png)



### Greeley

#### Breakdown by by Aid Type

![2004](images/plots/region_year/pie_sum_65.png)  | ![2009](images/plots/region_year/pie_sum_70.png)  | ![2016](images/plots/region_year/pie_sum_77.png)
------------- | -------------  | -------------
------------- | -------------  | -------------

#### Breakdown by Aid Type 2004-2016

![2001](images/plots/region/pie_sum_5.png)

### Pueblo

#### Breakdown by by Aid Type

![2004](images/plots/region_year/pie_sum_91.png)  | ![2009](images/plots/region_year/pie_sum_96.png)  | ![2016](images/plots/region_year/pie_sum_103.png)
------------- | -------------  | -------------


#### Breakdown by Aid Type 2004-2016

![2001](images/plots/region/pie_sum_7.png)


### Grand Junction / Western Slope

#### Breakdown by by Aid Type

![2004](images/plots/region_year/pie_sum_52.png)  | ![2009](images/plots/region_year/pie_sum_57.png)  | ![2016](images/plots/region_year/pie_sum_64.png)
------------- | -------------  | -------------
------------- | -------------  | -------------

#### Breakdown by Aid Type 2004-2016

![2001](images/plots/region/pie_sum_4.png)

### Misc and Unassigned Schools

#### Breakdown by by Aid Type

![2004](images/plots/region_year/pie_sum_78.png)  | ![2009](images/plots/region_year/pie_sum_83.png)  | ![2016](images/plots/region_year/pie_sum_90.png)
------------- | -------------  | -------------



#### Breakdown by Aid Type 2004-2016

![2001](images/plots/region/pie_sum_6.png)



# Breakdown of Institutions' Awardees

There are 29 unique institutions described in the dataset. For any given year, if the awardees associated with the institution was greater than 5% of total awardees for the year, the institution is represented. For all institutions which make up less than or equal to 5% of total awardees, that institution is grouped into 'Other'.

![2001](images/institution_piecharts/2001.png)  | ![2009](images/institution_piecharts/2009.png)  | ![2017](images/institution_piecharts/2017.png)
------------- | -------------  | -------------

From 2001 to 2017 we can see still about half of institution awardees are enrolling in smaller institutions (those individual institutions which make of less than 5% of total awardees for the year).

We see the percent of awardees enrolling in community colleges and other more affordable institutions increasing. Front Range Community College, Colorado Mountain College, and Pikes Peak Community College are all more prevalent in 2017 than they were in 2001.

On the flip-side, larger more expensive institutions have seen the percent of awardees decreasing. This can be seen with Colorado State University, University of Colorado Denver, and University of Colorado Boulder from 2001 to 2017.

![2001-2017 stacked chart](images/stacked_perc_charts/intst_type.png)

#### Percentage of Awardees from Institution Types in 2001 and 2017

Year  | Universities | Community Colleges | State Colleges
------------- | ------------- | ------------- | -------------
2001  | 62%  | 27%  | 11%
2017  | 50%  | 34%  | 16%

Taking a more generalized approach, and looking at Universities, Community Colleges, and State Colleges, it is easier to see the same trends. The percentage of students receiving awards from smaller institutions (community colleges and state colleges) is increasing. Meanwhile, the percentage of students receiving awards from larger universities is decreasing.

## Breakdown of Awarded Degrees

Awardees of the institutions are in various degree programs, which include: Associate, Bachelor, Certificate, Doctoral, Masters, OtherGraduate, Professional, Specialist. We can look at how the breakdown of degrees have changed from 2001 to 2017.

![2001](images/degree_piecharts/2001.png)  | ![2009](images/degree_piecharts/2009.png)  | ![2017](images/degree_piecharts/2017.png)
------------- | -------------  | -------------

The percent of awardees enrolling in Bachelor and Masters degree programs have taken a dip from 2001 and 2017, while the percent of those awardees from institutions for Certificate degrees has increased (almost doubled). This seems to support the 'Breakdown of Institutions' analysis - less percentages of people are opting to go with the more expensive education options (large universities and longer degree programs) and more are opting to go with the less expensive options (more affordable universities and shorter degree programs).

![2001-2017 stacked chart](images/stacked_perc_charts/degree_type.png)

#### Percentage of Awardees from Degree Types in 2001 and 2017

Year  | Bachelors | Associate | Masters | Certificate
------------- | ------------- | ------------- | ------------- | -------------
2001  | 46%  | 21%  | 18% | 15%
2017  | 37%  | 19%  | 15% | 29%

The percentage of awards given out to Bachelors students has decreased by almost 10% while awards given out to students gaining Certificates has nearly doubled.

## Breakdown of Awardees Programs

Awardees of the institutions are more specifically in certain programs. The programs vary from sociology to welding to law and everything in between. Over 500 specific programs are detailed. We categorized these programs into nine buckets to make for easier analysis. The buckets are:
* Computer Science
* Art/History
* Social Science
* Math/Engineering
* Physical/Medical/Wellness
* Law
* General Science
* Labor
* Business

![2001](images/program_piecharts/2001.png)  | ![2009](images/program_piecharts/2009.png)  | ![2017](images/program_piecharts/2017.png)
------------- | -------------  | -------------

#### Percentage of Awardees from Program Types in 2001 and 2017

Year  | Social Science | Arts/History | Physical/Medical/Wellness | Labor/Trade
------------- | ------------- | ------------- | ------------- | -------------
2001  | 22%  | 23%  | 10% | 3%
2017  | 16%  | 19%  | 18% | 7%

We can see a bit of a shift from traditional programs like Social Sciences, The Arts, and History towards modern programs like computer science, health and wellness, as well as trade programs.


## Breakdown by Metro Areas

To further break down the analysis into more granular segments, we did similar analysis on seven different 'metro' areas we defined. They are:

* Boulder
* Colorado Springs
* Denver
* Fort Collins
* Greeley
* Pueblo
* Grand Junction (Western Slope)

### Boulder

#### Breakdown by Institution Type

![2001](images/boulder/boulder2001_type.png)  | ![2009](images/boulder/boulder2009_type.png)  | ![2017](images/boulder/boulder2017_type.png)
------------- | -------------  | -------------

#### Breakdown by Degree

![2001](images/boulder/boulder2001_degree.png)  | ![2009](images/boulder/boulder2009_degree.png)  | ![2017](images/boulder/boulder2017_degree.png)
------------- | -------------  | -------------

#### Breakdown by Program

![2001](images/boulder/boulder2001_prog.png)  | ![2009](images/boulder/boulder2009_prog.png)  | ![2017](images/boulder/boulder2017_prog.png)
------------- | -------------  | -------------

### Colorado Springs

#### Breakdown by Institution Type

![2001](images/colorado_springs/csprings2001_type.png)  | ![2009](images/colorado_springs/csprings2009_type.png)  | ![2017](images/colorado_springs/csprings2017_type.png)
------------- | -------------  | -------------

#### Breakdown by Degree

![2001](images/colorado_springs/csprings2001_degree.png)  | ![2009](images/colorado_springs/csprings2009_degree.png)  | ![2017](images/colorado_springs/csprings2017_degree.png)
------------- | -------------  | -------------

#### Breakdown by Program

![2001](images/colorado_springs/csprings2001_prog.png)  | ![2009](images/colorado_springs/csprings2009_prog.png)  | ![2017](images/colorado_springs/csprings2017_prog.png)
------------- | -------------  | -------------

### Denver

#### Breakdown by Institution Type

![2001](images/denver/denver2001_type.png)  | ![2009](images/denver/denver2009_type.png)  | ![2017](images/denver/denver2017_type.png)
------------- | -------------  | -------------

#### Breakdown by Degree

![2001](images/denver/denver2001_degree.png)  | ![2009](images/denver/denver2009_degree.png)  | ![2017](images/denver/denver2017_degree.png)
------------- | -------------  | -------------

#### Breakdown by Program

![2001](images/denver/denver2001_prog.png)  | ![2009](images/denver/denver2009_prog.png)  | ![2017](images/denver/denver2017_prog.png)
------------- | -------------  | -------------

### Fort Collins

#### Breakdown by Institution Type

![2001](images/ftcollins/ftcollins2001_type.png)  | ![2009](images/ftcollins/ftcollins2009_type.png)  | ![2017](images/ftcollins/ftcollins2017_type.png)
------------- | -------------  | -------------

#### Breakdown by Degree

![2001](images/ftcollins/ftcollins2001_degree.png)  | ![2009](images/ftcollins/ftcollins2009_degree.png)  | ![2017](images/ftcollins/ftcollins2017_degree.png)
------------- | -------------  | -------------

#### Breakdown by Program

![2001](images/ftcollins/ftcollins2001_prog.png)  | ![2009](images/ftcollins/ftcollins2009_prog.png)  | ![2017](images/ftcollins/ftcollins2017_prog.png)
------------- | -------------  | -------------

### Greeley

#### Breakdown by Institution Type

![2001](images/greeley/greeley2001_type.png)  | ![2009](images/greeley/greeley2009_type.png)  | ![2017](images/greeley/greeley2017_type.png)
------------- | -------------  | -------------

#### Breakdown by Degree

![2001](images/greeley/greeley2001_degree.png)  | ![2009](images/greeley/greeley2009_degree.png)  | ![2017](images/greeley/greeley2017_degree.png)
------------- | -------------  | -------------

#### Breakdown by Program

![2001](images/greeley/greeley2001_prog.png)  | ![2009](images/greeley/greeley2009_prog.png)  | ![2017](images/greeley/greeley2017_prog.png)
------------- | -------------  | -------------

### Pueblo

#### Breakdown by Institution Type

![2001](images/pueblo/pueblo2001_type.png)  | ![2009](images/pueblo/pueblo2009_type.png)  | ![2017](images/pueblo/pueblo2017_type.png)
------------- | -------------  | -------------

#### Breakdown by Degree

![2001](images/pueblo/pueblo2001_degree.png)  | ![2009](images/pueblo/pueblo2009_degree.png)  | ![2017](images/pueblo/pueblo2017_degree.png)
------------- | -------------  | -------------

#### Breakdown by Program

![2001](images/pueblo/pueblo2001_prog.png)  | ![2009](images/pueblo/pueblo2009_prog.png)  | ![2017](images/pueblo/pueblo2017_prog.png)
------------- | -------------  | -------------

### Grand Junction (Western Slope)

#### Breakdown by Institution Type

![2001](images/wslope/wslope2001_type.png)  | ![2009](images/wslope/wslope2009_type.png)  | ![2017](images/wslope/wslope2017_type.png)
------------- | -------------  | -------------

#### Breakdown by Degree

![2001](images/wslope/wslope2001_degree.png)  | ![2009](images/wslope/wslope2009_degree.png)  | ![2017](images/wslope/wslope2017_degree.png)
------------- | -------------  | -------------

#### Breakdown by Program

![2001](images/wslope/wslope2001_prog.png)  | ![2009](images/wslope/wslope2009_prog.png)  | ![2017](images/wslope/wslope2017_prog.png)
------------- | -------------  | -------------


# Breakdown of Business Entity Data

We then looked at business entity formation data to get an idea of whether start-ups were growing or shrinking in Colorado and the specific metro areas. We wanted to see if areas with higher number of start-ups saw an increase in per capita GDP. We used per capita GDP as our target metric because it measures the total output of the economy while accounting for population growth or decline within those areas. We used the real per capita GDP so that we had a specific dollar value to tie it to to control for inflation over time. For this section we used data from many sources including but not limited to the Colorado Department of State, U.S. Bureau of Economic Analysis, Federal Reserve Bank of St. Louis, and the Colorado Department of Local Affairs. From these sources we used population data, state GDP data, business entity formation data, and real per capita GDP data for state and metro areas.  

Our main dataset was the Business Entity Dataset from CDOS - Colorado Department of State, a CIM dataset. From here we focused our study on the years 2001-2017 in order to match it with the Degrees Awarded dataset above. We then found data to match this time period for state population, state GDP (current dollars), and state and metro area real per capita GDP (chained 2012 dollars for state GDP and chained 2009 dollars for metro area GDP) to complete our analysis. We decided to focus on seven (7) metro areas across Colorado, including Denver-Aurora-Lakewood, Boulder, Colorado Springs, Fort Collins, Grand Junction, Greeley, and Pueblo.

## Cleaning and Preparing the Data

We started by cleaning and preparing the data. Initially, our dataset consisted of 1,848,357 rows (businesses formed) and 35 columns of data. The first record of an entity formation date started at 03/05/1864 and ended at 4/11/2019.

We then checked for null values using some code and then the missingno matrix plot.

![Missing Data - Raw Entity Formation Dataset](images/all_bus_msno.png)

We then dropped all unnecessary columns and rows from the dataset to focus on our intended time period and saved a new clean csv with that data. Then we filtered the data and dropped any unnecessary rows in order to target the metro areas. We did this by creating a dictionary mapping the metro area to all zip codes contained within that metro area. Once we had that data cleaned and prepped, we created a new csv file with that data.

Reference: The cleaning and preparation of the business dataset can be found in the go-code-co_data_clean Jupyter Notebook.  

## State Business Entity, Population, and Gross Domestic Product (GDP) Summary Data for Entire Time Period 2001-2017

Total Number of Businesses Formed 2001-2017: 1,147,849

Status of Businesses Formed:

![Entity Status](images/Top4EntityStatusofAllBusinessesFormed2001-2017.png)

Entity Status  | Total Businesses | Percent of Total
------------- | ------------- | -------------
Delinquent  | 486,725 | 42.40%
Good Standing  | 408,635  | 35.60%
Voluntarily Dissolved  | 208,854  | 18.20%
Administratively Dissolved  | 27,006  | 2.35%
Noncompliant  | 12,288  | 1.07%
Withdrawn  | 2,159  | 0.19%
Exists  | 2,066  | 0.18%
Dissolved (Term Expired)  | 99  | 0.01%
Judicially Dissolved  | 16  | 0.00%
Effectiveness Prevented  | 1  | 0.00%

Type of Businesses Formed:

![Entity Type](images/Top3EntityTypesofAllBusinessesFormed2001-2017.png)

Entity Type  | Total Businesses | Percent of Total
------------- | ------------- | -------------
Limited Liability Company  | 864,556 | 75.32%
Corporation  | 211,689  | 18.44%
Nonprofit Corporation  | 50,853  | 4.43%
Limited Liability Partnership  | 6,931  | 0.60%
Limited Liability Limited Partnership  | 6,062  | 0.53%
Limited Partnership  | 4,293  | 0.37%
General Partnership  | 2,146  | 0.19%
Limited Partnership Association  | 374  | 0.03%
Cooperative  | 316  | 0.03%
Unincorporated Nonprofit Association  | 267 | 0.02%
Corporation Sole | 173 | 0.02%
Limited Cooperative Association | 100 | 0.01%
Cooperative Association | 79 | 0.01%
Foreign Limited Liability Company | 4 | 0.00%
Ditch Company | 4 | 0.00%
Foreign Other | 1 | 0.00%
Foreign Corporation | 1 | 0.00%

Number of Businesses Formed Per Year:

![Number of Businesses Formed Per Year](images/StateNumberofBusinessesFormedPerYear.png) | ![Number of Businesses Per 1000 Residents](images/StateBusinessesFormedPer1000Residents.png)
----- | -----
Number of Businesses Formed Per Year | Number of Businesses Per 1000 Residents

State Population Trends:

![State Population](images/PopulationPerYearinColorado2001-2017.png) | ![State Population Zoomed In](images/StatePopulationPerYear.png)
----- | -----
State Population | State Population Trend with Linear Regression Line Zoomed-in

State Gross Domestic Product (GDP) Trends:

![GDP](images/StateGDP2001-2017LinearRegressioninCurrentDollars.png) | ![Real Per Capita GDP](images/StateRealGDPPerCapita2001-2017LinearRegression.png)
----- | -----
State GDP (current dollars) | State Real Per Capita GDP Trend (chained 2012 dollars)


## Breakdown of Metro Areas 2001-2017

After looking at state-wide data, we decided to break out seven (7) metro areas and compare them to each other using the state data as a benchmark. We looked at entity status, entity type and real per capita GDP chained to 2009 dollars. Unfortunately, we were not able to find reliable population data that matched our areas as well as timeline so we were not able to compare the number of businesses per 1000 residents to the state's analysis.

Metro Areas:
* Boulder
* Colorado Springs
* Denver (Denver-Aurora-Lakewood)
* Grand Junction
* Greeley
* Fort Collins
* Pueblo


### Boulder Metro Area

Total Number of Businesses Formed in Boulder:  87,542

Status of Businesses Formed:

![Entity Status](images/Top4EntityStatusofBoulderBusinessesFormed2001-2017.png)

Entity Status  | Total Businesses
------------- | -------------
Good Standing  | 33,499  
Delinquent | 33,278
Voluntarily Dissolved  | 17,476  
Administratively Dissolved  | 2,196

Type of Businesses Formed:

![Entity Type](images/Top3EntityTypesofBoulderBusinessesFormed2001-2017.png)

Entity Type  | Total Businesses
------------- | -------------
Limited Liability Company  | 68,603
Corporation  | 13,957  
Nonprofit Corporation  | 3,672


Number of Businesses Formed Per Year:

![Number of Businesses Formed Per Year](images/BoulderNumberofBusinessesFormedPerYear.png)

Real Per Capita GDP (chained 2009 dollars) Trends:

![Real Per Capita GDP](images/BoulderRealGDPPerCapita2001-2017.png) | ![Real Per Capita GDP Zoomed-in](images/BoulderRealGDPPerCapita2001-2017Zoomed.png)
----- | -----
Real Per Capita GDP | Real Per Capita GDP Zoomed-in


### Colorado Springs Metro Area

Total Number of Businesses Formed in Colorado Springs:  110,486

Status of Businesses Formed:

![Entity Status](images/Top4EntityStatusofColoradoSpringsBusinessesFormed2001-2017.png)

Entity Status  | Total Businesses
------------- | -------------
Delinquent | 48,004
Good Standing  | 38,082  
Voluntarily Dissolved  | 20,426  
Administratively Dissolved  | 2,261


Type of Businesses Formed:

![Entity Type](images/Top3EntityTypesofColoradoSpringsBusinessesFormed2001-2017.png)

Entity Type  | Total Businesses
------------- | -------------
Limited Liability Company  | 79,255
Corporation  | 23,811
Nonprofit Corporation  | 5,169


Number of Businesses Formed Per Year:

![Number of Businesses Formed Per Year](images/ColoradoSpringsNumberofBusinessesFormedPerYear.png)

Real Per Capita GDP (chained 2009 dollars) Trends:

![Real Per Capita GDP](images/ColoradoSpringsRealGDPPerCapita2001-2017.png) | ![Real Per Capita GDP Zoomed-in](images/ColoradoSpringsRealGDPPerCapita2001-2017Zoomed.png)
----- | -----
Real Per Capita GDP | Real Per Capita GDP Zoomed-in


### Denver (Denver-Aurora-Lakewood) Metro Area

Total Number of Businesses Formed in Denver: 615,787

Status of Businesses Formed:

![Entity Status](images/Top4EntityStatusofDenverBusinessesFormed2001-2017.png)

Entity Status  | Total Businesses
------------- | -------------
Delinquent | 274,455
Good Standing | 205,182
Voluntarily Dissolved | 111,268
Administratively Dissolved | 15,979

Type of Businesses Formed:

![Entity Type](images/Top3EntityTypesofDenverBusinessesFormed2001-2017.png)

Entity Type  | Total Businesses
------------- | -------------
Limited Liability Company  | 465,610
Corporation  | 116,056
Nonprofit Corporation  | 23,564

Number of Businesses Formed Per Year:

![Number of Businesses Formed Per Year](images/DenverNumberofBusinessesFormedPerYear.png)

Real Per Capita GDP (chained 2009 dollars) Trends:

![Real Per Capita GDP](images/DenverRealGDPPerCapita2001-2017.png) | ![Real Per Capita GDP Zoomed-in](images/DenverRealGDPPerCapita2001-2017Zoomed.png)
----- | -----
Real Per Capita GDP | Real Per Capita GDP Zoomed-in


### Grand Junction Metro Area

Total Number of Businesses Formed in Grand Junction: 25,141

Status of Businesses Formed:

![Entity Status](images/Top4EntityStatusofGrandJunctionBusinessesFormed2001-2017.png)

Entity Status  | Total Businesses
------------- | -------------
Delinquent | 10,878
Good Standing | 9,222
Voluntarily Dissolved | 4,269
Administratively Dissolved | 418

Type of Businesses Formed:

![Entity Type](images/Top3EntityTypesofGrandJunctionBusinessesFormed2001-2017.png)

Entity Type  | Total Businesses
------------- | -------------
Limited Liability Company  | 19,052
Corporation  | 4,105
Nonprofit Corporation  | 1,457

Number of Businesses Formed Per Year:

![Number of Businesses Formed Per Year](images/GrandJunctionNumberofBusinessesFormedPerYear.png)

Real Per Capita GDP (chained 2009 dollars) Trends:

![Real Per Capita GDP](images/GrandJunctionRealGDPPerCapita2001-2017.png) | ![Real Per Capita GDP Zoomed-in](images/GrandJunctionRealGDPPerCapita2001-2017Zoomed.png)
----- | -----
Real Per Capita GDP | Real Per Capita GDP Zoomed-in


### Greeley Metro Area

Total Number of Businesses Formed in Greeley: 44,006

Status of Businesses Formed:

![Entity Status](images/Top4EntityStatusofGreeleyBusinessesFormed2001-2017.png)

Entity Status  | Total Businesses
------------- | -------------
Delinquent | 18,118
Good Standing | 16,975
Voluntarily Dissolved | 7,372
Administratively Dissolved | 847

Type of Businesses Formed:

![Entity Type](images/Top3EntityTypesofGreeleyBusinessesFormed2001-2017.png)

Entity Type  | Total Businesses
------------- | -------------
Limited Liability Company  | 34,374
Corporation  | 6,943
Nonprofit Corporation  | 1,871

Number of Businesses Formed Per Year:

![Number of Businesses Formed Per Year](images/GreeleyNumberofBusinessesFormedPerYear.png)

Real Per Capita GDP (chained 2009 dollars) Trends:

![Real Per Capita GDP](images/GreeleyRealGDPPerCapita2001-2017.png) | ![Real Per Capita GDP Zoomed-in](images/GreeleyRealGDPPerCapita2001-2017Zoomed.png)
----- | -----
Real Per Capita GDP | Real Per Capita GDP Zoomed-in


### Fort Collins Metro Area

Total Number of Businesses Formed in Fort Collins: 64,084

Status of Businesses Formed:

![Entity Status](images/Top4EntityStatusofFortCollinsBusinessesFormed2001-2017.png)

Entity Status  | Total Businesses
------------- | -------------
Good Standing | 25,624
Delinquent | 24,670
Voluntarily Dissolved | 11,593
Administratively Dissolved | 1,274

Type of Businesses Formed:

![Entity Type](images/Top3EntityTypesofFortCollinsBusinessesFormed2001-2017.png)

Entity Type  | Total Businesses
------------- | -------------
Limited Liability Company  | 50,325
Corporation  | 9,709
Nonprofit Corporation  | 2,944

Number of Businesses Formed Per Year:

![Number of Businesses Formed Per Year](images/FortCollinsNumberofBusinessesFormedPerYear.png)

Real Per Capita GDP (chained 2009 dollars) Trends:

![Real Per Capita GDP](images/FortCollinsRealGDPPerCapita2001-2017.png) | ![Real Per Capita GDP Zoomed-in](images/FortCollinsRealGDPPerCapita2001-2017Zoomed.png)
----- | -----
Real Per Capita GDP | Real Per Capita GDP Zoomed-in


### Pueblo Metro Area

Total Number of Businesses Formed in Pueblo: 14,930

Status of Businesses Formed:

![Entity Status](images/Top4EntityStatusofPuebloBusinessesFormed2001-2017.png)

Entity Status  | Total Businesses
------------- | -------------
Delinquent | 6,617
Good Standing | 5,212
Voluntarily Dissolved | 2,533
Administratively Dissolved | 325

Type of Businesses Formed:

![Entity Type](images/Top3EntityTypesofPuebloBusinessesFormed2001-2017.png)

Entity Type  | Total Businesses
------------- | -------------
Limited Liability Company  | 10,872
Corporation | 2,896
Nonprofit Corporation | 842

Number of Businesses Formed Per Year:

![Number of Businesses Formed Per Year](images/PuebloNumberofBusinessesFormedPerYear.png)

Real Per Capita GDP (chained 2009 dollars) Trends:

![Real Per Capita GDP](images/PuebloRealGDPPerCapita2001-2017.png) | ![Real Per Capita GDP Zoomed-in](images/PuebloRealGDPPerCapita2001-2017Zoomed.png)
----- | -----
Real Per Capita GDP | Real Per Capita GDP Zoomed-in


# Data Sets

### CIM Data:

Business Entity Data: CDOS - Colorado Department of State (https://www.sos.state.co.us/biz/BusinessEntityCriteriaExt.do).  
Link: https://data.colorado.gov/Business/Business-Entities-in-Colorado/4ykn-tg5h

Post-Secondary Financial Aid Demographics in Colorado - Financial Aid averages based on demographic breakdown of post-secondary students since 2004 from the Colorado Department of Higher Education (CDHE).
Link: https://data.colorado.gov/Higher-Education/Post-Secondary-Financial-Aid-Demographics-in-Color/g53r-j5td

Degrees Awarded: CDHE - Colorado Department of Higher Education (http://highered.colorado.gov/).  
Link: https://data.colorado.gov/Higher-Education/Degrees-Awarded-to-Post-Secondary-Graduates-in-Col/hxf8-ab6k


### Non-CIM Data:

Total Per Capita Real GDP Colorado Springs (chained 2009 dollars, not seasonally adjusted): U.S. Bureau of Economic Analysis, Total Per Capita Real Gross Domestic Product for Colorado Springs, CO (MSA) [PCRGMP17820], retrieved from FRED, Federal Reserve Bank of St. Louis; April 10, 2019.
Link: https://fred.stlouisfed.org/series/PCRGMP17820

Total Per Capita Real GDP Boulder (chained 2009 dollars, not seasonally adjusted): U.S. Bureau of Economic Analysis, Total Per Capita Real Gross Domestic Product for Boulder, CO (MSA) [PCRGMP14500], retrieved from FRED, Federal Reserve Bank of St. Louis; April 10, 2019.
Link: https://fred.stlouisfed.org/series/PCRGMP14500

State Population Data: Colorado Department of Local Affairs.
Link: https://demography.dola.colorado.gov/births-deaths-migration/data/components-change/

State GDP (millions of current dollars): U.S. Bureau of Economic Analysis, Total Gross Domestic Product for Colorado 2001-2017.
Link: https://apps.bea.gov/itable/iTable.cfm?ReqID=70&step=1#reqid=70&step=1&isuri=1

State Per capita real GDP (chained 2012 dollars, not seasonally adjusted): U.S. Bureau of Economic Analysis 2001-2017.
Link: https://apps.bea.gov/itable/iTable.cfm?ReqID=70&step=1#reqid=70&step=1&isuri=1

Total Per Capita Real GDP Denver-Aurora-Lakewood (chained 2009 dollars, not seasonally adjusted): U.S. Bureau of Economic Analysis, Total Per Capita Real Gross Domestic Product for Denver-Aurora-Lakewood, CO (MSA) [PCRGMP19740], retrieved from FRED, Federal Reserve Bank of St. Louis; April 10, 2019.
Link: https://fred.stlouisfed.org/series/PCRGMP19740

Total Per Capita Real GDP Pueblo (chained 2009 dollars, not seasonally adjusted): U.S. Bureau of Economic Analysis, Total Per Capita Real Gross Domestic Product for Pueblo, CO (MSA) [PCRGMP39380], retrieved from FRED, Federal Reserve Bank of St. Louis; April 10, 2019.
Link: https://fred.stlouisfed.org/series/PCRGMP39380

Total Per Capita Real GDP Fort Collins (chained 2009 dollars, not seasonally adjusted): U.S. Bureau of Economic Analysis, Total Per Capita Real Gross Domestic Product for Fort Collins, CO (MSA) [PCRGMP22660], retrieved from FRED, Federal Reserve Bank of St. Louis; April 10, 2019.
Link: https://fred.stlouisfed.org/series/PCRGMP22660

Total Per Capita Real GDP Greeley (chained 2009 dollars, not seasonally adjusted): U.S. Bureau of Economic Analysis, Total Per Capita Real Gross Domestic Product for Greeley, CO (MSA) [PCRGMP24540], retrieved from FRED, Federal Reserve Bank of St. Louis; April 10, 2019.
Link: https://fred.stlouisfed.org/series/PCRGMP24540

Total Per Capita Real GDP Grand Junction (chained 2009 dollars, not seasonally adjusted): U.S. Bureau of Economic Analysis, Total Per Capita Real Gross Domestic Product for Grand Junction, CO (MSA) [PCRGMP24300], retrieved from FRED, Federal Reserve Bank of St. Louis; April 10, 2019.
Link: https://fred.stlouisfed.org/series/PCRGMP24300
