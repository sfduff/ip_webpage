#!/usr/bin/python3
# read_timecapsule_file.py
# alpha at 2020-09-26

# read time capsule baseconfig file and return host, ip and mac address
# details as a list of dictionary items

import plistlib
import json

def leases():
    try:
        plist_file = "Time Capsule.baseconfig"
        with open( plist_file, 'rb' ) as f:
            plist_data = plistlib.load( f, fmt = None, dict_type = dict )
    except IndexError:
        plist_file = '<stdin>'
        plist_data = plistlib.loads( sys.stdin.buffer.read() )
#       plist_data["dhSL"]["leases"] = ( {  "hostname": "server",
#                                           "interface": "bridge0",
#                                           "ipAddress": "192.168.1.174",
#                                           "leaseEnds": "Fri Sep 11 08:34:13 2020",
#                                           "leaseEndsTime": 1599809653,
#                                           "macAddress": "B8:27:EB:10:F6:5D",
#                                           "pool": "fixed" }
#                                       )

    leases = dict.fromkeys( range( 253 ), {} ) # create a dict of dict with primary keys ie. { 1: {} }
    for plist_record in plist_data[ "dhSL" ][ "leases" ]:
        ip = plist_record[ "ipAddress" ].split( "." ) # get the last number of the full ip address
        if ip[ 0 ] == '192':
            lease_record = {}
            record_key = int( ip[ 3 ] )
            if 'hostname' in plist_record.keys(): # if hostname is missing, use macAddress
                lease_record[ "hostname" ] = plist_record[ "hostname" ]
            else:
                lease_record[ "hostname" ] = plist_record[ "macAddress" ]
            lease_record[ "ipAddress" ] = plist_record[ "ipAddress" ]
            lease_record[ "macAddress" ] = plist_record[ "macAddress" ]
            lease_record[ "state" ] = 'erm'
            leases[ record_key ]=dict( lease_record )

    for lease_record in range( 253 ):
        if leases[ lease_record ] == {}:
            leases.pop( lease_record )

    #print( json.dumps( leases, indent=2, sort_keys = True ) )
    print( str( len( plist_data[ "dhSL" ][ "leases" ] ) )+ " entries in .baseconfig" )
    print( str( len( leases ) )+" entries processed")
    return leases
#   leases = { ip : { 'hostname': '',
#                     'ipAddress': '000.000.000.000',
#                     'macAddress': '',
#                     'state': '' }}


if __name__ == "__main__":
    leases();
