# django-jfu2
jQuery-File-Upload for Django

# Installation
1. `settings.py`

2. Setup javascript and stylesheets.

3. Create your own javascript.


# Custom settings
## Custom attachment model
1. Make a subclass of the class `AbstractAttachment`.

2. Override the method `get_object()` of `FileUploadView` class which returns your object of the subclass.

# License
MIT
