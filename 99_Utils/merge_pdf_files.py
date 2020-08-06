from PyPDF2 import PdfFileMerger, PdfFileReader
import sys
import glob
############################################################################################################################################
##A python utility to merge a number of pdf files into a single file
#
# What does it solve: I needed it because all the NCERT books I was getting had 1 file for each chapter, so I needed something to merge them.
#####
# Usage: python merge_pdf_files.py <input-name pattern> <optput file>
# e.g. to merger all the (pdf) files in folder ghdv1dd starting with ghdv, use fopllowing:
#  python merge_pdf_files.py  "ghdv1dd/ghdv*"   durva_class7.pdf
#####
# Gotchas:
# - Quotes around filename or (in Linux) it will expand the *
# - Input file will be picked on the basis of filename (and not content) - alphabetical order.
# Works for me, but I would do it someday:
# - Use getopts instead of positional ar
# - Exception / Error handling
# - Don't overwrite the output file if it already exists.
############################################################################################################################################
if len(sys.argv[1:]) != 2:
    print("Invalid usage, received", len(sys.argv), " arguments, expects 2 input-fileanme prefix and 2. ouptput filename")
    print("In case you are using wild-card for first argument, use quotes around it.")
    exit -1

#Use getopt instead of fixed, positional arguments
input_prefix=sys.argv[1]
output_file=sys.argv[2]

print("Reading all the input files:"+  input_prefix + ", to join into a single file :" + output_file)
mergedObject = PdfFileMerger()

#Get a list of all the files with this pattern
all_the_files=glob.glob(input_prefix)

#Pick all the files and merge it
for file in all_the_files:
    print("Merging file:", file)
    mergedObject.append(PdfFileReader(file, 'rb'))


# Write all the files into a file which is named as shown below
#
mergedObject.write(output_file)
print("....merged all into file:", output_file)