import matplotlib.pyplot as plt
import seaborn as sns

def plot_clusters(df):
    """Grafico dei cluster clienti per Reddito e Spesa"""
    plt.figure(figsize=(8,6))
    sns.scatterplot(
        data=df, x='Reddito_mensile', y='Spesa_mensile',
        hue='Cluster', palette='Set2', s=100
    )
    plt.title('Segmentazione Clienti')
    plt.xlabel('Reddito Mensile')
    plt.ylabel('Spesa Mensile')
    plt.legend(title='Cluster')
    plt.show()
