# CNS 2023 Spring Hw2
## TLS
There are several human-laboring steps to finish the problem.
```shell
python code4.py # You will get private_key.pem with the program.
```
* Add `private_key.pem` to the wireshark. It helps to decrypt the message within the packets
* Search through the wireshark, we can find the public key of the server and the valid username and password from Alice. Besides, we can find the command to find the key.
* Then, we can use following command to generate the root certificate and our certificate, i.e. `eve.crt`.
```shell
openssl req -new -key rootKey.key -out request.csr # get csr: enter (TW / Taiwan / Taipei / NTU CNS / VIP / VIP / cns@csie.ntu.edu.tw)
openssl req -x509 -new -key rootKey.key -out root.crt # get root certificate: enter (TW / Taiwan / Taipei / NTU CNS / ROOT / ROOT / cns@csie.ntu.edu.tw)
openssl x509 -req -in request.csr -CA root.crt -CAkey rootKey.key -CAcreateserial -out eve.crt -days 365 # get eve.crt
```
* The next step is to connect to server with the root key and `eve.crt`.
```shell
openssl s_client -connect cns.csie.org:12345 -cert eve.crt -key rootKey.key # connect to server:
```
* The final step is to enter the username, password and the command to get the flag.
    * username: Alice413
    * password: dogsarecute
    * command: Flag...plzzzzz...
## Little Knowledge Proof
```shell
python code5.py --problem 1 # flag1
python code5.py --problem 2 # flag2
python code5.py --problem 3 # flag3
```
## Clandestine Operation II
* I just finished the generation of type1 and the formatting of type2.
```shell
python code6.py
```
## So Anonymous, So Hidden
```shell
python code7.py --problem 1 # flag1
python code7.py --problem 2 # flag2
```
* Since the name of `lib.py` is different, if TA wants to run my code please change `code7-lib.py` to `lib.py` first.