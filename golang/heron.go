package kata

import "math"

func Heron(a, b, c float64) (area float64) {
  var s float64 = (a + b + c) / 2
  area = math.Sqrt(s* (s-a) * (s-b) * (s-c))
  return area
}