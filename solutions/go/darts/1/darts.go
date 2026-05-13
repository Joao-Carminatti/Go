package darts

func Score(x, y float64) int {
	d := x*x + y*y

    switch {
        case d <= 1:
        return 10
        case d <= 25:
        return 5
        case d <= 100:
        return 1
        default:
        return 0
    }
}
