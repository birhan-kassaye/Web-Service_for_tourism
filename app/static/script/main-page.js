$('document').ready( function () {
   $.ajax({
    type: 'GET',
    url: 'http://0.0.0.0:5001/api/v1/cities',
    success: function (data) {
      const info = data;
      let names = [];
      for (i in info) {
        if (info[i]['__class__'] == 'City'){
          names.push(info[i]['name']);
        }
      }
      names.sort(function (a, b) {
            return a.localeCompare(b);
      });
      for (let j = 0; j < names.length; j++) {
        let name = names[j]
        $("#all-cities ol").append('<li><a href="/' + name + '">' + name +'</a></li>');
    }  
    }
  });
/*   readjsonfile = $.getJSON('static/file.json', function (data) {
    const info = data;
    let names = [];
    for (i in info) {
      if (info[i]['__class__'] == 'City'){
	names.push(info[i]['name']);
      }
    }
    names.sort(function (a, b) {
          return a.localeCompare(b);
    });
    for (let j = 0; j < names.length; j++) {
      let name = names[j]
      $("#all-cities ol").append('<li><a href="/' + name + '">' + name +'</a></li>');
    }
  });*/
});
