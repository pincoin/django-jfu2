from django import forms

class SummernoteWidget(forms.TextArea):


    class Media:
        css = {
            'all': (
                'css/summernote/summernote-lite.css',
            )
        }
        js = (
            'js/summernote/summernote-lite.js',
        )
