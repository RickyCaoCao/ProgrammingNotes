# HTTP Notes

## Ports
- Port 80 for HTTP
- Port 443 for HTTPS

## X-Frame-Options

**Clickjacking:** fooling the user on clicking something that is is different than what the user thinks.

For example, an illegitimate website using an iframe to host a legitimate website with its own credit card form at the bottom. More examples: <https://en.wikipedia.org/wiki/Clickjacking>

X-frame-options is a response header that can be used by legitimate websites to prevent clickjacking. More specifically, it prevents the website from being hosted in iframes.

There are 3 values:
- DENY: reject all iframe loading
- SAMEORIGIN: same domain can use iframe
- ALLOW-FROM: whitelisted domain for iframe


 
- determines if page can b