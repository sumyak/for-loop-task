import pandas as pd
data= pd.read_csv('https://raw.githubusercontent.com/sumyak/COVID-19/master/task%208/datasets_557629_1188648_StatewiseTestingDetails.csv')

#print(data)
a=input("Enter a Indian State/UnionTerritory:")
#print(data.loc[(data['State'] == a)])
print("Enter the dates")
b=input("Enter the start : ")
c=input("Enter the end : ")
d=(list(data.index[(data['Date'] == b)&( data['State']==a)]))
d1=' '.join(map(str,d))
d2=int(d1)
e=(list(data.index[(data['Date'] == c)&( data['State']==a)]))
e1=' '.join(map(str,e))
e2=int(e1)
df=(data[d2:e2])
print(df)
Positive=(list(df['Positive']))
Negative=(list(df['Negative']))
TotalSamples=(list(df['TotalSamples']))
index=(list(df['Date']))
df1 = pd.DataFrame({'negative cases': Negative,'TotalSamples':TotalSamples,
                  'positive cases': Positive}, index=index)
ax = df1.plot.barh()
