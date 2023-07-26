#!/usr/bin/env python
import binascii
import sys
import os

result = ""

def fetch_certificate_as_der_hex(bytes_file):

    der_hex_representation = binascii.hexlify(bytes_file," ").decode()

    return der_hex_representation

if len(sys.argv)<2:
    print("Usage: python3 "+sys.argv[0]+" <file.der>")
    exit()

try:
    file_path = sys.argv[1]
    full_name= os.path.basename(file_path)
    file_name = os.path.splitext(full_name)
    filename = file_name[0]
    # Download AIA Root Certificate e.g "./helloRoot.crt"
    # openssl s_client -host slscr.update.microsoft.com -port 443 -showcerts < /dev/null | sed -n '/BEGIN/,/END/p' | openssl x509 -outform DER > o.der
    # If it is PEM convert it to DER with the command below
    # cat o.pem |  sed -n '/BEGIN/,/END/p' | openssl x509 -outform DER > o.der
    with open(file_path,'rb') as f:
        file_data = fetch_certificate_as_der_hex(f.read())
        file_data  = file_data.replace("\n","").upper().split(" ")
        for x in file_data:
            result = result+"\\x"+x
        print("[\""+filename+"\"] = \""+result+"\"")
    """
    Add it to a cacert.zeek file and the load it to local.zeek
    cacert.zeek contents example
    redef SSL::root_certs += {
        ["test"] = "hex" ,
        ["test2"] = "hex2"
    };
    """
    f.close()
except FileNotFoundError as e:
    print("Certificate File not found...")
