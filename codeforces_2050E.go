package main

import (
	"fmt"
	"strconv"
	"bufio"
	"os"
)

func iterative_solution() {
	s := bufio.NewScanner(os.Stdin)
	s.Scan()
	t, err := strconv.Atoi(s.Text())
	if err != nil {
		panic(err)
	}

	for range t {
		s.Scan()
		s1 := s.Text()
		s.Scan()
		s2 := s.Text()
		s.Scan()
		s3 := s.Text()

		dp := map[int]map[int]uint{
			len(s1): map[int]uint{
				len(s2): 0,
			},
		}

		i := len(s1)+1
		for i > 0 {
			i -= 1
			dp[i] = map[int]uint{}
			j := len(s2)+1
			for j > 0 {
				j -= 1
				if i == len(s1) && j == len(s2) {
					continue
				}
				a1 := ^uint(0)
				a2 := ^uint(0)

				if i < len(s1) {
					x := uint(0)
					if s1[i] != s3[i+j] {
						x = 1
					}
					a1 = dp[i+1][j] + x
				}

				if j < len(s2) {
					x := uint(0)
					if s2[j] != s3[i+j] {
						x = 1
					}
					a2 = dp[i][j+1] + x
				}

				if a1 < a2 {
					dp[i][j] = a1
				} else {
					dp[i][j] = a2
				}
			}
		}

		fmt.Printf("%d\n", dp[0][0])
	}
}

func recursive_solution() {
	s := bufio.NewScanner(os.Stdin)
	s.Scan()
	t, err := strconv.Atoi(s.Text())
	if err != nil {
		panic(err)
	}

	for range t {
		s.Scan()
		s1 := s.Text()
		s.Scan()
		s2 := s.Text()
		s.Scan()
		s3 := s.Text()

		dp := map[int]map[int]uint{}

		var solve func(i,j int) uint
		solve = func (i, j int) uint {
			if dp[i] == nil {
				dp[i] = map[int]uint{}
			}

			if i == len(s1) && j == len(s2) {
				dp[i][j] = 0
				return 0
			}

			if ans, ok := dp[i][j]; ok {
				return ans
			}

			a1 := ^uint(0)
			a2 := ^uint(0)

			if i < len(s1) {
				a1 = solve(i+1, j)
				if s1[i] != s3[i+j] {
					a1 += 1
				}
			}
			if j < len(s2) {
				a2 = solve(i, j+1)
				if s2[j] != s3[i+j] {
					a2 += 1
				}
			}

			ans := a1
			if a2 < a1 {
				ans = a2
			}

			dp[i][j] = ans
			return ans
		}

		fmt.Printf("%d\n", solve(0,0))
	}
}

func main() {
	recursive_solution()
}
