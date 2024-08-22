import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

data = pd.read_csv(r'C:\Users\user\Downloads\python-sample-vscode-flask-tutorial-main\python-sample-vscode-flask-tutorial-main/employee.csv')
print(data)


plt.hist(data['Age'], bins=10, edgecolor='black')

    # Add titles and labels
plt.title('Histogram of Employee Ages')
plt.xlabel('Age')
plt.ylabel('Frequency')

    # Show the plot
plt.show()


