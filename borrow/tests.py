from django.test import TestCase
from datetime import date
from books.models import Book
from .models import BorrowRecord
from django.core.exceptions import ObjectDoesNotExist

class BorrowRecordDeleteTest(TestCase):

    def setUp(self):
        # Create book and borrow record
        self.book = Book.objects.create(
            title="Django Basics",
            author="John Doe",
            isbn="1234567890123",
            description="A beginner guide to Django.",
            category="Programming",
            published_date=date.today(),
            available_copies=5
        )
        self.borrow = BorrowRecord.objects.create(
            borrower_name="Alice",
            book=self.book,
            borrowed_date=date.today(),
            is_returned=False
        )

    def test_borrow_record_delete(self):
        # Act: Delete the borrow record
        self.borrow.delete()

        # Refresh book to ensure available_copies remain correct
        self.book.refresh_from_db()

        # Assertions
        self.assertEqual(BorrowRecord.objects.count(), 0)
        # Trying to fetch deleted record should raise ObjectDoesNotExist
        with self.assertRaises(ObjectDoesNotExist):
            BorrowRecord.objects.get(id=self.borrow.id)