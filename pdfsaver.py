import aspose.words as aw

# load TXT document
doc = aw.Document("text.txt")

# save TXT as PDF file
doc.save("text.pdf", aw.SaveFormat.PDF)