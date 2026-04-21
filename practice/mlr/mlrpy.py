from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,r2_score
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df=pd.read_csv('sales.csv')
model=LinearRegression()
X=df.drop("sales",axis=1)
y=df["sales"]
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)
model.fit(X_train,y_train)
y_pred=model.predict(X_test)
print(r2_score(y_test,y_pred))


sns.scatterplot(x=y_test, y=y_pred)
plt.plot([y_test.min(), y_test.max()],
         [y_test.min(), y_test.max()],
         color="red")

plt.show()