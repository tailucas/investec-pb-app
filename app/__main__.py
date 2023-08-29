import configparser
import logging
import pprint
import sys

from datetime import datetime
from typing import Optional

log = logging.getLogger()
formatter = logging.Formatter('%(name)s %(threadName)s [%(levelname)s] %(message)s')
log_handler = logging.StreamHandler(stream=sys.stdout)
log_handler.setFormatter(formatter)
log.addHandler(log_handler)
log.setLevel(logging.DEBUG)

pp = pprint.PrettyPrinter(indent=2)


from investec_api_python import InvestecOpenApiClient


if __name__ == "__main__":
    card_sandbox = False
    config = configparser.RawConfigParser()
    config.read('creds.properties')
    creds = dict(config.items('creds'))

    client = InvestecOpenApiClient(
        client_id=creds['client_id'],
        secret=creds['client_secret'],
        api_key=creds['api_key'],
        use_sandbox=True,
        additional_headers={'Accept-Encoding': 'gzip, deflate, br'})

    access_token: Optional[str] = client.access_token
    token_expiry: Optional[datetime] = client.access_token_expiry
    log.info(f'API access token is: {access_token} with expiry of {token_expiry}')

    log.info('Transferring...')
    try:
        response = client.transfer(account_id='3353431574710166878182963', beneficiary_account_id='3353431574710163189587446', amount=10, my_reference='API transfer', their_reference='API transfer')
        pp.pprint(response)
    except Exception as e:
        print(e)

    access_token = client.access_token
    token_expiry = client.access_token_expiry
    log.info(f'API access token is: {access_token} with expiry of {token_expiry}')

    log.info('Paying...')
    try:
        response = client.pay(account_id='3353431574710166878182963', beneficiary_id='MTAxODk2ODk0MTQ5NzM=', amount=10, my_reference='API transfer', their_reference='API transfer')
        pp.pprint(response)
    except Exception as e:
        print(e)

    if access_token and token_expiry:
        log.info('Creating new client with token re-use.')
        client = None
        client = InvestecOpenApiClient(
            client_id=creds['client_id'],
            secret=creds['client_secret'],
            api_key=creds['api_key'],
            use_sandbox=True,
            additional_headers={'Accept-Encoding': 'gzip, deflate, br'},
            access_token=(access_token, token_expiry))

        log.info('Listing beneficiary categories...')
        response = client.get_beneficiary_categories()
        pp.pprint(response)
        log.info('Listing beneficiaries...')
        response = client.get_beneficiaries()
        pp.pprint(response)
        log.info('Listing accounts...')
        response = client.get_accounts()
        pp.pprint(response)
        if len(response) > 0:
            account_id = response[0]['accountId']
            log.info(f'Getting balance for account {account_id}')
            response = client.get_account_balance(account_id=account_id)
            pp.pprint(response)
            log.info(f'Getting account transactions for account {account_id}')
            response = client.get_account_transactions(account_id=account_id, from_date='2023-08-01', transaction_type='CardPurchases')
            pp.pprint(response)

        if card_sandbox:
            log.info('Listing cards...')
            response = client.get_cards()
            pp.pprint(response)
