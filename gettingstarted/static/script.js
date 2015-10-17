function initMap() {
  var myLatLng = {lat: -25.363, lng: 131.044};
  var dataset = {% autoescape off %}{{rel}};{% endautoescape %}

  var map = new google.maps.Map(document.getElementById('map'), {
    zoom: 4,
    center: myLatLng,
    disableDefaultUI: true
  });

  var marker = new google.maps.Marker({
    position: myLatLng,
    map: map,
    title: 'Hello World!'
  });
}