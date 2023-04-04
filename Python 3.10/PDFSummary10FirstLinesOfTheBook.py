import PyPDF3
import re

# Open the PDF file in read-binary mode
with open('book.pdf', 'rb') as pdf_file:
    # Read the PDF content
    pdf_reader = PyPDF3.PdfFileReader(pdf_file)
    content = ''
    for page_num in range(pdf_reader.numPages):
        page = pdf_reader.getPage(page_num)
        content += page.extractText()

    # Clean the content by removing newlines and extra whitespaces
    content = re.sub('\n', ' ', content)
    content = re.sub('\s+', ' ', content)

    # Extract the first 10% of sentences as summary
    sentences = content.split('.')
    num_sentences = len(sentences)
    num_summary_sentences = max(1, round(num_sentences * 0.1))
    summary = '. '.join(sentences[:num_summary_sentences]) + '.'

    # Print the summary
    print(summary)
