import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "YourAccountSid"
# Your Auth Token from twilio.com/console
auth_token  = "your_auth_token"

client = Client(account_sid, auth_token)

month_list = ['january', 'february', 'march', 'april', 'may', 'jun']

for month in month_list:
    sales_table = pd.read_excel(f'{month}.xlsx')
    if (sales_table['Vendas'] > 55000).any():
        seller = sales_table.loc[sales_table['Vendas'] > 55000, 'Vendedor'].values[0]
        sales = sales_table.loc[sales_table['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'In month {month} someone hit the goal. Seller={seller}, sales={sales}')
        message = client.messages.create(
            to="Youphone",
            from_="number phone in the Twilio Account",
            body=f'In month {month} someone hit the goal. Seller={seller}, sales={sales}'
        )
        print(message.sid)
