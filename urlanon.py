#!/usr/bin/env python3
"""Anonymize URL in clipboard

License: MIT
(c) Bego Mario Garde <pixolin@pixolin.de>
"""
import argparse
import re
import sys

import pyperclip


def main():
    url: str = validate_arguments()
    anonymized: str = anonymize_url(url=url)
    print(anonymized)
    pyperclip.copy(anonymized)


def anonymize_url(url) -> str:
    """regex for url-parts, extract domain name, anonymize, reconstruct

    Args:
        url (str): URL to anonymize

    Returns:
        str: anonymized URL
    """
    pattern: object = re.compile(r"(https?://)(www\.)?(.+\.)([a-z]{2,}\/?)")
    match: object = pattern.search(url)
    if match is not None:
        schema = match.group(1)
        www = match.group(2)
        domain = match.group(3)
        tld = match.group(4)
    else:
        print("Couldn't convert string. Not an URL?")
        sys.exit(1)

    if not www:
        www = ""

    if len(domain) > 7:
        anonymized_domain = domain[:3] + "..." + domain[-4:]
    else:
        anonymized_domain = domain[0] + "***" + domain[-2:]

    new_url = schema + www + anonymized_domain + tld
    return new_url


def validate_arguments() -> str:
    """Validate script arguments"""
    parser: object = argparse.ArgumentParser(
        prog="urlanon",
        description="Anonymize URL",
        epilog="(c) 2023 Bego Mario Garde <pixolin@pixolin.de>",
    )
    # parser.add_argument("plugin")
    parser.add_argument(
        "-v", "--version", action="version", version="%(prog)s 0.1.0"
    )
    parser.add_argument(
        "url",
        type=str,
        action="store",
        nargs=1,
        help="URL to anonymize",
    )
    args = parser.parse_args()

    # return the name of the desired plugin
    return args.url[0].lower()


if __name__ == "__main__":
    main()
