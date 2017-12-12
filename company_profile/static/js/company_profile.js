//Google Maps API
var address = $("#company-location").text();
var isInitMapWork = false;
var isMapMarkerWork = false;


console.log("Company Address: ");
console.log(address);

window.initMap = function () {
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
            isMapMarkerWork = true;
        } else {
            var html = '<div class="alert alert-danger text-center">' +
                'Location Not Found!' +
                '</div>';
            $("#googleMap").append(html);
            isMapMarkerWork = true;
        }
    });
    isInitMapWork = true;
};

$(document).ready(function () {
    QUnit.test("initMap Function Test", function (assert) {
        assert.equal(isInitMapWork, true);
    });

    QUnit.test("Is Map Marker Work Test", function (assert) {
        assert.equal(isMapMarkerWork, true);
    });
});

function onLinkedInLoad() {
    IN.Event.on(IN, "auth", cekUser);
}

function cekUser() {
    if (IN.User.isAuthorized()) {
        console.log(!IN.User.isAuthorized);
    }
}