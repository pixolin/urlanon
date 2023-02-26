#!/usr/bin/env python3
"""Anonymize URL in clipboard

License: MIT
(c) Bego Mario Garde <pixolin@pixolin.de>
"""
import argparse
import sys
from urllib.parse import urlparse, urlunparse

import pyperclip


def main():
    url: str = validate_arguments()
    # parse url
    parsed: list = parse_url(url)
    # pick domain from parsed address and anonymize
    netloc = parsed[1]
    anonymized_domain = anonymize(netloc)
    rendered = unparse_render_url(parsed, anonymized_domain)
    print(f"Copied: {rendered}")
    pyperclip.copy(rendered)


def validate_arguments() -> str:
    """Ensure URL was provided

    Returns:
        str: URL
    """
    parser: object = argparse.ArgumentParser(
        prog="urlanon",
        description="Anonymize URL",
        epilog="(c) 2023 Bego Mario Garde <pixolin@pixolin.de>",
    )

    parser.add_argument(
        "-v", "--version", action="version", version="%(prog)s 0.2.1"
    )
    parser.add_argument(
        "url",
        type=str,
        action="store",
        nargs=1,
        help="URL to anonymize",
    )
    args = parser.parse_args()

    url: str = args.url[0].lower()

    # URL must begin with http:// or https://
    allowed_scheme = ("http://", "https://")
    if not url.startswith(allowed_scheme):
        print("An error occured.")
        print(f'Is "{url}" a proper URL?')
        sys.exit(1)
    return url


def parse_url(url) -> list:
    """Parse URL into list

    Args:
        url (str): URL to parse

    Returns:
        list: URL, splitted into parts
    """

    parsed = urlparse(url)

    address = []
    address.append(parsed.scheme)
    address.append(parsed.netloc)
    address.append(parsed.path)
    address.append(parsed.params)
    address.append(parsed.query)
    address.append(parsed.fragment)
    return address


def anonymize(fulldomain):
    """Extract domain name and replace middle part with dots

    Args:
        fulldomain (str): sub-, second-level and top-level-domain

    Returns:
        str: netlocator with anonymized domain
    """
    domain_parts = fulldomain.split(".")
    sld = domain_parts[-2]
    if len(sld) <= 6:
        sld = sld[0] + "..." + sld[-1]
    else:
        sld = sld[:3] + "..." + sld[-3:]
    domain_parts[-2] = sld
    fulldomain = ".".join(domain_parts)
    return fulldomain


def unparse_render_url(address, domain):
    """Replace domain and render as complete URL

    Args:
        address (list): parts of URL as list
        domain (str): anonymized domain

    Returns:
        str: rendered URL
    """
    address[1] = domain
    output = urlunparse(address)
    return output


if __name__ == "__main__":
    main()
