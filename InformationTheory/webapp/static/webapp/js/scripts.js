

$(document).ready(function(){
  $(".card-footer").click(function(){
  	var $thisParagraph = $( this );
  	$thisParagraph.find( ".desc" ).slideToggle("slow");
  	$thisParagraph.find( ".rot_object" ).toggleClass('rotate');
  });
});