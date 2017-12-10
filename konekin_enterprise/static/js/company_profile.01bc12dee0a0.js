console.log($("#company-location").text());
var address = $("#company-location").text();

function initMap() {
    var geocoder = new google.maps.Geocoder();
    geocoder.geocode({'address': address}, function (results, status) {
        if (status === google.maps.GeocoderStatus.OK) {
            var propertiPeta = {
                center: results[0].geometry.location,
                zoom: 15,
                mapTypeId: google.maps.MapTypeId.ROADMAP
            };
            var peta = new google.maps.Map(document.getElementById("googleMap"), propertiPeta);
            var marker = new google.maps.Marker({
                map: peta,
                position: results[0].geometry.location
            });
        } else {
            var html = '<div class="alert alert-danger text-center">' +
                'Location Not Found!' +
                '</div>';
            $("#googleMap").append(html)
        }
    });
}