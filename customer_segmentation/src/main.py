from src.data_loader import load_data
from src.segmentation import segment_customers
from src.visualization import plot_clusters

def main():
    df = load_data("data/clienti.csv")
    df_segmented = segment_customers(df, n_clusters=3)
    print(df_segmented)
    plot_clusters(df_segmented)

if __name__ == "__main__":
    main()
