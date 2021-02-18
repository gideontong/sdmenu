# SDHMenu

**SDHMenu** is a simple way to query UC San Diego's HDH dining halls.

## Installation

```bash
$ pip install SDHMenu
Successfully installed SDHMenu-1.0.0
```

## Example

```py
>>> from SDHMenu import menu
>>> my_menu = menu()
<menu {64 Degrees, Cafe Ventanas, Canyon Vista, ...}>

>>> my_menu.get('64')
[<menu_item 'Avocado Toast'>, <menu_item 'Bacon Bobcat Sandwich'>, ...]
```
