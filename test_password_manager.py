import unittest
import os
import string
from main import generate_password, encrypt_message, decrypt_message, load_key, save_password, retrieve_passwords

class TestPasswordManager(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.key = load_key()

    def tearDown(self):
        # Clean up the passwords file after each test to avoid interference
        if os.path.exists("passwords.txt"):
            os.remove("passwords.txt")

    # Test password generation with valid length
    def test_generate_password(self):
        password = generate_password(12)
        self.assertEqual(len(password), 12)
        self.assertTrue(any(char.islower() for char in password))
        self.assertTrue(any(char.isupper() for char in password))
        self.assertTrue(any(char.isdigit() for char in password))
        self.assertTrue(any(char in string.punctuation for char in password))

    # Test password generation with minimum length
    def test_generate_password_min_length(self):
        password = generate_password(4)
        self.assertEqual(len(password), 4)
    
    # Test password generation with maximum length
    def test_generate_password_max_length(self):
        password = generate_password(100)
        self.assertEqual(len(password), 100)
    
    # Test password generation with invalid length (negative)
    def test_generate_password_negative_length(self):
        password = generate_password(-5)
        self.assertIsNone(password)

    # Test password generation with excessively large length
    def test_generate_password_excessive_length(self):
        password = generate_password(101)
        self.assertIsNone(password)

    # Test encrypt/decrypt message with valid input
    def test_encrypt_decrypt_message(self):
        message = "TestPassword123!"
        encrypted_message = encrypt_message(message, self.key)
        decrypted_message = decrypt_message(encrypted_message, self.key)
        self.assertEqual(decrypted_message, message)
    
    # Test encryption with empty input
    def test_encrypt_empty_message(self):
        encrypted_message = encrypt_message("", self.key)
        self.assertIsNone(encrypted_message)

    # Test decryption with empty input
    def test_decrypt_empty_message(self):
        decrypted_message = decrypt_message(b"", self.key)
        self.assertIsNone(decrypted_message)

    # Test encryption with invalid key
    def test_encrypt_message_with_invalid_key(self):
        invalid_key = b"invalid_key_for_testing"  # Simulate an invalid key
        message = "TestPassword123!"
        encrypted_message = encrypt_message(message, invalid_key)
        self.assertIsNone(encrypted_message)

    # Test decryption with invalid key
    def test_decrypt_message_with_invalid_key(self):
        message = "TestPassword123!"
        encrypted_message = encrypt_message(message, self.key)
        invalid_key = b"invalid_key_for_testing"
        decrypted_message = decrypt_message(encrypted_message, invalid_key)
        self.assertIsNone(decrypted_message)

    # Test saving and retrieving passwords
    def test_save_and_retrieve_passwords(self):
        password = "SamplePassword123!"
        encrypted_password = encrypt_message(password, self.key)
        save_password(encrypted_password)

        with open("passwords.txt", "r") as file:
            lines = file.readlines()
            self.assertEqual(len(lines), 1)
            self.assertIn(encrypted_password.decode(), lines[0])

        # Retrieve and decrypt saved passwords
        retrieve_passwords(self.key)

    # Test retrieve passwords when no file exists
    def test_retrieve_passwords_no_file(self):
        self.assertFalse(os.path.exists("passwords.txt"))
        retrieve_passwords(self.key)

    # Test loading key with missing file
    def test_load_key_no_file(self):
        if os.path.exists("secret.key"):
            os.remove("secret.key")
        key = load_key()
        self.assertIsNotNone(key)
        self.assertTrue(os.path.exists("secret.key"))

if __name__ == "__main__":
    unittest.main()
