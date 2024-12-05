# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D

# Load dataset
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
columns = ["Pregnancies", "Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI", "DiabetesPedigree", "Age", "Outcome"]
data = pd.read_csv(url, header=None, names=columns)

# a) Correlation and Scatter Plots
plt.figure(figsize=(10, 6))
sns.heatmap(data.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Matrix")
plt.show()

sns.pairplot(data, vars=["Glucose", "BMI", "Age", "Insulin"], hue="Outcome", diag_kind="kde")
plt.show()

# b) Histograms
data.hist(bins=20, figsize=(15, 10), color='skyblue', edgecolor='black')
plt.suptitle("Histograms of Dataset Features")
plt.show()

# c) Three-dimensional Plotting
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(data['Glucose'], data['BMI'], data['Age'], c=data['Outcome'], cmap='viridis')
ax.set_xlabel("Glucose")
ax.set_ylabel("BMI")
ax.set_zlabel("Age")
ax.set_title("3D Scatter Plot: Glucose, BMI, Age")
plt.show()
