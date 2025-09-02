from paddleocr import PaddleOCR

ocr= PaddleOCR(
    use_doc_orientation_classify=False,
    use_doc_unwarping=False,
    use_textline_orientation=False
)

result = ocr.predict(
    input=r"/home/chandrahaas/codes/SaarathiFinance/DocumentParser/2526BA139 April25 SAARTHI FINANCE.pdf")

print(result)