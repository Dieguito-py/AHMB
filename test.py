import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('dados.csv')

data['timestamp'] = pd.to_datetime(data['timestamp'])
data['timestamp'] = (data['timestamp'] - pd.Timestamp("1970-01-01")) // pd.Timedelta('1s')

le = LabelEncoder()
data['activity'] = le.fit_transform(data['activity'])

X = data.drop('activity', axis=1)
y = data['activity']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier()
model.fit(X_train, y_train)

# create confusion matrix
y_true = [0, 1, 2, 0, 1, 2, 0, 1, 2]
y_pred = [0, 1, 2, 1, 1, 2, 0, 0, 2]

labels = ['Class 0', 'Class 1', 'Class 2']

cm = confusion_matrix(y_true, y_pred)

plt.figure(figsize=(10, 8))
sns.heatmap(cm, annot=True, cmap='Blues', fmt='g', xticklabels=labels, yticklabels=labels)
plt.xlabel('Predicted')
plt.ylabel('True')
plt.title('Confusion Matrix')
plt.show()