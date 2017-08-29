# -*- coding: utf-8 -*-

from zaifapi import ZaifTradeApi  # Zaifが公開している認証情報が必要なAPIを実行するクラス
from pprint import pprint  # 表示用(jsonをきれいに表示してくれる)

if __name__ == '__main__':
    key = '371f8a5e-0f45-45a0-9fe3-bbedb3ef2f23'
    secret = '7f96e2b1-3c9c-4f20-8537-92e4fe452fab'

    zaif = ZaifTradeApi(key, secret)
    pprint(zaif.get_info())
