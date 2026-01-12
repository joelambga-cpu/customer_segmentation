import pandas as pd
from sklearn.cluster import KMeans

def segment_customers(df: pd.DataFrame, n_clusters: int = 3) -> pd.DataFrame:
    """
    Applica KMeans per segmentare i clienti.
    Restituisce DataFrame con colonna 'Cluster'.
    """
    features = df[['Età', 'Reddito_mensile', 'Spesa_mensile']]
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    df['Cluster'] = kmeans.fit_predict(features)
    return df
