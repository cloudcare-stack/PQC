import numpy as np

'''
    Author: Colin McAteer
    Due Date: 9/28/2025
'''

class A2:
    # define a method generate_public_key_vector that takes as input 4 VALUES
    def generate_public_key_vector(self, A, s, e, mod):
        '''
        Args:
            A (m X n): maxtrix
            s (int): Secret key
            e (int): Error vector
            mod (int): Modulus
        '''
        A = np.array(A)
        s = np.array(s)
        e = np.array(e)
        b = (A.dot(s) + e) % mod
        
        # return as NumPy array
        return b

    # define a method encrypt that takes input 4 VALUES
    def encrypt(self, public_key, r, message_bit, mod):
        '''
        Args:
            public_key (tuple): A, b
            r (list): Binary vector (0s and 1s)
            message_bit (int): 0 or 1
            mod (int): Modulus
        '''
        A, b = public_key
        A = np.array(A)
        b = np.array(b)
        r = np.array(r)

        u = np.sum(A[r == 1], axis = 0) % mod
        v = np.sum(b[r == 1]) % mod

        #add [p/2] if message == 1
        if message_bit == 1:
            v = (v + mod // 2) % mod

        #return the encryption tuple
        return (u, v)

    # define a method decrypt that takes as input 3 VALUES
    def decrypt(self, private_key, cipher, p):
        '''
        Args:
            s (list): Secret key vector
            cipher(tuple): (u, v)
            mod(int): Modulus
        '''
        u, v = cipher
        u = np.array(u)
        s = np.array(private_key)

        #compute dot product mod p
        result = np.dot(u, s) % p
        diff = (v - result) % p


        #return decrypted message (0 or 1)
        if (diff <= p // 4).any() or (diff >= p - (p // 4)).all():
            return 0
        else:
            return 1