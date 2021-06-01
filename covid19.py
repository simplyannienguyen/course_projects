import io
import pandas as pd
import requests as r
pd.set_option('display.max_columns', 500)

filepath = r"C:\Users\VBoadi\OneDrive\Documents\TTU MASTERS\FALL2020\ISQS6339_Business Intelligence\Final Project/"
filetoprocess1= 'https://covidtracking.com/data/download/florida-history.csv'
filetoprocess2='https://covidtracking.com/data/download/new-york-history.csv'
filetoprocess3='https://covidtracking.com/data/download/california-history.csv'
filetoprocess4='https://covidtracking.com/data/download/texas-history.csv'
filetoprocess5='https://covidtracking.com/data/download/colorado-history.csv'
filetoprocess6='https://covidtracking.com/data/download/wisconsin-history.csv'
filetoprocess7='https://covidtracking.com/data/download/illinois-history.csv'
filetoprocess8= 'https://covidtracking.com/data/download/washington-history.csv'
filetoprocess9='https://covidtracking.com/data/download/alabama-history.csv'
filetoprocess10='https://covidtracking.com/data/download/arizona-history.csv'
filetoprocess11='https://covidtracking.com/data/download/georgia-history.csv'
fileout = 'Final.csv'

###############################################################################
#                      File Read direct from Web Request                      #
###############################################################################
res1 = r.get(filetoprocess1)
res1.status_code
df_FL = pd.read_csv(io.StringIO(res1.text))  
df_FL

res2 = r.get(filetoprocess2)
res2.status_code
df_NY = pd.read_csv(io.StringIO(res2.text))  
df_NY

res3 = r.get(filetoprocess3)
res3.status_code
df_CA = pd.read_csv(io.StringIO(res3.text))  
df_CA

res4 = r.get(filetoprocess4)
res4.status_code
df_TX = pd.read_csv(io.StringIO(res4.text))  
df_TX

res5 = r.get(filetoprocess5)
res5.status_code
df_CO = pd.read_csv(io.StringIO(res5.text))  
df_CO

res6 = r.get(filetoprocess6)
res6.status_code
df_WI = pd.read_csv(io.StringIO(res6.text))  
df_WI

res7 = r.get(filetoprocess7)
res7.status_code
df_IL = pd.read_csv(io.StringIO(res7.text))  
df_IL

res8 = r.get(filetoprocess8)
res8.status_code
df_WA = pd.read_csv(io.StringIO(res8.text))  
df_WA

res9 = r.get(filetoprocess9)
res9.status_code
df_AL = pd.read_csv(io.StringIO(res9.text))  
df_AL

res10 = r.get(filetoprocess10)
res10.status_code
df_AZ = pd.read_csv(io.StringIO(res10.text))  
df_AZ

res11 = r.get(filetoprocess11)
res11.status_code
df_GA = pd.read_csv(io.StringIO(res11.text))  
df_GA

###############################################################################
#                        Appended/Clean Up                                    #
###############################################################################

df  = [df_FL,df_NY,df_CA,df_TX,df_CO,
          df_WI,df_IL,df_WA,df_AL,df_AZ,df_GA]


df_append = pd.concat(df)

df_results = df_append[['date','state','death','hospitalized','negative',
                        'positive','totalTestsPeopleAntibody','totalTestsPeopleViral']]


df_results['death'].fillna(0, inplace=True)
df_results['hospitalized'].fillna(0, inplace=True)
df_results['negative'].fillna(0, inplace=True)
df_results['positive'].fillna(0, inplace=True)


###############################################################################
#                        Corr/Outputs                                        #
###############################################################################


corr_Matrix = df_results.corr()

print(corr_Matrix)

df_results.to_csv(filepath + fileout, sep=',', index=False)

###############################################################################

