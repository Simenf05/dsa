# Denne filen inneholder skjelettet til Oppgave 2 på Praktisk Øving 2 i TDT4160
j tests

########################################################################################
######################## Skriv koden din under denne linja #############################
########################################################################################

# Denne funksjonen tar inn en lenket liste med tall, og regner ut summen.
#
# En lenket liste er en datastruktur der hvert element inneholder adressen til neste element.
# Hvert element i lista ser slik ut:
#
# Byte offset:
# 0     1     2     3     4     5      6      7     8
# +-----------------------+-------------------------+
# | tallverdi             | peker til neste element |
# +-----------------------+-------------------------+
#
# Gitt at adressen til et element ligger i a0-registeret,
# kan man lese tallverdien med
#     lw a2, 0(a0)
# og lese pekeren til neste element med
#     lw a3, 4(a0)
#
# Listen er slutt når pekeren til neste element er lik 0
#
# Funksjonen skal ta inn adressen til første element i a0.
# Når funksjonen returnerer skal summen av listen ligge i a0.
sum_linked_list:

    addi s0, x0, 0
    
    loop:
        lw t0, 0(a0)
        lw t1, 4(a0)
        
        add, s0, s0, t0
        mv a0, t1
        
        bne t1, x0, loop
    
    mv a0, s0

    ret

########################################################################################
######################## Skriv koden din over denne linja ##############################
########################################################################################

tests:

    #### Tester sum_linked_list-funksjonen ####
    la a0, linked_list_0    # Adressen til første element
    call sum_linked_list
    li a1, 79               # Forventet sum
    bne a0, a1, sum_linked_list_failed

    la a0, linked_list_2    # Begynner litt senere i lista
    call sum_linked_list
    li a1, 62               # Forventet sum
    bne a0, a1, sum_linked_list_failed

    #### Alle tester bestått! ####
    j all_tests_passed

sum_linked_list_failed:
    mv t0, a0 # Svar gitt av funksjonen
    mv t1, a1 # Forventet svar
    la a0, wrong_sum_linked_list
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
wrong_sum_linked_list: .string "Fikk feil svar fra sum_linked_list: "
expected: .string "\nForventet svar: "
tests_passed: .string "Alle tester var vellykkede!"

# Testdata for sum_linked_list
linked_list_6:  .word 18, 0
linked_list_5:  .word 7, linked_list_6
linked_list_4:  .word 19, linked_list_5
# Put some dummy data in between list elements
.word 10, 20, 30
linked_list_3:  .word 15, linked_list_4
linked_list_2:  .word 3, linked_list_3
linked_list_1:  .word 7, linked_list_2
# More dummy data
.word 444
linked_list_0:  .word 10, linked_list_1
