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


})