$(function () {

	ajouter = function(id){
		var panier = localStorage.getItem("dreamteam-panier"); 
		if (panier == null) {
			panier = {}
		}else{
			panier = JSON.parse(panier)
		}
		panier[id] = 1
		localStorage.setItem("dreamteam-panier", JSON.stringify(panier)); 
		session("dreamteam-panier", JSON.stringify(panier)); 
		$("#panier_length").text(Object.keys(panier).length);
		$(".produits button#"+id).parent().html('<h6 class="text-center">Ajouté au panier</h6>')
		$(".produits button#"+id).hide();
	}
	
	
	add = function(id){
		var qte = $("input#"+id).val()
		qte = qte*1 +1
		$("input#"+id).val(qte)
		var panier = localStorage.getItem("dreamteam-panier"); 
		panier = JSON.parse(panier)
		panier[id] = qte
		localStorage.setItem("dreamteam-panier", JSON.stringify(panier)); 
		session("dreamteam-panier", JSON.stringify(panier)); 
	}
	
	remove = function(id){
		var qte = $("input#"+id).val()
		if(qte > 1){
			qte = qte*1 -1
			$("input#"+id).val(qte)
			var panier = localStorage.getItem("dreamteam-panier"); 
			panier = JSON.parse(panier)
			panier[id] = qte
			localStorage.setItem("dreamteam-panier", JSON.stringify(panier)); 
			session("dreamteam-panier", JSON.stringify(panier)); 
		}
	}

	delete_from_panier = function(id){
		var panier = localStorage.getItem("dreamteam-panier"); 
		panier = JSON.parse(panier)
		delete panier[id]
		localStorage.setItem("dreamteam-panier", JSON.stringify(panier)); 
		session("dreamteam-panier", JSON.stringify(panier)); 
		$("div.produit_panier#"+id).hide(700)
		$("#panier_length").text(Object.keys(panier).length);

		var url = "/dreamteam/boutique/panier_price/"
		var formdata = new FormData();
		$.post({ url: url, data: formdata, contentType: false, processData: false }, function (data) {
            if (data.status) {
				$("#total_price_panier").text(data.price);
            } else {
                Alerter.error('Erreur !', data.message);
            }
        }, 'json')
	}
})