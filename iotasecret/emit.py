import time,json
from iota import Iota, ProposedTransaction, Address, TryteString, Fragment, Transaction,adapter
from .common import Crypt
class Controller(Crypt):
    def __init__(self,secret):
        super(Controller,self).__init__(secret)
        self.api = Iota(adapter='https://nodes.thetangle.org:443',local_pow=False)

    def emit(self,message):
        datum = self.encrypt(json.dumps([time.time(),message]))
        tx = ProposedTransaction(
            address = Address(self.address),
            value = 0,
            message = TryteString.from_bytes(datum)
        )
        startTime = time.time()
        print(f"Sending datum: {datum}")
        try:
            bundle = self.api.send_transfer(transfers=[tx])['bundle']
        except adapter.BadApiResponse as e:
            print("Bad response from server. Failed to send. Retry")
            return self.emit(message)
            
        duration = time.time() - startTime
        reference = bundle.transactions[0].hash            
        print(f'Sent in {duration:.01f} secconds to {reference}')

if __name__=="__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('secret', type=str, help='A passphrade used for encrytion and decryption.')
    parser.add_argument('message', type=str, help='Data you want securly stored.')
    args = parser.parse_args()
    controller = Controller(args.secret)
    controller.emit(args.message)
