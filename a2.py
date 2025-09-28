import num as np

'''
Args:
    A (m X n): maxtrix
    s (int): Secret key
    e (int): Error vector
    mod (int): Modulus
'''

# define a method generate_public_key_vector that takes as input 4 VALUES
def generate_public_key_vector(self, A, s, e, mod):
    
    A = np.array(A)
    s = np.array(s)
    e = np.array(e)
    b = (A.dots(s) + e) % mod
    
    # return as NumPy array
    return b

# define a method encrypt that takes input 4 VALUES
def encrypt(self, public_key, r, message_bit, mod):

    
    return (u, v)

# define a method decrypt that takes as input 3 VALUES
def decrypt(self, private_key, cipher, q):

    return