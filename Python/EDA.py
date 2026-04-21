import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('titanic.csv')
print((df.isna().sum()))
df['Age']=df['Age'].fillna(df['Age'].mean())
print((df.isna().sum()))
# print(dir(df))
# print(help(pd.DataFrame.map))
df["Cabin"]=df['Cabin'].map(lambda x: 0 if pd.isna(x) else 1)
print(df['Cabin'])
df['Sex']=df['Sex'].map({'male':0,'female':1})
plt.hist(df['Age'], bins=5, color='skyblue', edgecolor='black')
plt.title("Distribution of Column")
plt.show()


plt.scatter(df['Age'], df['Sex'], alpha=0.5)
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.show()

sns.pairplot(df, hue='Survived') 
plt.show()

corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Matrix")
plt.show()