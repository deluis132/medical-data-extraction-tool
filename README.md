# Medical Data Extraction Tool 

The Medical Data Extraction Tool automates the extraction of relevant information from patient files, accelerating data preparation for statistical analysis.

## Table of Contents

- [Project Description](#project-description)
- [Installation](#installation)
- [Usage](#usage) 
- [Contributing](#contributing)
- [License](#license)

## Project Description

The Medical Data Extraction Tool aims to streamline manual data collection efforts and enhance the efficiency of data preparation for statistical analysis. By leveraging Regular Expressions, the tool automatically extracts relevant medical information from patient files, facilitating faster and improved data collection while saving personnel time and energy.

The tool is primarily designed to extract pertinent information from patients in Neuro Oncology studies and serves as a versatile template for data collection efforts across various study areas, including Breast, Phase 1, GI, GU, and more.

Key Features:
- Automated extraction of medical information from PDF files using Regular Expressions.
- Customizable regex patterns to adapt to different study areas and file formats.

Usage Examples:
- Extracting patient demographics, treatment details, and outcomes from Neuro Oncology study reports.
- Generating structured datasets for statistical analysis from unstructured patient files.

## Installation

### Requirements

Before using the Medical Data Extraction Tool, ensure you have the following requirements installed:
- Python 3.x
- PyPDF2

### Optional: Installing Python

If you don't have Python installed on your system, you can download and install it from the official Python website: [Python Downloads](https://www.python.org/downloads/)

### Downloading Requirements

To install the required dependencies for this project, please download the requirements.txt file from the repository and run the following command:

py -m pip install -r requirements.txt 

### Potential Problems and Troubleshooting
If you encounter any issues during installation or usage of the tool, the following resources may help:

[PyPDF2 Documentation](https://pypdf2.readthedocs.io/en/3.0.0/)
[Python Installation Guide](https://docs.python.org/3/using/windows.html#installation-steps)

## Usage

### Preparing PDF Files

Before running the Medical Data Extraction Tool, ensure that the PDF files containing patient data are in a readable format. Many files downloaded from Electronic Medical Records (EMR) systems are scanned images and need to be converted to readable text files using Optical Character Recognition (OCR) technology.

- Use Adobe Acrobat or similar software with OCR capabilities to convert scanned PDFs to searchable text files.

- Save the converted text files in a directory accessible to the Medical Data Extraction Tool. Please note that Python may not have access to network drives such as O or P drives, so it's recommended to use folders directly on the Desktop or in a local directory.

After follow the subsequent steps. 

1. **Create a Directory**: On your desktop, create a folder named `patient_files`.

2. **Move PDF Files**: Move all the PDF files containing patient data into the `patient_files` folder.

3. **Verify Directory Path**: Ensure that the directory path to the `patient_files` folder is correct. By default, the Medical Data Extraction Tool expects the `patient_files` folder to be located on your desktop. If you have saved the folder in a different location, you will need to modify the directory path accordingly.

4. **Run the Tool**: Once the PDF files are stored in the `patient_files` folder and the directory path is verified, you can proceed to run the Medical Data Extraction Tool.

If you encounter any issues with the directory path or accessing the patient files, refer to the troubleshooting section in the README file or reach out for assistance.

### Running the Tool

Once the PDF files are converted to readable text format, follow these steps to use the Medical Data Extraction Tool:
1. Open a command prompt.
2. Navigate to the directory where you've saved the Python script for the Medical Data Extraction Tool. When using the tool, make sure you're working within this directory. For convenience during execution, it's recommended to save the script in a location easily accessible from your personal O drive or Desktop.
3. Run the Python script and follow the prompt to enter the absolute directory path where the text files are stored on your system. Once entered, the script will proceed to extract the medical data from the files within the specified directory. Refer to the examples below for the commands to execute the script in the command prompt.

py medical_data_extraction.py 

### Optimization Tips

For optimal performance and efficiency, consider the following tips:
- Batch Processing: The program is best optimized when processing multiple patient files simultaneously. Consider running the tool on batches of files rather than individual files to maximize efficiency. The more files processed at once, the better the overall performance.

## Contributing

We welcome contributions from interested parties to enhance the functionality and scope of the Medical Data Extraction Tool. There are several ways you can contribute:
- Extending Regex Patterns: The tool's regex patterns are currently optimized for Nurse Reports. However, to optimize research efforts department-wide, we invite contributions to expand regex patterns across various study areas, including pathology reports. This will enable the tool to extract relevant information from a broader range of medical documents, facilitating comprehensive data collection for diverse research studies.
- Adding Regex Patterns for Different Patient Medical Information: Consider contributing regex patterns for different patient medical information categories, such as pathology reports, imaging findings, or treatment history. Creating separate classes or modules for regex patterns of interest across relevant information categories will improve the tool's versatility and usefulness in extracting specific data elements from medical documents.
- Adjusting Note Presentation: In addition to program enhancements, consider adjusting the way notes are presented within extracted data. For example, standardizing the format of certain information categories, such as listing mutations as "Mutations:", can improve data consistency and readability.

## License

Feel free to use, modify, and adjust the program as you see fit. 
Originally created by Deluis Fernandez

---

Thank you for checking out the Medical Data Extraction Tool! Your interest and support are greatly appreciated. If you have any questions or suggestions, feel free to reach out.





