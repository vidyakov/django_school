'use strict';


const axios = require('axios');

axios.get('/api/students/')
    .then((response) => {
        console.log(response.data);
    })
    .catch((error) => {
        console.log(error);
    });


fetch('/api/courses/')
    .then(response => response.json())
    .catch(error => console.log(error));
