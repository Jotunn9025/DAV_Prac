import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df=pd.read_csv('rawsal.csv')
df['x']=df['YearsExperience']
df['y']=df['Salary']
df['x2']=df['x']**2
df['xy']=df['x'] * df['y']
n=len(df)
a1=(n*df['xy'].sum()-df['x'].sum()*df['y'].sum())/((n*df['x2'].sum())-(df['x'].sum()**2))
a0=df['y'].mean()-df['x'].mean()*a1
line_df=np.linspace(df['x'].min(),df['x'].max(),100)
pred_line=a0+a1*line_df
plt.scatter(df['x'],df['y'])
plt.plot(line_df,pred_line,color="red")
plt.show()