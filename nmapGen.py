


import nmap

nmp = nmap.PortScannerAsync()
def callback_result(host, scan_result):
    print '==========='
    print host, scan_result

nmp.scan(hosts=hostsfile, arguments="-O -v", callback=callback_result)
while nmp.still_scanning():
    print("Waiting >>>")
    nm.wait(2)  