''' Read pdf files and split it using specific number of pages '''
# Import the libraries
from PyPDF2 import PdfReader,PdfWriter
from math import ceil
import random, string 



# split pdf into n  pages
def split_pdf(filepath, file_name,folder_to_save,split_size = 10):
    """Split pdf into n pages. Default is set to 10 """

    #variable to store the output of split pdf paths
    pdfs = []

    with open(filepath, "rb") as infile:
        # Read input pdf
        inputpdf = PdfReader(infile, strict=False)

        #initiate split pdf 
        outputpdf = PdfWriter()

        #iterate through the file to split 
        for page_number in range(len(inputpdf.pages)):
            if (page_number + 1) % split_size == 0 or page_number == len(inputpdf.pages) - 1:
                outputpdf.add_page(inputpdf.pages[page_number])
                split_filename = (
                    str(ceil((page_number + 1) / split_size))
                    + "_"
                    + "".join(
                        random.choices(string.ascii_lowercase + string.digits, k=7)
                    )
                    + file_name
                )
                #creation of output path 
                to_store = folder_to_save + "/" + split_filename
                pdfs.append(to_store)

                #Write the output 
                with open(to_store, "wb") as outputStream:
                    outputpdf.write(outputStream)

                #create a new outputpdf object
                outputpdf = PdfWriter()
            else:
                outputpdf.add_page(inputpdf.pages[page_number])

        #delete the input pdf after process
        del inputpdf

        #return 
        return pdfs


if __name__ == "__main__":
    file_path = "sample.pdf"
    file_name = file_path.split("/")[-1]
    folder_to_save = "split_file"
    path_file = split_pdf(file_path, file_name,folder_to_save)

