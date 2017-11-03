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
