import queue
def RPN(expression):
    out = ""
    opQ = queue.LifoQueue()
    for component in expression:
        if component.isdigit():
            # is an operand
            out += component
        else:
            match component:
                case "(":
                    opQ.put(comonent)
                case ")":
                    current = opQ.get()
                    while not opQ.empty() and current != "(":
                        out+=current
                default:
                    # operator
                    # check the priority of the operands
                    match component:
                        case "^":
                            opQ.put(component)
                        case "/":
                            opQ.put(component)
                        case "*" | "%":
                            opQ.put(component)
                        case "+":
                            opQ.put(component)
                        case "-":
                            opQ.put(component)
    return out

if __name__ == "__main__":
    print(RPN("((m-n)^(o+p)/(q+r)+s)*t"))

#in: ((m-n)^(o+p)/(q+r)+s)*t
#out: mn-op+^qr+/s+t*
#stack: 

#in: ((m+n)/o+(p-q)*r)/s
#out: mn+opq-r*+/s/
#stack: 

#in: mno-p*+q/r-
#out: 
#stack: (m+(n-o)*p)/q-r

#in: omn+*pq-%r/
#out: omn+*pq-%r/
#stack: ((o*(m+n))%(p-q))/r

#Ex. 5
#in: 8 5 * 3 6 2 ^ - 9 + 1 / - =
#out: 64
#stack: 40 - -24

# next week test:
# bin, dec, oct, hex, two's compliment conversions
# arithmetic in binary, decimal
# INFIX, POSTFIX, PREFIX
# worth 50 points, 40 minutes