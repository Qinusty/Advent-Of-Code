module Main where
import Data.List (sort)

main = do
	input <- getContents
	-- part 1 -- print (sum (map (\line -> (getSurfaceArea line) + getSmallestSide line) (lines input)))	
	-- part 2
	print (sum (map (\line -> getRibbonLength line) (lines input)))

getSurfaceArea line = 2*l*w + 2*w*h + 2*h*l
	where 
	w = getWidth line
	l = getLength line
	h = getHeight line

getSmallestSide line = getArea (sort (getDimensions line))
	where 
	getArea sortedList = (head sortedList) * (head (tail sortedList))

getRibbonLength line = process (sort (getDimensions line))
	where 
	process sortedList = (2* head sortedList) + (2*head (tail sortedList)) + (product sortedList)
getDimensions line = (getWidth line : ((getHeight line) : ((getLength line) : [])))

getLength rawData =  read (innerProcessing rawData) :: Int 
	where
	innerProcessing ('x':cs) = []
	innerProcessing (c:cs) = c : (innerProcessing cs)

getWidth rawData = read (innerProcessing rawData 0) :: Int
	where 
	innerProcessing ('x':cs) 1 = []
	innerProcessing (c:cs) 1 = c : (innerProcessing cs 1)
	innerProcessing ('x':cs) 0 = (innerProcessing cs 1)
	innerProcessing (c:cs) _ = (innerProcessing cs 0)

getHeight rawData = read (innerProcessing rawData 0) :: Int
	where
	innerProcessing [] 2 = []
        innerProcessing (c:cs) 2 = c : (innerProcessing cs 2)
        innerProcessing ('x':cs) 1 = (innerProcessing cs 2)
	innerProcessing (c:cs) 1 = (innerProcessing cs 1)
	innerProcessing ('x':cs) 0 = (innerProcessing cs 1)
        innerProcessing (c:cs) 0 = (innerProcessing cs 0)

