# %%
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# %%
# Extracted MEV - Gross Profit
data_cum_gp = pd.read_csv(
    'data/cumulative_extracted_mev_gross_profit.csv').drop('Unnamed: 0', axis=1)
data_cum_gp.columns = ['time', 'value']

data_gp = pd.read_csv(
    'data/daily_extracted_mev_gross_profit.csv').drop('Unnamed: 0', axis=1)
data_gp.columns = ['time', 'value']

# %%
fig = make_subplots(specs=[[{"secondary_y": True}]])

fig.add_trace(go.Line(
    name='Cumulative',
    x=data_cum_gp['time'],
    y=data_cum_gp['value']
), secondary_y=False)

fig.add_trace(go.Line(
    name='Daily',
    x=data_gp['time'],
    y=data_gp['value'],
), secondary_y=True)

fig.update_layout(dict(
    template='ggplot2',
    title='Cumulative & Daily Extracted MEV - Gross Profit',
    width=800,
    height=600
))

fig.write_image('figures/svg/cumulative_daily_extracted_mev_gross_profit.svg')
fig.write_image(
    'figures/png/cumulative_daily_extracted_mev_gross_profit.png', scale=2)

fig.show()

# %%
# Cumulative Sum of Miner Payments for MEV
data_cum_payment = pd.read_csv(
    'data/cumulative_sum_of_miner_payments_for_mev.csv').drop('Unnamed: 0', axis=1)
data_cum_payment.columns = ['time', 'value']

# %%
fig = make_subplots()

fig.add_trace(
    go.Scatter(
        x=data_cum_payment['time'],
        y=data_cum_payment['value'],
        fill='tozeroy',
        name='Cumulative'
    )
)

fig.update_layout(dict(
    template='ggplot2',
    title='Cumulative Sum of Miner Payments for MEV',
    width=800,
    height=600,
))

fig.write_image('figures/svg/cumulative_sum_of_miner_payments_for_mev.svg')
fig.write_image(
    'figures/png/cumulative_sum_of_miner_payments_for_mev.png', scale=2)

fig.show()

# %%
# Percent of Total Block Gas used by MEV Transactions
data_gas_used = pd.read_csv(
    'data/percent_of_total_block_gas_used_by_mev_transactions.csv').drop('Unnamed: 0', axis=1)

data_gas_used.columns = ['time', 'type', 'value']
print(data_gas_used)

# %%
fig = px.area(
    data_gas_used,
    x='time',
    y='value',
    color='type',
    template='ggplot2'
)

fig.update_layout(dict(
    template='ggplot2',
    title='Percent of Total Block Gas used by MEV Transactions',
    yaxis=dict(tickformat=".1%"),
    width=1000,
    height=600,
))

fig.write_image(
    'figures/svg/percent_of_total_block_gas_used_by_mev_transactions.svg')
fig.write_image(
    'figures/png/percent_of_total_block_gas_used_by_mev_transactions.png', scale=2)

fig.show()

# %%
# Twitter and Google Trend Data
data_trend = pd.read_csv(
    'data/trend_volume.csv').drop('Unnamed: 0', axis=1)

data_trend.columns = ['date', 'google_trend', 'tweet_volume', 'tweet_len']

data_tweet_volume = data_trend[['date', 'tweet_volume']].query(
    'tweet_volume > 0')
data_google_trend = data_trend[['date', 'google_trend']].query(
    'google_trend > 0')
# %%
fig = make_subplots()

fig.add_trace(go.Line(
    name='Google Trend',
    x=data_google_trend['date'],
    y=data_google_trend['google_trend'],
    yaxis='y2',
    opacity=.8
))

fig.add_trace(go.Line(
    name='Tweets Volume',
    x=data_tweet_volume['date'],
    y=data_tweet_volume['tweet_volume'],
    yaxis='y3',
    opacity=.8
))

fig.add_trace(go.Line(
    name='Gross Profit',
    x=data_gp['time'],
    y=data_gp['value'],
    yaxis='y1'
))

fig.update_layout(dict(
    template='ggplot2',
    title='Daily Extracted MEV - Gross Profit v.s. Google Trend and Twitter Volume',
    width=1000,
    height=600,
    xaxis=dict(
        domain=[0, 0.8],
        range=['2020-01-01', '2022-10-01']
    ),
    yaxis=dict(
        title="Gross Profit",
        side='left'
    ),
    yaxis2=dict(
        title="Google Trend",
        anchor="x",
        overlaying="y",
        side="right"
    ),
    yaxis3=dict(
        title="Tweets Volume",
        anchor="free",
        overlaying="y",
        side="right",
        position=0.9
    )
))

fig.write_image(
    'figures/svg/mev_daily_gross_profit_vs_trend.svg')
fig.write_image(
    'figures/png/mev_daily_gross_profit_vs_trend.png', scale=2)

fig.show()

# %%
