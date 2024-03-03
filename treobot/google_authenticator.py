import os
import base64
import hashlib
import hmac
import time


class GoogleAuthenticator:
  _codeLength = 6

  def create_secret(self, secret_length=16):
    if secret_length < 16 or secret_length > 128:
      raise ValueError('Bad secret length')
    secret = os.urandom(secret_length)
    return base64.b32encode(secret).decode('utf-8')

  def get_code(self, secret, time_slice=None):
    if time_slice is None:
      time_slice = int(time.time()) // 30

    secretkey = base64.b32decode(secret, True)
    time_bytes = time_slice.to_bytes(8, 'big', signed=False)

    hmac_hash = hmac.new(secretkey, time_bytes, hashlib.sha1).digest()
    offset = hmac_hash[-1] & 0x0F
    code = (int.from_bytes(hmac_hash[offset:offset + 4], 'big')
            & 0x7FFFFFFF) % (10**self._codeLength)

    return str(code).zfill(self._codeLength)

  def set_code_length(self, length):
    self._codeLength = length
    return self
