package main

import (
	"fmt"
	"strings"
	"os"
	"strconv"
)

func parseEquation(equation string) (parseEquation []string) {
	// split the equation based on delimiter of result and operations
	if len(equation) == 0 {
		return
	}
	parts := strings.Split(equation, ": ")
	// get the inputs for the equation
	inputs := strings.Split(parts[1], " ")
	// result of the equation
	parseEquation = append(parseEquation, parts[0])
	// add the inputs at the end
	parseEquation = append(parseEquation, inputs...)
	return
}

func parseEquations(equations string) (parsedEquations []string) {
	// split based on \n
	parsedEquations = append(parsedEquations, strings.Split(equations, "\n")...)
	return
}

func getInputFromFile(filename string) (data string) {
	fileStream, err := os.ReadFile(filename)
	if err != nil {
		panic(err)
	}
	return string(fileStream) // no need to manually append each byte
}

func evaluateEquation(equationComponents []string) bool {
	equationResult, _ := strconv.Atoi(equationComponents[0])
	inputs := equationComponents[1:]
	characters := []string{"+", "*"}
	return generateAllPossibleCombinations(characters, len(inputs)-1, inputs, equationResult)
}

func generateAllPossibleCombinations(characters []string, nrCharacters int, inputs []string, equationResult int) bool {
	// create a stack-like structure
	var possibleCombinations [][]string
	visited := make(map[string]bool)
	// initialize the stack with the first possible operator
	stack := make([]string, nrCharacters)
	for i := 0; i < nrCharacters; i++ {
		stack[i] = characters[0] // initialize with the first operator
	}

	// start backtracking to generate all combinations
	return backtrack(0, characters, &possibleCombinations, visited, &stack, inputs, equationResult)
}

func backtrack(index int, characters []string, operations *[][]string, visited map[string]bool, stack *[]string, inputs []string, equationResult int) bool {
	// If we've reached the end of the stack, check the result
	if index == len(*stack) {
		// Join the stack to get a combination of operators
		str := strings.Join(*stack, "")

		// If this combination has not been visited before
		if !visited[str] {
			// Mark it as visited
			visited[str] = true

			// Make a deep copy of the stack (to store it in operations)
			newStack := make([]string, len(*stack))
			copy(newStack, *stack)

			// Try the solution and see if it works
			currentResult, _ := strconv.Atoi(inputs[0]) // Start with the first input
			for i := 1; i < len(inputs); i++ {
				// Use the operator in the stack to calculate the result
				if (*stack)[i-1] == "+" {
					integer, _ := strconv.Atoi(inputs[i])
					currentResult += integer
				} else {
					integer, _ := strconv.Atoi(inputs[i])
					currentResult *= integer
				}
			}

			// Check if the result matches the equation result
			if currentResult == equationResult {
				// If it matches, we found a valid solution
				*operations = append(*operations, newStack)
				// Return true only if we want the first valid solution
        return true
				// For exploring all combinations, you can remove this return
			}
		}
		// Continue to explore other combinations
		return false
	}

	// Try each operator at the current position
	for _, operator := range characters {
		// Set the operator in the current position of the stack
		(*stack)[index] = operator

		// Recursively backtrack with the next index
		if backtrack(index+1, characters, operations, visited, stack, inputs, equationResult) {
			return true // If a solution is found, stop the recursion
		}
	}

	// If no solution is found at this level, backtrack and continue
	return false
}

func main() {
	// Initialize random seed
	calibration := 0
	var filename string
	fmt.Print("Filename: ")
	fmt.Scan(&filename)
	// Get equations from file
	equations := parseEquations(getInputFromFile(filename))
	for _, equation := range equations[:len(equations)-1] {
		components := parseEquation(equation)
		if evaluateEquation(components) {
			integer, _ := strconv.Atoi(components[0])
			calibration += integer
		}
	}
	fmt.Printf("The total calibration result is %d\n", calibration)
}

