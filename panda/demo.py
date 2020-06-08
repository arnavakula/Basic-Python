import pandas

df1 = pandas.DataFrame([[2, 4, 6], [10, 20, 30]], columns = ['Price', 'Age', 'Value'], index = ['First', 'Second'])
print(df1)

df2 = pandas.DataFrame([{'Name': 'John', 'Surname':'Lennon'}, {'Name': 'Jack'}])
print(df2)

print(df1.mean().mean()) #first mean returns a panda-series, second returns a float
print(df1.Price.max(), df1.Price.min())