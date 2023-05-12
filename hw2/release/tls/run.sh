#1. get csr:
openssl req -new -key rootKey.key -out request.csr
#//enter info (TW / Taiwan / Taipei / NTU CNS / VIP / VIP / cns@csie.ntu.edu.tw)

#2. get root certificate:
openssl req -x509 -new -key rootKey.key -out root.crt
#//enter info (TW / Taiwan / Taipei / NTU CNS / ROOT / ROOT / cns@csie.ntu.edu.tw)

#3. get eve.crt:
openssl x509 -req -in request.csr -CA root.crt -CAkey rootKey.key -CAcreateserial -out eve.crt -days 365

#4. connect to server:
openssl s_client -connect cns.csie.org:12345 -cert eve.crt -key rootKey.key