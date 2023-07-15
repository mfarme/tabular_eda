import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from IPython.display import HTML

def describe(df):
    """Generate descriptive statistics."""
    print(df.describe().to_html())

def histograms(df):
    """Plot histograms of columns.""" 
    for col in df.columns:
        plt.figure()
        sns.distplot(df[col])
        plt.title(col)
        plt.tight_layout()
        
    return HTML(plt.gcf().canvas.toDataURL())

def correlations(df):
    """Plot correlations between columns."""
    corr = df.corr()
    plt.figure()
    sns.heatmap(corr, 
                xticklabels=corr.columns,
                yticklabels=corr.columns)
    
    return HTML(plt.gcf().canvas.toDataURL())
    
def package(df):
    """Generate EDA report."""
    
    report = f"<h1>Exploratory Data Analysis</h1>" 
    report += f"<h2>Dataset Shape: {df.shape}</h2>"
    
    describe(df)
    histograms(df)
    correlations(df)
    
    print(report)