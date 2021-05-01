#!/usr/bin/python3
# client.py

from socketIO_client import SocketIO, LoggingNamespace
from time import sleep
from ping3 import ping, verbose_ping

leases = {}
#   leases = { ip : { 'hostname': '',
#                     'ipAddress': '000.000.000.000',
#                     'macAddress': '',
#                     'state': '' }}

def recieve_data( data ):
    global leases
    leases = data.copy()
    print( 'recieve_data -> leases' )

def monitor():
    global leases

    def change_state( new_state ):
        leases[ lease_record ][ 'state' ] = new_state
        new_record = { lease_record: leases[ lease_record ] }
        print( 'update line -> ' + str( new_record ) )
        socketIO.emit( 'update_line', new_record )
        socketIO.wait( seconds = 1 )

    for lease_record in leases:
        ping_result = ping( leases[ lease_record ][ "ipAddress" ] )
        print( leases[ lease_record ][ "ipAddress" ] + ' -> '+ str( ping_result ) ) #rem later
        if str( ping_result ) == "None": #ping failed
            if not leases[ lease_record ][ 'state' ] == 'off':
                change_state( 'off' )
        else: # ping succeeded
            if not leases[ lease_record ][ 'state' ] == 'on':
                change_state( 'on' )


if __name__ == '__main__':
    socketIO = SocketIO( 'server', 5000 )
    socketIO.on( 'recieve_data', recieve_data )
    socketIO.emit( 'data_request' )
    socketIO.wait( seconds = 1 )
    monitor() # replace these with a loop later
    monitor() # second pass to confirm only updating changes
