from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile


class ProfileTestCase(TestCase):

    def setUp(self):
        self.u = User.objects.create_user(username='First tester', email=None, password='abc')
        self.u.id = 5000000
        self.testp = Profile.objects.create(user=self.u)

    def testCreate(self):
        """Checks that the user was activated when created; will later to change with confirmation email
        """
        testp = Profile.objects.get(user__username='First tester')
        self.assertEqual(testp.user.is_active, True)
