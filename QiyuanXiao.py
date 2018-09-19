import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.DataFrame.from_csv("F:\\UIUC\\590DV\\homework2\\gun-violence.csv")

# question 1
killedn = df['n_killed'].sum()
print(str(killedn)+" people have been killed.")
plt.plot(df['date'], df['n_killed'])
plt.show()

# question 2
injuredn = df['n_injured'].sum()
print(str(injuredn)+" people have been injured.")
plt.plot(df['date'], df['n_injured'])
plt.show()

# question 3
def filter_m(inp, column, value):
    output = {}
    good = inp[column] >= value
    for k in inp:
        output[k] = inp[k][good]
    return output

def filter_l(inp, column, value):
    output = {}
    good = inp[column] <= value
    for k in inp:
        output[k] = inp[k][good]
    return output

counti = 0
for index, row in df.iterrows():
    if row['date'] >= '2013-1-1' and row['date'] <= '2013-2-1':
        counti += row['n_injured']
print(str(counti) + " people have been injured between Jan.1st 2013 and Feb.1st 2013.")

years_filter = filter_m(filter_l(df, 'date', '2013-2-1'), 'date', '2013-1-1')
plt.plot(years_filter['date'],years_filter['n_injured'])
plt.show()

# question 4
# I don't know which field represent involved in the gun violence. I suppose all data in 'gun-violence' is involved in gun violence?

# question 5
df2 = df.sort_values(by='n_injured', ascending=False)
countnj = 1
print("The locations of the top 10 highest number of injuries are:")
while(countnj <= 10):
    for index, row in df2.iterrows():
        countnj += 1
        print(row['address'])
