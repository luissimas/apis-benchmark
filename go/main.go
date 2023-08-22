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
	ID          uuid.UUID `json:"id"`
	Name        string    `json:"name"`
	ReleaseDate time.Time `json:"release_date"`
	Director    string    `json:"director"`
	Description string    `json:"description,omitempty"`
	Duration    uint      `json:"duration,omitempty"`
	Budget      uint      `json:"budget,omitempty"`
	CreatedAt   time.Time `json:"created_at"`
	UpdatedAt   time.Time `json:"updated_at"`
}

func createData() []Movie {
	var movies []Movie
	for i := 0; i < 1000; i++ {
		m := Movie{
			ID:          uuid.New(),
			Name:        "any-movie-name",
			ReleaseDate: time.Now(),
			Director:    "any-movie-director",
			Description: "any-movie-description",
			Duration:    1000,
			Budget:      10000,
		}
		movies = append(movies, m)
	}
	return movies
}

func main() {
	log.Printf("Config loaded:\n\tAPI: %v\n\tDB: %v\n", config.GetAPI(), config.GetDB())
	db, err := database.CreateDatabase()
	if err != nil {
		log.Fatalf("Error creating database connection: %v\n", err)
	}
	log.Print("Connected to the database.")

	movies := createData()

	router := gin.Default()

	router.GET("/db", func(c *gin.Context) {
		var movies []Movie
		err := db.Limit(20).Find(&movies).Error
		if err != nil {
			c.JSON(http.StatusInternalServerError, nil)
			log.Fatal(err)
			return
		}
		c.JSON(http.StatusOK, movies)
	})
	router.GET("/cache", func(c *gin.Context) { c.IndentedJSON(http.StatusOK, movies) })

	url := fmt.Sprintf("%s:%s", config.GetAPI().Host, config.GetAPI().Port)

	log.Fatal(router.Run(url))
}
