# print_receipt.py

from escpos.printer import Usb


def printer_print(in_text):
    try:
        p = Usb(0x0416, 0x5011) #, 0, profile="TM-T88III")
        p.text(in_text)
        p.text("\n")
    except:
        print("Connection to printer failed. \n")
        print(in_text)
        print("\n")