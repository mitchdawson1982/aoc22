package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func partOne() {

	m := map[int][]string{
		1: []string{"D", "M", "S", "Z", "R", "F", "W", "N"},
		2: []string{"W", "P", "Q", "G", "S"},
		3: []string{"W", "R", "V", "Q", "F", "N", "J", "C"},
		4: []string{"F", "Z", "P", "C", "G", "D", "L"},
		5: []string{"T", "P", "S"},
		6: []string{"H", "D", "F", "W", "R", "L"},
		7: []string{"Z", "N", "D", "C"},
		8: []string{"W", "N", "R", "F", "V", "S", "J", "Q"},
		9: []string{"R", "M", "S", "G", "Z", "W", "V"},
	}

	file, err := os.Open("input.txt")
	if err != nil {
		fmt.Println("Error Opening The File", err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		vals := strings.Split(scanner.Text(), " ")
		moves, _ := strconv.Atoi(vals[1])
		fromStack, _ := strconv.Atoi(vals[3])
		// toStack, _ := strconv.Atoi(vals[5])

		s := m[fromStack][:-moves]

		fmt.Println(s)

		// move 3 from 5 to 3
		// fmt.Printf("%d\n", moves)
		// fmt.Printf("%d\n", fromStack)
		// fmt.Printf("%d\n", toStack)
	}

	fmt.Println(m[1])

}

func main() {
	arr1 := [6]int{10, 11, 12, 13, 14, 15}
	myslice := arr1[len(arr1)-2:]
	arr1 = arr1[0 : len(arr1)-2]

	fmt.Printf("myslice = %v\n", myslice)
	fmt.Printf("length = %d\n", len(myslice))
	fmt.Printf("capacity = %d\n", cap(myslice))
	// partOne()
}
