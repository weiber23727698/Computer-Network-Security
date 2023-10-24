from Crypto.Util.number import getPrime, isPrime, GCD, bytes_to_long, long_to_bytes
import base64

c1 = b"HI9OZ9haVvc1gTyTFdr75OJ8tTklxQgczgGzwRYAUb6vN8oUyP6fgsPpIoYeXNAOtzIWBHH5Yyrj4sKuQN2j1GQFWjwoLA66SSNCNlbnRvAJqiUpTE7VuhVsy0jdGApf9aVvNO2S-MTAPLodXCo0PpMDFfj_oLfQdFTTv-W-WMRC0MpxxZ_T0UkE1EZ8SjJpxMqeJsq-CuXSNqjfaY3bC_-i05nr64ZO1YMNFa2-nVAM6QG4yKuLtLTjru5mT1b2hIcB1wMQpNIC9LEliu33eEVtB_j0Qn135Rw4knwEuf8jyMK0IMOwx1nzIMyR1lBM9X5yx8lvxSSgrHE6m6Nn2A"
c2 = b"NjFAI4NIKVoE8tsJf_y9x57qtBwwsX-YktkAumzFEZo5PWFZp9ASsLleMrO9cys-DKrEDUZyBjuw14TuYjZoLr-Q4bivyDKe8DQtwzKu3MUY7O-sIex4bx5dSWUB72uyunbMLrL3w4Ig2Qh4lZOkhcyPztz13A-voof8K-sD9ZCqOmgs_McZn2HW8Csyv36L0mLFFoXKlMZVqWSJPZ-gO7lz-4Z2XY8-99JVZOaaJEMgHvHNGnAalwCvgjHwc12IlNmfFKRihMmPN1l6iT2ukPsKD5RSjKSY0E7jc12oYExkSLpasfeCkLXmmOQaaTYzSI5O7n8t7TaNrs1ewe8UPQ"

m1 = b'{"alg":"RS256","typ":"JWT"}{"username":"guest","flag1":"CNS{JW7_15_N07_a_900d_PLACE_70_H1DE_5ecrE75}","exp":1686321967}'
m2 = b'{"alg":"RS256","typ":"JWT"}{"username":"guest","flag1":"CNS{JW7_15_N07_a_900d_PLACE_70_H1DE_5ecrE75}","exp":1686323331}'

e = [3, 17, 66537]
cipher1, cipher2 = bytes_to_long(c1), bytes_to_long(c2)
message1, message2 = bytes_to_long(m1), bytes_to_long(m2)

for x in e:    
    N = GCD(pow(cipher1, x) - message1, pow(cipher2, x) - message2)
    print(e, N)
    print(long_to_bytes(N))