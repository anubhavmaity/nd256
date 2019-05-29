import hashlib
import datetime


def calc_hash(data):
    sha = hashlib.sha256()
    hash_str = data.encode('utf-8')
    sha.update(hash_str)
    return sha.hexdigest()

class Block:

    def __init__(self, data):
      self.timestamp = datetime.datetime.now(datetime.timezone.utc)
      self.data = data
      self.previous_hash = None
      self.hash = calc_hash(data)

    def __repr__(self):
      return "Block is created on {} with data {} and its hashed value as {}".format(self.timestamp, self.data, self.hash)


class BlockChain:

    def __init__(self):
      self.head = None
      self.block_address = {}

    def add(self, data):
      block = Block(data)
      if self.head:
        block.previous_hash = self.head.hash
      self.head = block
      self.block_address[self.head.hash] = block

    def remove(self, data):
      hashed_data = calc_hash(data)
      current_block = self.head
      if current_block and current_block.hash == hashed_data:
        self.head = self.block_address[current_block.previous_hash] if current_block.previous_hash in self.block_address else None
        del self.block_address[current_block.hash]
        current_block.previous_hash = None
        return current_block

      while current_block:
        if current_block.hash == hashed_data:
          previous_block.previous_hash = current_block.previous_hash
          del self.block_address[hashed_data]
          current_block.previous_hash = None
          return current_block
        previous_block = current_block
        current_block = self.block_address[current_block.previous_hash] if current_block.previous_hash in self.block_address else None

      return current_block

    def traverse(self):
      block = self.head
      str = ''
      while True:
        if not block:
          str += 'None'
        else:
          str += repr(block) + ' -> '
        if block and block.previous_hash in self.block_address:
          block = self.block_address[block.previous_hash]
        else: 
          break
      return str

def block_chain_app():
  block_chain = BlockChain()
  print(block_chain.traverse())
  # None
  block_chain.add("Transaction 9")
  block_chain.add("Transaction 10")
  block_chain.add("Transaction 11")
  block_chain.add("Transaction 12")
  block_chain.remove("Transaction 10")
  block_chain.remove("Transaction 9")
  print(block_chain.traverse())
  # Block is created on 2019-05-29 09:48:55.100351+00:00 with data Transaction 12 and its hashed value as 58396bf6a2d410da6c5fee52df975e41ca92f0195db0a9624c96ebec9230b420 -> Block is created on 2019-05-29 09:48:55.100343+00:00 with data Transaction 11 and its hashed value as d0516c65790519d9e739b5596a1e467009dfacfa9155740aaf2620d3914cb6b6 ->


if __name__ == '__main__':
  block_chain_app()


        
