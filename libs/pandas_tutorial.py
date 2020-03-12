import numpy as np
import pandas as pd

data = np.array([['', 'Col1', 'Col2'],
                 ['Row1', 1, 2],
                 ['Row2', 3, 4]])
np_2d=np.array([[3,2],[5,4]])
df=pd.DataFrame(data=np_2d,

                   columns=data[0, 1:])
df_dict=pd.DataFrame(data={1: ['1', '3'], 2: ['1', '2'], 3: ['2', '4']})

print('basic dataframe',df)
print('simple dataframe',df_dict)

pd_series=pd.Series({"Belgium":"Brussels", "India":"New Delhi", "United Kingdom":"London", "United States":"Washington"})
print('Series pandas ',pd_series)

print('df.shape',df.shape)
print('df.index',df.index)
print('df.loc',df.loc[0][1])
print('df.iloc',df.iloc[1]['Col2'])
print('df.iloc to selelct rows',df.iloc[0])
print('df.iloc to selelct coulumns',df.iloc[:,0].tolist())
print('set_index',df.set_index('Col2'))
print('reset_index',df.reset_index(level=0,drop=True,inplace=True))
df['col3']=[1,2]
# df.insert(2,'Col3',[],True)
# df.assign(col3=[1,2])
# df.append([8,7],ignore_index=True)
print(df)

data1 = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Height': [5.1, 6.2, 5.1, 5.2],
        'Qualification': ['Msc', 'MA', 'Msc', 'Msc']}

# Convert the dictionary into DataFrame
df1 = pd.DataFrame(data1)

# Declare a list that is to be converted into a column
address = ['Delhi', 'Bangalore', 'Chennai', 'Patna']

# Using 'Address' as the column name
# and equating it to the list
df1['Address'] = address
df1.insert(3, "Age", [21, 23, 24, 21], False)
# df1 = df.assign(address1 = ['Delhi', 'Bangalore', 'Chennai', 'Patna'])

print('after inserting column',df1)
print('df.drop',df.drop('Col1',axis=1,inplace=True))
print(df)
df=df.append(pd.DataFrame(data=[[1,2]],columns=['col3','Col2']),ignore_index=True)
print('after adding rows',df)
print('df.drop_duplicate',df.drop_duplicates(keep='last'))
print('df.drop',df.drop(df.index[2]))
print('df.rename',df.rename(columns={'col3':'Col3'},index={1:'one'}))
print('df.replace',df,df.replace([1,2],['one','two'],inplace=True))
print('map',df.iloc[0].map(lambda str:str.upper()))
# print(df.apply(lambda str:str.upper()))
print(df.applymap(lambda Str:Str.upper() if type(Str)==str else Str+1))
empty_df = pd.DataFrame(np.nan, index=[0,1,2,3], columns=['A'])
print('empty_df',empty_df)
# print('df.pivot',df.pivot(index='ol3',values='Col1'))
#pivot
#stack
#unstack
#melt
#iterrows
#to_csv
#to_excel
#read_cssv

