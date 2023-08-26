$('document').ready( function () {
   readjsonfile = $.get('../file.json', function (data) {
    for (i in data) {
      $('div #all-cities').append("<li>i['name']</li>")
    }
  });
});
