/*Scroll to top when arrow up clicked BEGIN*/
$(window).scroll(function() {
  var height = $(window).scrollTop();
  if (height > 100) {
    $('#goToTop').fadeIn();
  } else {
    $('#goToTop').fadeOut();
  }
});
$(document).ready(function() {
  $("#goToTop").click(function(event) {
    event.preventDefault();
    $("html, body").animate({ scrollTop: 0 }, "slow");
    return false;
  });

});
