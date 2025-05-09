package main

import (
	"errors"
	"fmt"
)

func calculateDiscount(price float64, customerType string) (float64, error) {
	if customerType == "" {
		return 0, errors.New("customer type not provided")
	}
	if price < 0 {
		return 0, errors.New("price cannot be negative")
	}
	if customerType == "gold" {
		if price > 100 {
			return price * 0.1, nil
		} else {
			return price * 0.05, nil
		}
	} else if customerType == "silver" {
		if price > 50 {
			return price * 0.05, nil
		} else {
			return 0, nil
		}
	} else {
		return 0, errors.New("invalid customer type")
	}
}

func main() {
	price := 120.0
	customerType := "gold"
	discount, err := calculateDiscount(price, customerType)
	if err != nil {
		fmt.Printf("Error: %v\n", err)
		return
	}
	fmt.Printf("Discount: %.2f\n", discount)
}

