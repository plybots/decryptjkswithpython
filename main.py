# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
import base64

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Encrypted message received from Java
    encrypted_message_base64 = "IfJIfQi6VRa5zaGKt7m6cEQarY7b531uABKAEu9+goQ82B8nF94Kcz1R+q6aBXUeFd6g5yRbATe3NlNZ0toaZU6NdD/VaU5G5MfzvfTbutGunex2DLt7rs9xH6pu1wPr7QQP7NrPAXaY8k1UrZoxKxcONUr3LrFsAVTUSCIxFMaIIb/QHB1rOjtDmviepo8NRhM9J4CMEBHzHHCuNHLvlqzKetdccXpLH4rHIvJrXKJUSDMEIcNyjO7m+h/2DCb+fiH4xhuTJS0qJtIQRnTMI5FmHc2xUD6wQgjPKgp/C1LeJreNVTOpcC7jvJO0af7LH/1CGTexBw8WyRxaUBWA2Q=="  # Replace with the actual base64-encoded encrypted message

    # Load private key from PEM file
    private_key_path = "C:\\Users\\whipp\\Projects\\encryptwithjks\\src\\main\\resources\\privatekey.pem"  # Replace with the actual path to your private key file

    with open(private_key_path, 'r') as key_file:
        private_key_data = key_file.read()

    private_key = RSA.import_key(private_key_data)

    # Decode the base64-encoded encrypted message
    encrypted_message_bytes = base64.b64decode(encrypted_message_base64)

    # Decrypt the message using the private key with PKCS#1 v1.5 padding
    cipher = PKCS1_v1_5.new(private_key)
    decrypted_message_bytes = cipher.decrypt(encrypted_message_bytes, sentinel=None)

    # Convert the decrypted bytes to a string
    decrypted_message = decrypted_message_bytes.decode('utf-8')

    # Print the decrypted message
    print("Decrypted Message:", decrypted_message)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
