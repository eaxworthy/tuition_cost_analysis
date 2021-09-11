# -*- coding: utf-8 -*-
"""
@author: SamDe
"""

'''
This program creates a pandas dataframe from a .csv, which i have already done some inital
preparation on. The data comes from the US Department of Accrediation.
It contains data on every accredited institution of higher education in the country.
source: https://ope.ed.gov/dapip/#/download-data-files
furtheremore, i added a column called "ranking" which I added the US News and World Reports
Top 25 rankings to the respective schools (the rankings are for 2021).

What this program does is load the file, delete extraneous columns, add a new column with "region", do some aggregating by region, and perform a chi-square test.
The program also saves several .csvs with the munged and then appended versions of the file, in case I want to use these later.

The main questions I am interested in answering are:
Where are the top 25 schools located (what regions of the country?)
Where are the schools in the country located in general?
Is there a significant difference between the regions schools are located in the country and where the top 25 schools are located?

I was able to answer these questions successfully.
It turns out the highest proportion of schools are in the midwest and the south, but the highest proprtion of top 25 schools
are in the northeast and the west. There is a significant statistical difference betweent the distribution of schools across the country
and the distribution of the top 25 schools that cannot be explaiend by chance alone.

'''

import csv
import pandas as pd
import numpy as np


df = pd.read_csv('C:\\Users\\SamDe\\Desktop\\MS\\IST_652_Python\\homework\\homework1\\accredited_institutions.csv', index_col=0)
df

'''
               parent_institution_id  ... ranking
institution_id                        ...        
128540                             -  ...       1
121150                             -  ...       2
129905                             -  ...       3
108676                             -  ...       4
121415                             -  ...       4
                             ...  ...     ...
251251                             -  ...       0
251279                             -  ...       0
251288                             -  ...       0
251297                             -  ...       0
251303                             -  ...       0

[32915 rows x 15 columns]
'''
type(df)
'''
pandas.core.frame.DataFrame
'''
df.columns
'''
Index(['parent_institution_id', 'ope_id', 'institution_name',
       'parent_institution_name', 'institution_type', 'city', 'inst_state',
       'zipcode', 'complete_address', 'general_phone', 'admin_name',
       'admin_phone', 'admin_email', 'last_updated_by_dept_of_edu', 'ranking'],
      dtype='object')
'''
df.dtypes
'''
parent_institution_id           object
ope_id                          object
institution_name                object
parent_institution_name         object
institution_type                object
city                            object
inst_state                      object
zipcode                        float64
complete_address                object
general_phone                   object
admin_name                      object
admin_phone                     object
admin_email                     object
last_updated_by_dept_of_edu     object
ranking                        int64
dtype: object
'''
del df['parent_institution_id'],df['ope_id'],df['parent_institution_name'],df['institution_type'],df['city'],df['zipcode'],df['complete_address'], df['general_phone'],df['admin_name'],df['admin_phone'],df['admin_email'],df['last_updated_by_dept_of_edu']

df

df.to_csv('C:\\Users\\SamDe\\Desktop\\MS\\IST_652_Python\\homework\\homework1\\accredited_institutions_select_fields_only.csv')

'''
 institution_name  ... ranking
institution_id                                                     ...        
128540                                       Princeton University  ...       1
121150                                         Harvard University  ...       2
129905                Columbia University in the City of New York  ...       3
108676                                            Yale University  ...       4
121415                      Massachusetts Institute of Technology  ...       4
                                                          ...  ...     ...
251251                          The Skin Institute Internationale  ...       0
251279          Omni Eye Services of Atlanta Residency in Ocul...  ...       0
251288          Omni Eye Center Residency in Ocular Disease an...  ...       0
251297          Bright Eyes Vision Clinic Residency in Pediatr...  ...       0
251303          Vision Northwest Residency in Vision Therapy R...  ...       0

[32915 rows x 3 columns]
'''
df.columns
'''
Index(['institution_name', 'inst_state', 'ranking'], dtype='object')
'''
df.dtypes
'''
institution_name    object
inst_state          object
ranking              int64
dtype: object
'''
df = df.head(25)

df = df.set_index(np.arange(0,25))

df

'''
                               institution_name inst_state  ranking
0                          Princeton University         NJ        1
1                            Harvard University         MA        2
2   Columbia University in the City of New York         NY        3
3                               Yale University         CT        4
4         Massachusetts Institute of Technology         MA        4
5                         University of Chicago         IL        6
6                           Stanford University         CA        6
7                    University of Pennsylvania         PA        8
8            California Institute of Technology         CA        9
9                       Northwestern University         IL        9
10                     Johns Hopkins University         MD        9
11                              Duke University         NC       12
12                            Dartmouth College         NH       13
13                             Brown University         RI       14
14                        Vanderbilt University         TN       14
15            Washington University in St Louis         MO       16
16                              Rice University         TX       16
17                           Cornell University         NY       18
18                     University of Notre Dame         IN       19
19       University of California - Los Angeles         CA       20
20                             Emory University         GA       21
21           University of California, Berkeley         CA       22
22                        Georgetown University         DC       23
23            University of Southern California         CA       24
24           University of Michigan - Ann Arbor         MI       24

[25 rows x 3 columns]
'''
# save this as a csv

df.to_csv('C:\\Users\\SamDe\\Desktop\\MS\\IST_652_Python\\homework\\homework1\\top_25_accredited_institutions.csv')

# examine the data another way

for row in df.loc[:, ['institution_name','inst_state','ranking']].itertuples():
    print(row)
'''
Pandas(Index=0, institution_name='Princeton University', inst_state='NJ', ranking=1)
Pandas(Index=1, institution_name='Harvard University', inst_state='MA', ranking=2)
Pandas(Index=2, institution_name='Columbia University in the City of New York', inst_state='NY', ranking=3)
Pandas(Index=3, institution_name='Yale University', inst_state='CT', ranking=4)
Pandas(Index=4, institution_name='Massachusetts Institute of Technology', inst_state='MA', ranking=4)
Pandas(Index=5, institution_name='University of Chicago', inst_state='IL', ranking=6)
Pandas(Index=6, institution_name='Stanford University', inst_state='CA', ranking=6)
Pandas(Index=7, institution_name='University of Pennsylvania', inst_state='PA', ranking=8)
Pandas(Index=8, institution_name='California Institute of Technology', inst_state='CA', ranking=9)
Pandas(Index=9, institution_name='Northwestern University', inst_state='IL', ranking=9)
Pandas(Index=10, institution_name='Johns Hopkins University', inst_state='MD', ranking=9)
Pandas(Index=11, institution_name='Duke University', inst_state='NC', ranking=12)
Pandas(Index=12, institution_name='Dartmouth College', inst_state='NH', ranking=13)
Pandas(Index=13, institution_name='Brown University', inst_state='RI', ranking=14)
Pandas(Index=14, institution_name='Vanderbilt University', inst_state='TN', ranking=14)
Pandas(Index=15, institution_name='Washington University in St Louis', inst_state='MO', ranking=16)
Pandas(Index=16, institution_name='Rice University', inst_state='TX', ranking=16)
Pandas(Index=17, institution_name='Cornell University', inst_state='NY', ranking=18)
Pandas(Index=18, institution_name='University of Notre Dame', inst_state='IN', ranking=19)
Pandas(Index=19, institution_name='University of California - Los Angeles', inst_state='CA', ranking=20)
Pandas(Index=20, institution_name='Emory University', inst_state='GA', ranking=21)
Pandas(Index=21, institution_name='University of California, Berkeley', inst_state='CA', ranking=22)
Pandas(Index=22, institution_name='Georgetown University', inst_state='DC', ranking=23)
Pandas(Index=23, institution_name='University of Southern California', inst_state='CA', ranking=24)
Pandas(Index=24, institution_name='University of Michigan - Ann Arbor', inst_state='MI', ranking=24)
'''

# this is a dictionary that has the regions of states
# i will use it to add regions to the dataframe
# source: https://code.activestate.com/recipes/580661-states-to-regions/
'''
N - Northeast 
W - West 
M - Midwest 
S - South 
O - Other
'''

regions = {
        'AK': 'O',
        'AL': 'S',
        'AR': 'S',
        'AS': 'O',
        'AZ': 'W',
        'CA': 'W',
        'CO': 'W',
        'CT': 'N',
        'DC': 'N',
        'DE': 'N',
        'FL': 'S',
        'GA': 'S',
        'GU': 'O',
        'HI': 'O',
        'IA': 'M',
        'ID': 'W',
        'IL': 'M',
        'IN': 'M',
        'KS': 'M',
        'KY': 'S',
        'LA': 'S',
        'MA': 'N',
        'MD': 'N',
        'ME': 'N',
        'MI': 'W',
        'MN': 'M',
        'MO': 'M',
        'MP': 'O',
        'MS': 'S',
        'MT': 'W',
        'NA': 'O',
        'NC': 'S',
        'ND': 'M',
        'NE': 'W',
        'NH': 'N',
        'NJ': 'N',
        'NM': 'W',
        'NV': 'W',
        'NY': 'N',
        'OH': 'M',
        'OK': 'S',
        'OR': 'W',
        'PA': 'N',
        'PR': 'O',
        'RI': 'N',
        'SC': 'S',
        'SD': 'M',
        'TN': 'S',
        'TX': 'S',
        'UT': 'W',
        'VA': 'S',
        'VI': 'O',
        'VT': 'N',
        'WA': 'W',
        'WI': 'M',
        'WV': 'S',
        'WY': 'W'
}

# making a list of regions for the states in the dataframe
region = []
for state in df['inst_state']:
    region.append(regions[state])
    print(len(region))
# adding the list as a pandas series to the dataframe
df['region'] = region


df.loc[:,['inst_state','region']]
'''
   inst_state region
0          NJ      N
1          MA      N
2          NY      N
3          CT      N
4          MA      N
5          IL      M
6          CA      W
7          PA      N
8          CA      W
9          IL      M
10         MD      N
11         NC      S
12         NH      N
13         RI      N
14         TN      S
15         MO      M
16         TX      S
17         NY      N
18         IN      M
19         CA      W
20         GA      S
21         CA      W
22         DC      N
23         CA      W
24         MI      W
'''
# i am going to save a csv at the end that has the region for every institution, so i'll do this in a little bit

# now i can group by region


regions_top_25 = df.groupby(['region']).size().reset_index(name='counts')
regions_top_25
'''
  region  counts
0      M       4
1      N      11
2      S       4
3      W       6
'''
# let's save this as a new csv
# for some reason i was able to use backslash before but then it started raising errors so i'm using forward slashes for paths.
# i guess that's a Pandas idosyncracy
regions_top_25.to_csv('C:/Users/SamDe/Desktop/MS/IST_652_Python/homework/homework1/regions_top25.csv')

# and i can look at the mean ranking of school by region
regions_top_25.groupby(['region']).mean()
'''
        ranking
region         
M         12.50
N          9.00
S         15.75
W         17.50
'''
# this is somewhat misleading as most of the top 10 are in the northeast

top_10 = regions_top_25.head(10)
regions_top_10 = top_10.groupby(['region']).size().reset_index(name='counts')

'''
  region  counts
0      M       2
1      N       6
2      W       2
'''

# we will save this too
regions_top_10.to_csv('C:/Users/SamDe/Desktop/MS/IST_652_Python/homework/homework1/regions_top_10.csv')
top_10.groupby(['region']).mean()
'''
         ranking
region          
M       7.500000
N       3.666667
W       7.500000
'''
# mean isn't really a great measure for this
# i would say count is the best

# let's look at all the institutions again and add regions, then groupby region and get a count
df = pd.read_csv('C:\\Users\\SamDe\\Desktop\\MS\\IST_652_Python\\homework\\homework1\\accredited_institutions_select_fields_only.csv', index_col=0)

# this is the file i saved earlier

df.head()
'''
                                           institution_name inst_state  ranking
institution_id                                                                 
128540                                 Princeton University         NJ        1
121150                                   Harvard University         MA        2
129905          Columbia University in the City of New York         NY        3
108676                                      Yale University         CT        4
121415                Massachusetts Institute of Technology         MA        4
'''
df.tail()
'''
                                                 institution_name  ... ranking
institution_id                                                     ...        
251251                          The Skin Institute Internationale  ...       0
251279          Omni Eye Services of Atlanta Residency in Ocul...  ...       0
251288          Omni Eye Center Residency in Ocular Disease an...  ...       0
251297          Bright Eyes Vision Clinic Residency in Pediatr...  ...       0
251303          Vision Northwest Residency in Vision Therapy R...  ...       0
'''
# adding regions

region = []
for state in df['inst_state']:
    if state in regions.keys():
        region.append(regions[state])
        continue
    else:
        region.append('U')
        # we will use U for unknown, it seems that there are some missing values here
        continue

df['region'] = region
df
'''
                                                 institution_name  ... region
institution_id                                                     ...       
128540                                       Princeton University  ...      N
121150                                         Harvard University  ...      N
129905                Columbia University in the City of New York  ...      N
108676                                            Yale University  ...      N
121415                      Massachusetts Institute of Technology  ...      N
                                                          ...  ...    ...
251251                          The Skin Institute Internationale  ...      O
251279          Omni Eye Services of Atlanta Residency in Ocul...  ...      S
251288          Omni Eye Center Residency in Ocular Disease an...  ...      W
251297          Bright Eyes Vision Clinic Residency in Pediatr...  ...      M
251303          Vision Northwest Residency in Vision Therapy R...  ...      W

[32915 rows x 4 columns]
'''
# save this one
df.to_csv('C:/Users/SamDe/Desktop/MS/IST_652_Python/homework/homework1/accredited_institutions_select_fields_with_regions.csv')

# time to group
regions_all = df.groupby(['region']).size().reset_index(name='counts')
regions_all
'''
  region  counts
0      M    9975
1      N    6912
2      O     514
3      S    7921
4      U     422
5      W    7171
'''
# let's look at these as proportions
regions_all['proportion'] = regions_all['counts'] / df[df.columns[0]].count()
# and let's do a sort
regions_all.sort_values('proportion', ascending = False)
'''
  region  counts  proportion
0      M    9975    0.303053
3      S    7921    0.240650
5      W    7171    0.217864
1      N    6912    0.209995
2      O     514    0.015616
4      U     422    0.012821
'''
# so it looks like the largest proportion of schools in the country are actually in the midwest and the south
# compare that to the top 25 proportions
regions_top_25['proportion'] = regions_top_25['counts'] / 25
regions_top_25.sort_values('proportion', ascending = False)
'''
  region  counts  proportion
1      N      11        0.44
3      W       6        0.24
0      M       4        0.16
2      S       4        0.16
'''
# it looks like there is a definite difference between these distributions
# i suspect a chi-square test will reveal that is the case
# i will look up how to do one in Python

# i need to get rid of the unknown and other in regions_all to use this as my expected frequencies
regions_all_observed = regions_all.loc[[0,1,3,5],].reset_index()
del regions_all_observed['index']
regions_all_observed
'''
  region  counts  proportion
0      M    9975    0.303053
1      N    6912    0.209995
2      S    7921    0.240650
3      W    7171    0.217864
'''
# side-by-side comparison with the top 25
regions_top_25
'''
  region  counts  proportion
0      M       4        0.16
1      N      11        0.44
2      S       4        0.16
3      W       6        0.24
'''

import scipy.stats as stats
alpha = 0.05
# observed frequency is first argument, expected frequency is second argument
chi_square = chi_square = stats.chisquare(regions_top_25['counts'],regions_all_observed['counts'])

p_value = chi_square[1]
conclusion = "Failed to reject the null hypothesis."
if p_value <= alpha:
    conclusion = "Null Hypothesis is rejected."
        
print("chisquare-score is:", chi_square[0], " and p value is:", p_value)
print(conclusion)
'''
chisquare-score is: 31929.02614996437  and p value is: 0.0
Null Hypothesis is rejected.
'''
# so we can conclude that the differences in the distribution of schools in the top 25 compared to all schools is not by chance alone