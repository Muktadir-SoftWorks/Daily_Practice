//object

let car = {
    brand: "Toyota",
    model: "Corolla",
    year: 2022,
    features: ["AC", "Bluetooth", "Hybrid"],
    start: function() {
      console.log("Car Started");
    }
  };
  
  console.log(car.features);
  car.start();
   

//json

let carJson = {
    "brand": "Toyota",
    "model": "Corolla",
    "year": 2022,
    "features": ["AC", "Bluetooth", "Hybrid"],
    "start": function() {
      console.log("Car Started");
    }
  };
  
  // Displaying the original object
  console.log("JavaScript Object:", carJson);
  
  // Converting object to JSON (functions will be excluded in JSON)
  let carJsonString = JSON.stringify(carJson);
  console.log("JSON Format:", carJsonString);
  
  // Converting JSON back to a JavaScript object
  let carObj = JSON.parse(carJsonString);
  console.log("Converted JavaScript Object:", carObj);
  
  // Accessing the method after JSON conversion
  // Note: The "start" function is excluded during stringification, so it won't be present in `carObj`.