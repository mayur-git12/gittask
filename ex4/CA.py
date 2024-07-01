from Crypto.PublicKey import RSA

# #Generate a public/private key pair for the certificate authority. The public key of the CA is self-signed.
def generateCAkeys():
    new_key = RSA.generate(2048)

    private_key = new_key.exportKey("PEM")
    public_key = new_key.publickey().exportKey("PEM")

    print(private_key.decode("utf-8"))
    fd = open("private_key.pem", "wb")
    fd.write(private_key)
    fd.close()

    print(public_key.decode("utf-8"))
    fd = open("public_key.pem", "wb")
    fd.write(public_key)
    fd.close()
generateCAkeys() 

def generateCertificate(user_id, user_pub_key):

    return 

    