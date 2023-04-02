import sys
import subprocess

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python run.py [node|client|wallet] [port]")
        sys.exit(1)

    command = sys.argv[1]

    if command == 'node':
        port = sys.argv[2] if len(sys.argv) > 2 else '5000'
        subprocess.run(f"python node.py {port}", shell=True)
    elif command == 'client':
        subprocess.run("python client.py", shell=True)
    elif command == 'wallet':
        subprocess.run("python wallet.py", shell=True)
    else:
        print("Invalid command. Use 'node', 'client', or 'wallet'.")
