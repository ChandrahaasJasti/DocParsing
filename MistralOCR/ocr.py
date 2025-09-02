import os
from mistralai import Mistral
import json
from dotenv import load_dotenv
load_dotenv(dotenv_path=r"/home/chandrahaas/codes/SaarathiFinance/DocumentParser/.env")
api_key = os.getenv('OCR')


class ocr_check:
    def __init__(self,api_key):
        self.api_key=api_key
        
    def ocr_local(self,path):
        client = Mistral(api_key=self.api_key)

        uploaded_pdf = client.files.upload(
        file={
            "file_name": path,
            "content": open(path, "rb"),
        },
        purpose="ocr")  

        signed_url = client.files.get_signed_url(file_id=uploaded_pdf.id)
        ocr_response = client.ocr.process(
            model="mistral-ocr-latest",
            document={
                "type": "document_url",
                "document_url": signed_url.url,
            }
        )
        return ocr_response

    def ocr_url(self,url):
        client = Mistral(api_key=self.api_key)
        ocr_response = client.ocr.process(
            model="mistral-ocr-latest",
            document={
                "type": "document_url",
                "document_url": url
            },
            include_image_base64=True
        )
        return ocr_response

    def ocr_image(self,url):
        client = Mistral(api_key=self.api_key)
        ocr_response = client.ocr.process(
        model="mistral-ocr-latest",
        document={
            "type": "image_url",
            "image_url": url
        })
        return ocr_response

    def response_parser(self,data):
        big=[]
        l=data['pages']
        for i in range(len(l)):
            mini=[]
            mini.append(l[i]['markdown'])
            big.append(mini)
        return big

#print(resp)