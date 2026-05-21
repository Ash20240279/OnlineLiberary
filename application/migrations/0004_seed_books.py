from django.db import migrations

def seed_books(apps, schema_editor):
    Book = apps.get_model('application', 'Book')
    
    books_data = [
        {
            'title': 'The Great Gatsby',
            'author': 'F. Scott Fitzgerald',
            'category': 'Fiction',
            'status': 'available',
            'image': 'https://covers.openlibrary.org/b/id/7222246-L.jpg',
            'year': 1925,
            'pages': 180,
            'description': 'A classic novel about wealth, love, and the American Dream.'
        },
        {
            'title': 'Clean Code',
            'author': 'Robert C. Martin',
            'category': 'Technology',
            'status': 'borrowed',
            'image': 'https://covers.openlibrary.org/b/id/9611980-L.jpg',
            'year': 2008,
            'pages': 464,
            'description': 'A guide to writing clean and maintainable code.'
        },
        {
            'title': 'Atomic Habits',
            'author': 'James Clear',
            'category': 'Self Development',
            'status': 'available',
            'image': 'https://covers.openlibrary.org/b/id/14842614-L.jpg',
            'year': 2018,
            'pages': 320,
            'description': 'Practical methods for building good habits and breaking bad ones.'
        },
        {
            'title': 'Rich Dad Poor Dad',
            'author': 'Robert Kiyosaki',
            'category': 'Fiction',
            'status': 'available',
            'image': 'https://covers.openlibrary.org/b/id/240726-L.jpg',
            'year': 1997,
            'pages': 336,
            'description': 'Lessons about money, investing, and financial thinking.'
        },
        {
            'title': 'Sapiens',
            'author': 'Yuval Noah Harari',
            'category': 'History',
            'status': 'available',
            'image': 'https://covers.openlibrary.org/b/id/8370226-L.jpg',
            'year': 2011,
            'pages': 443,
            'description': 'A brief history of humankind from ancient times to today.'
        }
    ]
    
    for book_info in books_data:
        Book.objects.get_or_create(
            title=book_info['title'],
            author=book_info['author'],
            defaults={
                'category': book_info['category'],
                'status': book_info['status'],
                'image': book_info['image'],
                'year': book_info['year'],
                'pages': book_info['pages'],
                'description': book_info['description'],
            }
        )

def unseed_books(apps, schema_editor):
    Book = apps.get_model('application', 'Book')
    Book.objects.filter(
        title__in=[
            'The Great Gatsby',
            'Clean Code',
            'Atomic Habits',
            'Rich Dad Poor Dad',
            'Sapiens'
        ]
    ).delete()

class Migration(migrations.Migration):

    dependencies = [
        ('application', '0003_alter_userprofile_profile_pic'),
    ]

    operations = [
        migrations.RunPython(seed_books, unseed_books),
    ]
