DStore - Storage
################
DStore provides an abstraction layer to store the model instances.



MemoryStore
===========
The default storage in DStore is the MemoryStore.

This simply stores the model instances in an array in memory.

Keep in mind that this storage type is runtime only, meaning that the data is wiped when the application closes.

MySQLStore
==========
This storage type allows model instances to be stored in a MySQL DataBase.

In order to use this storage type, you need to install the Python Package for it.

Install From PyPi
-----------------
DStore is available from the PyPi repository at `DStore <https://pypi.python.org/pypi/DStore>`_.

This means that all you have to do to install PyMan is run the following in a console:

.. code-block:: console

    $ pip install dstore-mysql

Install From Source
-------------------
DStore can also be installed from source by downloading from GitHub and running setup.py.

.. code-block:: console

    $ wget https://github.com/MarkLark/dstore-mysql/archive/master.tar.gz
    $ tar xvf master.tar.gz
    $ cd dstore-mysql-master
    $ python setup.py install