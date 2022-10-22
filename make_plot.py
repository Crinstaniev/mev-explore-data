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

fig.write_image('figures/svg/percent_of_total_block_gas_used_by_mev_transactions.svg')
fig.write_image(
    'figures/png/percent_of_total_block_gas_used_by_mev_transactions.png', scale=2)

fig.show()

# %%
