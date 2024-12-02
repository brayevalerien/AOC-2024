import Data.List

parse :: [String] -> ([Int], [Int])
parse content = parse_aux content [] []
    where
        parse_aux :: [String] -> [Int] -> [Int] -> ([Int], [Int]) 
        parse_aux [] left right = (left, right)
        parse_aux (x:xs) left right =
            let [l, r] = words x
            in parse_aux xs ((read l):left) ((read r):right)
    
result :: [Int] -> [Int] -> Int
-- There probably is a more elegant way to do it using folding
result left right = sum $ map (\l -> l*(count right l)) left
    where
        count :: (Eq a) => [a] -> a -> Int
        count list element = length $ filter (==element) list

main = do
    content <- readFile "day01/input.txt"
    let (left, right) = parse (lines content)
    putStrLn $ show (result left right)
