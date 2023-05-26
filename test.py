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
            "hash": "90217d9c7860ca244b3488d60c88361c0c9a77f4f61ef3e77341bb8ad97ff2c1",
            "index": 1,
            "merkle_root": "51e0996b018ecf9266fea443ba627e1047777907125d139cbb20117d3bc1f38a",
            "nonce": 778,
            "previous_block_hash": "5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9",
            "timestamp": 1685094219612,
            "transactions": [
                {
                    "amount": 50,
                    "recipient": "896e6a100f5a417585d311bc19457d53",
                    "sender": "0",
                    "transaction_id": "43a4c847cb144ca0ac8aba70b57bfcce"
                }
            ]
        },
        {
            "hash": "0000817f4532c673af30f14269830cd46e87b09adf4e3d5e12c08a5dec83d80f",
            "index": 2,
            "merkle_root": "4ab33c6d3f1ec9fabe52374319d7f2143e7b236bd28ba3697a18dfeca63b1d74",
            "nonce": 13232,
            "previous_block_hash": "90217d9c7860ca244b3488d60c88361c0c9a77f4f61ef3e77341bb8ad97ff2c1",
            "timestamp": 1685094268854,
            "transactions": [
                {
                    "amount": 6.25,
                    "recipient": "00",
                    "sender": "00",
                    "transaction_id": "6e28d74b4f814b4f9d186fc9d1fa00dd"
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
            "recipient": "96508369f8564e31b460883a178d62e7",
            "sender": "00",
            "transaction_id": "ca72e8cb2e0d473f89f35c75b7b366c4"
        }
    ]
}
    

    print('VALID:', bitcoin.chain_is_valid(bc1['chain']))
    #print(bitcoin.hash_block(previous_block_hash,current_block_data,900))

if __name__ == "__main__":
    main()
