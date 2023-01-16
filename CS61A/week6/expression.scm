(* 1 3 5 (+ 2 4 6))

; (if <predicate> <consequent> <alternative>)
; (and <e1> ... <en>)
; (or <e1> ... <en>)

; binding symbols:
; (define <symbol> <expression>)
(define pi 3.14)

; define a new procedure
; (define (<symbol> <parameters>) <body>)
(define (say s) display s)

(define (square a) (* a a))

(define (average a b)
    (/ (+ a b) 2)
    )

(define (s x)
    (define (update guess)
        (if (= (square guess) x)
            guess
            (update (average guess (/ x guess)))
            )
        )
    (update 1)
    )