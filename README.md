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

