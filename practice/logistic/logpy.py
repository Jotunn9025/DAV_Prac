from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report,accuracy_score,ConfusionMatrixDisplay,confusion_matrix
import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv('titanic.csv')
df['Age']=df['Age'].fillna(df['Age'].mean())
df['Sex']=df['Sex'].map({
    "male":0,"female":1
})
df["Cabin"]=df["Cabin"].map(lambda x: 0 if pd.isna(x) else 1)
print(df.head())

model=LogisticRegression()
X=df.drop(["PassengerId","Name","Ticket","SibSp","Parch","Embarked","Survived"],axis=1)
y=df["Survived"]
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
model.fit(X_train,y_train)
y_pred=model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test,y_pred):.2f}")
print("Classification Report:")
print(classification_report(y_test,y_pred))
cm=confusion_matrix(y_test,y_pred)
disp=ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot()
plt.show()