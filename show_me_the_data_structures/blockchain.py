import hashlib



class Block:

    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash()

    def calc_hash data(self):
      sha = hashlib.sha256()
      hash_str = self.data.encode('utf-8')
      sha.update(hash_str)
      return sha.hexdigest()

class BlockChain:

    def __init__(self):
        self.head = None
        self.map = {}

    def add(self, block):
        # if self.head:
        #
        # else:
        #     self.head =
        pass
