import numpy as np
from a2 import A2

def main():
    a2 = A2()

    # Given example from assignment
    A = np.array([
        [1, 6, 6, 2],
        [6, 0, 5, 3],
        [2, 5, 4, 1]
    ])
    s = np.array([3, 4, 0, 6])
    e = np.array([0, -1, 1])
    p = 7

    print("===== TEST 1: Public Key Generation =====")
    b = a2.generate_public_key_vector(A, s, e, p)
    print("Computed b:", b)
    print("Expected b: [4 0 5]")
    assert np.array_equal(b, np.array([4, 0, 5])), "Public key generation failed!"
    print("Public key generation passed!\n")

    public_key = (A, b)

    print("===== TEST 2: Encryption (message = 0) =====")
    r = np.array([1, 0, 1])
    ciphertext_0 = a2.encrypt(public_key, r, 0, p)
    print("Ciphertext (msg=0):", ciphertext_0)
    print("Expected: ([3,4,3,3], 2)")
    assert np.array_equal(ciphertext_0[0], np.array([3, 4, 3, 3])) and ciphertext_0[1] == 2, "Encryption (0) failed!"
    print("Encryption (message=0) passed!\n")

    print("===== TEST 3: Encryption (message = 1) =====")
    ciphertext_1 = a2.encrypt(public_key, r, 1, p)
    print("Ciphertext (msg=1):", ciphertext_1)
    print("Expected: ([3,4,3,3], 5)")
    assert np.array_equal(ciphertext_1[0], np.array([3, 4, 3, 3])) and ciphertext_1[1] == 5, "❌ Encryption (1) failed!"
    print("Encryption (message=1) passed!\n")

    print("===== TEST 4: Decryption =====")
    msg0 = a2.decrypt(s, ciphertext_0, p)
    msg1 = a2.decrypt(s, ciphertext_1, p)
    print("Decrypted (msg=0):", msg0, "| Expected: 0")
    print("Decrypted (msg=1):", msg1, "| Expected: 1")
    assert msg0 == 0, "Decryption (0) failed!"
    assert msg1 == 1, "Decryption (1) failed!"
    print("Decryption passed!\n")

    print("All tests passed successfully!")

if __name__ == "__main__":
    main()
