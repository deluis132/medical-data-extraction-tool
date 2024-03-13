import os 
import PyPDF2 
import re 

# Function to open and read each PDF file
def open_pdf(pdf_filename):
    """
    Opens and reads a PDF file.
    
    Args:
        pdf_filename (str): Name of the PDF file.
        
    Returns:
        str: Contents of the PDF file.
    """
    try:
        with open(f'{directory_path}/{pdf_filename}', 'rb') as file: 
            pdf_reader = PyPDF2.PdfReader(file)
            number_pages = len(pdf_reader.pages)
            all_text = []
            for page_index in range(number_pages):
                page = pdf_reader.pages[page_index]
                text = page.extract_text()
                all_text.append(text)

            all_text = ''.join(all_text)
            return all_text
    except Exception as e:
        print(f"Error opening PDF file '{pdf_filename}': {e}")
        return None

# Function to perform regex on text
def perform_regex(text_content): 
    """
    Performs regex on text to extract relevant information.
    
    Args:
        text_content (str): Text content of the file.
        
    Returns:
        None
    """
    try: 
        # Regular expression patterns for data extraction
        regex_patterns = {
            'MRN': '[0-9]{7,15}',
            'Gender': r'(?i)(Male|Man||Woman|Female)',
            'Race': r'(?i)(black|white|hispanic|asian)',
            'DOB': r'\bDOB\b\s*(\d{1,2}/\d{1,2}/\d{2,4})',
            'Date': r'\d{1,2}/\d{1,2}/\d{2,4}', 
            'Lesion Site': r'(?i)History\s*of\s*present\s*Illness:.*?\bwith\b(.*?)\b(?:s/p|status post)\b\s*(GTR|gross total resection|resection))',
            'First Surgery Extent': r'(?i)History\s*of\s*present\s*Illness:.*?\b(?:s/p|status post)\b\s*((?:GTR|gross total resection|resection))', 
            'Date Sample Obtained':  r'(?i)History\s*of\s*present\s*Illness:.*?\b(?:s/p|status post)\b\s*(?:GTR|gross total resection|resection)\s*(?:\((\d{1,2}/\d{1,2}/\d{2,4})\)|(\d{1,2}/\d{1,2}/\d{2,4}))',
            'KPS': [
                r'KPS\s*&\s*ECOG.*?(\b\d{1,3}\b)',
                r'KPS:\s*(\d{1,3})',
                r'(?i)Karnofsky Performance Status:\s*(\d{1,3}\%)'
            ], 
            'WHO Grade': r'(?i)(WHO grade.*?[A-Z]{1,3})', 
            'IDH-1': '[^,()\.]*\bIDH(?:-\d)?\b[^,()\.]*', 
            'MGMT': '[^,()\.]*\bMGMT\b[^,()\.]*', 
            'EGFR': '[^,()\.]*\b(?:\+)?EGFR(?:[a-zA-Z]*)?\b[^,()\.]*',
            'GFAP': '[^,()\.]*\bGFAP\b[^,()\.]*', 
            'OLIG-2': '[^,()\.]*\bOLIG(?:-\d)?\b[^,()\.]*',
            'PDGFR-A': '[^,()\.]*\bPDGFR(?:-[A-Z])?\b[^,()\.]*',
            'PTEN': '[^,()\.]*\bPTEN\b[^,()\.]*',
            'P53': '[^,()\.]*\bP53\b[^,()\.]*',
            'ATRX': '[^,()\.]*\bATRX\b[^,()\.]*',
            'SOX-2': '[^,()\.]*\SOX(?:-\d)?\b[^,()\.]*',
            'TERT': '[^,()\.]*\bTERT\b[^,()\.]*',
            'HER2/NEU': '[^,()\.]*\bHER2|NEU\b[^,()\.]*'
        }

        # Search for predefined regex patterns within the text content extracted from the PDF file.
        # Iterate through each predefined pattern and attempt to find a match within the text.
        # Print the result if a match is found, indicating the type of information extracted,
        # or print 'Not Found' if no match is found for a particular pattern.
        for key, pattern in regex_patterns.items():

            if key in ('WHO Grade', 'Lesion Site', 'First Surgery Extent', 'Date Sample Obtained'): 
                # Handle specific patterns with additional processing
                pattern = re.compile(pattern, re.DOTALL)
                result = pattern.search(text_content)
                if result:
                    print(f'{key}:', result.group(1))
                else: 
                    print(f'{key}: Not Found')

            elif key in ('KPS'):
                # Handle patterns with multiple variations
                match_found = False
                for pattern_variation in pattern:
                    variation = re.compile(pattern_variation, re.DOTALL)
                    result = variation.search(text_content)
                    if result:
                        print(f'{key}:', result.group(1))
                        match_found = True
                        break 
                if not match_found:
                    print(f'{key}: No Match Found')
            else: 
                # Handle general regex patterns
                pattern = re.compile(pattern)
                result = pattern.search(text_content)
                if result:
                    print(f'{key}:', result.group())
                else: 
                    print(f'{key}: Not Found')
    except Exception as e:
        print(f"Error performing regex: {e}") 
        
while True:
    # Validate directory path input
    directory_path = input('Enter Directory Folder Name Here: ')
    
    # Retrieve the name of PDF files located within the specified directory
    directory_files = [filename for filename in os.listdir(directory_path) if filename.endswith('.pdf')]
    if not directory_files:
        print("No PDF files found in the specified directory.")
        # Prompt user to run the program again
        run_again = input("Do you want to run the program again? (yes/no): ")
        if run_again.lower() != 'yes':
            break
        else:
            continue

    # Open and perform regex search on each PDF file within the directory
    for filename in directory_files:
        print(filename)
        pdf_text = open_pdf(filename)
        perform_regex(pdf_text)
    
    # Signal the end of the process
    print('Extraction complete! All relevant information has been extracted from the PDF files.')
    
    # Prompt user to run the program again
    run_again = input("Do you want to run the program again? (yes/no): ")
    if run_again.lower() != 'yes':
        break




    
    
    
