# SMTP-SSLyze

This small Python script aims to wrap the fantastic [SSLyze](https://github.com/nabla-c0d3/sslyze) tool to analyze MX servers's TLS capabilities of a given domain.

The output is a simple Go/NoGo report intended to help you decide if you can send emails to this domain with a required level of security.

SMTP-SSLyze only checks for TLS versions 1.2 and 1.3 (as other versions are deprecated).

## Installation

SMTP-SSLyze is distributed as a Docker image, so you first need to [install Docker](https://docs.docker.com/get-docker/).

Then get the SMTP-SSLyze Docker image:

    docker pull jnury/smtp-sslyze

## Usage

To check the TLS capabilities of an email domain run:

    docker run --rm smtp-sslyze domain.com

You'll get an output looking like

    Email domain:           domain.com
    MX servers:
      - mx1.domain.com
      - mx2.domain.com
    TLS 1.2 capable:        YES
    TLS 1.3 capable:        YES
    Prefered cypher:        TLS_DHE_RSA_WITH_AES_256_CBC_SHA256
    Certificate issuer:     Thawte RSA CA 2018
    Certificate expiration: 2020.12.25
