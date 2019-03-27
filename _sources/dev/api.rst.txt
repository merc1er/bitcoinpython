.. _api:

Developer Interface
===================

.. module:: bitcoinpython

.. _keysapi:

Keys
----

.. autoclass:: bitcoinpython.Key

.. autoclass:: bitcoinpython.PrivateKey
    :members:
    :undoc-members:
    :inherited-members:

.. autoclass:: bitcoinpython.PrivateKeyTestnet
    :members:
    :undoc-members:
    :inherited-members:

.. autoclass:: bitcoinpython.wallet.BaseKey
    :members:
    :undoc-members:

Network
-------

.. autoclass:: bitcoinpython.network.NetworkAPI
    :members:
    :undoc-members:

.. autoclass:: bitcoinpython.network.services.BitpayAPI
    :members:
    :undoc-members:
    :inherited-members:

.. autoclass:: bitcoinpython.network.services.BlockchainAPI
    :members:
    :undoc-members:

.. autoclass:: bitcoinpython.network.services.SmartbitcoinpythonAPI
    :members:
    :undoc-members:

.. autoclass:: bitcoinpython.network.meta.Unspent
    :members:
    :undoc-members:

Exchange Rates
--------------

.. autofunction:: bitcoinpython.network.currency_to_satoshi
.. autofunction:: bitcoinpython.network.currency_to_satoshi_cached
.. autofunction:: bitcoinpython.network.satoshi_to_currency
.. autofunction:: bitcoinpython.network.satoshi_to_currency_cached

.. autoclass:: bitcoinpython.network.rates.RatesAPI
    :members:
    :undoc-members:

.. autoclass:: bitcoinpython.network.rates.BitpayRates
    :members:
    :undoc-members:

.. autoclass:: bitcoinpython.network.rates.BlockchainRates
    :members:
    :undoc-members:

Fees
----

.. autofunction:: bitcoinpython.network.get_fee
.. autofunction:: bitcoinpython.network.get_fee_cached

Utilities
---------

.. autofunction:: bitcoinpython.verify_sig

Exceptions
----------

.. autoexception:: bitcoinpython.exceptions.InsufficientFunds
