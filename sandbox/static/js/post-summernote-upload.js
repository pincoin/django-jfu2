$(document).ready(function () {
    var $sn = $('#id_body');

    $sn.summernote({
        placeholder: 'Please, type your message',
        tabsize: 2,
        height: 300,
        callbacks: {
            onInit: function () {
                $nEditor = $sn.next();
                $nImageInput = $nEditor.find('.note-image-input');
            },
            onImageUpload: function (files) {
                // https://github.com/blueimp/jQuery-File-Upload/wiki/API#initialization
                // Initializes file upload widget
                $nImageInput.fileupload({
                    url: '/upload'
                });

                // https://github.com/blueimp/jQuery-File-Upload/wiki/API#programmatic-file-upload
                // Upload files programmatically for browsers with support for XHR file uploads
                var jqXHR = $nImageInput.fileupload('send', {
                    files: files
                }).done(function (data, textStatus, jqXHR) {
                    $.each(data.files, function (index, file) {
                        $sn.summernote('insertImage', file.url);

                        $('#thumbnail-list').append(
                            '<div class="col-lg-2 col-md-3 col-sm-4 mt-2">\n' +
                            '  <div class="card h-100">\n' +
                            '    <div class="card-body">\n' +
                            '      <img class="card-img-top" src="' + file.url + '" width="118" height="68">\n' +
                            '    </div>\n' +
                            '    <div class="card-footer text-center">\n' +
                            '      <a href="#" class="btn-sm btn-danger">Delete</a>\n' +
                            '    </div>\n' +
                            '  </div>\n' +
                            '</div>')

                        // This hidden field must be sent in order to make a relationship.
                        $("<input>", {
                            type: "hidden",
                            name: "attachments",
                            value: file.pk
                        }).appendTo("form");
                    });
                }).fail(function (jqXHR, textStatus, errorThrown) {
                    console.log('Failed to upload');
                });
            }
        }
    })
});