# Uploads file to IPFS and provides CID

import ipfshttpclient
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Valid path required...")
        sys.exit(1)

    client = ipfshttpclient.connect('/ip4/127.0.0.1/tcp/5001')
    file_path = sys.argv[1]
    res = client.add(file_path)
    print("Address: " + res['Hash'])
