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
		$(".panier_length").text(Object.keys(panier).length);
		$(".produits").find("button#"+id).hide();
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
		$("div.produit_panier#"+id).hide(500)
		$(".panier_length").text(Object.keys(panier).length);

		if (Object.keys(panier).length == 0){
			$("div.panier-container").html(`
				<div class='container'>
					<div class='text-center'>
						<h4 >Aucun article dans votre panier pour le moment !</h4>
						<i class='fa fa-shopping-cart fa-4x' aria-hidden='true'></i>
					</div>
				</div>
			`)
		}

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