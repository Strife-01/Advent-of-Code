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
	possibleOperations := generateAllPossibleCombinations(characters, len(inputs)-1)
	for operationTrie := 0; operationTrie < len(possibleOperations); operationTrie++ {
    currentOperations := possibleOperations[operationTrie]
    currentResult, _ := strconv.Atoi(inputs[0])
    for i := 1; i < len(inputs); i++ {
      if currentOperations[i - 1] == "+"{
        integer, _ := strconv.Atoi(inputs[i])
        currentResult += integer
      } else {
        integer, _ := strconv.Atoi(inputs[i])
        currentResult *= integer
      }
    }
    if currentResult == equationResult {
      return true
    }
	}
	return false
}

func generateAllPossibleCombinations(characters []string, nrCharacters int) [][]string {
	// create a stack-like structure
	var possibleCombinations [][]string
  var visited = make(map[string]bool)
  // generate the innitial state
  stack := make([]string, nrCharacters)
  for i := 0; i < nrCharacters; i++ {
    stack = append(stack, characters[0])
  }
	
  //add the values 
  
  backtrack(0, characters, &possibleCombinations, visited, &stack)

  return possibleCombinations
}

func backtrack(index int, characters []string, operations *[][]string, visited map[string]bool, stack *[]string ) {
  if index == len(*stack) {
    str := strings.Join(*stack, "")

    if !visited[str] {
      visited[str] = true
      var new_stack = make([]string, len(*stack));
      copy(new_stack, *stack)
      *operations = append(*operations, new_stack)
    }
  
    return
  }

  for _, operator := range characters {
    (*stack)[index] = operator

    backtrack(index + 1, characters, operations, visited, stack)
  }
}


func foundAlready(stack []string, possibleCombinations [][]string) bool {
  possibleOperators := strings.Join(stack, "")
  for i := 0; i < len(possibleCombinations); i++ {
    currentCheck := strings.Join(possibleCombinations[i], "")
    if possibleOperators == currentCheck {
      return true
    }
	}
	return false
}

func main() {
	// Initialize random seed
  calibration := 0
  var filename string;
  fmt.Print("Filename: ")
  fmt.Scan(&filename)
	// Get equations from file
	equations := parseEquations(getInputFromFile(filename))
  for _, equation := range equations[:len(equations) - 1] {
		components := parseEquation(equation)
	  //	fmt.Println(components)
    if evaluateEquation(components) {
      integer, _ := strconv.Atoi(components[0])
      calibration += integer
    }

	}
  fmt.Printf("The total calibration result is %d\n", calibration)
}

