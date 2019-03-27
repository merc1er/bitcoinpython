.. _fees:

Fees
====

For now, bitcoinpython provides a 4 satoshi/byte fee.

Transactions will likely be confirmed in the next block.

.. code-block:: python

    >>> from bitcoinpython.network import get_fee
    >>>
    >>> get_fee()
    4
