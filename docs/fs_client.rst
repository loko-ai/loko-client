FS Client
==========

FS Client interacts with **loko-orchestrator APIs**. You can use it to manage LoKo data. We provide both a synchronous and
asynchronous client.

To use FS Client you have to provide the gateway url. Usually, when you're working on a docker container deployed on the
loko network the url is ``https://gateway:8080/routes/``. Otherwise, the url is ``https://localhost:9999/routes/``.

.. code-block:: python

    gw = 'http://gateway:8080/routes/'
    fsclient = FSClient(gateway=gw)

If you need the **async** version:

.. code-block:: python

    gw = 'http://gateway:8080/routes/'
    fsclient = AsyncFSClient(gateway=gw)


You can **list directory** contents using:

.. code-block:: python

    fsclient.ls('/data/data/datasets')

If you have to **read files**, use:

.. code-block:: python

    fsclient.read('/data/data/titanic.csv', mode='r')

You can use ``mode='rb'`` to get the file bytes or, if you're using the `AsyncFSClient`, ``content=True`` to read file
content on your own:

.. code-block:: python

    resp = await fsclient.read('/data/data/titanic.csv', content=True)
    async for line in resp:
        print(line)

You can **save** or **update** files using:

.. code-block:: python

    fsclient.save('data/data/test/test.txt', b'hello')
    fsclient.update('data/data/test/test.txt', b'updated')

    with open('./myfile.txt', 'rb') as f:
        fsclient.save('data/data/test/myfile.txt', f)

You can also **save** and **delete** directories:

.. code-block:: python

    fsclient.save('data/data/test2')
    fsclient.delete('data/data/test2')

Or files:

.. code-block:: python

    fsclient.delete('data/data/test/test.txt')

To create a **copy** or **move** a file use:

.. code-block:: python

    fsclient.copy('data/data/test/test.txt', 'data/data/test/test2.txt')
    fsclient.move('data/data/test/test.txt', 'data/data/test/test3.txt')

