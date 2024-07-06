from django.test import TestCase

from core.models import User


class UserModelTests(TestCase):
    def test_create_user_success(self) -> None:
        email: str = "user@example.com"
        password: str = "testpass123"

        user: User = User.objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_user_without_email_raises_error(self) -> None:
        with self.assertRaisesMessage(
            expected_exception=ValueError,
            expected_message="Missing required field: email",
        ):
            User.objects.create_user(
                email=None,
                password="testpass123",
            )

    def test_create_user_without_password_raises_error(self) -> None:
        with self.assertRaisesMessage(
            expected_exception=ValueError, expected_message="Missing required field: password"
        ):
            User.objects.create_user(
                email="user@example.com",
                password=None,
            )

    def test_create_superuser_success(self) -> None:
        email: str = "user@example.com"
        password: str = "testpass123"

        user: User = User.objects.create_superuser(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)

    def test_create_superuser_without_email_raises_error(self) -> None:
        with self.assertRaisesMessage(
            expected_exception=ValueError,
            expected_message="Missing required field: email",
        ):
            User.objects.create_superuser(
                email=None,
                password="testpass123",
            )

    def test_create_superuser_without_password_raises_error(self) -> None:
        with self.assertRaisesMessage(
            expected_exception=ValueError, expected_message="Missing required field: password"
        ):
            User.objects.create_superuser(
                email="user@example.com",
                password=None,
            )
