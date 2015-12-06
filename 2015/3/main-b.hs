module Main where
import Data.List (nub)

main = do
	content <- getContents
	print (getUniqueCount (processInput content))

getUniqueCount = length . nub

processInput input = (0,0) : (move ((0,0), (0,0)) input)
	where
	move :: ((Int, Int), (Int, Int)) -> String -> [(Int, Int)]
	move _ [] = []
	-- Manage robosanta and santa by alternating the positions passed... 
	-- (santa, robot santa) - Keeps swapping
	move ((x1, y1), (x2, y2)) ('^':cs) = (x1,y1+1) : ((x2,y2) : (move ((x2, y2), (x1, y1+1)) cs))	
	move ((x1, y1), (x2, y2)) ('v':cs) = (x1,y1-1) : ((x2,y2) : (move ((x2, y2), (x1, y1-1)) cs))
	move ((x1, y1), (x2, y2)) ('>':cs) = (x1+1,y1) : ((x2,y2) : (move ((x2, y2), (x1+1, y1)) cs))
	move ((x1, y1), (x2, y2)) ('<':cs) = (x1-1,y1) : ((x2,y2) : (move ((x2, y2), (x1-1, y1)) cs))
