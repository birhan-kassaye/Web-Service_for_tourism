$('document').ready(function () {
  const readjsonfile = $.getJSON('static/file.json', function(data){
    const list = data;
    for (i in list) {
      if (list[i]['__class__'] == 'TouristSite'){
	let name = list[i]['name'];
      	$('#touristsites ol').append('<li>' + name + '</li>')
      }
    }
  });
});
