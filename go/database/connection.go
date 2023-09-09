package database

import (
	"api/config"
	"fmt"
	"github.com/jmoiron/sqlx"
	_ "github.com/lib/pq"
)

func CreateDatabase() (*sqlx.DB, error) {
	conf := config.GetConfig()
	connStr := fmt.Sprintf("host=%s port=%s user=%s password=%s dbname=%s sslmode=disable", conf.DBHost, conf.DBPort, conf.DBUser, conf.DBPassword, conf.DBDatabase)
	db, err := sqlx.Connect("postgres", connStr)
	if err != nil {
		return nil, err
	}
	db.SetMaxOpenConns(100)
	db.SetMaxIdleConns(1)

	return db, err
}
