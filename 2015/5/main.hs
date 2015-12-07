module Main where

import Data.List (group)

main = do
	contents <- getContents
	print (length (filter isSafe (lines contents)))
		-- has 3 or more voewls, has atleast 1 case of double letter and has none of the avoid strings
isSafe input = (countVowels input >= 3) && (hasDoubleLetter input) && (hasNoAvoidStrings input)  
	where
	countVowels :: String -> Int
	countVowels = length . filter (\x -> x `elem` "aeiou")
	hasDoubleLetter :: String -> Bool
	hasDoubleLetter cs = length (filter (\cs -> (length cs) > 1) (group cs)) > 0
	hasNoAvoidStrings string = length (filter (\s -> substring s string) avoidStrings) == 0
			where 
			avoidStrings = ["ab","cd","pq","xy"]
			-- Substring code snippet taken from http://stackoverflow.com/a/30588782
			substring :: String -> String -> Bool
			substring (x:xs) [] = False
			substring xs ys
				| prefix xs ys = True
				| substring xs (tail ys) = True
				| otherwise = False
				where
				prefix :: String -> String -> Bool
				prefix [] ys = True
				prefix (x:xs) [] = False
				prefix (x:xs) (y:ys) = (x == y) && prefix xs ys


