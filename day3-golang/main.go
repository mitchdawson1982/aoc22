package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

const (
	letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
)

func partOne() {
	file, err := os.Open("input.txt")
	if err != nil {
		fmt.Println("Error Opening The File", err)
	}
	defer file.Close()
	var counter int

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		midPoint := len(line) / 2
		firstHalf := line[0:midPoint]
		secondHalf := line[midPoint:]

		for _, letter := range firstHalf {
			result := strings.ContainsAny(string(letter), secondHalf)
			if result == true {
				fmt.Printf("%c\n", letter)
				counter = counter + strings.Index(letters, string(letter)) + 1
				break
			}
		}
	}
	fmt.Printf("%d\n", counter)
}

func partTwo() {
	file, err := os.Open("input.txt")
	if err != nil {
		fmt.Println("Error Opening The File", err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	scanner.Split(bufio.ScanLines)
	var lines []string
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}
	file.Close()

	var chunkSize int
	chunkSize = 3

	var chunks [][]string
	for i := 0; i < len(lines); i += chunkSize {
		end := i + chunkSize
		if end > len(lines) {
			end = len(lines)
		}
		chunks = append(chunks, lines[i:end])
	}
	var counter int
	for _, chunk := range chunks {
		s1 := chunk[0]
		s2 := chunk[1]
		s3 := chunk[2]
		for _, letter := range s1 {
			if (strings.ContainsAny(string(letter), s2)) && (strings.ContainsAny(string(letter), s3)) {
				counter = counter + strings.Index(letters, string(letter)) + 1
				break
			}
		}
	}
	fmt.Printf("%d\n", counter)
}

func main() {
	partOne()
	partTwo()
}
