if (!$) {
    $ = django.jQuery;
}

// A $( document ).ready() block.
$( document ).ready(function() {
    
    var mymap = L.map('mapid').setView([31.3231,48.6793], 13);
    L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
        attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
        maxZoom: 18,
        id: 'mapbox/streets-v11',
        tileSize: 512,
        zoomOffset: -1,
        accessToken: 'pk.eyJ1IjoibWFqaWQxNjUiLCJhIjoiY2s5ZHlpZzRmMDBlZzNnbGhsbWY5ZzU1ciJ9.hapfCYp2wEWNnFwkPyAC8g'
    }).addTo(mymap);
    var layerGroup = L.layerGroup().addTo(mymap);

    function onMapClick(e) {
        // remove all the markers in one go
        layerGroup.clearLayers();
        L.marker(e.latlng).addTo(layerGroup);

        var loc = ""+e.latlng.lat + "," + e.latlng.lng
        document.getElementById('map_id').setAttribute('value',loc)
    }

    mymap.on('click', onMapClick);

});



