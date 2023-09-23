$('document').ready(function () {
  document.getElementById('clickable-heading').addEventListener('click', function() {
    window.location.href = '/';
  });
/*
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
	      $("#touristsites ol").append('<li><a href="/' + city + "/" + name  + '">' + name +'</a></li>');
            } else {
	      continue;
	    }
          } else {
            continue;
          }
        }
      }
    }
  });



  $.ajax( {
    type: 'GET',
    url: 'http://127.0.0.1:5001/api/v1/all',
    success: function (data) {
      const list = data;
      for (i in list) {
        if (list[i]['__class__'] == 'TouristSite'){
        	let name = list[i]['name'];
        	let city = 'none';
        	if (list[i]['city_id'] == $('#touristsites').attr('city_id')) {
          	for (j in list) {
            		if (list[j]['__class__'] == 'City') {
              			if (list[i]['city_id'] == list[j]['id']){
                			city = list[j]['name'];
                			break;
              			} else {
                			continue;
              			}
            		} else {
              			continue
            		}
          	}
          	$('#touristsites ol').append('<li><a href="/' + city + '/' + name  + '">' + name +'</a></li>');
        	}
        }
      }
    }
  });

  const readjsonfile = $.getJSON('static/file.json', function(data){
    const list = data;
    for (i in list) {
      if (list[i]['__class__'] == 'TouristSite'){
	let name = list[i]['name'];
	let city = 'none';
	if (list[i]['city_id'] == $('#touristsites').attr('city_id')) {
	  for (j in list) {
	    if (list[j]['__class__'] == 'City') {
	      if (list[i]['city_id'] == list[j]['id']){
	        city = list[j]['name'];
		break;
	      } else {
	        continue;
	      }
	    } else {
	      continue
	    }
	  }
	  $('#touristsites ol').append('<li><a href="/' + city + '/' + name  + '">' + name +'</a></li>');
        }
      }
    }
  });*/
  
});
