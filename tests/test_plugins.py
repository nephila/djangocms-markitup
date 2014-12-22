# -*- coding: utf-8 -*-
from cms.api import add_plugin
from django.template import RequestContext

from djangocms_helper.base_test import BaseTestCase


class PluginTest(BaseTestCase):
    _pages_data = (
        {'en': {'title': 'Page title', 'template': 'page.html', 'publish': True},
         'fr': {'title': 'Titre', 'publish': True},
         'it': {'title': 'Titolo pagina', 'publish': False}},
    )
    def test_plugin_render(self):
        pages = self.get_pages()
        placeholder = pages[0].placeholders.get(slot='content')

        plugin = add_plugin(placeholder, 'MarkItUpPlugin', 'en', body='**Bold**')
        request = self.get_page_request(pages[0], self.user, r'/en/', lang='en', edit=True)
        context = RequestContext(request, {})
        rendered = plugin.render_plugin(context, placeholder)
        self.assertTrue('<strong>Bold</strong>' in rendered)

    def test_plugin_render_empty(self):
        test_string = '''

        '''
        pages = self.get_pages()
        placeholder = pages[0].placeholders.get(slot='content')

        plugin = add_plugin(placeholder, 'MarkItUpPlugin', 'en', body=test_string)
        request = self.get_page_request(pages[0], self.user, r'/en/', lang='en', edit=True)
        context = RequestContext(request, {})
        rendered = plugin.render_plugin(context, placeholder)
        self.assertTrue('<p></p>' in rendered)