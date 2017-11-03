"""Test parser to ensure we are getting expected values."""
import os
import pytest
import PyPDF2

from ..scripts import tmobile_bill_parser


@pytest.fixture
def pdf_docs():
    """Fixture containing all bills."""
    paths = ['../bills/' + bill for bill in os.listdir('../bills')]
    return paths


@pytest.fixture
def pdf_docs_text(pdf_docs):
    """Fixture that extracts text from the pdf."""
    bills = []
    for bill in pdf_docs:
        page_texts = []
        pdf_bill = PyPDF2.PdfFileReader(open(bill, 'rb'))
        for page in range(3, pdf_bill.numPages):
            raw_page = pdf_bill.getPage(page)
            raw_text = raw_page.extractText()
            prepared_page = raw_text.split('\n')
            page_texts.append(prepared_page)
        bills.append(page_texts)
    return bills


def test_third_page_as_start_assumption(pdf_docs):
    """Test that the starting page contains unique text."""
    for bill in pdf_docs:
        pdf_bill = PyPDF2.PdfFileReader(open(bill, 'rb'))
        page = pdf_bill.getPage(3)
        page = page.extractText()
        assert 'Usage details' in page


def test_second_page_not_starting_point(pdf_docs):
    """Test page before starting page does not contain starting text."""
    for bill in pdf_docs:
        pdf_bill = PyPDF2.PdfFileReader(open(bill, 'rb'))
        page = pdf_bill.getPage(2)
        page = page.extractText()
        assert 'Usage details' not in page


def test_fourth_page_not_starting_point(pdf_docs):
    """Test that the next page never contains 'Usage details'."""
    for bill in pdf_docs:
        pdf_bill = PyPDF2.PdfFileReader(open(bill, 'rb'))
        page = pdf_bill.getPage(2)
        page = page.extractText()
        assert 'Usage details' not in page


def test_last_character_assumption_after_split(pdf_docs_text):
    """Test that the last character is an empty string after splitting."""
    for bill in pdf_docs_text:
        for text in bill:
            assert text[-1] == ''
