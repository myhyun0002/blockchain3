# main.py
from app.blockchain import Blockchain

def main():
    # Blockchain 생성자를 이용해 인스턴스를 생성하고, 필요한 인자를 전달합니다.
    bitcoin = Blockchain()

    # previous_block_hash = '519619156945694516'
    # current_block_data = [
    #     {
    #         'amount' : 10,
    #         'sender' : 'BAD48461AB6',
    #         'recipient' : 'ag4a6e4g9a4w5eg',
    #     },
    #     {
    #         'amount' : 30,
    #         "sender" : '15DSGA86G4AD46GAE',
    #         'recipient' : 'aega6we16ga1we65g1',
    #     },
    #     {
    #         'amount' : 100,
    #         "sender" : 'GAWEKGAWE66GA16W1E1661',
    #         'recipient' : 'a6w191a9be156b1a',
    #     },
    # ]
    # nonce = 100


    bc1 = {
    "chain": [
        {
            "hash": "c508f51ca3ed3d7af1842e50d6fd7ea2a2d046a324a00b447a4875545fc71532",
            "index": 1,
            "merkle_root": "25f854be9f7a4d6952775b88a425e9c876010c5fa56d8c54eaae2bda456a3443",
            "nonce": 778,
            "previous_block_hash": "5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9",
            "timestamp": 1684738845446,
            "transactions": [
                {
                    "amount": 50,
                    "recipient": "5136ccfbe4bc45628a86caaecc440cfb",
                    "sender": "0",
                    "transaction_id": "9e68000db7ca4492a4fea0f146a354e7"
                }
            ]
        },
        {
            "hash": "000077e9e3a6b230d247e15cb3e302db45d867ad54fcce80504206571fe1d04b",
            "index": 2,
            "merkle_root": "2b743aebfd39acd9961bb82988a6f2c2e165e76032c0a2a8b5495046602bd778",
            "nonce": 29126,
            "previous_block_hash": "c508f51ca3ed3d7af1842e50d6fd7ea2a2d046a324a00b447a4875545fc71532",
            "timestamp": 1684738855094,
            "transactions": [
                {
                    "amount": 6.25,
                    "recipient": "00",
                    "sender": "00",
                    "transaction_id": "f33d101c0f544d2e825cf039b1b5a3c5"
                },
                {
                    "amount": 300,
                    "recipient": "sdfs",
                    "sender": "myhyun0002"
                }
            ]
        }
    ],
    "current_node_url": "http://localhost:5000",
    "genesis_nonce": 778,
    "merkle_tree_proecss": [],
    "network_nodes": [],
    "pending_transactions": [
        {
            "amount": 6.25,
            "recipient": "6a155c62f4ff4fd386ba0f8a815ac59e",
            "sender": "00",
            "transaction_id": "52308296225743a8a6f6473b2f8a20a2"
        }
    ]
}

    

    print('VALID:', bitcoin.chain_is_valid(bc1['chain']))
    #print(bitcoin.hash_block(previous_block_hash,current_block_data,900))

if __name__ == "__main__":
    main()
