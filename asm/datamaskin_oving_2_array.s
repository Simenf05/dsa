j tests

########################################################################################
######################## Skriv koden din under denne linja #############################
########################################################################################

# Denne funksjonen tar inn en liste med 32-bits tall,
# og regner ut summen av tallene.
# Adressen til det første elementet i listen ligger i a0.
# Lengden på listen ligger i a1.
# Når funksjonen returnerer skal summen ligge i a0.
sum_array:
    
    addi s0, x0, 0
    addi t0, x0, 0
    
    loop:
        lw t1, 0(a0)
        add s0, s0, t1
        addi a0, a0, 4
        
        addi t0, t0, 1
        bne a1, t0, loop

    # Tips: husk at 32-bits tall tar opp 4 bytes,
    # så for hvert nye tall i listen øker adressen med 4.
    mv a0, s0
    ret

########################################################################################
######################## Skriv koden din over denne linja ##############################
########################################################################################

tests:

    #### Tester sum_array-funksjonen ####
    la a0, oneToTen    # Adressen til lista
    li a1, 10          # Lendgen på lista
    call sum_array
    li a1, 55          # Forventet sum
    bne a0, a1, sum_array_failed

    la a0, oneToTen    # Adressen til lista
    addi a0, a0, 4     # Hopp over første element
    li a1, 8           # Lendgen på lista (hopp over siste)
    call sum_array
    li a1, 44          # Forventet sum
    bne a0, a1, sum_array_failed

    #### Alle tester bestått! ####
    j all_tests_passed

sum_array_failed:
    mv t0, a0 # Svar gitt av funksjonen
    mv t1, a1 # Forventet svar
    la a0, wrong_sum_array
    li a7, 4 # Print string
    ecall
    mv a0, t0
    li a7, 1 # Print int
    ecall
    la a0, expected
    li a7, 4 # Print string
    ecall
    mv a0, t1
    li a7, 1 # Print int
    ecall
    j abort

abort:
    # Exit med kode 1
    li a0, 1
    li a7, 93
    ecall

all_tests_passed:
    la a0, tests_passed
    li a7, 4 # Print string
    ecall

    # Exit med kode 0
    li a7, 10
    ecall

.data
wrong_sum_array: .string "Fikk feil svar fra sum_array: "
expected: .string "\nForventet svar: "
tests_passed: .string "Alle tester var vellykkede!"

# Testdata for sum_array
oneToTen: .word 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
