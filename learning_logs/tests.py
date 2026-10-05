from django.contrib.auth.models import User
from django.test import TestCase, override_settings
from django.urls import reverse
from .models import Topic, Entry


@override_settings(SECURE_SSL_REDIRECT=False)
class AuthenticationAndOwnershipTests(TestCase):
    def setUp(self):
        self.owner = User.objects.create_user('owner', password='test-only-password')
        self.other = User.objects.create_user('other', password='test-only-password')
        self.topic = Topic.objects.create(text='Private topic', owner=self.owner)
        self.entry = Entry.objects.create(topic=self.topic, text='Private entry')

    def test_anonymous_cannot_read_topics(self):
        self.assertEqual(self.client.get(reverse('learning_logs:topics')).status_code, 302)

    def test_other_user_cannot_read_or_modify_entries(self):
        self.client.force_login(self.other)
        self.assertEqual(self.client.get(reverse('learning_logs:topic', args=[self.topic.pk])).status_code, 404)
        response = self.client.post(reverse('learning_logs:edit_entry', args=[self.entry.pk]), {'text': 'changed'})
        self.assertEqual(response.status_code, 404)
        self.entry.refresh_from_db()
        self.assertEqual(self.entry.text, 'Private entry')

    def test_owner_can_read_topic_and_logout_uses_post(self):
        self.client.force_login(self.owner)
        response = self.client.get(reverse('learning_logs:topic', args=[self.topic.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Private entry')
        self.assertContains(response, 'method="post"')
        self.assertEqual(self.client.get(reverse('users:logout')).status_code, 405)
        self.assertEqual(self.client.post(reverse('users:logout')).status_code, 200)
        self.assertNotIn('_auth_user_id', self.client.session)
