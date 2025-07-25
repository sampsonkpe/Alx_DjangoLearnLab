# HTTPS Deployment Notes

To deploy with HTTPS:
- Set up Nginx/Apache as a reverse proxy.
- Use Certbot to generate SSL certificates.
- Redirect HTTP to HTTPS.
- Ensure Django settings for HTTPS are enabled.

Certificates can be tested with tools like [SSL Labs](https://www.ssllabs.com/ssltest/).

