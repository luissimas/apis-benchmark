package main

import (
	"api/config"
	"api/database"
	"fmt"
	"log"
	"net/http"
	"time"

	"github.com/gin-gonic/gin"
	"github.com/google/uuid"
)

type Movie struct {
	ID          uuid.UUID `db:"id" json:"id"`
	Name        string    `db:"name" json:"name"`
	ReleaseDate time.Time `db:"release_date" json:"release_date"`
	Director    string    `db:"director" json:"director"`
	Description string    `db:"description" json:"description,omitempty"`
	Duration    uint      `db:"duration" json:"duration,omitempty"`
	Budget      uint      `db:"budget" json:"budget,omitempty"`
	CreatedAt   time.Time `db:"created_at" json:"created_at"`
	UpdatedAt   time.Time `db:"updated_at" json:"updated_at"`
}

func createMovies() []Movie {
	movies := make([]Movie, 1000)
	for i := 0; i < len(movies); i++ {
		m := Movie{
			ID:          uuid.New(),
			Name:        "any-movie-name",
			ReleaseDate: time.Now(),
			Director:    "any-movie-director",
			Description: "any-movie-description",
			Duration:    1000,
			Budget:      10000,
		}
		movies[i] = m
	}
	return movies
}

func main() {
	db, err := database.CreateDatabase()
	if err != nil {
		log.Fatalf("Error creating database connection: %v\n", err)
	}
	log.Print("Connected to the database.")
	defer db.Close()

	router := gin.New()
	router.Use(gin.Recovery())

	router.GET("/db", func(c *gin.Context) {
		var movies []Movie
		err := db.Select(&movies, "SELECT * FROM movies LIMIT 20")
		if err != nil {
			c.JSON(http.StatusInternalServerError, nil)
			log.Fatal(err)
			return
		}
		c.JSON(http.StatusOK, movies)
	})
	router.GET("/cache", func(c *gin.Context) { c.JSON(http.StatusOK, createMovies()) })

	conf := config.GetConfig()
	url := fmt.Sprintf("%s:%s", conf.ServerHost, conf.ServerPort)

	log.Fatal(router.Run(url))
}
