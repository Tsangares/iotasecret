from .emit import Controller
from .collect import Collector
import argparse,datetime
def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('mode', type=str,choices=['emit','read'], help='Either emit or read a message.')
    parser.add_argument('secret', type=str, help='A passphrade used for encrytion and decryption.')
    parser.add_argument('--message', type=str, help='Data you want securly stored. Use in emit mode.',default=None)
    parser.add_argument('--all', action='store_true', help='Get all messages. Use in read mode.',default=False)
    args = parser.parse_args()
    if args.mode == 'emit':
        if args.message is None:
            raise Exception("You forgot your --message argument. See --help for details.")
        controller = Controller(args.secret)
        controller.emit(args.message)
    elif args.mode == 'read':
        collector = Collector(args.secret)
        if args.all:
            messages = collector.read()
            for time,msg in messages:
                timestamp = datetime.datetime.fromtimestamp(time)
                print(f"{timestamp}: {msg}\n")
        else:
            print(collector.readLatest())

