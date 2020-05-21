from django import forms


class MapWidget(forms.widgets.TextInput):
    template_name = 'core/map.html'
    class Media:
        css = {'all': (
            "https://unpkg.com/leaflet@1.6.0/dist/leaflet.css", 
            'core/css/map.css'
            
            )}
        js = ('shop/js/jquery.min.js',
            "https://unpkg.com/leaflet@1.6.0/dist/leaflet.js",
            'core/js/map.js'
        )

    def __init__(self, attrs=None, *args, **kwargs):
        super().__init__(attrs)