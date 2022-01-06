from pycoingecko import CoinGeckoAPI
import pandas as pd
import yfinance as yf
from datetime import datetime
from datetime import timedelta
import plotly.graph_objects as go
from fbprophet import Prophet
#from fbprophet.plot import plot_plotly, plot_components_plotly
import warnings

warnings.filterwarnings('ignore')

pd.options.display.float_format = '${:,.2f}'.format


# TODO: passer les bons paramètres à la fonction
def forecast_prophet(symbol, start_date, end_date):
    eth_df = yf.download(symbol, start_date, end_date)

    # check de la qualité des données reçues
    print(eth_df.tail())
    print(eth_df.info())
    print(eth_df.isnull().sum())
    print(eth_df.columns)

    eth_df.reset_index(inplace=True)
    print(eth_df.columns)

    # dataframe avec date et prix d'ouverture
    df = eth_df[["Date", "Open"]]

    new_names = {
        "Date": "ds",
        "Open": "y",
    }
    df.rename(columns=new_names, inplace=True)
    print(df.tail())

    # plot the open price
    x = df["ds"]
    y = df["y"]

    fig = go.Figure()

    fig.add_trace(go.Scatter(x=x, y=y))

    # Set title
    fig.update_layout(
        title_text="Time series plot of Ethereum Open Price",
    )

    fig.update_layout(
        xaxis=dict(
            rangeselector=dict(
                buttons=list(
                    [
                        dict(count=1, label="1m", step="month", stepmode="backward"),
                        dict(count=6, label="6m", step="month", stepmode="backward"),
                        dict(count=1, label="YTD", step="year", stepmode="todate"),
                        dict(count=1, label="1y", step="year", stepmode="backward"),
                        dict(step="all"),
                    ]
                )
            ),
            rangeslider=dict(visible=True),
            type="date",
        )
    )



def test():
    today = datetime.today().strftime('%Y-%m-%d')
    start_date = '2016-01-01'
    end_date = today

    forecast_prophet("ETH-USD", start_date, end_date)

test()