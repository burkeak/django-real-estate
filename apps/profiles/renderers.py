import json

from rest_framework.renderers import JSONRenderer


class ProfileJSONRenderer(JSONRenderer):
    charset = "utf-8"
    # A function that overides the Json renderer to render our in a profile namespace
    def render(self, data, accepted_media_types=None, renderer_context=None):
        errors = data.get("errors", None)

        if errors is not None:
            return super(ProfileJSONRenderer, self).render(data)

        return json.dumps({"profile": data})

