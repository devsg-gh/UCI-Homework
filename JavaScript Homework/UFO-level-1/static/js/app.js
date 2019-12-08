// from data.js
var tableData = data;

// Get a reference to the table body
var tbody = d3.select("tbody");

//ufoSighting report values (Date, City, State, Country, Shape, Duration, Comments)
tableData.forEach(function(ufoSightingReport) {
    // console.log(ufoSightingReport);
    var row = tbody.append("tr");
    Object.entries(ufoSightingReport).forEach(function([key, value]) {
    //   console.log(key, value);
      // Append a cell to the row for each value
      // in the ufoSighting report object
      var cell = row.append("td");
      cell.text(value);
    });
  });
  
  // Select the button
var button = d3.select("#filter-btn");
// var button = d3.select("#form-control);

button.on("click", function() {

    // Select the input element and get the raw HTML node
    var inputElement = d3.select("#datetime");
     // Get the value property of the input element
    var inputValue = inputElement.property("value");
    var filteredData = tableData.filter(sighting => sighting.datetime === inputValue);
    

d3.event.preventDefault();
tbody.text("");

  console.log(filteredData);

  filteredData.forEach(function(ufoSightingReport) {

    var row = tbody.append("tr");
    Object.entries(ufoSightingReport).forEach(function([key, value]) {

      var cell = row.append("td");
      cell.text(value);
    });
  });

});

var button1 = d3.select("#reset-btn");

button1.on("click", function() {

tableData.forEach(function(ufoSightingReport) {
    // console.log(ufoSightingReport);
    var row = tbody.append("tr");
    Object.entries(ufoSightingReport).forEach(function([key, value]) {
    //   console.log(key, value);
      // Append a cell to the row for each value
      // in the ufoSighting report object
      var cell = row.append("td");
      cell.text(value);
    });
  });

});