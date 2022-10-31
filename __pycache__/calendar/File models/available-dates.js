module.exports = (sequelize, DataTypes) => {
    const { Sequelize } = sequelize;
    const AvailableDates = sequelize.define('availableDates', {
      date: {
        type: DataTypes.DATE,
      },
      opened: {
        type: DataTypes.BOOLEAN,
      },
      pricingPremium: {
        type: DataTypes.STRING,
      },
    }, {
      tableName: 'available_dates',
      underscored: true,
      timestamps: false,
      schema: process.env.DATABASE_SCHEMA,
    });
  
    return AvailableDates;
  };
  