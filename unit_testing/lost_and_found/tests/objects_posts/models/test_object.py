from django.core import exceptions
from django.core.exceptions import ValidationError

from lost_and_found.objects_posts.models import Object
from django.test import TestCase


class TestObjectModel(TestCase):

    def setUp(self):
        self.valid_data = {
            # 'id': 45,
            'name': 'Book',
            'image': 'https://upload.wikimedia.org/wikipedia/commons/b/b6/Gutenberg_Bible%2C_Lenox_Copy%2C_New_York_Public_Library%2C_2009._Pic_01.jpg',
            'width': 5,
            'height': 4,
            'weight':2
        }


    def test_create_object__name_with_more_than_10_chars__expect_validation_error(self):

        self.valid_data['name'] ='sadfasfasfasassafas'



        with self.assertRaises(exceptions.ValidationError) as context:
            obj = Object.objects.create(**self.valid_data)
            obj.full_clean()

        self.assertEqual('dsafsa',context.exception)
