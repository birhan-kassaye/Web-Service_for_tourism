$('document').ready( function() {
  let filters = [];
  $('.checkoption').click(function() {
    $('.checkoption').not(this).prop('checked', false);
    filters.push($(this).attr('data-name'))
  });

  $('.locationoption').click(function() {
    $('.locationoption').not(this).prop('checked', false)
    filters.push($(this).attr('data-name'))
  });

  $('.regionoption').click(function() {
    $('.regionoption').not(this).prop('checked', false);
    filters.push($(this).attr('data-name'))
  });

  $('.weatheroption').click(function() {
    $('.weatheroption').not(this).prop('checked', false);
    filters.push($(this).attr('data-name'))
  });
	console.log(filters)
});
