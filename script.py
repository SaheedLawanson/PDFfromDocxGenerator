import base64, os
from docxtpl import DocxTemplate
from docx2pdf import convert

doc = DocxTemplate('Statements of Accounts.docx')
context = { 
    'start_date' : '2021-05-01',
    'end_date': '2021-05-10',
    'account_number': '1',
    'account_type': 'Savings',
    'currency': 'NGN',
    'opening_balance': '2000',
    'closing_balance': '2000',
    'total_credit': '200',
    'total_debit': '200',
    'available_balance': '1500',
    'customer_name': 'Tonya Philips',
    'created_at': '2022-04-15',
    'data': 'Hi there',
    'test': 'test',
    'myList': [
        {
            'id': 1, 'reference': '001', 
            'debit': 200, 'credit': 0, 
            'balance': 1800, 'remarks': "loss"
        },
        {
            'id': 2, 'reference': '002', 
            'debit': 0, 'credit': 200, 
            'balance': 2000, 'remarks': "re-gain"
        }
    ]
}

doc.render(context)
doc.save('generated_doc.docx')
convert("generated_doc.docx")

with open("generated_doc.pdf", "rb") as pdf_file:
    encoded_string = base64.b64encode(pdf_file.read())
    print(encoded_string)

os.remove("generated_doc.docx")
os.remove("generated_doc.pdf")