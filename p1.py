import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
import plotly.graph_objects as go
from plotly.subplots import make_subplots

import warnings
# Ignore all warnings
warnings.filterwarnings("ignore", category=FutureWarning)

#Plot graph function
def make_graph(stock_data, revenue_data, stock):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("Historical Share Price", "Historical Revenue"), vertical_spacing = .3)
    stock_data_specific = stock_data[stock_data.Date <= '2021--06-14']
    revenue_data_specific = revenue_data[revenue_data.Date <= '2021-04-30']
    fig.add_trace(go.Scatter(x=pd.to_datetime(stock_data_specific.Date), y=stock_data_specific.Close.astype("float"), name="Share Price"), row=1, col=1)
    fig.add_trace(go.Scatter(x=pd.to_datetime(revenue_data_specific.Date), y=revenue_data_specific.Revenue.astype("float"), name="Revenue"), row=2, col=1)
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)
    fig.update_layout(showlegend=False,
    height=900,
    title=stock,
    xaxis_rangeslider_visible=True)
    fig.show()

# Getting Tesla's stock data using yfinanace
tesla = yf.Ticker('TSLA')
tesla_data = tesla.history(period='max')
tesla_data.reset_index(inplace=True)
# tesla_data.head() 

url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm'
html_data = requests.get(url).text
soup = BeautifulSoup(html_data, 'html.parser')
tables = soup.find_all('table')
for i, table in enumerate(tables):
    if('Tesla Quarterly Revenue' in str(table)):
        tableNumber = i
print(f'Table number for Tesla is {tableNumber}')
#First table is the table we need to use
tesla_revenue = pd.DataFrame(columns = ['Date', 'Revenue'])
for row in tables[tableNumber].tbody.find_all('tr'):
    col = row.find_all('td')
    if (col !=[] ):
        date = col[0].text.strip()
        revenue = col[1].text.strip().replace('$', '').replace(',', '')
        new_row = pd.DataFrame({"Date": [date], "Revenue": [revenue]})
        tesla_revenue = pd.concat([tesla_revenue, new_row], ignore_index=True)

#To remove comma and dollar sign
tesla_revenue["Revenue"] = tesla_revenue['Revenue'].str.replace(',|\$',"", regex=True)
#Removing null or empty lines
tesla_revenue.dropna(inplace=True)
tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""]

# Getting GameStop's stock data using yfinanace
gamestop = yf.Ticker('GME')
gme_data = gamestop.history(period = 'max')
gme_data.reset_index(inplace=True)
# gme_data.head()

url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html'
html_data_2 = requests.get(url).text
soup = BeautifulSoup(html_data_2, 'html.parser')

tables = soup.find_all('table')
for i, table in enumerate(tables):
    if ('GameStop Quarterly Revenue' in str(table)):
        tableNumber = i
print(f'Table number for GameStop is {tableNumber}')
gamestop_revenue = pd.DataFrame(columns=['Date', 'Revenue'])
for row in tables[tableNumber].tbody.find_all('tr'):
    col = row.find_all('td')
    if (col !=[] ):
        date = col[0].text.strip()
        revenue = col[1].text.strip().replace('$', '').replace(',', '')
        new_row = pd.DataFrame({'Date':[date], 'Revenue':[revenue]})
        gamestop_revenue = pd.concat([gamestop_revenue, new_row], ignore_index=True)

# Ploting Tesla's stock graph
make_graph(tesla_data, tesla_revenue, 'Tesla')
# Ploting GameStop's stock graph
make_graph(gme_data, gamestop_revenue, 'GameStop' )

