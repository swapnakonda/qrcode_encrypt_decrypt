import cv2
from cryptography.fernet import Fernet


class QRCodeDecryption:

    def read_qrcode_image(self):
        qr_img = cv2.imread("qr-img.jpg")
        qr_det = cv2.QRCodeDetector()
        encrypted_data, pts, st_code = qr_det.detectAndDecode(qr_img)
        print("information:-", encrypted_data)
        return encrypted_data

    def decrypt_info(self, encrypted_data):
        f = Fernet('5jyFfIy3FjhWnWBSNCZSmCe3paPaqevSRKm-sGhtlTg=')
        decrypted_data = f.decrypt(encrypted_data).decode()
        print("decrypted_data:-", decrypted_data)
        print(type(decrypted_data))
        decoded_data_list = decrypted_data.decode()
        print('decoded_data_list - ', decoded_data_list)
        print('type of decrypted data - ', type(decoded_data_list))


obj = QRCodeDecryption()
encrypted_data = obj.read_qrcode_image()
obj.decrypt_info(encrypted_data)
