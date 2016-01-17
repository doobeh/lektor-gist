# -*- coding: utf-8 -*-
from lektor.pluginsystem import Plugin
from markupsafe import Markup

GIST_EMBED = '''
    <div class="gist">
        <script src='https://gist.github.com/{gist}.js'></script>
        <noscript>
            <pre><code>#!/bin/bash ...</code></pre>
        </noscript>
    </div>
'''

class GistPlugin(Plugin):
    name = u'Gist'
    description = u'adds `gist` jinja filter to embed snippets'

    def on_setup_env(self):
        def gist(id_):
            return Markup(GIST_EMBED.format(gist=id_))

        self.env.jinja_env.filters['gist'] = gist
