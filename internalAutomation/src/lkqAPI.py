from zeep import Client
from dotenv import load_dotenv
import os

wsdl = "https://lkqintegrationqc.ekeyconnect.com/Ordering.svc?wsdl"

client = Client(wsdl=wsdl)
checkDropShipAvailability = {
    "request": {
        "UserRequestInfo": {
            "AccountNumber": "837903",
            "BusinessTypeForAccountNumber": "Salvage",
            "UserName": "837903.factorywheel",
            "UserPassword": "fact0rywh33l",
            "VerificationCode": "3ecb234b-b7c7-40aa-926e-85ac0a82f5bb"
        },
        "PartsWithQuantity": [
            {
                "PartWithQuantityRequest": {
                    "PartNumber": "ALY64108U45",
                    "Quantity": 1
                }
            }
        ]
    }
}

class LKQConnection():

    def __init__(self):
        load_dotenv()
        self.client = Client(
            "https://lkqintegrationqc.ekeyconnect.com/Ordering.svc?wsdl"
        )
        self._password = os.getenv("LKQ-PW")
        self._verificationCode = os.getenv("LKQ-VC")
    

    def checkAvailability(self, partNumber, qty):
        request = {
            "request": {
                "UserRequestInfo": {
                    "AccountNumber": "837903",
                    "BusinessTypeForAccountNumber": "Salvage",
                    "UserName": "837903.factorywheel",
                    "UserPassword": self._password,
                    "VerificationCode": self._verificationCode
                },
                "PartsWithQuantity": [
                    {
                        "PartWithQuantityRequest": {
                            "PartNumber": partNumber,
                            "Quantity": qty
                        }
                    }
                ]
            }
        }
        return self.client.service.CheckDropShipAvailability(**request)

# can pass in dictionaries to methods
print(type(client.service.CheckDropShipAvailability(**checkDropShipAvailability).json))