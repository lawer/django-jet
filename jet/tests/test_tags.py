from django import forms
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.test.client import RequestFactory
from django.urls import reverse

from jet.templatetags.jet_tags import jet_next_object, jet_previous_object, jet_select2_lookups
from jet.tests.models import SearchableTestModel, TestModel


class TagsTestCase(TestCase):
	def setUp(self):
		self.models = []
		self.searchable_models = []

		self.models.append(TestModel.objects.create(field1='first', field2=1))
		self.models.append(TestModel.objects.create(field1='second', field2=2))
		self.searchable_models.append(SearchableTestModel.objects.create(field1='first', field2=1))
		self.searchable_models.append(SearchableTestModel.objects.create(field1='second', field2=2))

	def test_select2_lookups(self):
		class TestForm(forms.Form):
			form_field = forms.ModelChoiceField(SearchableTestModel.objects)

		value = self.searchable_models[0]

		form = TestForm(initial={'form_field': value.pk})
		field = form['form_field']
		field = jet_select2_lookups(field)
		choices = [choice for choice in field.field.choices]

		self.assertEqual(len(choices), 1)
		self.assertEqual(choices[0][0], value.pk)

	def test_select2_lookups_posted(self):
		class TestForm(forms.Form):
			form_field = forms.ModelChoiceField(SearchableTestModel.objects)

		value = self.searchable_models[0]

		form = TestForm(data={'form_field': value.pk})
		field = form['form_field']
		field = jet_select2_lookups(field)
		choices = [choice for choice in field.field.choices]

		self.assertEqual(len(choices), 1)
		self.assertEqual(choices[0][0], value.pk)

	def test_non_select2_lookups(self):
		class TestForm(forms.Form):
			form_field = forms.ModelChoiceField(TestModel.objects)

		value = self.searchable_models[0]

		form = TestForm(initial={'form_field': value.pk})
		field = form['form_field']
		field = jet_select2_lookups(field)
		choices = [choice for choice in field.field.choices]

		self.assertEqual(len(choices), len(self.models) + 1)

	def test_jet_sibling_object_next_url(self):
		instance = self.models[0]
		ordering_field = 1  # field1 in list_display
		preserved_filters = '_changelist_filters=o%%3D%d' % ordering_field

		expected_url = reverse('admin:%s_%s_change' % (
			TestModel._meta.app_label,
			TestModel._meta.model_name
		), args=(self.models[1].pk,)) + '?' + preserved_filters

		user = get_user_model().objects.create_user(
			username='admin',
			password='passadmin'
		)

		request = RequestFactory().get(expected_url)
		request.user = user
		context = {
			'original': instance,
			'preserved_filters': preserved_filters,
			'request': request,
		}

		actual_url = jet_next_object(context)['url']

		self.assertEqual(actual_url, expected_url)

	def test_jet_sibling_object_previous_url(self):
		instance = self.models[0]
		ordering_field = 1  # field1 in list_display
		preserved_filters = '_changelist_filters=o%%3D%d' % ordering_field

		changelist_url = reverse('admin:%s_%s_change' % (
			TestModel._meta.app_label,
			TestModel._meta.model_name
		), args=(self.models[1].pk,)) + '?' + preserved_filters

		user = get_user_model().objects.create_user(
			username='admin',
			password='passadmin'
		)
		request = RequestFactory().get(changelist_url)
		request.user = user
		context = {
			'original': instance,
			'preserved_filters': preserved_filters,
			'request': request,
		}

		previous_object = jet_previous_object(context)
		expected_object = None

		self.assertEqual(previous_object, expected_object)
