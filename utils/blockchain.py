from typing import Tuple
from eth_account import Account
import secrets
import os
from web3 import Web3
from web3.types import Wei

from cloverland.env import NETWORK_RPC_URL


web3 = Web3(Web3.HTTPProvider(NETWORK_RPC_URL))


def create_wallet() -> Tuple[str, str]:
    private_key = f"0x{secrets.token_hex(32)}"
    account = Account.from_key(private_key)

    return [account.address, private_key]


def transfer(
    to_wallet: str,
    from_wallet: str,
    private_key: str,
    value_wei: Wei,
):
    nonce = web3.eth.get_transaction_count(from_wallet)
    gas_price = web3.eth.gas_price
    gas_limit = 21000
    amount_to_send = value_wei - gas_price * gas_limit

    transaction = {
        "nonce": nonce,
        "to": to_wallet,
        "value": amount_to_send,
        "gasPrice": gas_price,
        "gas": gas_limit,
    }

    signed_tx = web3.eth.account.sign_transaction(transaction, private_key)
    transaction_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)

    return transaction_hash.hex()
