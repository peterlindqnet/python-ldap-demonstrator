from ldap3 import Server, Connection, ALL
import pprint

## Python replacement for SDI for verifying and manipulating LDAP and user data

# See: https://ldap3.readthedocs.io/en/latest/operations.html

## Iterator

ldap_host = 'ldap://<server>:<port>'
bind_user = '<bind user>'
bind_pwd = '<bind_pwd>'
basepoint = '<basepoint>'

# Not that much error handling yet, a connection fail will end all or skip entry

# Connect to server
server = Server(ldap_host, get_info=ALL)
conn = Connection(server, bind_user , bind_pwd, auto_bind=True)


# Non paged search

conn.search( basepoint, '(objectClass=*)', attributes= ['cn', 'givenName', 'mail'], paged_size= 2 )
for entry in conn.entries:
    print(entry.entry_to_ldif())


# Doing a paged search seems to require a additional manual handling to handle paged_cookie and doing subsequent searches

searchParameters = { 'search_base': basepoint, 'search_filter': '(objectClass=*)', 'attributes': ['cn', 'givenName', 'mail', 'objectclass'], 'paged_size': 5 }

while True:

    # Do search
    conn.search(**searchParameters)
    for entry in conn.entries:
        print(entry.entry_to_ldif())
    cookie = conn.result['controls']['1.2.840.113556.1.4.319']['value']['cookie']
    if cookie:
        searchParameters['paged_cookie'] = cookie
    else:
        break