const express = require('express');
const { PermissionMiddlewareCreator, RecordSerializer } = require('forest-express-sequelize');
const { availableSlots } = require('../models');

const router = express.Router();
const permissionMiddlewareCreator = new PermissionMiddlewareCreator('availableSlots');
const recordSerializer = new RecordSerializer({ name: 'availableSlots' });

// Get a list of Available slots
router.get('/availableSlots', permissionMiddlewareCreator.list(), (request, response, next) => {
  const { date } = request.query;
  const { duration } = request.query;
  return fetch(`https://apicallplaceholder/slots/?date=${date}&duration=${duration}`)
    .then((response) => JSON.parse(response))
    .then((matchingSlots) => {
      return recordSerializer.serialize(matchingSlots)
        .then((recordsSerialized) => response.send(recordsSerialized));
    })
    .catch((error) => {
      console.error(error);
    });
});


module.exports = router;