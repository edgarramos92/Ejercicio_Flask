$(function(){
	$('#btnLogging').click(function(){
		
		$.ajax({
			url: '/Logging',
			data: $('form').serialize(),
			type: 'POST',
			
			success: function(response){
				console.log(response);
			},
			error: function(error){
				console.log(error);
			}
		});
		$.alert(1);
	});
});
