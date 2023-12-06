# Vector-Barcode-PDF-Generation-and-Reading

A demo to generate a vector PDF with barcodes and read barcodes from it.

* `generate.py`: generate a vector PDF with two code 128 barcodes.
* `reader.py`: use [Dynamsoft Barcode Reader](https://www.dynamsoft.com/barcode-reader/overview/) to read the generated PDF file.


Dynamsoft Barcode Reader can directly read vector data or render a PDF page to an image to read. Directly reading the vector has a better performance.

Test Result:

```
Vector mode: 15.6253ms.
Raster mode: 84.721ms.
```
