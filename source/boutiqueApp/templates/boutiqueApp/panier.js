$(function () {

    $("form#formConnexion").submit(function(event) {
        Loader.start();
        var url = "/dreamteam/boutique/connexion/";
        var formData = new FormData($(this)[0]);
        $.post({ url: url, data: formData, processData: false, contentType: false}, function(data){
            if (data.status) {
                window.location.reload();
            }else{
                Loader.stop();
                Alerter.error('Erreur !', data.message);
            }
        });
        return false;
    });



    $("form#formInscription").submit(function(event) {
        Loader.start();
        var url = "/dreamteam/boutique/inscription/";
        var formData = new FormData($(this)[0]);
        $.post({ url: url, data: formData, processData: false, contentType: false}, function(data){
            if (data.status) {
                window.location.reload();
            }else{
                Loader.stop();
                Alerter.error('Erreur !', data.message);
            }
        });
        return false;
    });


    valider_commande = function (table, id) {
        url = "/dreamteam/boutique/valider_commande/";
        var token = $("div.token input[type=hidden]").val();
        alerty.confirm("Voulez-vous vraiment valider cette commande ?", {
            title: "Validation de votre commande",
            cancelLabel: "Non",
            okLabel: "OUI, Valider",
        }, function () {
            Loader.start()
            $.post(url, {'csrfmiddlewaretoken' :token}, (data) => {
                if (data.status) {
                    window.location.href = "/dreamteam/boutique/payement_commande/"+data.id+"/"
                } else {
                    Alerter.error('Erreur !', data.message);
                }
            }, "json");
        })
    }


})