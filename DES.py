import base64
from Cryptodome.Cipher import DES

def decrypt_text(ciphertext, key):
    key = base64.b64decode(key)
    text = base64.b64decode(ciphertext)
    iv = text[:8]
    text = text[8:]
    cipher = DES.new(key, DES.MODE_CBC, iv)
    decrypted_text = cipher.decrypt(text)
    try:
        return decrypted_text.decode('utf-8')
    except UnicodeDecodeError:
        return decrypted_text  # or handle it as needed

ciphertext = "upa4z5/RUfCx1HVLFKLXOlIYSKb8a7zGn4D+dlPRATPbnz4N4CCBdKWr978T35iXCktj86og7M+2Qv260qHwkhbpxM1lXXNFcT/v7cb3UFy/5Q9md49vA7I0o8XCsZyo7KOTgmRonpzXbHzwXVOimcfTnh2v9pdggxCumDQ5jVpGrF8S7agqo+Ogts7I+xWHVtOqtlvtgkwXdypikfDuzZV9/NaQCmChulm1No/GnZtPnxYsu5hZcPJN8MRUOUss+C9q+oIZGxf04cBbSZnt9RCPFkZcjxRcHLyVn2TfsR7OJ0sbc4z19MqUxQvXPmb8CsRdgbs6QQ6fxtJWBvkm6Bu3Leuuu1cNOqHmtjdamc5xUtpzi7Z4UVWNgk67FIuzQGDcTfThFNumpjIiS6A7jfQmxT+Y7cQqc4FyIz8+He4hQxCciwCu2XLtNOFk+GXpM7BKZ5g4rInvOoR24xfLsZ8FVUCCDOJkWBZJq+LNKuP1p5cq3OXJfGDOTAjT7a/5pJXSarWTGuLMhrVDXLDLHc/QjOvphAqLbg1kjbgY76WFZug9iktesLlpdBqpb/+8n8mrkXqCYy0cZcGlbLMOqgOhcsKSkDzRo08J4dqpQjyKCQroTltDbw=="
key = "c3Bpcml0dXM="

decrypted_text = decrypt_text(ciphertext, key)
print(decrypted_text)