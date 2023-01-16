; (lambda (<parameters>) <body>)

(define (plus4 x) (+ x 4))
; ==
(define plus4 (lambda (x) (+ x 4)))
