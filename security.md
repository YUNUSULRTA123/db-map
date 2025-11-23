# 🔐 Security Policy

This document describes the security guidelines and practices for the
Cartographic Telegram Bot project.

## 📦 Supported Versions

Security updates are provided for the latest stable version of the bot's
codebase.

  Version   Supported
  --------- -----------
  latest    ✅
  older     ❌

## 🔒 Security Practices

-   All secrets (such as the Telegram Bot Token) must be stored
    **outside the codebase**.
-   Use environment variables or a secure configuration file
    (`config.py`) excluded from version control.
-   Database files should not contain sensitive personal data beyond
    user IDs and city selections.
-   Implement rate limiting on deployments with high traffic.
-   Avoid logging user messages containing private information.
-   Always verify user input to prevent injection attacks.

## 🛡️ Reporting a Vulnerability

If you discover a security issue, please follow these steps:

1.  Do **not** publish the details publicly.
2.  Provide a detailed description of the issue.
3.  Send a private message or open a confidential issue with:
    -   Steps to reproduce
    -   Possible impact
    -   Suggested fix (optional)

We will respond as quickly as possible and provide a fix if necessary.

## ⚠️ Disclaimer

This bot is intended for educational and demonstration purposes.\
Ensure that production deployments follow enhanced security best
practices, such as:

-   Running the bot in isolated containers\
-   Using secure HTTPS proxies for API communication\
-   Regular dependency updates\
-   Database permission isolation
