csv2md
======

Python port of `CsvToMarkdownTable
<https://github.com/donatj/CsvToMarkdownTable/>`_.

Should work with both Python 2.7 and 3.X

install
-------

.. code::

    $ pip install csv2md

usage
-----


.. code:: python

    from csv2md import csv2md

    csv = 'column1,column2\nval1,val2\nval3,val4'

    markdown = csv2md(
        csv,
        delim=',',
        headers=True,
        padding=True
    )

    print(markdown)

    | column1 | column2 |
    |---------|---------|
    | val1    | val2    |
    | val3    | val4    |
