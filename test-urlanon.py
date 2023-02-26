import urlanon as url


def test_parse_url() -> None:
    assert url.parse_url("http://abc.de") == [
        "http",
        "abc.de",
        "",
        "",
        "",
        "",
    ]
    assert url.parse_url("https://abc.de") == [
        "https",
        "abc.de",
        "",
        "",
        "",
        "",
    ]
    assert url.parse_url("https://abc.de/about-me") == [
        "https",
        "abc.de",
        "/about-me",
        "",
        "",
        "",
    ]
    assert url.parse_url("http://abcdefghi.de") == [
        "http",
        "abcdefghi.de",
        "",
        "",
        "",
        "",
    ]
    assert url.parse_url("https://abcdefghi.de") == [
        "https",
        "abcdefghi.de",
        "",
        "",
        "",
        "",
    ]
    assert url.parse_url("https://abcdefghi.de/about-me") == [
        "https",
        "abcdefghi.de",
        "/about-me",
        "",
        "",
        "",
    ]


def test_anonymize():
    assert url.anonymize("abcde.com") == "a...e.com"
    assert url.anonymize("example.com") == "exa...ple.com"
    assert url.anonymize("www.example.com") == "www.exa...ple.com"
    assert url.anonymize("de.example.com") == "de.exa...ple.com"
    assert url.anonymize("shop.de.example.com") == "shop.de.exa...ple.com"


def test_unparse_render_url():
    address = ["https", "www.example.com", "/path/to/file.html", "", "", ""]
    domain = "www.exa...ple.com"
    assert (
        url.unparse_render_url(address, domain)
        == "https://www.exa...ple.com/path/to/file.html"
    )
