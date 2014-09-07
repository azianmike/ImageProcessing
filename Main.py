__author__ = 'michaelluo'

import socket
import json
import shutil
from ImageCompareFolder import sendComparedImagesGCM
from multiprocessing import Process
from readJson import readJSON
from loginAndRegister import login, register
from saveImageData import saveImageData, deleteFiles
from MongoAnalytics import storeUserNumberOfImages

#create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#bind the socket to a public host,
# and a well-known port
serversocket.bind((socket.gethostname(), 5069))
#become a server socket
serversocket.listen(5)  #only listens for 5 connections


def connAccepted(conn):
    try:
        data = json.loads(readJSON(conn))
        if data['function'] == 'register':
            successful = register(data)
            conn.send(successful+'\n')
        elif data['function'] == 'login':
            successful = login(data)
            print successful
            conn.send(successful+'\n')
            print 'done sending'
        elif data['function'] == 'upload':
            successful, returnFolder = saveImageData(data)
            conn.send(successful+'\n')
            gcm_ID = data['gcm_ID']
            if returnFolder != '-1':
                print 'DONE!' + str(returnFolder)
                sendComparedImagesGCM(returnFolder, gcm_ID)
                #storeUserNumberOfImages(data, returnFolder)
                deleteFiles(returnFolder)
        conn.close()
    except:
        print 'caught timeout'
        conn.close()
        exit(1)

while 1:
    #accept connections from outside
    print 'listening for data'
    (conn, address) = serversocket.accept()

    print 'accepted'
    print conn
    p = Process(target=connAccepted, args=(conn,))
    p.start()
    print 'process id:' + str(p.pid)

