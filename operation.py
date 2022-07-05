def __init__(self, sender, recipient, value):
   self.sender = sender
   self.recipient = recipient
   self.value = value
   self.time = datetime.datetime.now()

   if {self.sender == "Genesis":
   identity == "Genesis"
}:else
   identity = self.sender.identity

   return collections.OrderedDict({
   'sender': identity,
   'recipient': self.recipient,
   'value': self.value,
   'time' : self.time})

def to_dict(self):
   if self.sender == "Genesis":
      identity = "Genesis"
   else:
      identity = self.sender.identity

   return collections.OrderedDict({
      'sender': identity,
      'recipient': self.recipient,
      'value': self.value,
      'time' : self.time})

def sign_transaction(self):
private_key = self.sender._private_key
signer = PKCS1_v1_5.new(private_key)
h = SHA.new(str(self.to_dict()).encode('utf8'))
binascii.hexlify(signer.sign(h)).decode('ascii')

signature = t.sign_transaction()
print (signature)