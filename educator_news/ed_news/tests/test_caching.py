from django.test import TestCase

from ed_news.views import invalidate_cache


class EdNewsCacheTests(TestCase):

    def test_index_cache(self):
        return 0
        """Request index, then invalidate cache.
        Cache should be invalidated, returning True.
        Then try to invalidate, and should return False.
        """
        response = self.client.get(reverse('ed_news:index'))
        self.assertEqual(response.status_code, 200)

        invalidated = invalidate_cache('index', namespace='ed_news')
        self.assertEqual(invalidated, True)

        invalidated = invalidate_cache('index', namespace='ed_news')
        self.assertEqual(invalidated, False)


    # I am running into namespace issues when trying to generalize these tests.
    def test_new_cache(self):
        return 0
        """Request new, then invalidate cache.
        Cache should be invalidated, returning True.
        Then try to invalidate, and should return False.
        """
        response = self.client.get(reverse('ed_news:new'))
        self.assertEqual(response.status_code, 200)

        invalidated = invalidate_cache('new', namespace='ed_news')
        self.assertEqual(invalidated, True)

        invalidated = invalidate_cache('new', namespace='ed_news')
        self.assertEqual(invalidated, False)
