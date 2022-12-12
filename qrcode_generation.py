import qrcode
from cryptography.fernet import Fernet


class QRCodeGeneration:

    def __init__(self, name, age, phone, aadhar):
        self.name = name
        self.age = age
        self.phone = phone
        self.aadhar = aadhar

    def encrypt_data(self):
        """
         this method encrypts the data
        """
        key = Fernet.generate_key()
        f = Fernet(key)
        print("f key:-", key.decode())
        with open("pass.key", "wb") as key_file:
            key_file.write(key)
        data_str = '{},{},{},{}'.format(input_name, input_age, input_phone, input_aadhar)
        encrypted_data = f.encrypt(data_str.encode())
        print("encrypted_data:- ", encrypted_data)
        return encrypted_data
        # self.qrcode_generation(encrypted_data)

    def qrcode_generation(self, encrypted_data):
        qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=5)
        qr_img = qrcode.make(encrypted_data)
        qr_img.save("qr-img.jpg")
        print("Successfull generated QRCode")


input_name = input("enter name:- ")
input_age = int(input("enter age:- "))
input_phone = int(input("enter phone:- "))
input_aadhar = int(input("enter aadhar num:- "))

data_obj1 = QRCodeGeneration(input_name, input_age, input_phone, input_aadhar)
encrypted_data = data_obj1.encrypt_data()
data_obj1.qrcode_generation(encrypted_data)
