package main

import (
	"bufio"
	"context"
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"os"
	"time"

	"github.com/gorilla/mux"
	"go.mongodb.org/mongo-driver/bson"
	"go.mongodb.org/mongo-driver/bson/primitive"
	"go.mongodb.org/mongo-driver/mongo"
	"go.mongodb.org/mongo-driver/mongo/options"
)

// var serverAPIOptions = options.ServerAPI(options.ServerAPIVersion1)
// var clientOptions = options.Client().
// 	ApplyURI("mongodb+srv://Ulysses:Odessey123581321!@cluster0.6oh1v.mongodb.net/myFirstDatabase?retryWrites=true&w=majority").
// 	SetServerAPIOptions(serverAPIOptions)
var mdb = "mongodb://localhost:27017"
var ctx, cancel = context.WithTimeout(context.Background(), 500*time.Second)
// var client, mongoErr = mongo.Connect(ctx, clientOptions)
var client, mongoErr = mongo.Connect(ctx, options.Client().ApplyURI(mdb))
var db = client.Database("cs573Data")
var col = db.Collection("ted_talk")

func fetchTopics(response http.ResponseWriter, request *http.Request) {
	var results []string
	fmt.Println("Fetch Topics")
	response.Header().Add("content-type", "application/json")

	file, err := os.Open("tags.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		results = append(results, scanner.Text())
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}
	json.NewEncoder(response).Encode(results)
}

func fetchVideosByTopic(response http.ResponseWriter, request *http.Request) {
	var results []bson.D
	fmt.Println("Fetch Videos by Topic")

	params := mux.Vars(request)
	topic := params["topic"]
	opt := options.Find()
	opt.SetProjection(bson.M{"title": 1, "main_speaker": 1, "duration": 1, "views": 1, "tags": 1, "published_date": 1})
	cursor, err := col.Find(context.TODO(), bson.M{"tags": bson.M{"$in": []string{topic}}}, opt)

	if err != nil {
		// handle error
		fmt.Println(err)
	}
	if err := cursor.All(ctx, &results); err != nil {
		fmt.Println(err)
	}

	// save to map format
	var mappedResults []bson.M
	for _, r := range results {
		mappedResults = append(mappedResults, r.Map())
	}
	json.NewEncoder(response).Encode(mappedResults)
}

func fetchRelatedVideos(response http.ResponseWriter, request *http.Request) {
	var results []bson.D
	fmt.Println("Fetch Related Videos")

	title := request.FormValue("title")
	opt := options.Find()
	opt.SetProjection(bson.M{"related_talks": 1})
	cursor, err := col.Find(context.TODO(), bson.M{"title": title}, opt)

	if err != nil {
		// handle error
		fmt.Println(err)
	}
	if err := cursor.All(ctx, &results); err != nil {
		fmt.Println(err)
	}

	// save to map format
	var mappedResults []bson.M
	r := results[0].Map()["related_talks"]
	talks := r.(primitive.A)
	for _, v := range talks {
		mappedResults = append(mappedResults, v.(primitive.D).Map())
	}
	json.NewEncoder(response).Encode(mappedResults)
}

func setupRoutes() {
	if mongoErr != nil {
		fmt.Println("Error Connecting to MongoDB:")
		fmt.Println(mongoErr)
	}
	defer cancel()

	router := mux.NewRouter()
	router.HandleFunc("/gettopics", fetchTopics).Methods("GET")
	router.HandleFunc("/getvideos/{topic}", fetchVideosByTopic).Methods("GET")
	router.HandleFunc("/getrelated", fetchRelatedVideos).Methods("POST")

	if err := http.ListenAndServe(":3000", router); err != nil {
		fmt.Printf("Server cannot start: %v\n", err)
	}
}

func main() {
	fmt.Println("Start Application...")
	setupRoutes()
}
