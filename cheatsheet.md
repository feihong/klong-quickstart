# Examples

## Conditional

    :[0;:yes;:no]  -->  no
    :[1;:yes;:no]  -->  yes

## Size

    #42  -->  42
    #-42  -->  42
    #[1 2 3 4 5 6]  -->  6
    #"hello sam"  -->  9
    #0cX  -->  88

## Take

    3#!9  -->  [0 1 2]
    (-3)#!9  -->  [6 7 8]

## Drop

    3_!9  -->  [3 4 5 6 7 8]
    (-3)_!9  -->  [0 1 2 3 4 5]

## Reverse

    |!10  -->  [9 8 7 6 5 4 3 2 1 0]
    |"What the Poop"  -->  pooP eht tahW

## Each

    {1+x*x}'!6  -->  [ 1  2  5 10 17 26]
    {x;_5*.rn()}'20:^0  -->  [1 2 2 2 2 2 2 1 0 1 3 0 1 2 2 2 4 4 2 1]

## Each-2

    [1 2 3],'[4 5 6]  -->  [[1 4]
 [2 5]
 [3 6]]

## Each-Left

    1,:\[1 2 3]  -->  [[1 1]
 [1 2]
 [1 3]]

## Each-Right

    "a",:/"bcd"  -->  ['ba' 'ca' 'da']

## Each-Pair

    ,:'[1 2 3 4 5 6]  -->  [[1 2]
 [2 3]
 [3 4]
 [4 5]
 [5 6]]

## Over

    -/[1 2 3 4]  -->  -8

## Over-Neutral

    100-/[1 2 3 4]  -->  90

## Scan

    ,\"abcd"  -->  ['a' 'ab' 'abc' 'abcd']

## Scan-Over-Neutral

    1,\[2 3 4]  -->  [1 array([1, 2]) array([1, 2, 3]) array([1, 2, 3, 4])]

## Converge

    *:~[[[1 2 3] 4] 5]  -->  1

## Scan-Converging

    *\~[[[1 2 3] 4] 5]  -->  [array([array([array([1, 2, 3]), 4], dtype=object), 5], dtype=object)
 array([array([1, 2, 3]), 4], dtype=object) array([1, 2, 3]) 1]

## While

    {x>0}{x-3}:~10  -->  -2

## Scan-While

    {x>0}{x-3}\~10  -->  [10  7  4  1]

## Iterate

    5{x,"b"}:*"a"  -->  abbbbb

## Scan-Iterating

    5{x,"b"}\*"a"  -->  ['a' 'ab' 'abb' 'abbb' 'abbbb' 'abbbbb']
