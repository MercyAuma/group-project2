// Creating our initial map object
// We set the longitude, latitude, and the starting zoom level
// This gets inserted into the div with an id of 'map'
var myMap = L.map("map", {
  center: [38.30, -98.00],
  zoom: 4
});

// Adding a tile layer (the background map image) to our map
// We use the addTo method to add objects to our map
L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
// L.tileLayer("https://api.mapbox.com/styles/v1/mauma/ck8y47lqu03m31it4vnm9v7d9.html?fresh=true&title=copy&access_token={accessToken}", {
  attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
  maxZoom: 18,
  id: "mapbox.streets-basic",
  accessToken: API_KEY
}).addTo(myMap);

// Uncomment this link local geojson for when data.beta.nyc is down
var link = "static/data/usstates.json";

// Grabbing our GeoJSON data..
d3.json(link, function(data) {
  // Creating a GeoJSON layer with the retrieved data
  L.geoJson(data).addTo(myMap);
});

// // Our style object
// var mapStyle = {
//   color: "white",
//   fillColor: "pink",
//   fillOpacity: 0.5,
//   weight: 1.5
// };

// // Grabbing our GeoJSON data..
// d3.json(link, function(data) {
//   // Creating a geoJSON layer with the retrieved data
//   L.geoJson(data, {
//     // Passing in our style object
//     style: mapStyle
//   }).addTo(map);
// });

