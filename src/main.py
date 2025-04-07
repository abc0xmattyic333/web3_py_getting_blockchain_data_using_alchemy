# Hello, and welcome to this tutorial on how to use the Web3.py library to interact with the Ethereum blockchain, and other EVM-compatible blockchains.

# What is web3?
# Web3 is a term that refers to the third generation of the World Wide Web, which aims to create a decentralized and user-centric internet.
# It is built on blockchain technology and aims to give users more control over their data and online interactions.
# Web3 is often associated with decentralized applications (dApps) that run on blockchain networks, such as Ethereum.
# Web3.py is a Python library that allows developers to interact with the Ethereum blockchain and other EVM-compatible blockchains.

# I am using VS Code as my IDE, but you can use any IDE of your choice.
# I have created a new directory called "web3_py_getting_blockchain_data_using_alchemy" and inside it, I have created a new folder called src, 
# within that folder I have created a Python file called "main.py".
# It is a good practice to create an environment for your project to avoid any conflicts with other projects.
# You can use virtual environments or conda environments to create an isolated environment for your project.

# Import the Web3 library
# Web3.py is a Python library that allows you to interact with the Ethereum blockchain and other EVM-compatible blockchains.
# It provides a simple and easy-to-use interface for interacting with smart contracts, sending transactions, and querying blockchain data.
# In this tutorial, we will be using the Web3.py library to get the latest block from the Ethereum blockchain using Alchemy.

# Inside your terminal, run the following command to install the Web3.py library:
# pip install web3
# This command will install the Web3.py library and its dependencies.
# Once the installation is complete, we can start writing our code.

# You will need to create an Alchemy account and get your API key.
# Alchemy is a blockchain development platform that provides a suite of tools and services for building and scaling blockchain applications.
# It offers a powerful API that allows you to interact with the Ethereum blockchain and other EVM-compatible blockchains.
# You can sign up for a free account at https://www.alchemy.com/ and create a new app to get your API key.
# You will want to create a new app on the Alchemy dashboard and select the Ethereum network as your blockchain or enable other EVM-compatible blockchains.
# Once you have created your app, you will be able to see your API key in the app settings.
# Once you have your API key, you can use it to connect to the Ethereum blockchain using the Web3.py library.

# We will be using the Alchemy API to connect to the Ethereum blockchain and other EVM-compatible blockchains.

# Lets start by importing the Web3 library and creating a new Python file called "main.py".

from web3 import Web3


# Connect to the Ethereum network
# w3 = Web3(Web3.HTTPProvider('https://eth-mainnet.g.alchemy.com/v2/dWyoVQk_WuDlDxaYSGZmbU_ECahte9_m'))

# Connect to Solana network
# w3 = Web3(Web3.HTTPProvider('https://solana-mainnet.g.alchemy.com/v2/dWyoVQk_WuDlDxaYSGZmbU_ECahte9_m))

# Connect to Worldchain network
# w3 = Web3(Web3.HTTPProvider('https://worldchain-mainnet.g.alchemy.com/v2/dWyoVQk_WuDlDxaYSGZmbU_ECahte9_m'))

# Connect to Shape network
# w3 = Web3(Web3.HTTPProvider('https://shape-mainnet.g.alchemy.com/v2/dWyoVQk_WuDlDxaYSGZmbU_ECahte9_m'))

# Connect to ZKsync network
# w3 = Web3(Web3.HTTPProvider('https://zksync-mainnet.g.alchemy.com/v2/dWyoVQk_WuDlDxaYSGZmbU_ECahte9_m'))

# Connect to OP Mainnet network
# w3 = Web3(Web3.HTTPProvider('https://opt-mainnet.g.alchemy.com/v2/dWyoVQk_WuDlDxaYSGZmbU_ECahte9_m'))

# Connect to Polygon PoS network
# w3 = Web3(Web3.HTTPProvider('https://polygon-mainnet.g.alchemy.com/v2/dWyoVQk_WuDlDxaYSGZmbU_ECahte9_m'))

# Connect to Geist network
# w3 = Web3(Web3.HTTPProvider('https://geist-mainnet.g.alchemy.com/v2/dWyoVQk_WuDlDxaYSGZmbU_ECahte9_m'))

# Connect to Arbitrum
# w3 = Web3(Web3.HTTPProvider('https://arb-mainnet.g.alchemy.com/v2/dWyoVQk_WuDlDxaYSGZmbU_ECahte9_m'))

# Connect to Starknet
# w3 = Web3(Web3.HTTPProvider('https://starknet-mainnet.g.alchemy.com/starknet/version/rpc/v0_7/dWyoVQk_WuDlDxaYSGZmbU_ECahte9_m'))

# Connect to Arbitrum Nova
# w3 = Web3(Web3.HTTPProvider('https://arbnova-mainnet.g.alchemy.com/v2/dWyoVQk_WuDlDxaYSGZmbU_ECahte9_m'))

# Connect to Astar
# Web3(Web3.HTTPProvider('https://astar-mainnet.g.alchemy.com/v2/dWyoVQk_WuDlDxaYSGZmbU_ECahte9_m'))

# Connect to Polygon zkEVM network
# w3 = Web3(Web3.HTTPProvider('https://polygonzkevm-mainnet.g.alchemy.com/v2/dWyoVQk_WuDlDxaYSGZmbU_ECahte9_m'))

# Connect to ZetaChain
# w3 = Web3(Web3.HTTPProvider('https://zetachain-mainnet.g.alchemy.com/v2/dWyoVQk_WuDlDxaYSGZmbU_ECahte9_m'))

# Connect to Fantom Opera
# w3 = Web3(Web3.HTTPProvider('https://fantom-mainnet.g.alchemy.com/v2/dWyoVQk_WuDlDxaYSGZmbU_ECahte9_m'))

# Connect to Mantle
# w3 = Web3(Web3.HTTPProvider('https://mantle-mainnet.g.alchemy.com/v2/dWyoVQk_WuDlDxaYSGZmbU_ECahte9_m'))

# Connect to Berachain
# w3 = Web3(Web3.HTTPProvider('https://berachain-mainnet.g.alchemy.com/v2/dWyoVQk_WuDlDxaYSGZmbU_ECahte9_m'))

# Connect to Blast
# w3 = Web3(Web3.HTTPProvider('https://blast-mainnet.g.alchemy.com/v2/dWyoVQk_WuDlDxaYSGZmbU_ECahte9_m'))

# Connect to Linea
# w3 = Web3(Web3.HTTPProvider('https://linea-mainnet.g.alchemy.com/v2/dWyoVQk_WuDlDxaYSGZmbU_ECahte9_m'))

# Connect to Zora
# w3 = Web3(Web3.HTTPProvider('https://zora-mainnet.g.alchemy.com/v2/dWyoVQk_WuDlDxaYSGZmbU_ECahte9_m'))

# Connect to Polynomial
# w3 = Web3(Web3.HTTPProvider('https://polynomial-mainnet.g.alchemy.com/v2/dWyoVQk_WuDlDxaYSGZmbU_ECahte9_m'))

# Connect to Base
# w3 = Web3(Web3.HTTPProvider('https://base-mainnet.g.alchemy.com/v2/dWyoVQk_WuDlDxaYSGZmbU_ECahte9_m'))

# Connect to Scroll
# w3 = Web3(Web3.HTTPProvider('https://scroll-mainnet.g.alchemy.com/v2/dWyoVQk_WuDlDxaYSGZmbU_ECahte9_m'))

# Connect to Gnosis
# w3 = Web3(Web3.HTTPProvider('https://gnosis-mainnet.g.alchemy.com/v2/dWyoVQk_WuDlDxaYSGZmbU_ECahte9_m'))

# Connect to Frax
# w3 = Web3(Web3.HTTPProvider('https://frax-mainnet.g.alchemy.com/v2/dWyoVQk_WuDlDxaYSGZmbU_ECahte9_m'))

# Connect to BNB Smart Chain
# w3 = Web3(Web3.HTTPProvider('https://bnb-mainnet.g.alchemy.com/v2/dWyoVQk_WuDlDxaYSGZmbU_ECahte9_m'))

# Connect to Avalanche
# w3 = Web3(Web3.HTTPProvider('https://avax-mainnet.g.alchemy.com/v2/dWyoVQk_WuDlDxaYSGZmbU_ECahte9_m'))

# Connect to Celo
# w3 = Web3(Web3.HTTPProvider('https://celo-mainnet.g.alchemy.com/v2/dWyoVQk_WuDlDxaYSGZmbU_ECahte9_m'))

# Connect to Metis
# w3 = Web3(Web3.HTTPProvider('https://metis-mainnet.g.alchemy.com/v2/dWyoVQk_WuDlDxaYSGZmbU_ECahte9_m'))

# Connect to opBnb
# w3 = Web3(Web3.HTTPProvider('https://opbnb-mainnet.g.alchemy.com/v2/dWyoVQk_WuDlDxaYSGZmbU_ECahte9_m'))

# Connect to CrossFi
# w3 = Web3(Web3.HTTPProvider('https://crossfi-mainnet.g.alchemy.com/v2/dWyoVQk_WuDlDxaYSGZmbU_ECahte9_m'))

# Connect to Flow EVM
# w3 = Web3(Web3.HTTPProvider('https://flow-mainnet.g.alchemy.com/v2/dWyoVQk_WuDlDxaYSGZmbU_ECahte9_m'))

# Connect to Sei
# w3 = Web3(Web3.HTTPProvider('https://sei-mainnet.g.alchemy.com/v2/dWyoVQk_WuDlDxaYSGZmbU_ECahte9_m'))

# Connect to ApeChain
# w3 = Web3(Web3.HTTPProvider('https://apechain-mainnet.g.alchemy.com/v2/dWyoVQk_WuDlDxaYSGZmbU_ECahte9_m'))

# Connect to Lens
# w3 = Web3(Web3.HTTPProvider('https://lens-mainnet.g.alchemy.com/v2/dWyoVQk_WuDlDxaYSGZmbU_ECahte9_m'))

# Connect to Soneium
# w3 = Web3(Web3.HTTPProvider('https://soneium-mainnet.g.alchemy.com/v2/dWyoVQk_WuDlDxaYSGZmbU_ECahte9_m'))

# Connect to Rootstock
# w3 = Web3(Web3.HTTPProvider('https://rootstock-mainnet.g.alchemy.com/v2/dWyoVQk_WuDlDxaYSGZmbU_ECahte9_m'))

# Connect to Lumia
# w3 = Web3(Web3.HTTPProvider('https://lumia-prism.g.alchemy.com/v2/dWyoVQk_WuDlDxaYSGZmbU_ECahte9_m'))

# Connect to Unichain
# w3 = Web3(Web3.HTTPProvider('https://unichain-mainnet.g.alchemy.com/v2/dWyoVQk_WuDlDxaYSGZmbU_ECahte9_m'))

# Connect to Sonic
# w3 = Web3(Web3.HTTPProvider('https://sonic-mainnet.g.alchemy.com/v2/dWyoVQk_WuDlDxaYSGZmbU_ECahte9_m'))

# Connect to XMTP
# w3 = Web3(Web3.HTTPProvider('https://xmtp-testnet.g.alchemy.com/v2/dWyoVQk_WuDlDxaYSGZmbU_ECahte9_m'))

# Connect to Absract 
# w3 = Web3(Web3.HTTPProvider('https://abstract-mainnet.g.alchemy.com/v2/dWyoVQk_WuDlDxaYSGZmbU_ECahte9_m'))

# Connect to Monad
# w3 = Web3(Web3.HTTPProvider('https://monad-testnet.g.alchemy.com/v2/dWyoVQk_WuDlDxaYSGZmbU_ECahte9_m'))

# Connect to Superseed
# w3 = Web3(Web3.HTTPProvider('https://superseed-mainnet.g.alchemy.com/v2/dWyoVQk_WuDlDxaYSGZmbU_ECahte9_m'))

# Connect to Degen
# w3 = Web3(Web3.HTTPProvider('https://degen-mainnet.g.alchemy.com/v2/dWyoVQk_WuDlDxaYSGZmbU_ECahte9_m'))

# Connect to Settlus
# w3 = Web3(Web3.HTTPProvider('https://settlus-mainnet.g.alchemy.com/v2/dWyoVQk_WuDlDxaYSGZmbU_ECahte9_m'))

# Connect to Ink
# w3 = Web3(Web3.HTTPProvider('https://ink-mainnet.g.alchemy.com/v2/dWyoVQk_WuDlDxaYSGZmbU_ECahte9_m'))

# Connect to Ronin
# w3 = Web3(Web3.HTTPProvider('https://ronin-mainnet.g.alchemy.com/v2/dWyoVQk_WuDlDxaYSGZmbU_ECahte9_m'))

# Connect to Gensyn
# w3 = Web3(Web3.HTTPProvider('https://gensyn-testnet.g.alchemy.com/v2/dWyoVQk_WuDlDxaYSGZmbU_ECahte9_m'))

# Connect to Tea
# w3 = Web3(Web3.HTTPProvider('https://tea-sepolia.g.alchemy.com/v2/dWyoVQk_WuDlDxaYSGZmbU_ECahte9_m'))

# Get block by number
# block_number = 'latest'  # Replace with the desired block number or use 'latest'
# block = w3.eth.get_block(block_number) # Get the latest block

# Print the block information
# print(block)

# The above code will print the latest block information, including the block number, hash, timestamp, and other details.
# Run the script using the following command:
# python main.py

# You should see the latest block information printed in the terminal.

# Inside our images folder you will find pictures of the output of the code above.

# You will notice that most of the hashes are in hexadecimal format.
# A HexByte is a byte string that is represented in hexadecimal format.
# It is a common format used in blockchain development to represent binary data in a human-readable form.
# HexBytes are often used to represent transaction hashes, block hashes, and other binary data in the Ethereum blockchain.

# What is the difference between a hash and a parent hash?
# A hash is a fixed-size string of characters that is generated by a hash function.
# It is a unique identifier for a block or transaction in the blockchain.
# A parent hash is the hash of the previous block in the blockchain.
# It is used to link the blocks together and create a chain of blocks.
# sha3Uncles is a hash of the uncle blocks that are included in the block.
# Uncle blocks are blocks that were mined but not included in the main chain.
# They are included in the block to reward the miners who mined them.
# The uncle blocks are included in the block to increase the security of the blockchain and to prevent double spending.

# Lets now comment out our code and write to other EVM-compatible blockchains.

#############################################################################
#############################################################################
#############################################################################

# Connect to Worldchain 
# Successful

# Connect to Solana
# Unsuccessful

# Connect to Shape
# Successful

# Connect to ZKsync.
# Successful.

# Connect to OP Mainnet.
# Successful.

# I will now try to connect to Polygon PoS network.
# That was successful but the response was odd, it returned a PoA network.
# What is PoA network?

# A PoA network is a type of blockchain network that uses a proof-of-authority consensus mechanism to validate transactions and create new blocks.
# In a PoA network, a small number of trusted nodes are responsible for validating transactions and creating new blocks.
# I thought it was a PoS network? I still received some form of response.
# I will now try to connect to Geist network.
# Successful.

# Connect to Arbitrum
# Successful

# Connect to Starknet
# Unsuccessful

# It seems like half of our attempts have been successful, we will continue trying the other networks on Alchemy's platform.
# I will try to connect to Arbitrum Nova.
# Successful

# Connect to Astar
# Successful

# Connect to Polygon zkEVM network.
# Successful

# Connect to ZetaChain.
# Successful

# We have coverd a ton of information already, thank you for bearing with me throughout this course.

# Connect ro Fantom Opera
# Successful

# You will notice the metrics has been getting better without any failed requests.

# Connect to Mantle
# Successful

# Connect to Berachain
# Successful

# Connect to Blast
# Successful

# Connect to Linea
# Sorta successful

# Connect to Zora
# Successful

# Connect to Polynomial
# Was unsucessful

# Connect to Base
# Successful

# Connect to Scroll
# Somewhat successful

# Connect to Gnosis
# Successful

# Connect to Frax
# Unsuccessful

# Connect to BNB Smart Chain
# Successful

# Connect to Avalanche
# Somewhat successful

# Connect to Celo
# Successful

# Connect to Metis
# Successful

# Connect to opBnb
# Successful

# Connect to CrossFi
# Successful

# Connect to Flow EVM
# Successful

# Connect to Sei
# Successful

# Connect to ApeChain
# Successful

# Connect to Lens
# Successful

# Connect to Soneium
# Successful

# Connect to Rootstock
# Successful

# Connect to Lumia
# Successful

# Connect to Unichain
# Successful

# Connect to Sonic
# Successful

# Connect to XMTP
# Successful

# Connect to Absract
# Successful

# Connect to Monad 
# Successful

# Connect to Superseed
# Successful

# Connect to Degen
# Successful

# Connect to Settlus
# Successful

# Connect to Ink
# Successful

# Connect to Ronin
# Unsuccessful

# Connect to Gensyn
# Successful

# Connect to Tea
# Successful

###################################################################################
###################################################################################
###################################################################################

# After going through all the networks on Alchemy's platform, we have successfully connected to most of them.
# Some of them returned odd responses but we were able to connect to them.

# We will dive further into the Web3.py library in the next tutorial.

###################################################################################
####################################################################################
####################################################################################

# Hey, welcome back to the tutorial on how to use the Web3.py library to interact with the Ethereum blockchain and other EVM-compatible blockchains.
# In today's tutorial, we will be using the Alchemy API to get asset transfers from the Ethereum blockchain and other EVM-compatible blockchains.``

# Import the requests library to make HTTP requests
# The requests library is a simple and easy-to-use library for making HTTP requests in Python.
# It allows you to send HTTP requests and handle responses in a simple and intuitive way.
# It is a popular library for making API requests in Python and is widely used in the Python community.
import requests
import json

# 🔑 Replace with your own Alchemy API Key
ALCHEMY_API_KEY = "dWyoVQk_WuDlDxaYSGZmbU_ECahte9_m"

# Connect to Ethereum 
# URL = f"https://eth-mainnet.g.alchemy.com/v2/{ALCHEMY_API_KEY}" 

# Connect to WorldChain
# URL = f"https://worldchain-mainnet.g.alchemy.com/v2/dWyoVQk_WuDlDxaYSGZmbU_ECahte9_m"

# Connect to Shape
# URL = f"https://shape-mainnet.g.alchemy.com/v2/dWyoVQk_WuDlDxaYSGZmbU_ECahte9_m" #

# Connect to ZKsync
# URL = f"https://zksync-mainnet.g.alchemy.com/v2/dWyoVQk_WuDlDxaYSGZmbU_ECahte9_m"

# Connect to OP 
# URL = f"https://opt-mainnet.g.alchemy.com/v2/dWyoVQk_WuDlDxaYSGZmbU_ECahte9_m"

# Connect to Polygon PoS
# URL = f"https://polygon-mainnet.g.alchemy.com/v2/dWyoVQk_WuDlDxaYSGZmbU_ECahte9_m"

# Connect to Geist
# URL = f"https://geist-mainnet.g.alchemy.com/v2/dWyoVQk_WuDlDxaYSGZmbU_ECahte9_m"

# Connect to Arbitrum
URL = f"https://arb-mainnet.g.alchemy.com/v2/dWyoVQk_WuDlDxaYSGZmbU_ECahte9_m"

# 📦 Define the payload for the JSON-RPC request
payload = {
    "jsonrpc": "2.0",
    "id": 1,
    "method": "alchemy_getAssetTransfers",
    "params": [
        {
            "fromBlock": "0x0",                   # From genesis block
            "toBlock": "latest",
            "category": ["external", "erc20", "erc721", "erc1155"],
            "withMetadata": True,
            "excludeZeroValue": True,
            "maxCount": "0x64",                  # 100 in hex
        }
    ]
}

# 🔁 Send the POST request
response = requests.post(URL, json=payload)
result = response.json()

# 🖨️ Print some transfers
transfers = result.get("result", {}).get("transfers", [])

print(f"Found {len(transfers)} transfers:\n")
for t in transfers:
    print(f"{t['asset']} from {t['from']} → {t['to']} | Tx: {t['hash']}")

# The above code will print the asset transfers from the Ethereum blockchain.
# Nicely done! :)

# Now we will go through and try connecting to the other corresponding networks on Alchemy's platform.

# Check reponse for WorldChain
# Successful

# Connect to Shape
# Successful

# Connect to ZKsync
# Successful

# Connect to Optimism 
# Successful

# Connect to Polygon PoS
# Successful

# Connect to Geist
# Unsuccessful

# Connect to Arbitrum
# Successful

########### Grab some more coffee! :) ################
########### Save what you have done so far! ###########
########### Satage changes and commit them! ###############
########### Push to your remote repository! ###############
########### You are doing great! :) ####################