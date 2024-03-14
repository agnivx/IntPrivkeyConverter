import pyfiglet
import textwrap
import requests
import pyfiglet
import textwrap
import requests
import bitcoinlib

from bitcoinlib.keys import Key

banner_text = "IntPrivkey Converter"
wrapped_text = "\n".join(textwrap.wrap(banner_text, width=40))
banner = pyfiglet.figlet_format(wrapped_text)
print(banner)

# Print the welcome message
print('Welcome to IntPrivkey Converter!')

# Define a function to check the balance of a Bitcoin address
def check_balance(address):
    try:
        url = f"https://blockchain.info/q/addressbalance/{address}"
        response = requests.get(url)
        balance_satoshi = int(response.text)
        balance_btc = balance_satoshi / 10**8  # Convert Satoshi to BTC
        return balance_btc
    except Exception as e:
        print(f"Error checking balance: {e}")
        return None

def integer_to_private_key(integer_value):
    # Convert the integer to a 64-character hexadecimal string
    private_key_hex = format(integer_value, '064x')
    return private_key_hex

try:
    # Prompt for input of an integer
    integer_value = int(input("Enter an integer: "))

    # Convert integer to private key
    private_key_hex = integer_to_private_key(integer_value)

    # Create a Bitcoin key pair for compressed
    key_compressed = Key(private_key_hex)

    # Create a Bitcoin key pair for uncompressed
    key_uncompressed = Key(private_key_hex, compressed=False)

    # Get the WIF private keys for compressed and uncompressed addresses
    wif_private_key_compressed = key_compressed.wif()
    wif_private_key_uncompressed = key_uncompressed.wif()

    # Get the Bitcoin addresses
    btc_address_compressed = key_compressed.address()
    btc_address_uncompressed = key_uncompressed.address()

    # Check the balance of compressed and uncompressed addresses
    balance_compressed = check_balance(btc_address_compressed)
    balance_uncompressed = check_balance(btc_address_uncompressed)

    print("Private Key (Hexadecimal):", private_key_hex)
    print("WIF Private Key (Compressed):", wif_private_key_compressed)
    print("Bitcoin Address (Compressed):", btc_address_compressed)
    print(f"Balance (Compressed): {balance_compressed:.8f} BTC")
    print("WIF Private Key (Uncompressed):", wif_private_key_uncompressed)
    print("Bitcoin Address (Uncompressed):", btc_address_uncompressed)
    print(f"Balance (Uncompressed): {balance_uncompressed:.8f} BTC")
except ValueError:
    print("Invalid input. Please enter a valid integer.")