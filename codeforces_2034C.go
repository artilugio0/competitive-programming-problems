package main

import (
	"fmt"
	"strconv"
	"bufio"
	"os"
	"strings"
)

func move(r, c int, mv rune) []int {
	switch mv {
	case 'U':
		return []int{r-1, c}
	case 'L':
		return []int{r, c-1}
	case 'D':
		return []int{r+1, c}
	case 'R':
		return []int{r, c+1}
	}

	panic("invalid move")
}

func main() {
	s := bufio.NewScanner(os.Stdin)
	s.Scan()
	t, err := strconv.Atoi(s.Text())
	if err != nil {
		panic(err)
	}

	for range t {
		s.Scan()
		nm := strings.Fields(s.Text())
		n, _ := strconv.Atoi(nm[0])
		m, _ := strconv.Atoi(nm[1])

		rows := []string{}
		for range n {
			s.Scan()
			row := s.Text()
			rows = append(rows, row)
		}

		cache := map[int]map[int]bool{}
		visited := map[int]map[int]bool{}
		var badCell func(r, c int) bool
		badCell = func(r, c int) bool {
			if cache[r] == nil {
				cache[r] = map[int]bool{}
			}

			if visited[r] == nil {
				visited[r] = map[int]bool{}
			}

			if result, ok := cache[r][c]; ok {
				return result
			}

			if visited[r][c] {
				cache[r][c] = true
				return true
			}

			if r < 0 || c < 0 || r >= n || c >= m {
				cache[r][c] = false
				return false
			}

			visited[r][c] = true
			defer func() { visited[r][c] = false }()

			if rows[r][c] != '?' {
				next := move(r,c,rune(rows[r][c]))
				nr := next[0]
				nc := next[1]

				result := badCell(nr, nc)

				cache[r][c] = result
				return result
			}

			for _, mv := range "URDL" {
				next := move(r,c,mv)
				nr := next[0]
				nc := next[1]

				isBad := badCell(nr, nc)

				if isBad {
					cache[r][c] = true
					return true
				}
			}

			cache[r][c] = false
			return false
		}

		count := 0
		for r := range n {
			for c := range m {
				if badCell(r, c) {
					count += 1
				}
			}
		}

		fmt.Println(count)
	}
}
