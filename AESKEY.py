import base64
from Crypto.Cipher import AES

## Time & Date <3

# The JSON object containing the encrypted data
json_data = '''
{
    "iv": "jirytQahcnWoUKtDYk9Yw==",
    "v": 1,
    "iter": 256,
    "mode": "ccm",
    "adata": "",
    "cipher": "aes",
    "salt": "qE7CLva0jis=",
    "ct": "WKMgZK6cafU9lpe+v9eTk1vO5Gwnyq1Rffd2aKUwpmSosDjsU+SFsLXurnlqhUe8IG1pxsevTqlbe7xCDFbe"
}

# Convert the base64-encoded JSON object to a Python dictionary
data = json.loads(base64.b64decode(json_data))

# The key used for encryption
key = b'this_is_the_key_used_for_encryption'

# The salt value used for key derivation
salt = base64.b64decode(data['salt'])

# The initialization vector used for encryption
iv = base64.b64decode(data['iv'])

# The ciphertext to be decrypted
ct = base64.b64decode(data['ct'])

# Create an AES cipher in CCM mode with a 256-bit key size
cipher = AES.new(key, AES.MODE_CCM, iv=iv)

# Set the authentication data to an empty string
cipher.update(b'')

# Set the nonce (iv) length to 13 bytes
cipher.nonce_size = 13

# Decrypt the ciphertext and authenticate the data
plaintext = cipher.decrypt_and_verify(ct, data['adata'])

# Print the decrypted plaintext
print(plaintext.decode())
