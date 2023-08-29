$('document').ready( function () {
   readjsonfile = $.getJSON('static/file.json', function (data) {
    const info = data;
    for (i in info) {
      if (info[i]['__class__'] == 'City'){
        let name = info[i]['name'];
        console.log(i);
        $("#all-cities ol").append('<li>' + name +'</li>');
      }
    }
  });
});
