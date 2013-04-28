from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from cmsplugin_youtube.models import YouTube as YouTubeModel

from django.utils.translation import ugettext as _

class YouTubePlugin(CMSPluginBase):
    model = YouTubeModel
    name = _("YouTube")
    render_template = "cmsplugin_youtube/simple.html"

    def render(self, context, instance, placeholder):
        if instance.template:
            self.render_template = instance.template
        context.update({
            'object': instance,
            'placeholder': placeholder
        })
        return context

plugin_pool.register_plugin(YouTubePlugin)
