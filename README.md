# Stock and Revenue Data Visualization Project 

This project retrives, processes, and visualizes historical data stock and revenue from Tesla and GameStop. 

## Fetures 
#### Data Retrival 
yfinance library was used to fetch the stock data.
Revenue data was avaliable publicly on HTML tables, used requests and BeatifulSoup to scrape the data.
#### Data Cleaning
Revenue data was cleaned by removing commas, dollar sign, and empty values.
Convert the data into strucured pandas DataFrames.
#### Visualization
Used plotly to create interactive visualizations.
The first plot displays the historical share price of the companies.
The second plot shows the corresponding historical revenue.

## Technologies Used 
#### Python Libraries
yfinance for stock retrival.
pandas for data manipulation.
requests and BeatifulSoup for web scraping.
plotly for creating interactive plots.
#### Data Sources 
Stock data is retrieved from Yahoo finanace.
Revenue data is scraped from sample web page.

## How It Works
Stock data for Tesla and GameStop are both obtained using yfinance API. 
Revenue data is scraped from HTML tables, cleaned, and formatted.
The processed data is then visualized using interactive subplots.
