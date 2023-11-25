from ldap3 import Server, Connection, ObjectDef, AttrDef, Reader, Writer, ALL
import pprint

## Python replacement for SDI for verifying and manipulating LDAP and user data


## Iterator

ldap_host = 'ldap://<server>:<port>'
bind_user = '<bind user>'
bind_pwd = '<bind_pwd>'
basepoint = '<basepoint>'

# Not that much error handling yet, a connection fail will end all or skip entry

# Connect to server
server = Server(ldap_host, get_info=ALL)

with Connection(server, bind_user , bind_pwd, auto_bind=True) as conn:

    # Do search using abstration layer

    # Define object to be read back (i.e. objectclass)
    # We want to work with persons objects
    # In the background, this will fetch the schema from the server
    obj_person = ObjectDef('inetorgperson', conn)

    #print(obj_person)

    # This reader object will will use
    r = Reader(conn, obj_person, basepoint, '(uid=*)')

    # Do the paged search
    entries = r.search_paged(paged_size=2)

    # Do the paged search
    #entries = r.search()


    print(r)

    for entry in entries:
        #print(entry.entry_to_ldif())
        print("The name is " + entry.sn.value + " for user [" + entry.uid.value + "]" )
        '''
        if (entry.uid.value == "ville"):
            # Let's make the entry writeable
            print("Found kalle")
            e = entry.entry_writable()
            e.sn="Viking"
            print(e)
            e.entry_commit_changes()
            print(e)
        '''