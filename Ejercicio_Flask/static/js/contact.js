$(function(){
	$('#btnsend').click(function(){
		
		$.ajax({
			url: '/Contact',
			data: $('form').serialize(),
			type: 'POST',
			
			success: function(response){
				console.log(response);
			},
			error: function(error){
				console.log(error);
			}
		});
	});
});
