$(function () {
	
	add = function(id){
		var qte = $("input#"+id).val()
		$("input#"+id).val(qte*1 +1)
	}
		
	remove = function(id){
		 var qte = $("input#"+id).val()
		if(qte > 1){
			$("input#"+id).val(qte*1 -1)
		}
	}
})