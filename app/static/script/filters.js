$('document').ready( function() {
  /*var interval = setInterval(checkInput, 100);
  let filters = {};
  function checkInput() {
    $('.checkoption').click(function() {
      $('.checkoption').not(this).prop('checked', false);
      filters[$(this).attr('data-name')] = $(this).attr('data-value')
    });

    $('.locationoption').click(function() {
      $('.locationoption').not(this).prop('checked', false)
      filters[$(this).attr('data-name')] = $(this).attr('data-value')
    });

    $('.regionoption').click(function() {
      $('.regionoption').not(this).prop('checked', false);
      filters[$(this).attr('data-name')] = $(this).attr('data-value')
    });

    $('.weatheroption').click(function() {
      $('.weatheroption').not(this).prop('checked', false);
      if ($(this).is(':checked')) {
        filters[$(this).attr('data-name')] = $(this).attr('data-value')
      }
    });
  }*/

    $.getJSON('static/file.json', function (data) {
      const info = data;
      for (i in info) {
        if (info[i]['__class__'] == 'City') {
          let name = info[i]['name']
          if (filters['weather'] == info[i]['weather']) {
            $('#results').append('<li>'+ name + '</li>');
            console.log(info[i][name])
          }
        }
      }
    });

    $('#results').on('blur', function() {
      clearInterval(interval);
    });
    
});
