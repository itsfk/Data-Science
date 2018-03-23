import pandas as pd
import numpy as np
import requests as r
import matplotlib.pyplot as plt
import seaborn as sns
# url ='https://api.coinmarketcap.com/v1/ticker/'
# current = pd.DataFrame(r.get(url).json())
# print(current.head())
#                              Task 2
df=pd.read_csv('datasets/coinmarketcap_06122017.csv')
# Selecting the 'id' and the 'market_cap_usd' columns
market_cap_raw = df[['id','market_cap_usd']]
#                          Task 1 and 2
# print(market_cap_raw)
# Counting the number of values
# print(market_cap_raw.count())
#                              Task 3
# Filtering out rows without a market capitalization
cap = market_cap_raw.query('market_cap_usd > 0')
# print(cap.count())
# Counting the number of values again
#                              Task 4 and 5
#Declaring these now for later use in the plots
# TOP_CAP_TITLE = 'Top 10 market capitalization'
# TOP_CAP_YLABEL = '% of total cap'
# cap10=cap.head(10)
# cap10 = cap10.set_index('id')
# Calculating market_cap_perc
# cap10['market_cap_perc'] = cap10['market_cap_usd'] / sum(cap['market_cap_usd']) * 100
# index= np.arange(10)
# market_cap_perc = list(cap10.market_cap_perc)
# ax=sns.barplot(x=index,y=market_cap_perc)
# ax.set_xlabel("Index")
# ax.set_ylabel("Market Cap Percentage")
# plt.show()
#                              Task 6
volatality=df[['id','percent_change_24h','percent_change_7d']]
volatality=volatality.set_index('id').dropna()
# Sorting the DataFrame by percent_change_24h in ascending order
volatality = volatality.sort_values(by='percent_change_24h', ascending =True)
# print(volatality)
#                               task 7
# Defining a function with 2 parameters, the series to plot and the title
def top10_subplot(volatility_series, title):
    # Making the subplot and the figure for two side by side plots
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 6))

    # Plotting with pandas the barchart for the top 10 losers
    ax = axes[0].bar(volatality.index[:10], volatality[volatility_series].head(10))
    axes[0].tick_params(rotation=90)
    axes[0].set_title('Losers')

    # Setting the figure's main title to the text passed as parameter
    # ... YOUR CODE FOR TASK 7 ...

    fig.suptitle(title)

    # Setting the ylabel to '% change'
    # ... YOUR CODE FOR TASK 7 ...
    axes[0].set_ylabel('% change')
    axes[1].set_ylabel('% change')

    # Same as above, but for the top 10 winners
    ax = axes[1].bar(volatality.index[-10:], volatality[volatility_series][-10:])
    axes[1].tick_params(rotation=90)
    axes[1].set_title('Winners')

    # Returning this for good practice, might use later
    return fig, ax


DTITLE = "24 hours top losers and winners"

# Calling the function above with the 24 hours period series and title DTITLE
fig, ax = top10_subplot('percent_change_24h', DTITLE)
plt.show()