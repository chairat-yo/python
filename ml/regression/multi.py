import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

# df = pd.read_csv(r'C:\Users\Admin\Desktop\Learn+AI+ML+Sourcecode+dataset\data\advertising_1.csv')
df = pd.read_csv(r'C:\Users\Admin\Desktop\Learn+AI+ML+Sourcecode+dataset\data\advertising_1.csv', index_col=0)
print(df.head())

df.isnull().sum()

# plt.scatter(df.TV, df.Sales)
# plt.show()

print(df.corr())

sns.pairplot(data=df, x_vars=['TV', 'Radio', 'Newspaper'], y_vars='Sales', height=3.5, kind='reg')
plt.show()