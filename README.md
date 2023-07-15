# tabular_eda
Tabular EDA is a Python package for quick Exploratory Data Analysis on tabular datasets.

It provides easy to use functions for:

-Generating descriptive statistics
-Plotting histograms
-Visualizing correlations

The analysis is output in a clean HTML report showcasing the key aspects of your dataset.
Installation
Copy code

    pip install git+https://github.com/user/eda.git

## Usage
    import eda

    df = pd.read_csv("data.csv") 

    report = eda.describe(df)
    print(report)

## Contributing
Contributions to Tabular EDA are welcome! Please open an issue or pull request on GitHub.

## License
Tabular EDA is licensed under the MIT License. See LICENSE file for more details.
