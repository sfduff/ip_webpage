#!/usr/bin/python3
# main.py
# alpha at 2020-09-26

from flask import Flask, render_template, request
from flask_socketio import SocketIO
import read_timecapsule_file

leases = {}
#   leases = { ip : { 'hostname': '',
#                     'ipAddress': '000.000.000.000',
#                     'macAddress': '',
#                     'state': '' }}

app = Flask(__name__)
app.config[ 'SECRET_KEY' ] = 'vnkdjnfjknfl1232#'
socketio = SocketIO( app )

@app.route( '/' )
def default_route():
    print( '/ -> session.html' )
    return render_template( 'session.html' )

@socketio.on( 'data_request' )
def update_client():
    print('data_request -> receive_data')
    socketio.emit( 'recieve_data', leases )

@socketio.on( 'update_line' )
def update_line( lease_record, methods = ['GET', 'POST'] ):
    global leases
    print( 'update_line -> ' +str( lease_record ) )
    leases.update( lease_record )
    socketio.emit( 'update_line', lease_record )


if __name__ == '__main__':
    leases = read_timecapsule_file.leases()
    socketio.run( app, host = '0.0.0.0', debug = True )
