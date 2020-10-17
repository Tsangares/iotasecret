# Summary
Need to store a small piece of data from some device that needs to be read by another computer?

The usual way to do this is for the device to send data to a centrailized server, either a database, email or ssh.

By using the IOTA ledger you can retrieve this data easily without any intermediate server.

An example is having a Raspberry Pi connected to wifi; you need to ssh into this pi, but you don't know its ip because it is dynamically allocated. Simply have the pi store the ip when it connectes to wifi encrypted on the ledger using this command line utility. Then from any computer, using this utility, you can retrieve the ip of the pi to connect to it. This is done by simply using the same passphrase that the pi used to encrypt the message. 

Another example is having some note, like a long url, that is on one computer but is needed on another computer. You can store it on the ledger encrypted, and retrieve it from the other computer whenever you are ready.

The only requirement for two devices to communicate using this method is having a secure passphrase. This program uses the iotaledger like a map-key database, where the key is a hased version of your passphrase. Give your passphrase to someone else and they have access to the notes stored on the ledger.

# Flow Charts of the process
### Uploading
(Upload)[https://i.imgur.com/kN1WU81.png]

### Downloading
(Download)[https://i.imgur.com/MiBR11S.png]

# Installation

It is a pip package

    pip install iotasecret
	
## Sending a message

Once installed you will need to come up with a passphrase and a message to send. Once you are ready, execute the command

    iotasecret emit MYPASSPHRASE --message 'my message'
	
	
## Recieving a message

Remembering your passphrase, you can retrieve the latest note stored on the ledger by running,

    iotasecret read MYPASSPHRASE

## Recieve all messages

To retrieve all the messages you have sent,

    iotasecret read MYPASSPHRASE --all 
    

## Changing the node

By default the utility uses `nodes.thetangle.org`, as the IOTA node. If you want to use your own, or a different one simply use the argument `--node`

	iotasecret emit MYPASSPHRASE --message "New node" --node https://mynode.com:443
    iotasecret read MYPASSPHRASE --node https://mynode.com:443

### Example

    $> iotasecret emit MYPASSPHRASE --message 'my message'  
    Sending datum: b'gAAAAABfikdt56f1AzK0lG0IYArdfO914QPUnf6XaGQaNNiT-kixnfI2TvwrPPCQ-H9-q1OVbIs1WZNEQuDE-v7aCSqWSKHDpZmfbEIg62A7tdRd8wG8zm8CrD3QVRDpykZLfL0HaXnv'
    Sent in 2.8 secconds to HLJSPWFYKIRGRGMOVDLBFQ9VQCRBPJDMUOSTRORL9QAAJKCCSLMGH9LXQPYLRDTKAQILTZIECNJPA9999

    $> iotasecret read MYPASSPHRASE
    Fetched 1 events in 1.0 sec.
    2020-10-16 18:22:53.356271: my message
    
    $> iotasecret emit MYPASSPHRASE --message 'This is just a test'
    Sending datum: b'gAAAAABfikgMH4aBE6N1r4xPu3wKIzgSx_XRpb0LiQMoqtI27yzocmhhxpxdKz6jsRWs2w122N3KY-a0R4h52K0t-Zqr3fxy8Iultsn8xG2lhJ-tq_2DtHyLXQ4GltI7zft2lMC-cBJS'
    Sent in 10.7 secconds to WXLFBCUJVKXNUZOYCGPJMRDMIXNHJAYWJICKBEQDBYWWWZ9CMUQIHDKXTUPFAHJYRJIYJNFOVY9OA9999
    
    $> iotasecret emit MYPASSPHRASE --message 'Choose a better passphrase please.'
    Sending datum: b'gAAAAABfikgfUnHVcFUjK2SCTTH3a_VicNNQX8638x_gLcKQG8vMC-BAa_YBa4d_BOaqYaz8plL4xvN62tC9QEI2JovM8U9BQ2Mub68KIkNOQR9wDJMepR6rZiksblJtYnCbU2nRjIDfb5i4dG47jVEEAwhlGvhkoA=='
    Sent in 6.07 secconds to TBOEGNSD9JOSMBORSPIDXSNDUSFRUUGYVTJZCHF9ZUAQNOFORYALPGEJDOQJEZNLWUVPAPAOBMUW99999
    
    $> iotasecret read MYPASSPHRASE --all
    Fetched 3 events in 0.6 sec.
    2020-10-16 18:25:52.924940: Choose a better passphrase please.
    
    2020-10-16 18:25:32.310215: This is just a test
    
    2020-10-16 18:22:53.356271: my message



