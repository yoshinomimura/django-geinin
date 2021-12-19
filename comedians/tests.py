from django.test.testcases import TestCase
from comedians.models import Comedian
from django.urls import reverse


class HogeTest(TestCase):
    fixtures = ()

    def setUp(self):
        super(HogeTest, self).setUp()
        self.comedian = Comedian.objects.create(name="松本人志")

    def test_comedian(self):
        print('テスト開始')
        response = self.client.get(reverse('comedians:detail', kwargs={'comedian_id': self.comedian.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'comedians/detail.html')
        self.assertContains(response, f'{self.comedian.name}')
        print('テスト終了')