import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from plot import make_graph


###############################
######### Tesla Data ##########
###############################


# The stock is Tesla and its ticker symbol is TSLA
tesla = yf.Ticker("TSLA")

# Extract stock information and save it in a dataframe named tesla_data
tesla_data = tesla.history(period= "max")


tesla_data.reset_index(inplace = True)
print(tesla_data.head())



""" Webscraping to Extract Tesla Revenue Data """



# Download Tesla revenue data
html_data = requests.get(" https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue")

soup = BeautifulSoup(html_data.text)



# Using beautiful soup extract the table with Tesla Quarterly Revenue
# and store it into a dataframe named tesla_revenue
date = []
revenue = []


for i in soup.find_all('table')[1].find_all('td'):
    
    if(i.text):
        
        if(i.text[0] == '$'):
            revenue.append(i.text)
        else:
            date.append(i.text)
    else:
        revenue.append(0)
    

tesla_revenue = pd.DataFrame({"Date": pd.Series(date), "Revenue": pd.Series(revenue)})
tesla_revenue["Revenue"] = tesla_revenue["Revenue"].str.replace("$", "").str.replace(",", "")

print(tesla_revenue)


# removing the rows in the dataframe that are empty strings or are NaN in the Revenue column
tesla_revenue.dropna(inplace = True)

print(tesla_revenue.tail())


###############################
######### Tesla Data ##########
###############################

# The stock is GameStop and its ticker symbol is GME.
gme = yf.Ticker("GME")

# Using the ticker object and the function history extract stock information
# and save it in a dataframe named gme_dat
gme_data = gme.history(period="max")

gme_data.reset_index(inplace=True)
print(gme_data.head())



""" Webscraping to Extract GME Revenue Data """


html_data = requests.get(" https://www.macrotrends.net/stocks/charts/GME/gamestop/revenue")
soup = BeautifulSoup(html_data.text)

# Using beautiful soup extract the table with GameStop Quarterly Revenue
# and store it into a dataframe named gme_revenue

date_gme = []
revenue_gme = []

for i in soup.find_all('table')[1].find_all('td'):
    
    if(i.text[0] == '$'):
        revenue_gme.append(i.text)
    else:
        date_gme.append(i.text)
    
    

gme_revenue = pd.DataFrame({"Date": pd.Series(date_gme), "Revenue": pd.Series(revenue_gme)})
gme_revenue["Revenue"] = gme_revenue["Revenue"].str.replace("$", "").str.replace(",", "")


print(gme_revenue.tail())




""" Plot Tesla Stock Graph """


make_graph(tesla_data, tesla_revenue, 'Tesla')


""" Plot GameStop Stock Graph """

make_graph(gme_data, gme_revenue, 'GameStop')
















