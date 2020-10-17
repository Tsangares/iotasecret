# Installation

It is a pip package

    pip install iotasecret
	
## Sending a message

Once installed you will need to come up with a passphrase and a message to send. Once you are ready execute the command

    iotasecret emit MYPASSPHRASE --message 'my message'
	
	
## Recieving a message

Remember your passphrase and run the command,

    iotasecret read MYPASSPHRASE

## Recieve all messages

To retrieve all the messages you have sent,

    iotasecret read MYPASSPHRASE --all 
    
    
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



