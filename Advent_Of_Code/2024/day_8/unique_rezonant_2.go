package main

import (
	"fmt"
	"os"
	"errors"
  "strings"
)

const EMPTY_SPACE rune = '.'
const INTERFERE_ZONE rune = '#'

func getInputFromFile(filename string) (string, error) {
	fileStream, err := os.ReadFile(filename)
	if err != nil {
		return "", err
	}
	return string(fileStream), nil
}

func getFileName() (string, error) {
	if len(os.Args) != 2 {
		return "", errors.New("Usage ./unique_rezonant.go fileData.txt")
	}
	return os.Args[1], nil
}

func getCoordinates(dataGrid string, towersCoordinates *map[string][][2]int) (gridHeight int, gridWidth int){
  var dataArray = strings.Split(dataGrid, "\n")
  gridHeight = len(dataArray) - 1
  gridWidth = len(dataArray[0])

  for i := 0; i < gridHeight; i++ {
    for j := 0; j < gridWidth; j++ {
      if rune(dataArray[i][j]) != EMPTY_SPACE {
        var coord [2]int;
        coord[0] = i
        coord[1] = j
        (*towersCoordinates)[string(dataArray[i][j])] = append((*towersCoordinates)[string(dataArray[i][j])], coord)
      }
    }
  }
  return
}

func abs(a int, b int) int {
  if a < b {
    return b - a
  }
  return a - b
}

func main() {
	var filename, err = getFileName()
	if err != nil {
		fmt.Println(err)
		return
	}

	var fileData string
	fileData, err = getInputFromFile(filename)
	if err != nil {
		fmt.Println(err)
		return
	}

  var towersCoordinates = make(map[string][][2]int)
  var interferenceCoords = make(map[[2]int]bool)
  var gridHeight, gridWidth = getCoordinates(fileData, &towersCoordinates)
  
  //fmt.Println(gridHeight, gridWidth)

  for _, coordinateArray := range towersCoordinates {
    final_i_1, final_i_2, final_j_1, final_j_2 := 0, 0, 0, 0
    var coordsToAdd [2]int
    for i := 0; i < len(coordinateArray) - 1; i++ {
      for j := 1; j < len(coordinateArray); j++ {
        i1, j1 := coordinateArray[i][0], coordinateArray[i][1]
        i2, j2 := coordinateArray[j][0], coordinateArray[j][1]

        if i1 == i2 && j1 == j2 {
          continue
        }
        
        //slice1 := make([][2]int, 0)
        var direction_i_1, direction_j_1 string
        var distance_is, distance_js int
        distance_is = abs(i1, i2)
        distance_js = abs(j1, j2)
        
        var beginner_resonators [2]int;
        beginner_resonators[0] = i1
        beginner_resonators[1] = j1
        interferenceCoords[beginner_resonators] = true

        beginner_resonators[0] = i2
        beginner_resonators[1] = j2
        interferenceCoords[beginner_resonators] = true

        if i1 < i2 {
          final_i_1 = i1 - distance_is
          final_i_2 = i2 + distance_is
          direction_i_1 = "up"
        } else {
          final_i_1 = i1 + distance_is
          final_i_2 = i2 - distance_is
          direction_i_1 = "down"
        }

        if j1 < j2 {
          final_j_1 = j1 - distance_js
          final_j_2 = j2 + distance_js
          direction_j_1 = "left"
        } else {
          final_j_1 = j1 + distance_js
          final_j_2 = j2 - distance_js
          direction_j_1 = "right"
        }
        for final_i_1 >= 0 && final_i_1 < gridHeight && final_j_1 >= 0 && final_j_1 < gridWidth {
          coordsToAdd[0] = final_i_1
          coordsToAdd[1] = final_j_1
          //slice1 = append(slice1, coordsToAdd)
          if direction_i_1 == "up" {
            final_i_1 -= distance_is
          } else {
            final_i_1 += distance_is
          }

          if direction_j_1 == "left" {
            final_j_1 -= distance_js
          } else {
            final_j_1 += distance_js
          }

          fmt.Println(coordsToAdd[0], coordsToAdd[1])
          interferenceCoords[coordsToAdd] = true
        }

        for final_i_2 >= 0 && final_i_2 < gridHeight && final_j_2 >= 0 && final_j_2 < gridWidth {
          coordsToAdd[0] = final_i_2
          coordsToAdd[1] = final_j_2

          if direction_i_1 == "up" {
            final_i_2 += distance_is
          } else {
            final_i_2 -= distance_is
          }

          if direction_j_1 == "left" {
            final_j_2 += distance_js
          } else {
            final_j_2 -= distance_js
          }

          fmt.Println(coordsToAdd[0], coordsToAdd[1])
          interferenceCoords[coordsToAdd] = true
        }
        fmt.Println()

      }
    }
  }
  fmt.Println(towersCoordinates)
  fmt.Println(len(interferenceCoords))
}

