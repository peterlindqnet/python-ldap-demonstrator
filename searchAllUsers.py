import ldap
import pprint

## Python replacement for SDI for verifying and manipulating LDAP and user data


## Iterator

ldap_host = 'ldap://<server>:<port>'
bind_user = '<bind user>'
bind_pwd = '<bind_pwd>'
basepoint = '<basepoint>'

# Not that much error handling yet, a connection fail will end all or skip entry

# Connect to server
ldap_search = ldap.initialize(ldap_host)

# Add options here (this only turns of referrals, used by Active Directory)
ldap_search.set_option(ldap.OPT_REFERRALS, 0)

# Do Bind - add error handling here
ldap_search.simple_bind_s(bind_user, bind_pwd)

# Do search
result = ldap_search.search_s(basepoint, ldap.SCOPE_SUBTREE, 'objectclass=person')

# Check how many results
print("Found",  len(result), "entries")


# Setup pretty print
pp = pprint.PrettyPrinter(indent=2)



# This is the main loop

for entry in result:

    # Pretty print can be used to output objects
    #pp.pprint(entry[1].get('cn').decode())

    # Seems LDAP objects will be outputted as a list.
    # The list item is a tuple with two values, first entry is the DN, the second a dictionary of all attributes
    # Multivalued attributes will always be in an array
    # All attribute values will be as byte arrays, the caller will need to decode

    try: 
        print("Hello " +entry[1].get('cn')[0].decode() + ", your email seems to be " + entry[1].get('mail')[0].decode())
    except:
        print("Seems one of the attributes did not exist and calling decode on it caused an error")

    # Add any additional actions, transformation of data here



# Any wrap up code here