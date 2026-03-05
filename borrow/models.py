from django.db import models
from books.models import Book
from datetime import date

class BorrowRecord(models.Model):
    borrower_name = models.CharField(max_length=100, default="Guest")
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrowed_date = models.DateField(null=True, blank=True)
    return_date = models.DateField(null=True, blank=True)
    is_returned = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        is_new = self.pk is None

        # Get fresh book instance
        book = Book.objects.get(pk=self.book.pk)

        if is_new:
            if not self.is_returned:
                if book.available_copies > 0:
                    book.available_copies -= 1
                    book.save()
                else:
                    raise ValueError("No copies available")

        else:
            old_record = BorrowRecord.objects.get(pk=self.pk)

            if not old_record.is_returned and self.is_returned:
                book.available_copies += 1
                book.save()

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.borrower_name} borrowed {self.book.title}"