# django-jfu2
jQuery-File-Upload for Django

# Installation
1. `settings.py`

2. Setup javascript and stylesheets.

3. Create your own javascript.


# Custom settings
## `settings.py`
```
# JFU2 Settings
# The content-type header uploaded with the file (e.g. text/plain or application/pdf)
JFU2_CONTENT_TYPES = ['image', 'video']
# The allowed file extensions
JFU2_FILE_EXTENSIONS = ['jpg', 'jpeg', 'gif', 'png']
# The size, in bytes, of the uploaded file. (default: 2MB)
JFU2_MAX_UPLOAD_SIZE = 2097152
```

## Custom attachment model
1. Make a subclass of the class `AbstractAttachment`.

2. Override the method `get_object()` of `FileUploadView` class which returns your object of the subclass.

## basic-upload.js

`$('#id_body')`

`url: '/jfu2/upload'`

```
$("#files ul").append('<li>' + file.pk + ': <a href="' + file.url + '">' + file.name + '</a></li>');
```

## post-summernote-upload.js

```
$("<input>", {
    type: "hidden",
    name: "attachments",
    value: file.pk
}).appendTo("form");
```

# License
MIT
