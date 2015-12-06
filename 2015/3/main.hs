module Main where
import Data.List (nub)

main = do
	content <- getContents
	print (getUniqueCount (processInput content))

getUniqueCount :: [(Int, Int)] -> Int
getUniqueCount = length . nub

processInput input = move (0,0) input
	where
	move _ [] = []
	move (x,y) ('^':cs) = (x,y) : move (x, y+1) cs	
	move (x,y) ('v':cs) = (x,y) : move (x, y-1) cs
	move (x,y) ('>':cs) = (x,y) : move (x+1, y) cs
	move (x,y) ('<':cs) = (x,y) : move (x-1, y) cs
