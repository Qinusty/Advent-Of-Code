module Main where

main = do
	contents <- getContents
	print (processData contents 0)


processData :: String -> Int -> Int
processData [] pos = 0
processData (c:cs) (-1) = 0
processData ('(':cs) pos = 1 + (processData cs (pos+1))
processData (')':cs) pos = 1 + (processData cs (pos-1))

