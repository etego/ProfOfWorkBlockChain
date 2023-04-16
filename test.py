from blockchain import Blockchain, Block, Transaction
from wallet import Wallet

def test_blockchain():
    # Create wallets
    wallet1 = Wallet()
    wallet2 = Wallet()

    # Create blockchain
    blockchain = Blockchain()

    # Create transactions
    txn1 = Transaction(wallet1.public_key, wallet2.public_key, 10)
    txn1.sign(wallet1.private_key)

    txn2 = Transaction(wallet2.public_key, wallet1.public_key, 5)
    txn2.sign(wallet2.private_key)

    # Verify transactions
    assert txn1.verify_signature()
    assert txn2.verify_signature()

    # Create a new block and add transactions
    new_block = Block()
    new_block.add_transaction(txn1)
    new_block.add_transaction(txn2)

    # Mine the block
    blockchain.mine_block(new_block)

    # Validate the blockchain
    assert blockchain.is_valid()

    # Print the blockchain
    print("Blockchain:")
    print(blockchain)

if __name__ == '__main__':
    test_blockchain()
