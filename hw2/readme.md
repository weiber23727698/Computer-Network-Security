# CNS 2023 Spring Hw2
## TLS
There are several human-laboring steps to finish the problem.
reference: https://www.alpertron.com.ar/ECM.HTM?fbclid=IwAR1XpZX3O7-bIT0Q7hbE8aLeif0vOh1a-i4Rjstm4yAi702tZvh8kvWEO0w

reference: https://stackoverflow.com/questions/4798654/modular-multiplicative-inverse-function-in-python
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
Here is the code from reference. https://shrek.unideb.hu/~tengely/crypto/section-6.html#p-204-part9
```python
def PohligHellman(g,h,p):
    pretty_print(html('The prime $p$ is $%s$'%latex(p)))
    F = GF(p)
    g1 = F(g)
    h1 = F(h)
    N = p-1
    qi = [r^N.valuation(r) for r in prime_divisors(N)]
    pretty_print(html('Prime power divisors of $p-1: %s$'%latex(qi)))
    lqi = len(qi)
    Nqi = [N/q for q in qi]
    gi = [g1^r for r in Nqi]
    hi = [h1^r for r in Nqi]
    xi = [discrete_log(hi[i],gi[i]) for i in range(lqi)]
    pretty_print(html('Discrete logarithms $x_i = %s$'%latex(xi)))
    x = CRT(xi,qi)
    pretty_print(html(r'We have that $\log_g h = %s$'%latex(x)))
    return x
```
Here is the output from the code.
```
PohligHellman(11,9561649903826401194424429829087038008994189104830088932155338858706813419184358908819778209856931077467756994935446807814714436047612742953865073558777496,14441638348624213626083118173029616034636236203323405960283519413957104355762238013154233838351528737517308038661176687865191516418733778513644060317253479)

The prime p is 14441638348624213626083118173029616034636236203323405960283519413957104355762238013154233838351528737517308038661176687865191516418733778513644060317253479
Prime power divisors of p−1:[2,9904578032905937,288441413567621167681,3091058643093537522799545838540043339063,1080244137479689290215446159447411025741704035417740877269,756943935220796320321]
Discrete logarithms xi = [1,5433650772715221,215701847164204296075,1765169489445336822335616493450319873721,522719848230573526650683484133826256116093515592372329920,371628781438728217083]
We have that loggh = 1995135457311837329338013220674023065119097253499626394183669323611116768755869053

1995135457311837329338013220674023065119097253499626394183669323611116768755869053
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
