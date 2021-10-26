from django.test import TestCase
from lists.models import Item, List
from lists.forms import ItemForm, ExistingListItemForm
from django.utils.html import escape
from unittest import skip

# Create your tests here.
class HomePageTest(TestCase):


    def test_home_page_can_return_correct_content(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'lists/index.html')


class NewListTest(TestCase):


    def test_new_list_can_save_a_post_request(self):
        context = {'text': 'A new item'}
        response = self.client.post('/list/new', data=context)
        html = response.content.decode()

        self.assertEqual(1, Item.objects.count())
        item = Item.objects.first()
        self.assertEqual(item.text, context['text'])

    def test_new_list_can_redirect_after_post_request(self):
        context = {'text': 'A new item'}
        response = self.client.post('/list/new', data=context)
        list_ = List.objects.first()
        html = response.content.decode()

        self.assertRedirects(response, f'/list/{list_.pk}/')


    def test_dont_save_invlidation_list_item(self):
        context = {'text': ''}
        response = self.client.post('/list/new', data=context)
        self.assertEqual(Item.objects.count(), 0)
        self.assertEqual(List.objects.count(), 0)

    def test_for_invalid_input_render_home_template(self):
        context = {'text': ''}
        response = self.client.post('/list/new', data=context)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lists/index.html')
     
    def test_validation_errors_are_shown_on_home_page(self):
        context = {'text': ''}
        response = self.client.post('/list/new', data=context)
        expect_error = escape("You can't save an empty item")
        self.assertContains(response, expect_error)

    def test_for_invalid_input_passes_form_to_template(self):
        context = {'text': ''}
        response = self.client.post('/list/new', data=context)
        self.assertIsInstance(response.context['form'], ItemForm)


class ViewListTest(TestCase):


    def test_view_list_can_return_correct_content(self):
        list_ = List.objects.create()
        response = self.client.get(f'/list/{list_.pk}/')
        self.assertTemplateUsed(response, 'lists/list.html')

    def test_view_list_can_display_all_item_for_the_list(self):
        other_list = List.objects.create()
        Item.objects.create(text='other first item', list=other_list)
        Item.objects.create(text='other second item', list=other_list)
        
        correct_list = List.objects.create()
        Item.objects.create(text='first item', list=correct_list)
        Item.objects.create(text='second item', list=correct_list)
        
        response = self.client.get(f'/list/{correct_list.pk}/')

        self.assertContains(response, 'first item')
        self.assertContains(response, 'second item')
        self.assertNotContains(response, 'other first item')
        self.assertNotContains(response, 'other second item')

    def test_view_pass_list_context(self):
        list_ = List.objects.create()
        response = self.client.get(f'/list/{list_.pk}/')
        self.assertEqual(response.context['list'], list_)

        Item.objects.create(text='other first item', list=list_)

    def test_add_item_can_save_a_post_request_for_exsit_list(self):
        other_list = List.objects.create()
        correct_list = List.objects.create()
        context = {'text': 'A new item'}
        response = self.client.post(f'/list/{correct_list.pk}/', data=context)
        html = response.content.decode()

        self.assertEqual(1, Item.objects.count())
        item = Item.objects.first()
        self.assertEqual(item.text, context['text'])

    def test_add_item_can_redirect_after_post_request(self):
        context = {'text': 'A new item'}
        list_ = List.objects.create()
        response = self.client.post(f'/list/{list_.pk}/', data=context)
        html = response.content.decode()

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], f'/list/{list_.pk}/')

    def test_validation_error_end_on_view_list_page(self):
        list_ = List.objects.create()
        context = {'new-item': ''}
        response = self.client.post(f'/list/{list_.pk}/', data=context)
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lists/list.html')
        expect_error = escape("You can't save an empty item")
        self.assertContains(response, expect_error)

    def test_display_item_form(self):
        list_ = List.objects.create()
        response = self.client.get(f'/list/{list_.pk}/')
        self.assertIsInstance(response.context['form'], ExistingListItemForm)
        
 
    def test_duplicate_item_validtaion_eeors_end_on_list_pages(self):
        list1 = List.objects.create()
        item1 = Item.objects.create(list=list1, text='text')
        response = self.client.post(
            f'/list/{list1.id}/',
            data={'text': 'text'}
         )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lists/list.html')
        expect_error = escape("You've already got this in your list")
        self.assertContains(response, expect_error)
    
        
   




        
class ItemAndListTest(TestCase):


    def test_start_two_item_and_retrieve_it_later(self):
        list_ = List.objects.create()
        first_item = Item()
        first_item.text = 'first item'
        first_item.list = list_
        first_item.save()

        second_item = Item()
        second_item.text = 'second item'
        second_item.list = list_
        second_item.save()

        saved_item = list_.item_set.all()
        self.assertEqual(2, len(saved_item))

        first_saved_item, second_saved_item = saved_item

        self.assertEqual(first_saved_item.text, 'first item')
        self.assertEqual(first_saved_item.list, list_)
        self.assertEqual(second_saved_item.text, 'second item')
        self.assertEqual(second_saved_item.list, list_)
