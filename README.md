# ProfOfWorkBlockChain

Basic Blockchain with P2P Network and Wallet
This project is a simple implementation of a blockchain with a basic P2P network and wallet functionality. It demonstrates the core concepts of a blockchain, including mining, transaction validation, consensus, and wallet operations.

# Features
- Basic blockchain functionality
- Proof of Work (PoW) mining
- Simple transaction validation
- Basic consensus algorithm
- P2P network for node communication
- Wallet with public-private key pair generation and signature verification

# Dependencies
- Python 3.6+
- ecdsa (for wallet functionality)
- Git (optional)

# How to Run and Use
Clone the repository or download the source code:
```sh
git clone https://github.com/yourusername/blockchain-example.git
```
Change to the project folder:
```sh
cd blockchain-example
```
Create a Python virtual environment:
```sh
python -m venv venv
```
Activate the virtual environment:
On Windows:
```bash
venv\Scripts\activate
```
On macOS and Linux:
```sh
source venv/bin/activate
```
Install the required dependencies:
```sh
pip install -r requirements.txt
```
- Running the Nodes
Start the first node by running the run.py script with the node command:
```sh
python run.py node
```
Start additional nodes by specifying the port as a second argument:
```sh
python run.py node 5001
```
- Interacting with Nodes
Use the run.py script with the client command to interact with the nodes:
```sh
python run.py client
```
The client.py script demonstrates adding a new peer to a node and retrieving the list of peers from the node.

- Creating a Wallet and Testing Functionality

To create a wallet and test its functionality, run the run.py script with the wallet command:
```python
python run.py wallet
```
This script will generate a public-private key pair, sign a test message, and verify the signature.