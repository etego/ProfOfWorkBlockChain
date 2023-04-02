import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, timestamp, transactions, nonce):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.transactions = transactions
        self.nonce = nonce

    def hash(self):
        # Concatenate block data and hash it
        block_str = f'{self.index}{self.previous_hash}{self.timestamp}{self.transactions}{self.nonce}'
        return hashlib.sha256(block_str.encode()).hexdigest()

def create_genesis_block():
    # Create the first block of the blockchain, called the "Genesis Block"
    return Block(0, '0', time.time(), [], 0)

def mine_block(previous_block, transactions):
    index = previous_block.index + 1
    timestamp = time.time()
    nonce = 0
    new_block = Block(index, previous_block.hash(), timestamp, transactions, nonce)

    # Mine the block by incrementing the nonce until a valid Proof of Work is found
    while not is_valid_proof_of_work(new_block):
        nonce += 1
        new_block.nonce = nonce

    return new_block

def is_valid_proof_of_work(block, difficulty=4):
    # Check if the block's hash starts with the required number of leading zeros (difficulty)
    return block.hash()[:difficulty] == '0' * difficulty

def validate_transactions(transactions):
    # In this basic example, we only check if the sum of inputs equals the sum of outputs
    input_sum = sum(tx['input'] for tx in transactions)
    output_sum = sum(tx['output'] for tx in transactions)
    return input_sum == output_sum

def resolve_conflicts(blockchains):
    # A simple consensus algorithm that chooses the longest valid chain
    longest_chain = blockchains[0]
    max_length = len(longest_chain)

    for blockchain in blockchains[1:]:
        length = len(blockchain)
        if length > max_length:
            longest_chain = blockchain
            max_length = length

    return longest_chain

# Create and mine some blocks
blockchain = [create_genesis_block()]
num_blocks_to_mine = 5

for i in range(1, num_blocks_to_mine + 1):
    transactions = [{'input': 10, 'output': 10}]  # Basic transaction data
    if validate_transactions(transactions):
        new_block = mine_block(blockchain[-1], transactions)
        blockchain.append(new_block)
        print(f'Mined block {i}: {new_block.hash()}')
    else:
        print(f'Invalid transactions for block {i}')

# Simulate a conflict between multiple blockchains
blockchain1 = blockchain.copy()
blockchain2 = blockchain.copy()

# Mine a new block on each chain
block1_transactions = [{'input': 10, 'output': 10}]
block2_transactions = [{'input': 20, 'output': 20}]

if validate_transactions(block1_transactions):
    new_block = mine_block(blockchain1[-1], block1_transactions)
    blockchain1.append(new_block)

if validate_transactions(block2_transactions):
    new_block = mine_block(blockchain2[-1], block2_transactions)
    blockchain2.append(new_block)

# Use the consensus algorithm to resolve the conflict
blockchain = resolve_conflicts([blockchain1, blockchain2])
print(f'\nResolved blockchain: {[block.hash() for block in blockchain]}')