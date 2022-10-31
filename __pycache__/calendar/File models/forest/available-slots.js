const { collection } = require('forest-express-sequelize');

collection('availableSlots', {
  fields: [{
    field: 'startDate',
    type: 'Date',
  }, {
    field: 'endDate',
    type: 'Date',
  }, {
    field: 'time',
    type: 'String',
  }, {
    field: 'maxTimeSlot',
    type: 'Number',
  }],
  segments: [],
});
