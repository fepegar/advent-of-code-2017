main = do
    passphrases <- readFile "passphrases.txt"
    putStrLn passphrases
