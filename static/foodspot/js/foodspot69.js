$(document).ready( function(){
    $(".orderbtn").click(function(){	
	    p=$(this).prop("id");
	    $.ajax({
		type:"GET",
		url:"order/",
		data:{"itemId":p
		     //'csrfmiddlewaretoken': $("{% csrf_token %}") 
		     },
		success: function(data){
                    $('#selected').html("foo"+data.title);
                }
		//dataType:"json"
	    });
	    	
    });
});


