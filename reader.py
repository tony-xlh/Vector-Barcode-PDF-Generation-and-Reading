from dbr import *
import time
error = BarcodeReader.init_license("t0072oQAAAARFnEke5+r6mpH86BUK2+BVhS0cMaCA5stzOfw+HQrqrQCpQPOI/u08FZTWswj/2fZRm/MYqKu8/bpUv3oteykASSL2")
if error[0] != EnumErrorCode.DBR_OK:
    # Add your code for license error processing
    print("License error: "+ error[1])
reader = BarcodeReader()

def print_results(results):
    if results != None:
        i = 0
        for text_result in results:
            print("Barcode " + str(i))
            print("Barcode Format : " + text_result.barcode_format_string)
            print("Barcode Text : " + text_result.barcode_text)
            i = i+1

settings = reader.get_runtime_settings()
settings.pdf_reading_mode = EnumPDFReadingMode.PDFRM_VECTOR
reader.update_runtime_settings(settings)

start_time = time.time_ns()
results = reader.decode_file("code128_barcode.pdf")
end_time = time.time_ns()

print("=======")
print("Vector mode done in "+str((end_time - start_time)/1000000)+"ms.")
print_results(results)

settings = reader.get_runtime_settings()
settings.pdf_reading_mode = EnumPDFReadingMode.PDFRM_RASTER
reader.update_runtime_settings(settings)

start_time = time.time_ns()
results = reader.decode_file("code128_barcode.pdf")
end_time = time.time_ns()

print("=======")
print("Raster mode done in "+str((end_time - start_time)/1000000)+"ms.")
print_results(results)
