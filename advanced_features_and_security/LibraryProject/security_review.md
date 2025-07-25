# Django Security Settings Review

## HTTPS and SSL
- Enabled SECURE_SSL_REDIRECT to force HTTPS.
- Set HSTS headers to enforce secure connections for one year.
- Included subdomains and preload directive.

## Secure Cookies
- SESSION_COOKIE_SECURE and CSRF_COOKIE_SECURE ensure cookies are sent over HTTPS.

## Secure Headers
- DENY framing to prevent clickjacking.
- Disabled MIME-sniffing with SECURE_CONTENT_TYPE_NOSNIFF.
- Enabled browser XSS filter.

## Notes
- Additional headers like CSP (Content Security Policy) can further improve security.
- Production deployment should use a properly configured web server with valid certificates.

