import pandas as pd
import matplotlib.pyplot as plt


def load_data():
    df = pd.read_csv('data.csv')

    # Fixing columns names
    df.columns = [col.strip() for col in df.columns]

    return df

df = load_data()

def plotScatter():
    """
    Generates a scatter plot with a legend based on the specified columns in a pandas DataFrame.

    Args:
        None
    Returns:
        None (displays the plot)

    """

    print(list(df.columns))

    x_col = input('Select X axis column: ')
    y_col = input('Select Y axis column: ')

    colors = {'Developing': 0, 'Developed': 1}

    # Drop rows with missing values in the specified columns
    sub_df = df.dropna(subset=[x_col, y_col], axis=0).reset_index(drop=True)

    # Map categorical values to numerical values using the colors dictionary
    status_numerical = sub_df['Status'].map(colors)


    # Create the scatter plot
    fig, ax = plt.subplots()
    scatter = ax.scatter(sub_df[x_col], sub_df[y_col], c=status_numerical, alpha=0.8)

    # Set the title and axis labels
    ax.set_title(f"{y_col} vs. {x_col}")
    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)

    # create a dictionary to map numerical values to string labels
    labels = {0: 'Developing', 1: 'Developed'}

    # Add a legend to the plot using the labels dictionary
    legend = ax.legend(*scatter.legend_elements(), loc='lower right')
    for i, label in labels.items():
        legend.get_texts()[i].set_text(label)

    plt.show()

def plotPie():
    """
    Plots a pie chart of the variable of a given country over the years.

    Parameters:
    -----------
    None

    Returns:
    --------
    None
        This function doesn't return anything. It just displays the plot.

    Example:
    --------
    plotPie('Afghanistan')
    """
    country = input('Select country from countries.txt file: ')

    print('Features:')
    # Print the list of available columns and ask the user to select one
    print(list(df.columns))
    variable = input('Select Feature other than Year: ')

    # Get the feature for the given country
    x = df[df.Country == country][['Year',variable]]

    try:
        # Create the pie chart
        fig, ax = plt.subplots(figsize = (7,7))
        plt.pie(x[variable], labels=x.Year, autopct='%1.1f%%')

        # Add a title to the chart
        plt.title(f'{variable} of {country} over years')

        # Show the plot
        plt.show()
    except:
        print('Cannot create pie chart for given inputs.\nPlease try again with other country or feature.')


def plotBar():
    """
    Plots a bar chart for comparison of countries over different variables

    Parameters:
    -----------
    None

    Returns:
    --------
    None
        This function doesn't return anything. It just displays the plot.

    Example:
    --------
    plotBar()
    """

    print('Features:')
    # Print the list of available columns and ask the user to select one
    print(list(df.columns))
    column = input('Select Column: ')

    # Get the data for the selected country and column
  
    x = df.groupby('Country')[column].agg('mean').sort_values(ascending=False)[:20]

    fig, ax = plt.subplots(figsize = (10,5))
    plt.bar(x.index, x.values)
    plt.xticks(rotation=45, ha='right')
    plt.title(f'Comparison of top 20 countries in {column}')
    plt.xlabel('Country')
    plt.ylabel(column)
    plt.show()
