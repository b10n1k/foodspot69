$(document).ready( function(){
    $(".orderbtn").click(function(){	
	    p=$(this).prop("id");
	    $.ajax({
		type:"GET",
		url:"order/",
		data:{'itemId':p
		     //'csrfmiddlewaretoken': $("{% csrf_token %}") 
		     },
		success: displayItem,
		dataType:'json'
	    });
	    //preventDefault();
	
    });

    function displayItem(data){
	  
	$('#selected').html(JSON.strigify(data));
    }
});


