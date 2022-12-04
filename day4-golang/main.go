package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func partOne() {
	file, err := os.Open("input.txt")
	if err != nil {
		fmt.Println("Error Opening The File", err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	var counter int
	for scanner.Scan() {
		vals := strings.Split(scanner.Text(), ",")

		a, _ := strconv.Atoi(strings.Split(vals[0], "-")[0])
		b, _ := strconv.Atoi(strings.Split(vals[0], "-")[1])
		c, _ := strconv.Atoi(strings.Split(vals[1], "-")[0])
		d, _ := strconv.Atoi(strings.Split(vals[1], "-")[1])

		if (a <= c) && (c <= d) && (d <= b) || (c <= a) && (a <= b) && (b <= d) {
			counter++
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
	var counter int
	for scanner.Scan() {
		vals := strings.Split(scanner.Text(), ",")

		a, _ := strconv.Atoi(strings.Split(vals[0], "-")[0])
		b, _ := strconv.Atoi(strings.Split(vals[0], "-")[1])
		c, _ := strconv.Atoi(strings.Split(vals[1], "-")[0])
		d, _ := strconv.Atoi(strings.Split(vals[1], "-")[1])

		if (a <= c) && (c <= b) || (a <= d) && (d <= b) || (c <= a) && (a <= d) || (c <= b) && (b <= d) {
			counter++
		}
	}
	fmt.Printf("%d\n", counter)

}

func main() {
	partOne()
	partTwo()
}
