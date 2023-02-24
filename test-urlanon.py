import urlanon as url


def test_url() -> None:
    assert url.anonymize_url("http://abc.de") == "http://a***c.de"
    assert url.anonymize_url("https://abc.de") == "https://a***c.de"
    assert url.anonymize_url("https://abc.de/about-me") == "https://a***c.de/"
    assert url.anonymize_url("http://abcdefghi.de") == "http://abc...ghi.de"
    assert url.anonymize_url("https://abcdefghi.de") == "https://abc...ghi.de"
    assert (
        url.anonymize_url("https://abcdefghi.de/about-me")
        == "https://abc...ghi.de/"
    )
