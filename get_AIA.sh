#!/bin/bash
WORKING_DIR="/tmp"
#URL="slscr.update.microsoft.com"
URL=$1
openssl s_client -host $URL -port 443 -showcerts < /dev/null | sed -n '/BEGIN/,/END/p' | openssl x509 -noout -text > $WORKING_DIR/temp.txt 2>/dev/null
AIA_URL=$(cat $WORKING_DIR/temp.txt | grep "CA Issuers" | grep -oE "http://.*\.crt" )
curl $AIA_URL -s -o $WORKING_DIR/temp_aia.crt
SHA256SUM=$(sha256sum $WORKING_DIR/temp_aia.crt | cut -d' ' -f1)
CRT_NAME=$(openssl x509 -in $WORKING_DIR/temp_aia.crt -noout -text | sed -nr 's/Issuer:\s+(.*)/\1/p' | awk '{$1=$1};1')
mv $WORKING_DIR/temp_aia.crt $WORKING_DIR/"$CRT_NAME".crt
ZEEK_RECORD=$(python3 convert_der_to_zeek_cert.py $WORKING_DIR/"$CRT_NAME".crt)

echo -e "\n\n"
echo $ZEEK_RECORD

rm -f $WORKING_DIR/{temp.txt,"$CRT_NAME".crt}
