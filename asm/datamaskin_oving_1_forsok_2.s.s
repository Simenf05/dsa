# Denne filen inneholder skjelettet til Praktisk Øving 1 i faget TDT4160
# Kopier filen inn i Ripes-simulatoren, enten lokalt eller på ripes.me

# I Ripes velger du CPUen "Single Cycle Processor" eller "5-Stage processor".
# Pass også på å huke av for ISA Exts.-valget "M".

# I denne øvingen skal du implementere tre funksjoner.
# Vi har ikke egentlig kommet til funksjoner enda, men du trenger foreløpig kun å vite én ting:
#     IKKE bruk registeret som heter x1 / ra.
#     Dette er retur-adressen som hoppes til når funksjonen er ferdig (ret-instruksjonen).
#     All andre registere står du fritt til å bruke.
#
# Merk også at merkelapper du definerer må være unike på tvers av hele filen.
# Merkelapper kan kun inneholde bokstaver, tall og _, og kan ikke begynne med et tall.

addi, a0, x0, -2
addi, a1, x0, 2
addi, a2, x0, 4

call median


j tend

j tests

########################################################################################
######################## Skriv koden din under denne linja #############################
########################################################################################

# Oppgave 1:
# Denne funksjonen tar inn ett tall x i registeret a0
# Hvis tallet er et partall skal x/2 returneres
# Hvis tallet er et oddetall skal 3*x + 1 returners.
# Returverdien skal legges i registeret a0

collatz:
    
    addi, a1, x0, 2
    rem, a1, a0, a1
    
    beq, a1, x0, partall
    
    addi, a1, x0, 3
    mul, a0, a0, a1
    addi, a0, a0, 1
    
    j end_collatz

partall:
    addi, a1, x0, 2
    div, a0, a0, a1
       
end_collatz:
    ret


# Oppgave 2:
# Denne funksjonen tar inn tre tall, i registrene a0, a1 og a2
# Når funksjonen er ferdig skal det mellomste tallet ligge i a0
# Hvis f.eks. a0 = 6, a1 = -2 og a2 = 4, skal svaret bli a0 = 4

median:    
        
    slt, a3, a0, a1
    slt, a4, a0, a2
    slt, a5, a1, a2
    
    and, a6, a4, a5
    bgt, a6, x0, biggest_is_a2
    
    or, a6, a3, a4
    not, a6, a6
    bgt, a6, x0, biggest_is_a0
    
    j biggest_is_a1
    
biggest_is_a2:
    bgt, a3, x0, middle_is_a1
    j middle_is_a0

biggest_is_a0:
    bgt, a5, x0, middle_is_a2
    j middle_is_a1

biggest_is_a1:
    bgt, a4, x0, middle_is_a2
    j middle_is_a0

middle_is_a1:
    add, a0, x0, a1
    j median_end
    
middle_is_a0:
    add, a0, x0, a0
    j median_end

middle_is_a2:
    add, a0, x0, a2
    j median_end
    
median_end:
    ret


# Oppgave 3:
# Denne funksjonen tar inn ett tall, n >= 1, i registeret a0
# Den regner ut fibonacci-tall f(n), der f(n) er definert slik:
#  f(0) = 0
#  f(1) = 1
#  f(n) = f(n-1) + f(n-2),   for alle n > 1

fibonacci:

    # Tips: I denne oppgaven bør du IKKE bruke rekursjon
    # Bruk heller en løkke, og bruk to registere for å representere f(i-1) og f(i)
    # Inni løkken erstatter du registrene med heholdsvis f(i) og f(i+1)

    # Forlater fibonacci-funskjonen her
    ret

########################################################################################
######################## Skriv koden din over denne linja ##############################
########################################################################################

tests:

    #### Tester collatz-funksjonen ####
    li a0, 8
    call collatz
    li t0, 4
    bne a0, t0, collatz_test_failed

    li a0, 21
    call collatz
    li t0, 64
    bne a0, t0, collatz_test_failed

    li a0, 440
    call collatz
    li t0, 220
    bne a0, t0, collatz_test_failed


    #### Tester median-funksjonen ####
    li a0, 8
    li a1, 12
    li a2, 20
    call median
    li t0, 12
    bne a0, t0, median_test_failed

    li a0, 32
    li a1, 17
    li a2, 5
    call median
    li t0, 17
    bne a0, t0, median_test_failed

    li a0, -5
    li a1, -9
    li a2, 4
    call median
    li t0, -5
    bne a0, t0, median_test_failed

    li a0, 6
    li a1, 21
    li a2, 14
    call median
    li t0, 14
    bne a0, t0, median_test_failed

    li a0, 21
    li a1, 7
    li a2, 13
    call median
    li t0, 13
    bne a0, t0, median_test_failed


    #### Tester fibonacci-funksjonen ####
    li a0, 1
    call fibonacci
    li t0, 1
    bne a0, t0, fibonacci_test_failed

    li a0, 2
    call fibonacci
    li t0, 1
    bne a0, t0, fibonacci_test_failed

    li a0, 4
    call fibonacci
    li t0, 3
    bne a0, t0, fibonacci_test_failed

    li a0, 14
    call fibonacci
    li t0, 377
    bne a0, t0, fibonacci_test_failed


    #### Alle tester bestått! ####
    j all_tests_passed


collatz_test_failed:
    mv t0, a0
    la a0, wrongCollatz
    li a7, 4 # Print string
    ecall
    mv a0, t0
    li a7, 1 # Print int
    ecall
    j abort

median_test_failed:
    mv t0, a0
    la a0, wrongMedian
    li a7, 4 # Print string
    ecall
    mv a0, t0
    li a7, 1 # Print int
    ecall
    j abort

fibonacci_test_failed:
    mv t0, a0
    la a0, wrongFibonacci
    li a7, 4 # Print string
    ecall
    mv a0, t0
    li a7, 1 # Print int
    ecall
    j abort

abort:
    # Exit med kode 1
    li a0, 1
    li a7, 93
    ecall

all_tests_passed:
    la a0, testsPassed
    li a7, 4 # Print string
    ecall

    li a7, 10
    ecall    
    
.data
wrongCollatz: .string "Fikk feil svar på collatz: "
wrongMedian: .string "Fikk feil svar på median: "
wrongFibonacci: .string "Fikk feil svar på fibonacci: "
testsPassed: .string "Alle tester var vellykkede!"



tend:
    addi, s2, x0, 1