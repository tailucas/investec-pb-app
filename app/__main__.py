import configparser
import logging
import pprint
import sys

log = logging.getLogger()
formatter = logging.Formatter('%(name)s %(threadName)s [%(levelname)s] %(message)s')
log_handler = logging.StreamHandler(stream=sys.stdout)
log_handler.setFormatter(formatter)
log.addHandler(log_handler)
log.setLevel(logging.DEBUG)

pp = pprint.PrettyPrinter(indent=2)

from investec_api_python import SAPBAccountInformation

if __name__ == "__main__":
    config = configparser.RawConfigParser()
    config.read('creds.properties')
    creds = dict(config.items('creds'))

    client = SAPBAccountInformation(
        client_id=creds['client_id'],
        secret=creds['client_secret'],
        api_key=creds['api_key'],
        use_sandbox=True,
        additional_headers={'Accept-Encoding': 'gzip, deflate, br'})

    log.info('Transferring...')
    try:
        response = client.transfer(account_id='3353431574710166878182963', beneficiary_account_id='3353431574710163189587446', amount=10, my_reference='API transfer', their_reference='API transfer')
        pp.pprint(response)
    except Exception as e:
        print(e)
    log.info('Paying...')
    try:
        response = client.pay(account_id='3353431574710166878182963', beneficiary_id='MTAxODk2ODk0MTQ5NzM=', amount=10, my_reference='API transfer', their_reference='API transfer')
        pp.pprint(response)
    except Exception as e:
        print(e)

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
