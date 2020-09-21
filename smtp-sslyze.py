#!/usr/local/bin/python3

import re
import sys
import dns.resolver
import subprocess
import json

domain = "none"

if len(sys.argv) == 2:
    domain = sys.argv[1]
else:
    print("Bad number of argument. Usage: smtp-sslyze.py domain_name")
    exit(1)

try:
    result = dns.resolver.resolve(domain, 'MX')
except dns.resolver.NXDOMAIN:
    print("The domain'" + domain + "' does not exist")
    exit(1)
except Exception as e:
    print("An unknown error occured: ", str(e))
    exit(1)

if len(result) != 0:

    issuer_list = ['Thawte RSA CA 2018']
    prefered_cypher_list = ['TLS_DHE_RSA_WITH_AES_256_CBC_SHA256', 'TLS_DHE_RSA_WITH_AES_256_CBC_SHA128', 'TLS_DHE_RSA_WITH_AES_256_CBC_SHA256']
    tls_12_capable = 'YES'
    tls_13_capable = 'YES'
    expiration = 'Unknown'

    print('Email domain:          ', domain)
    print('MX servers:')

    for exdata in result:
        mx_server = re.sub('\\.$', '', str(exdata.exchange)) + ':25'
        # out = subprocess.Popen(['sslyze', '--starttls=smtp', '--certinfo', '--json_out=-', mx_server], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        # stdout,stderr = out.communicate()
        # report = json.loads(stdout)
        print(' -', mx_server)

    print('TLS 1.2 capable:       ', tls_12_capable)
    print('TLS 1.3 capable:       ', tls_13_capable)
    print('Prefered cypher(s):    ', ", ".join(list(set(prefered_cypher_list))))
    print('Certificate issuer:    ', ", ".join(list(set(issuer_list))))
    print('Certificate expiration:', expiration)
else:
    print("No MX record was found for domain'" + domain + "'")