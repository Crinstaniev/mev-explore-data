# %%
import pickle
import requests
import pandas as pd
import json

url = dict(
    cumulative_extracted_mev_gross_profit='https://data.flashbots.net/api/public/dashboard/12568e65-103a-4f61-a45c-ab8c4770b266/card/670?parameters=%5B%5D',
    daily_extracted_mev_gross_profit='https://data.flashbots.net/api/public/dashboard/12568e65-103a-4f61-a45c-ab8c4770b266/card/671?parameters=%5B%5D',
    cumulative_sum_of_miner_payments_for_mev='https://data.flashbots.net/api/public/dashboard/12568e65-103a-4f61-a45c-ab8c4770b266/card/675?parameters=%5B%5D',
    percent_of_total_block_gas_used_by_mev_transactions='https://data.flashbots.net/api/public/dashboard/12568e65-103a-4f61-a45c-ab8c4770b266/card/774?parameters=%5B%5D'
)

result = dict()
# %%
for key in url.keys():
    _result = requests.get(url[key]).content
    result[key] = json.loads(_result).get('data').get('rows')
    df = pd.DataFrame(result[key])
    df.to_csv(f'data/{key}.csv')


pickle.dump(result, open('tmp/raw.pkl', 'wb'))

# %%
