"""This has been maintained for posterity."""
import PyPDF2


"""Module for parsing tmobile bill PDFs."""


def parse_billy(filename):
    """Master function to parse T-Mobile PDFs. Going to be broken up."""
    # ====== init ======
    pdf_bill = PyPDF2.PdfFileReader(open(filename, 'rb'))
    # So far, the relevant information starts on the 3rd (index) page
    bill_dict = {}
    section_dict = {}
    # ====== init ======
    for page in range(3, pdf_bill.numPages):

    # ======= Method for preparation of the text. ========
        raw_page = pdf_bill.getPage(page)
        text_page = raw_page.extractText()
        split_text_page = text_page.split('\n')
        while '' in split_text_page:
            split_text_page.remove('')
    # ====================================================

        if 'Total:' in split_text_page:  # main function

    # ======= Method to handle discontinuous records =======
            # Either the end of the pdf or switching to a new section
            header = split_text_page.index('Date and time')
            end_of_section = split_text_page.index('Total:')
            second_dict = {}
            section_label = split_text_page[header - 2]
            for i, column in enumerate(split_text_page[header:header + 6]):
                column_index = header + i
                second_dict[column] = split_text_page[column_index + 6:end_of_section:6]
            bill_dict[section_label] = {key: section_dict.get(key, []) + second_dict[key] for key in second_dict.keys()}
            if split_text_page[end_of_section + 2] == 'Data':
                start_of_next_section = end_of_section + 4
            else:
                start_of_next_section = end_of_section + 5
            next_section = split_text_page[start_of_next_section::]
            section_dict = {}
            second_dict = {}
            for column in next_section[:6]:
                column_index = next_section.index(column)
                section_dict[column] = next_section[column_index + 6::6]
    # =======================================================

        else:
    # ======= Method to handle continuous list of records =======
            pivot_index = split_text_page.index('Date and time')
            for i, column in enumerate(split_text_page[pivot_index:pivot_index + 6]):
                column_index = pivot_index + i
                values = split_text_page[column_index + 6::6]
                if column in section_dict:
                    section_dict[column] = section_dict[column] + values
                else:
                    section_dict[column] = values
    # ===============================================================

    return bill_dict