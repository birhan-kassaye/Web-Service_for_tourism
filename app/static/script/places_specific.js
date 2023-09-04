$('document').ready( function () {
   readjsonfile = $.getJSON('static/file.json', function (data) {
    const info = data;
    for (i in info) {
      if (info[i]['__class__'] == 'TouristSite'){
        let name = info[i]['name'];
	let city = "none";
	for (j in info) {
	  if (info[j]['__class__'] == 'City'){
	    if (info[i]['city_id'] == info[j]['id']){
	      city = info[j]['name']
	    }
	  } else {
	    continue;
	  }
	}
        $("#all-cities ol").append('<li><a href="/' + city + "/" + name  + '">' + name +'</a></li>');
      }
    }
  });
});
