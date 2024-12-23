from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Create dummy users'

    def handle(self, *args, **kwargs):
        users_data = [
            {'username': 'user1', 'email': 'user1@example.com', 'password': 'password123'},
            {'username': 'user2', 'email': 'user2@example.com', 'password': 'password123'},
            {'username': 'user3', 'email': 'user3@example.com', 'password': 'password123'},
        ]

        for user_data in users_data:
            if not User.objects.filter(username=user_data['username']).exists():
                User.objects.create_user(**user_data)
                self.stdout.write(self.style.SUCCESS(f"User {user_data['username']} created successfully"))
            else:
                self.stdout.write(self.style.WARNING(f"User {user_data['username']} already exists"))