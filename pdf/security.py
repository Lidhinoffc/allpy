# '''
# encrypt / decrypt'''

import fitz


def encrypt(input_file, password, save):
    """
    Password protect PDF.
    """

    pdf = fitz.open(input_file)

    pdf.save(
        save,
        encryption=fitz.PDF_ENCRYPT_AES_256,
        owner_pw=password,
        user_pw=password
    )

    pdf.close()



def decrypt(input_file, password, save):
    """
    Remove password from PDF.
    """

    pdf = fitz.open(input_file)

    if pdf.authenticate(password):

        pdf.save(
            save,
            encryption=fitz.PDF_ENCRYPT_NONE
        )

    pdf.close()