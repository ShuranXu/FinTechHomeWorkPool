# Homework 6 - Pythonic Monopoly

![Toronto at night](Images/toronto.jpg)

The Homework 6 includes Rental Analysis Report and Toronto Dwelling Analysis Dashboard. 

## __Rental Analysis Report__

The rental analysis report is located at Starter_Code/rental_analysis.ipynb. It includes the following parts:

- Dwelling Types Per Year
- Average Monthly Shelter Costs in Toronto Per Year
- Average House Value per Year
- Average Prices By Neighbourhood
- Number of Dwelling Types per Year
- Top 10 Most Expensive Neighbourhoods
- Neighbourhood Map
- Cost Analysis

To run rental_analysis.ipynb, open up Jupyter Lab, setup execution environment that contains pyviz and then run all cells.

## __Toronto Dwelling Analysis Dashboard__

This dashboard presents a visual analysis of historical house values, dwelling types per neighbourhood and dwelling costs in Toronto, Ontario according to census data from 2001 to 2016. 

Users can navigate through the tabs above to explore more details about the evolution of the real estate market across these years

The dashboard includes the following tabs:

- Welcome Page (Neighbourhood Map)
- Year Market Analysis
- Sheltor Costs vs House Value
- Neighbourhood Analysis
- Top Expensive Neighbourhood

To run the datashboard, navigate to Starter_Code/dashboard.ipynb, setup execution environment that contains pyviz and then run all cells. Please note that missing mapbox environment variable could prevent plots including scatter map from drawing. 

_Note_: To  run dashboard as an web app, make sure `dashboard.servable()` is executed and navigate to Starter_Code/ and run `./run.sh`. 