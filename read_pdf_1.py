import pdfplumber

## open pdf
with pdfplumber.open('erebor.pdf') as pdf:
    ## read first page
    page = pdf.pages[0]
    ## extract text
    text = page.extract_text()
    print(f'Number of pages: {len(pdf.pages)}') ##print number of pages
    print(f'Contents of first page:\n{text}')##print contents of first pageLoop through all pages and extract any tables found on each page — if a table is found, print the page number and the first row of the table
    for i, page in enumerate(pdf.pages):## Loop through all pages and extract any tables found on each page — if a table is found, print the page number and the first row of the table
        tables = page.extract_tables()
        if tables:
            print(f'Page {i+1} has {len(tables)} table(s).')
            for j, table in enumerate(tables):
                print(f'First row of table {j+1} on page {i+1}: {table[0]}')