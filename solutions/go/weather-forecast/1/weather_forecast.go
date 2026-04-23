// Package weather provides tools to report current weather conditions.
package weather

var (
    // CurrentCondition represents the current weather conditions.
	CurrentCondition string
	// CurrentLocation represents the location of the current weather.
	CurrentLocation  string
)

// Forecast returns a formatted string with the current weather condition for a given city.
func Forecast(city, condition string) string {
	CurrentLocation, CurrentCondition = city, condition
	return CurrentLocation + " - current weather condition: " + CurrentCondition
}
