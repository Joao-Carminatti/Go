package cars

// CalculateWorkingCarsPerHour calculates how many working cars are
// produced by the assembly line every hour.
func CalculateWorkingCarsPerHour(productionRate int, successRate float64) float64 {
	p := float64(productionRate) * successRate / 100
    return p
}

// CalculateWorkingCarsPerMinute calculates how many working cars are
// produced by the assembly line every minute.
func CalculateWorkingCarsPerMinute(productionRate int, successRate float64) int {
	carsPerHours := CalculateWorkingCarsPerHour(productionRate, successRate)
    i := carsPerHours / 60
    return int(i)
    
}

// CalculateCost works out the cost of producing the given number of cars.
func CalculateCost(carsCount int) uint {
	groups10 := carsCount / 10
    missingCars := carsCount % 10

    costGroup := float32(groups10) * 95000
    costIndividual := float32(missingCars) * 10000

    return uint(costGroup + costIndividual)
}
