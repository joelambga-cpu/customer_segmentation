# Customer Segmentation

A Python learning project that groups fictional customers with K-means using age, monthly income and monthly spending.

## Workflow

Read the sample CSV, assign three clusters, print the resulting table and display an income-versus-spending scatter plot.

## Installation and usage

From a terminal with Python available:

```powershell
git clone https://github.com/joelambga-cpu/customer_segmentation.git
cd customer_segmentation/customer_segmentation
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m src.main
```

On macOS/Linux, replace `.\.venv\Scripts\python.exe` with `.venv/bin/python`.

## Method and limitations

The current implementation uses raw, unscaled features and `random_state=42`. Income and spending therefore have a larger numerical scale than age. The three-cluster choice is illustrative; cluster quality and stability have not been validated. Cluster labels are not established customer personas or evidence of commercial impact.

## Files

- [Fictional customer data](customer_segmentation/data/clienti.csv)
- [Clustering implementation](customer_segmentation/src/segmentation.py)
- [Visualization](customer_segmentation/src/visualization.py)
