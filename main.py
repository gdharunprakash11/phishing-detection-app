import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib

# load dataset
data = pd.read_csv("PhiUSIIL_Phishing_URL_Dataset.csv")

# numeric features only
X = data.select_dtypes(include=['number'])
y = data["label"]

# split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# model create
model = LogisticRegression(max_iter=2000)

# train
model.fit(X_train, y_train)

# predict
y_pred = model.predict(X_test)

# accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# save model (LAST step)
joblib.dump(model, "phishing_model.pkl")
print("Model saved ✅")