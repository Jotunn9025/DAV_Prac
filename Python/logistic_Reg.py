import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay,accuracy_score, classification_report

df = pd.read_csv("titanic.csv")
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1}) 
df['Age'] = df['Age'].fillna(df['Age'].mean())
df = df[['Pclass', 'Sex', 'Fare', 'Age', 'Survived']].dropna() 
X = df.drop('Survived', axis=1)
y = df['Survived']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

accuracy_score = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy_score:.2f}")
print("Classification Report:")
print(classification_report(y_test, y_pred))
cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=['Died', 'Survived'])

disp.plot(cmap='Blues', values_format='d')
plt.title("Titanic Survival Confusion Matrix")
plt.show()