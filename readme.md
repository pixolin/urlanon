# urlanon

Small Python3 script to anonymze URLs.

## Usage

`urlanon.py https://myexample.com` \
will anonymize an URL by keeping the first and last three letters and replacing the rest with an ellipsis, e.g. `https://mye...ple.com`. For domains shorter than 6 letters, only the first and last letter of the domain name are used, `https://test.org` becomes `https://t***t.org`. The URL is copied to your clipboard.

## Installation

```bash
pip install -r requirements
chmod a+x urlanon.py
```

---

License MIT, (c) Bego Mario Garde <pixolin@pixolin.de>
