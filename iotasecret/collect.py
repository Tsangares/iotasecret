import time,json,math,datetime
from iota import Iota, ProposedTransaction, Address, TryteString, Fragment, Transaction
from .common import Crypt
class Collector(Crypt):
    def __init__(self,secret,node='https://nodes.thetangle.org:443'):
        super(Collector,self).__init__(secret)
        self.api = Iota(adapter=node)

    def getData(self,txHash):
        hashes=api.find_transactions(addresses=[address,])['hashes']
        
    def decode(self,frag):
        hiddenMessage = frag.signature_message_fragment.decode()
        decrypted = self.decrypt(bytes(hiddenMessage,'utf=8'))
        return json.loads(decrypted)
        
    def read(self,silent=False):
        address = Address(self.address)
        txHashes = self.api.find_transactions(addresses=[address,])['hashes']
        batchSize=80
        sets = math.ceil(len(txHashes)/batchSize)
        txs = []
        for i in range(sets):
            start=time.time()
            resp = self.api.get_transaction_objects(txHashes[i*batchSize:(i+1)*batchSize])['transactions']
            txs+=resp
            duration = time.time() - start
            if not silent: print(f'Fetched {len(resp)} events in {duration:.1f} sec.')
        return sorted([self.decode(t) for t in txs], key=lambda a: a[0],reverse=True)
    
    def readLatest(self,silent=False):
        messages = self.read()
        secconds,msg = messages[0]
        timestamp = datetime.datetime.fromtimestamp(secconds)
        return f'{timestamp}: {msg}'
if __name__=='__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('secret', type=str, help='A passphrade used for encrytion and decryption.')
    args = parser.parse_args()
    collector = Collector(args.secret)
    print(collector.readLatest())
