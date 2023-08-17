package database

import (
	"api/config"
	"fmt"

	"gorm.io/driver/postgres"
	"gorm.io/gorm"
)

func CreateDatabase() (*gorm.DB, error) {
	conf := config.GetDB()
	connStr := fmt.Sprintf("host=%s port=%s user=%s password=%s dbname=%s sslmode=disable", conf.Host, conf.Port, conf.User, conf.Password, conf.Database)

	db, err := gorm.Open(postgres.Open(connStr), &gorm.Config{})
	if err != nil {
		return nil, err
	}

	return db, err
}
