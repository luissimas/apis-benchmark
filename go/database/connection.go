package database

import (
	"api/config"
	"fmt"
	"github.com/jmoiron/sqlx"
	_ "github.com/lib/pq"
)

func CreateDatabase() (*sqlx.DB, error) {
	conf := config.GetDB()
	connStr := fmt.Sprintf("host=%s port=%s user=%s password=%s dbname=%s sslmode=disable", conf.Host, conf.Port, conf.User, conf.Password, conf.Database)
	db, err := sqlx.Connect("postgres", connStr)
	if err != nil {
		return nil, err
	}
	db.SetMaxOpenConns(100)
	db.SetMaxIdleConns(1)

	return db, err
}
