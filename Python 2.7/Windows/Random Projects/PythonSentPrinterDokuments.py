import os,sys
import win32print
p = win32print.OpenPrinter ("name printer ") 
job = win32print.StartDocPrinter (p, 1, ("test of raw data", None, "RAW"))
win32print.StartPagePrinter (p)
win32print.WritePrinter (p, "data to print")
win32print.EndPagePrinter (p)
