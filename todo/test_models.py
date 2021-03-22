from django.test import TestCase
from .models import items


class TestModels (TestCase):
    def test_done_defaults_to_false(self):
        item = items.objects.create(name='test todo item')
        self.assertFalse(item.done)

    def test_item_returns_name(self):
        item = items.objects.create(name='test todo item')
        self.assertEqual(str(item), 'test todo item')
        

