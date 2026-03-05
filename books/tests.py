from django.test import TestCase
from datetime import date
from .models import Book

class BookModelTest(TestCase):

    def test_delete_book(self):
        """
        TC-04:
        Verifies that a Book record can be deleted from the database.
        """

        # Arrange: Create the book to delete
        book = Book.objects.create(
            title="Django Basics",
            author="John Doe",
            isbn="1234567890123",
            description="A beginner guide to Django.",
            category="Programming",
            published_date=date.today(),
            available_copies=5
        )

        # Act: Delete the book
        book.delete()

        # Assert: Ensure the book no longer exists
        self.assertEqual(Book.objects.count(), 0)

        # Optional: Confirm deletion raises DoesNotExist if retrieved
        from django.core.exceptions import ObjectDoesNotExist
        with self.assertRaises(ObjectDoesNotExist):
            Book.objects.get(isbn="1234567890123")
