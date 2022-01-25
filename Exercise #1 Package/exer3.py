import pandas as pd
names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,95,77,78,99]
GradeList = zip(names,grades)
df = pd.DataFrame(data=GradeList,
columns=['Names','Grades'])
df
df['Grades'].count() # number of values
df['Grades'].mean()  # arithmetic average
df['Grades'].std()   # standard deviation
df['Grades'].min()   # minimum
df['Grades'].max()   # maximum
df['Grades'].quantile(.25)  # first quartile
df['Grades'].quantile(.5)   # second quartile
df['Grades'].quantile(.75)  # third quartile

