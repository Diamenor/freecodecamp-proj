import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    
    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'],
                color="#8bd3c7")

    
    # Create first line of best fit
    fit = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Once a line is written by Y = aX + b, 
    # where 'a' represents the slope and 'b' the intersection of the line,
    # we can say that:
    X = np.arange(df['Year'].min(),2051)
    Y = fit.slope * X + fit.intercept

    plt.plot(X,Y, color="#fd7f6f")

    
    # Create second line of best fit
    df_2000 = df[df['Year'] >= 2000]

    fit = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])

    X = np.arange(df_2000['Year'].min(),2051)
    Y = fit.slope * X + fit.intercept

    plt.plot(X,Y, color="#bd7ebe")


    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()