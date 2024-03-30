# main.py

from data_import import import_data
from data_cleaning import clean_data
from data_analysis import analyze_data
from data_visualization import visualize_data

def main():
    # Import data
    data = import_data("data.csv")
    
    # Clean data
    clean_data(data)
    
    # Analyze data
    results = analyze_data(data)
    
    # Visualize data
    visualize_data(results)

if __name__ == "__main__":
    main()
