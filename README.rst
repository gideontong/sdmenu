SDHMenu
=======

**SDHMenu** is a simple way to query UC San Diego's HDH dining halls.

Installation
------------

.. code-block:: console

    $ pip install SDHMenu


Quick Example
-------------

.. code-block:: python

    >>> from SDHMenu import menu
    >>> my_menu = menu()
    <menu {64 Degrees, Cafe Ventanas, Canyon Vista, ...}>

    >>> my_menu.get('64')
    [<menu_item 'Avocado Toast'>, <menu_item 'Bacon Bobcat Sandwich'>, ...]
