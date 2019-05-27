import hashlib
import datetime


def calc_hash(data):
    sha = hashlib.sha256()
    hash_str = data.encode('utf-8')
    sha.update(hash_str)
    return sha.hexdigest()

class Block:

    def __init__(self, data):
      self.timestamp = datetime.datetime.now()
      self.data = data
      self.previous_hash = None
      self.hash = calc_hash(data)

    def __repr__(self):
      return "Block is created on {} with data {} and its hashed value as {}, the previous hash is {}".format(self.timestamp, self.data, self.hash, self.previous_hash) 


class BlockChain:

    def __init__(self):
      self.head = None
      self.block_address = {}

    def add(self, data):
      block = Block(data)
      # print(block)
      if self.head:
        block.previous_hash = self.head.hash
      self.head = block
      self.block_address[self.head.hash] = block

    def remove(self, data):
      hashed_data = calc_hash(data)
      next_block = current_block = self.head
      if current_block.hash == hashed_data:
        self.head = self.block_address[current_block.previous_hash]
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
        current_block = self.block_address[block.previous_hash]

    def traverse(self):
      block = self.head
      while True:
        print(block)
        if block.previous_hash in self.block_address:
          block = self.block_address[block.previous_hash]
        else: 
          break

def block_chain_app():
  block_chain = BlockChain()
  block_chain.add("Transaction 9")
  block_chain.add("Transaction 10")
  block_chain.traverse()      


if __name__ == '__main__':
  block_chain_app()


        
