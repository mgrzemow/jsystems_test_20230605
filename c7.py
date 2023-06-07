import pytest
import logging

logging.basicConfig(filename='moj.log', filemode='wt', encoding='utf8', level=logging.DEBUG)


def f1(level, message):
    lgr = logging.getLogger(__name__)
    lgr.log(level, message)
