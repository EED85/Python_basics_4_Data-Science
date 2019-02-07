#%% [markdown]
# # import packages

#%%
import numpy as np
import pandas as pd
from pandas import Series,DataFrame

#%% [markdown]
# # Creating Dataframes


#%% [markdown]
# ## with Dictonary
d = {'name' : ['EED','J','Marge'],'height' : [1.80,1.7,1.6]}
df = DataFrame(d)
df.head()

#%% [markdown]
# ## with a list
d1 = {'name' : "EED",'age' : 30}
d2 = {'name' : 'J','age' : 29}
d3 = {'name' : 'Meggie','age' : 25}
l= []
l.append(d1);l.append(d2);l.append(d3)
df1 = DataFrame(l)
df1.head()

#%% [markdown]
# ## with an named index for row and column 
df2 = DataFrame({'eyecolor':['green','green']
                ,'haircolor':['brown','red']},
                index=pd.Index(['EED','J'],name='name')
                ,columns=pd.Index(['eyecolor','haircolor'],name = 'attribute')
                )
df2.head()
#%% [markdown]
# ## Clipboard
# df3 = DataFrame
# df3.read_clipboard()
# df3.head()





#%% [markdown]
# # Creating Index
df1 = df1.set_index('name')
df = df.set_index('name')


#%% [markdown]
# # Basic Operations

#%% [markdown]
# ## remove column


# ## adding new column
# ### one value 

df2['weight'] = np.NaN
df2

#%% [markdown]

# ## replace


#%% [markdown]

# # Merging on Index 1:1

# ## inner join
pd.merge(df,df1,left_index=True,right_index=True,how='inner')

#%% [markdown]

# ## outer join
pd.merge(df,df1,left_index=True,right_index=True,how='outer')

#%% [markdown]

# ## right join
pd.merge(df,df1,left_index=True,right_index=True,how='right')

#%% [markdown]

# ## left join
pd.merge(df,df1,left_index=True,right_index=True,how='left')

#%% [markdown]

# # Merging on columns
# ##inner join

pd.merge(df,df1,left_on='name',right_on='name',how='inner')



