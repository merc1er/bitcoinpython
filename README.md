<p align="center">
  <a href="https://blurry.cash">
    <img src="https://github.com/merc1er/bitcoinpython/raw/master/docs/source/_static/bitcoinpython.png" width="90" height="90">
  </a>
</p>

<h3 align="center">BitcoinPython</h3>
<h4 align="center">Bitcoin Cash Python library</h4>

<p align="center">
  <img src="https://img.shields.io/pypi/v/bitcoinpython.svg?style=flat-square" alt="BitcoinPython version">
  <img src="https://img.shields.io/pypi/pyversions/bitcoinpython.svg?style=flat-square" alt="Python Versions">
  <img src="https://travis-ci.org/merc1er/bitcoinpython.svg?branch=master" alt="Build status">
  <img src="https://img.shields.io/codecov/c/github/merc1er/bitcoinpython.svg?style=flat-square" alt="Code Coverage">
  <img src="https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square" alt="MIT license">
</p>

## Quickstart

BitcoinPython is so easy to use, in fact, you can do this:

```python
>>> from bitcoinpython import Key
>>>
>>> k = Key()
>>> k.address
'bitcoincash:qp0hamw9rpyllkmvd8047w9em3yt9fytsunyhutucx'
>>>
>>> k.get_balance('usd')
'2'
>>>
>>> # Let's donate a dollar to CoinSpice.io
>>> outputs = [
>>>     ('bitcoincash:qz69e5y8yrtujhsyht7q9xq5zhu4mrklmv0ap7tq5f', 1, 'usd'),
>>>     # you can add more recipients here
>>> ]
>>>
>>> k.send(outputs)
'6aea7b1c687d976644a430a87e34c93a8a7fd52d77c30e9cc247fc8228b749ff'
```

Done ✅ Here is the transaction:  
https://explorer.bitcoin.com/bch/tx/6aea7b1c687d976644a430a87e34c93a8a7fd52d77c30e9cc247fc8228b749ff

## Features

- Python's fastest available implementation (100x faster than closest library)
- Seamless integration with existing server setups
- Supports keys in cold storage
- Fully supports 25 different currencies
- First class support for storing data in the blockchain
- Deterministic signatures via RFC 6979
- Exchange rate API, with optional caching
- Optimal transaction fee API, with optional caching
- Compressed public keys by default
- Multiple representations of private keys; WIF, PEM, DER, etc.
- Standard P2PKH transactions

## Installation

BitcoinPython is distributed on `PyPI` and is available on Linux/macOS and Windows with Python 3.5+

```shell
$ pip3 install bitcoinpython
```

## Credits

Forked from Ofek's Bit and Teran McKinney's bitcash

- [ofek](https://github.com/ofek/bit) for the original bit codebase
- [teran-mckinney](https://github.com/sporestack/bitcash) for the bitcash fork
- [bjarnemagnussen](https://github.com/bjarnemagnussen/bit/tree/segwit) for his segwit code for the necessary BIP-143 support
