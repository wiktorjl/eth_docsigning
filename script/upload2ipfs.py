# Uploads file to IPFS and provides CID

import ipfshttpclient
import sys
import requests
import argparse
from dotenv import load_dotenv
import os


load_dotenv()
app_key = os.getenv("IPFS_PROJECT_ID")
secret_key = os.getenv("IPFS_SECRET_KEY")


parser = argparse.ArgumentParser()
parser.add_argument("--mode", "-m", type=str)
parser.add_argument("--file", "-f", type=str)
args = parser.parse_args()


def upload_via_local_node(file_path):
    client = ipfshttpclient.connect('/ip4/127.0.0.1/tcp/5001')

    res = client.add(file_path)
    print("Address: " + str(res['Hash']))


def upload_via_gateway(file_path):

    url = 'https://ipfs.infura.io:5001/api/v0/add'

    files = {
        'file': file_path
    }

    response = requests.post(url, files=files, auth=(app_key, secret_key))

    # Print the IPFS hash of the uploaded file
    print("Address: " + str(response.text))


if __name__ == "__main__":
    if args.file is None or args.mode is None:
        print("Valid path and run mode are required...")
        sys.exit(1)

    file_path = args.file
    mode = args.mode

    if mode == "local":
        upload_via_local_node(file_path)
    elif mode == "gw":
        upload_via_gateway(file_path)
    else:
        print("Invalid mode")
        sys.exit(1)
