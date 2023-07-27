# Convert DER files to Zeek root_certs
If you want to get rid the notices `SSL certificate validation failed with ...` messages, you can download the Root Certificate and upload it to Zeek. 

## Why this happens

Zeek uses Mozilla's list with Root CA's, but some applications store some Root CA's in their local datastore (e.g microsoft update, apple etc.). Hence Zeek cannot resolve properly the certificate.



## Bash script to do all the steps

You can run the bash script which search in the Certificate. 

Then wil find the AIA URL and download the `crt` file. 

Finally the bash script will calls the Python script to convert to Zeek suitable format 
for `SSL::root_certs`.

Example:
```
./get_AIA.sh slscr.update.microsoft.com
```


## Steps for Python Script (If you don't want to run the bash script)

1. Download the `Root Certificate` .

2. If it is in `PEM` format first run the command  to convert it to `DER` format.
```
cat o.pem |  sed -n '/BEGIN/,/END/p' | openssl x509 -outform DER > o.der
```

3. Then run `python3 convert_DER_to_zeek.cert.py <file.der>`

4. Get the output of the above command and copy it to a `zeek script file`. Output example of the converter:
```
["KSNGlobalRootCAECC"] = "\x30\x82\x02\x52\x30\x82\x01\xB4\xA0\x03\x02\x01\x02\x02\x10\x14\x69\xC4\x69\xB6\xD5\x4E\x90\x4D\x6B\x82\x01\x4E\xFF\x92\x91\x30\x0A\x06\x08\x2A\x86\x48\xCE\x3D\x04\x03\x03\x30\x3E\x31\x0B\x30\x09\x06\x03\x55\x04\x06\x13\x02\x52\x55\x31\x12\x30\x10\x06\x03\x55\x04\x0A\x13\x09\x4B\x61\x73\x70\x65\x72\x73\x6B\x79\x31\x1B\x30\x19\x06\x03\x55\x04\x03\x13\x12\x4B\x53\x4E\x20\x47\x6C\x6F\x62\x61\x6C\x20\x52\x6F\x6F\x74\x20\x43\x41\x30\x1E\x17\x0D\x32\x30\x30\x36\x31\x32\x30\x39\x35\x32\x33\x36\x5A\x17\x0D\x33\x35\x30\x36\x31\x32\x31\x30\x30\x32\x33\x35\x5A\x30\x3E\x31\x0B\x30\x09\x06\x03\x55\x04\x06\x13\x02\x52\x55\x31\x12\x30\x10\x06\x03\x55\x04\x0A\x13\x09\x4B\x61\x73\x70\x65\x72\x73\x6B\x79\x31\x1B\x30\x19\x06\x03\x55\x04\x03\x13\x12\x4B\x53\x4E\x20\x47\x6C\x6F\x62\x61\x6C\x20\x52\x6F\x6F\x74\x20\x43\x41\x30\x81\x9B\x30\x10\x06\x07\x2A\x86\x48\xCE\x3D\x02\x01\x06\x05\x2B\x81\x04\x00\x23\x03\x81\x86\x00\x04\x00\xA8\x6D\x41\xC0\xF8\x37\xA8\xBD\x84\xCB\xC6\x52\xE2\xD1\x07\x24\x05\x35\x77\x60\x5B\x7E\xAA\xC9\xFE\xDA\x07\x38\x4F\xB7\xB0\xA0\x5F\xD1\xA7\x96\x9C\x05\xE3\xC3\xDC\x50\x63\xBA\x63\xD9\x00\x0D\x0A\xAE\x4C\x0C\x90\xA4\x9E\x77\x11\xC6\x8B\x7F\xCC\xB9\x51\xD6\x46\x01\x1D\x22\xD3\x67\x41\xE8\x0B\xEE\xC7\xD6\xAA\xCD\xBA\x7B\x93\x02\xA9\x93\xFD\x8C\x6E\x7E\xA6\x04\xD7\x92\x2B\x77\x9F\xAB\xCD\x0D\x83\xC3\x2E\x5E\x9A\xD4\x3A\x9F\x72\x16\xF3\x2C\xA4\x24\x9B\x66\x65\xDB\x2D\x2D\x06\xC9\x45\x7F\x19\x01\x08\x68\xAE\xA7\x98\x4B\x9F\xA3\x51\x30\x4F\x30\x0B\x06\x03\x55\x1D\x0F\x04\x04\x03\x02\x01\x86\x30\x0F\x06\x03\x55\x1D\x13\x01\x01\xFF\x04\x05\x30\x03\x01\x01\xFF\x30\x1D\x06\x03\x55\x1D\x0E\x04\x16\x04\x14\x45\x31\xC5\x21\x7B\x9C\xCC\xBB\x8D\xFF\x73\x6D\x13\x94\x33\x51\x21\x3C\x8B\xDC\x30\x10\x06\x09\x2B\x06\x01\x04\x01\x82\x37\x15\x01\x04\x03\x02\x01\x00\x30\x0A\x06\x08\x2A\x86\x48\xCE\x3D\x04\x03\x03\x03\x81\x8B\x00\x30\x81\x87\x02\x42\x00\xC2\x28\x41\x40\x53\x00\xBD\x02\x97\x3E\x94\x41\x99\xAE\x70\xE3\x51\x00\x4C\x13\x3D\xFD\xC3\x58\x5A\xBA\x54\xF8\x5F\x82\x9C\x2C\xA1\xC6\x05\x6C\x61\x9F\xA9\x49\x3A\x13\x86\xDB\xA2\xCB\x65\xDC\x07\xF1\xEA\xBB\x00\x18\x70\x29\xF2\x43\xA5\xFD\xC8\x54\x73\x53\xCD\x02\x41\x75\x42\xDB\x08\xA2\xDA\xAA\x8C\xEC\x93\x33\xBF\x02\x6C\xB0\xEA\xCD\x88\x92\x3A\x37\x2E\x6A\x30\x46\xD5\x2B\x14\xAA\x93\x9D\xF8\x05\x0A\x03\x3C\x40\xE8\x81\x3F\xAF\x66\x7F\x67\x96\x65\xE4\x6C\xC3\x89\x30\xBA\xDD\x45\x43\x16\x84\x9F\xB2\x72\x31\x23\xFA\xD6\x80"
```

## How to add it to Zeek

Create a `Zeek script` which will have structure like the below example:
```
redef SSL::root_certs += {
  ["KSNGlobalRootCAECC"] = "\x30\x82\x02\x52... ,
  ["test 2"] = "\x30\x82...
};
```

and load (`@load`) the `zeek script file` to your `local.zeek` .
