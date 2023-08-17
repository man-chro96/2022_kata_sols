package kata

func  Solution(n int) string {
	s := ""

	format := func(r int, x, y, z string) string {
		arr := []string{"", x, x+x, x+x+x, x+y, y, y+x, y+x+x, y+x+x+x, x+z}
		s := arr[n/r]
		return s
	}

	if n >= 1000 {
		for i := 0; i < n/1000; i++ {
			s += "M"
		}
		n = n % 1000
	}
	if n >= 100 {
		s += format(100, "C", "D", "M")
		n = n % 100
	}
	if n >= 10 {
		s += format(10, "X", "L", "C")
		n = n % 10
	}

	s += format(1, "I", "V", "X")
	return s
}