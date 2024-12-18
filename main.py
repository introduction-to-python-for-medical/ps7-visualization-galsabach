# Import libraries
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import fetch_openml

data = fetch_openml(name='wine', version=1, as_frame=True)
print(data.DESCR)
df = data.frame
df.sample(5)
df.describe()
df.dtypes
features = list(df.columns)
print("Available features:", features)
selected_features = [features[0], features[2], features[4], features[6], features[7]]
print("Selected features: ", selected_features)
fig, axs  = plt.subplots(1, len(selected_features), figsize = (20,3))
for ax, f in zip(axs, selected_features):
    ax.hist(df[f], bins=5, color='skyblue', edgecolor='black')
    ax.set_xlabel(f)
x=df[selected_features[0]]
y=df[selected_features[1]]
plt.scatter(x,y)
plt.xlabel(selected_features[0])
plt.ylabel(selected_features[1])
plt.show()
reference_feature = selected_features[1]
y = df[reference_feature]
fig, axs  = plt.subplots(1, len(selected_features), figsize = (20,3))
for ax, f in zip(axs, features):
  ax.scatter(df[f], y)
  ax.set_xlabel(f)

plt.show()
reference_feature = selected_features[0]  
comparison_feature = selected_features[1] 

# Create a scatter plot for the selected pair
plt.figure(figsize=(8, 6))
plt.scatter(df[reference_feature], df[comparison_feature], alpha=0.7, color='purple', s=50)
plt.title(f'Scatter Plot: {reference_feature} vs {comparison_feature}', fontsize=16, weight='bold')
plt.xlabel(reference_feature, weight='bold')
plt.ylabel(comparison_feature, weight='bold')
# Save the plot as an image file
plt.savefig('correlation_plot.png')
plt.show()

