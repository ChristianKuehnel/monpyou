#!/usr/bin/python3
"""Demo function to show how to use Monpyou."""

from monpyou import MonpYou
import argparse
import logging


def main(username: str, password: str):
    """Interaction with the MonpYou class."""
    mpy = MonpYou(username, password)
    for account in mpy.get_accounts():
        print("{} ({}): {} {}".format(account.name, account.iban, account.balance, account.currency))


if __name__ == '__main__':
    """simple command line wrapper.
    
    - Reads username/password as argument
    - sets loglevel
    - calls main function
    """

    parser = argparse.ArgumentParser()
    parser.add_argument('username')
    parser.add_argument('password')
    args = parser.parse_args()
    logging.basicConfig(level=logging.INFO)
    main(args.username, args.password)
