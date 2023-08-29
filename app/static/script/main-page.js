$('document').ready( function () {
   readjsonfile = $.get('static/file.json', function (data) {
    for (i in data) {
      $('div #all-cities').append(i)
    }
  });
});
