import pandas as pd

df = pd.read_csv('exer1.csv')


df[['Value']] = df[['Value']].apply(pd.to_numeric, errors='coerce')

print (df['Value'].mean())



# 4 more functions of Pandas

sum1 = df['Year'].sum()
max1 = df['Year'].max()
min1 = df['Year'].min()
count1 = df['Year'].count()

print ('Sum: ' + str(sum1))
print ('Max: ' + str(max1))
print ('Min: ' + str(min1))
print ('Count: ' + str(count1))

