nbdev_cards
================

<!-- WARNING: THIS FILE WAS AUTOGENERATED! DO NOT EDIT! -->

A deck of cards demo of [nbdev](https://nbdev.fast.ai/)

## Install

Install using:

    pip install nbdev-cards

or:

    conda install -c fastai nbdev-cards

## How to use

Fill me in please! Don’t forget code examples:

This lib provides a
[`Card`](https://Ber1812.github.io/nbdev-cards/cards.html#card) class
you can use to create, display and compare playing cards:

``` python
Card(1,3)
```

    3♦

Suits are numbered according to this lsit:

``` python
suits
```

    ['♣', '♦', '♥', '♠']

These are the ranks:

``` python
ranks
```

    [None, 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

For instance the rank at index `1` (not that there isn’t a playing car
at position 0, since we want the ranks to match the indices where
possible):

``` python
ranks[1]
```

    'A'
