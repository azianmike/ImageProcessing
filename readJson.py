__author__ = 'michaelluo'

def readJSON(conn):
    try:
        print 'reading in json data'
        data = ''
        while (1):
            dataRecv = conn.recv(2048)
            if(len(dataRecv) == 0):
                raise Exception("caught timeout")
            data += dataRecv
            if '\r\n\r\n' in dataRecv:
                print 'stopped reading in json'
                break;

        return data[:-4]
    except:
        print 'caught timeout while reading'